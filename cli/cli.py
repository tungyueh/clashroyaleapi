import argparse
import cmd
import json
import readline
import os
import sys
from typing import List

from pprint import pprint

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

    def do_get_clan(self, _):
        """Get information about a single clan by clan tag."""
        clan = self.cr_client.get_clan()
        pprint(clan._raw)

    def do_list_clan_member(self, _):
        """List clan members."""
        clan_member = self.cr_client.list_clan_member()
        for m in clan_member:
            print(m)

    def do_list_clan_war_log(self, _):
        """Retrieve clan's clan war log"""
        clan_war_log = self.cr_client.list_clan_war_log()
        for war_log in clan_war_log:
            print(f'Season={war_log.season_id} Date={war_log.created_date}')
            print(f'Collection day: ')
            for war_participant in war_log.participants:
                print(f'  {war_participant}')
            print(f'War day: ')
            for war_standing in war_log.standings:
                print(f'  {war_standing}')
            print('')

    def do_get_clan_current_war(self, _):
        """Retrieve information about clan's current clan war"""
        clan_current_war = self.cr_client.get_clan_current_war()
        print(f'war end time: {clan_current_war.war_end_time}')
        print(clan_current_war.clan)
        for war_participant in clan_current_war.participants:
            print(f'  {war_participant}')

    def do_get_player(self, _):
        """Get information about a single player by player tag."""
        player = self.cr_client.get_player()
        if self.verbose:
            pprint(player._raw)
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
