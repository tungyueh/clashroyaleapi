import unittest
import json

from clashroyaleapi import *


class TestClashRoyaleClient(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        with open('auth.json', 'rb') as fp:
            auth = fp.read()

        auth_json = json.loads(auth)
        token = auth_json['token']
        player_tag = auth_json['player_tag']
        clan_tag = auth_json['clan_tag']

        self.cr_client = ClashRoyaleClient(token, player_tag, clan_tag)
        super().__init__(*args, **kwargs)

    def test_get_clan(self):
        clan = self.cr_client.get_clan()
        self.assertIsInstance(clan, Clan)

    def test_list_clan_member(self):
        clan_member = self.cr_client.list_clan_member()
        for member in clan_member:
            self.assertIsInstance(member, ClanMember)

    def test_list_clan_war_log(self):
        clan_war_log = self.cr_client.list_clan_war_log()
        for war_log in clan_war_log:
            self.assertIsInstance(war_log, WarLog)

    def test_get_clan_current_war(self):
        current_war = self.cr_client.get_clan_current_war()
        self.assertIsInstance(current_war, CurrentWar)

    def test_get_player(self):
        player = self.cr_client.get_player()
        self.assertIsInstance(player, Player)

    def test_get_player_upcoming_chest(self):
        upcomming_chest = self.cr_client.get_player_upcoming_chest()
        for chest in upcomming_chest:
            self.assertIsInstance(chest, Chest)

    def test_get_player_battle_log(self):
        battle_logs = self.cr_client.get_player_battle_log()
        for battle_log in battle_logs:
            self.assertIsInstance(battle_log, BattleLog)

    def test_list_card(self):
        cards = self.cr_client.list_card()
        for card in cards:
            self.assertIsInstance(card, Card)


if __name__ == '__main__':
    unittest.main()
