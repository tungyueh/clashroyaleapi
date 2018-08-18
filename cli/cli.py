import argparse
import cmd
import json
import readline
import os
import sys
from typing import List

import pprint

from clashroyaleapi import ClashRoyaleClient, Card, Chest


def enable_mac_auto_complete():
    if 'libedit' in readline.__doc__:
        readline.parse_and_bind("bind ^I rl_complete")
    else:
        readline.parse_and_bind("tab: complete")


class ClashRoyaleCLI(cmd.Cmd):
    def __init__(self,
                 token: str,
                 player_tag: str,
                 clan_tag: str,
                 verbose: bool = False):
        self.cr_client = ClashRoyaleClient(token,
                                           player_tag,
                                           clan_tag)
        self.verbose = verbose

        self.history_file = os.path.expanduser('~/.clashroyale_cli_history')
        self.prompt = 'ClashRoyale: '
        super().__init__()

    def do_EOF(self, _):
        print('')
        return True

    def preloop(self):
        enable_mac_auto_complete()

        try:
            readline.read_history_file(self.history_file)
        except IOError:
            pass
        readline.set_auto_history(False)

    def postloop(self):
        readline.write_history_file(self.history_file)

    def precmd(self, line):
        if line != 'EOF':
            readline.add_history(line)
        return line

    def do_get_player(self, _):
        """Get information about a single player by player tag."""
        player = self.cr_client.get_player()
        if self.verbose:
            pprint.pprint(player._raw)
        else:
            print(player)

    def do_get_player_upcoming_chest(self, _):
        """Get list of reward chests that the player will receive next in the game."""
        chests: List[Chest] = self.cr_client.get_player_upcoming_chest()
        for c in chests:
            print(f'{c.index+1}: {c.name}')

    def do_get_player_battle_log(self, _):
        """Get list of recent battle results for a player."""
        battle_logs = self.cr_client.get_player_battle_log()

        print('{:<20} {:<25} {:<25} {:<15} {:>3}'.format(
            'Battle Time',
            'Battel Type',
            'Game Mode',
            'Battle Result',
            'Trophies'
        ))
        for battle_log in battle_logs:
            if battle_log.win:
                battle_result = 'win'
            else:
                battle_result = 'lose'
            print(f'{battle_log.battle_time} {battle_log.type:<25} '
                  f'{battle_log.game_mode:<25} {battle_result:<15} '
                  f'{battle_log.team_profile[0].trophy_change:>3}')

    def do_list_card(self, _):
        """Get list of all available cards."""
        cards: List[Card] = self.cr_client.list_card()
        for card in cards:
            print(card)


def main():
    parser = argparse.ArgumentParser(prog='ucc_cli')
    parser.add_argument('-v', '--verbose', action='store_true',
                        default=False, help='Print vebose message')
    parser.add_argument('-a', '--auth_file', metavar='auth_file', type=str,
                        default='', help='A path to auth_file.')
    args = parser.parse_args()
    auth_file = args.auth_file
    with open(auth_file, 'rb') as fp:
        auth = fp.read()

    auth_json = json.loads(auth)
    token = auth_json['token']
    player_tag = auth_json['player_tag']
    clan_tag = auth_json['clan_tag']

    verbose = args.verbose

    cc3_cli = ClashRoyaleCLI(token, player_tag, clan_tag, verbose)
    cc3_cli.cmdloop()


if __name__ == '__main__':
    sys.exit(main())
