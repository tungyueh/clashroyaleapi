import requests
from requests.utils import quote
from typing import Any, Dict, List, Optional

JsonDict = Dict[str, Any]


class Player:
    def __init__(self, mapping):
        self._raw: Dict[str, Any] = mapping
        self.tag: str = self._raw['tag']
        self.name: str = self._raw['name']
        self.king_tower_levle: int = self._raw['expLevel']
        self.trophies: int = self._raw['trophies']
        self.highest_trophies: int = self._raw['bestTrophies']

        self.arena: JsonDict = self._raw['arena']

        self.battle_count: int = self._raw['battleCount']
        self.wins: int = self._raw['wins']
        self.losses: int = self._raw['losses']
        self.three_crown_wins: int = self._raw['threeCrownWins']

        self.challenge_cards_won: int = self._raw['challengeCardsWon']
        self.challenge_max_wins: int = self._raw['challengeMaxWins']

        self.tournament_cards_won: int = self._raw['tournamentCardsWon']
        self.tournament_battle_count: int = self._raw['tournamentBattleCount']

        self.clan_role: str = self._raw['role']

        self.donations: int = self._raw['donations']
        self.donations_received: int = self._raw['donationsReceived']
        self.total_donations: int = self._raw['totalDonations']

        self.war_day_wins: int = self._raw['warDayWins']
        self.clan_cards_collected: int = self._raw['clanCardsCollected']

        self.clan: JsonDict = self._raw['clan']

        self.league_statistics: JsonDict = self._raw['leagueStatistics']

        self.achievements: JsonDict = self._raw['achievements']

        self.cards: List[Card] = self._raw['cards']
        self.current_favourite_card: Card = self._raw['currentFavouriteCard']

    def __repr__(self):
        return f'Player(tag={self.tag}, ' \
               f'name={self.name}, ' \
               f'trophies={self.trophies})'


class Chest:
    def __init__(self, mapping):
        self._raw: JsonDict = mapping
        self.index: int = self._raw['index']
        self.name: str = self._raw['name']


class Card:
    def __init__(self, mapping):
        self._raw: JsonDict = mapping
        self.name: str = self._raw['name']
        self.max_level: int = self._raw['maxLevel']
        self.icon_url: JsonDict = self._raw['iconUrls']

        self.id: int = self._raw.get('id')
        self.level: int = self._raw.get('level')
        self.count: int = self._raw.get('count')

    def __repr__(self):
        return f'Card(' \
               f'name={self.name}, ' \
               f'level={self.level}, ' \
               f'max_level={self.max_level},' \
               f'count={self.count})'


class ClashRoyaleClient:
    def __init__(self, token: str, player_tag: str, clan_tag: str):
        self.token = token
        self.player_tag = player_tag
        self.clan_tag = clan_tag
        self.auth = {'Authorization': 'Bearer ' + self.token}
        self.api_version = 'v1'
        self.base_url = 'https://api.clashroyale.com/'
        self.api_url = self.base_url + self.api_version

        def json_hook(dct: JsonDict):
            if 'currentFavouriteCard' in dct:
                return Player(dct)
            elif 'maxLevel' in dct:
                return Card(dct)
            elif 'index' in dct:
                return Chest(dct)
            return dct
        self._json_hook = json_hook

    def get_player(self, player_tag: Optional[str]=None) -> Player:
        if player_tag is None:
            player_tag = self.player_tag

        resp = requests.get(self.api_url + '/players/' + quote(player_tag),
                            headers=self.auth)
        resp.raise_for_status()
        return resp.json(object_hook=self._json_hook)

    def get_player_upcoming_chest(self, player_tag: Optional[str]=None
                                  ) -> List[Chest]:
        if player_tag is None:
            player_tag = self.player_tag

        resp = requests.get(self.api_url + '/players/' + quote(player_tag) +
                            '/upcomingchests',
                            headers=self.auth)
        resp.raise_for_status()
        return resp.json(object_hook=self._json_hook)['items']


    def get_player_battle_log(self,):
        pass

    def list_card(self) -> List[Card]:
        resp = requests.get(self.api_url + '/cards', headers=self.auth)
        resp.raise_for_status()
        return resp.json(object_hook=self._json_hook)['items']


