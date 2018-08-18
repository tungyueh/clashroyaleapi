import argparse
import cmd
import readline
import os
import sys
from typing import List

from clashroyaleapi.clashroyale import ClashRoyaleClient, Card


def enable_mac_auto_complete():
    if 'libedit' in readline.__doc__:
        readline.parse_and_bind("bind ^I rl_complete")
    else:
        readline.parse_and_bind("tab: complete")


class ClashRoyaleCLI(cmd.Cmd):
    def __init__(self, token):
        self.history_file = os.path.expanduser('~/.clashroyale_cli_history')
        self.prompt = 'ClashRoyale: '
        self.clash_royale_client = ClashRoyaleClient(token)
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
        readline.add_history(line)
        return line

    def do_list_card(self, _):
        """List all cards"""
        cards: List[Card] = self.clash_royale_client.list_card()
        for card in cards:
            print(card)


def main():
    parser = argparse.ArgumentParser(prog='ucc_cli')
    parser.add_argument('-a', '--auth_file', metavar='auth_file', type=str,
                        default='', help='A path to auth_file.')
    args = parser.parse_args()
    auth_file = args.auth_file
    with open(auth_file, 'rb') as fp:
        token = fp.read()

    cc3_cli = ClashRoyaleCLI(token.decode())
    cc3_cli.cmdloop()


if __name__ == '__main__':
    sys.exit(main())
