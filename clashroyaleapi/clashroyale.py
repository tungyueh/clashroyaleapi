import requests
from requests.utils import quote
from typing import Any, Dict, List, Optional

JsonDict = Dict[str, Any]


class ClanMember:
    def __init__(self, mapping):
        self._raw: JsonDict = mapping
        self.tag: str = self._raw['tag']
        self.name: str = self._raw['name']
        self.king_tower_level: int = self._raw['expLevel']
        self.trophies: int = self._raw['trophies']
        self.arena: JsonDict = self._raw['arena']
        self.clan_role: str = self._raw['role']
        self.clan_rank: Optional[int] = self._raw['clanRank']
        self.previous_clanRank: Optional[int] = self._raw['previousClanRank']
        self.donations: int = self._raw['donations']
        self.donations_received: int = self._raw['donationsReceived']
        self.clan_chest_points: int = self._raw.get('clanChestPoints', 0)

    def __repr__(self):
        return f'ClanMember(clan_rank={self.clan_rank}, ' \
               f'name={self.name}, ' \
               f'trophies={self.trophies}, ' \
               f'donations={self.donations}, ' \
               f'donations_received={self.donations_received}, ' \
               f'clan_chest_points={self.clan_chest_points})'


class Clan:
    def __init__(self, mapping):
        self._raw: Dict[str, Any] = mapping
        self.tag: str = self._raw['tag']
        self.name: str = self._raw['name']
        self.badge_id: int = self._raw['badgeId']
        self.type: str = self._raw['type']
        self.clan_score: int = self._raw['clanScore']
        self.required_trophies: int = self._raw['requiredTrophies']
        self.donations_per_week: int = self._raw['donationsPerWeek']
        self.clan_chest_level: int = self._raw['clanChestLevel']
        self.clan_chest_max_level: int = self._raw['clanChestMaxLevel']
        self.members: int = self._raw['members']
        self.location: JsonDict = self._raw['location']
        self.description: str = self._raw['description']
        self.clan_chest_status: str = self._raw['clanChestStatus']
        self.clan_chest_points: int = self._raw['clanChestPoints']
        self.memberList: List[ClanMember] = self._raw['memberList']


class WarClan:
    def __init__(self, mapping):
        self._raw: Dict[str, Any] = mapping
        self.badge_id: int = self._raw['badgeId']
        self.battles_played: int = self._raw['battlesPlayed']
        self.clan_score: int = self._raw['clanScore']
        self.crowns: int = self._raw['crowns']
        self.name: str = self._raw['name']
        self.participants: int = self._raw['participants']
        self.tag: str = self._raw['tag']
        self.wins: int = self._raw['wins']

    def __repr__(self):
        return f'WarClan(' \
               f'name={self.name}, ' \
               f'battles_played={self.battles_played}, ' \
               f'wins={self.wins},' \
               f'crowns={self.crowns}, ' \
               f'participants={self.participants})'


class WarStanding:
    def __init__(self, mapping):
        self._raw: Dict[str, Any] = mapping
        self.clan: WarClan = self._raw['clan']
        self.trophy_change: int = self._raw['trophyChange']

    def __repr__(self):
        return f'WarStanding(' \
               f'clan={self.clan}, ' \
               f'trophy_change={self.trophy_change})'


class WarParticipant:
    def __init__(self, mapping):
        self._raw: Dict[str, Any] = mapping
        self.tag: str = self._raw['tag']
        self.name: str = self._raw['name']
        self.cards_earned: int = self._raw['cardsEarned']
        self.battles_played: int = self._raw['battlesPlayed']
        self.wins: int = self._raw['wins']

    def __repr__(self):
        return f'WarParticipant(' \
               f'name={self.name}, ' \
               f'cards_earned={self.cards_earned}, ' \
               f'battles_played={self.battles_played}, ' \
               f'wins={self.wins})'


class WarLog:
    def __init__(self, mapping):
        self._raw: Dict[str, Any] = mapping
        self.season_id: int = self._raw['seasonId']
        self.created_date: str = self._raw['createdDate']
        self.participants: List[WarParticipant] = self._raw['participants']
        self.standings: List[WarStanding] = self._raw['standings']


class CurrentWar:
    def __init__(self, mapping):
        self._raw: Dict[str, Any] = mapping
        self.war_end_time: str = self._raw['warEndTime']
        self.clan: WarClan = self._raw['clan']
        self.participants: List[WarParticipant] = self._raw['participants']


class Player:
    def __init__(self, mapping):
        self._raw: Dict[str, Any] = mapping
        self.tag: str = self._raw['tag']
        self.name: str = self._raw['name']
        self.king_tower_level: int = self._raw['expLevel']
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

        self.clan_role: Optional[str] = self._raw.get('role')  # Maybe No Clan

        self.donations: int = self._raw['donations']
        self.donations_received: int = self._raw['donationsReceived']
        self.total_donations: int = self._raw['totalDonations']

        self.war_day_wins: int = self._raw['warDayWins']
        self.clan_cards_collected: int = self._raw['clanCardsCollected']

        self.clan: Optional[JsonDict] = self._raw.get('clan')  # Maybe No Clan

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


class BattleProfile:
    def __init__(self, mapping):
        self._raw: JsonDict = mapping
        self.tag: str = self._raw['tag']
        self.name: str = self._raw['name']
        self.crowns: int = self._raw['crowns']
        self.cards: List[Card] = self._raw['cards']

        self.clan: Optional[JsonDict] = self._raw.get('clan')  # Maybe No Clan
        self.starting_trophies: int = self._raw.get('startingTrophies')
        self.trophy_change: int = self._raw.get('trophyChange', 0)


class BattleLog:
    def __init__(self, mapping):
        self._raw: JsonDict = mapping
        self.type: str = self._raw['type']
        self.battle_time: str = self._raw['battleTime']
        self.arena: str = self._raw['arena']['name']
        self.game_mode: str = self._raw['gameMode']['name']
        self.deck_selection: str = self._raw['deckSelection']
        self.team_profile: List[BattleProfile] = self._raw['team']
        self.opponent_profile: List[BattleProfile] = self._raw['opponent']
        self.__post_init__()

    def __post_init__(self):
        if self.team_profile[0].crowns > self.opponent_profile[0].crowns:
            self.win = True
        else:
            self.win = False


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

        def clan_json_hook(dct: JsonDict):
            if 'clanRank' in dct:
                return ClanMember(dct)
            elif 'requiredTrophies' in dct:
                return Clan(dct)
            return dct
        self._clan_json_hook = clan_json_hook

        def war_json_hook(dct: JsonDict):
            if 'battlesPlayed' in dct and 'participants' in dct:
                return WarClan(dct)
            elif 'clan' in dct and 'trophyChange' in dct:
                return WarStanding(dct)
            elif 'cardsEarned' in dct:
                return WarParticipant(dct)
            elif 'seasonId' in dct:
                return WarLog(dct)
            elif 'warEndTime' in dct:
                return CurrentWar(dct)
            return dct
        self._war_json_hook = war_json_hook

        def player_json_hook(dct: JsonDict):
            if 'currentFavouriteCard' in dct:
                return Player(dct)
            elif 'maxLevel' in dct:
                return Card(dct)
            elif 'index' in dct:
                return Chest(dct)
            elif 'battleTime' in dct:
                return BattleLog(dct)
            elif 'crowns' in dct and 'cards' in dct:
                return BattleProfile(dct)
            return dct
        self._player_json_hook = player_json_hook

    def get_clan(self, clan_tag: Optional[str]=None) -> Clan:
        if clan_tag is None:
            clan_tag = self.clan_tag

        resp = requests.get(self.api_url + '/clans/' + quote(clan_tag),
                            headers=self.auth)
        resp.raise_for_status()
        return resp.json(object_hook=self._clan_json_hook)

    def list_clan_member(self, clan_tag: Optional[str]=None
                         ) -> List[ClanMember]:
        if clan_tag is None:
            clan_tag = self.clan_tag

        resp = requests.get(self.api_url + '/clans/' + quote(clan_tag) +
                            '/members',
                            headers=self.auth)
        resp.raise_for_status()
        return resp.json(object_hook=self._clan_json_hook)['items']

    def list_clan_war_log(self, clan_tag: Optional[str]=None) -> List[WarLog]:
        if clan_tag is None:
            clan_tag = self.clan_tag

        resp = requests.get(self.api_url + '/clans/' + quote(clan_tag) +
                            '/warlog',
                            headers=self.auth)
        resp.raise_for_status()
        return resp.json(object_hook=self._war_json_hook)['items']

    def get_clan_current_war(self, clan_tag: Optional[str]=None
                             ) -> CurrentWar:
        if clan_tag is None:
            clan_tag = self.clan_tag
        resp = requests.get(self.api_url + '/clans/' + quote(clan_tag) +
                            '/currentwar',
                            headers=self.auth)
        resp.raise_for_status()
        return resp.json(object_hook=self._war_json_hook)

    def get_player(self, player_tag: Optional[str]=None) -> Player:
        if player_tag is None:
            player_tag = self.player_tag

        resp = requests.get(self.api_url + '/players/' + quote(player_tag),
                            headers=self.auth)
        resp.raise_for_status()
        return resp.json(object_hook=self._player_json_hook)

    def get_player_upcoming_chest(self, player_tag: Optional[str]=None
                                  ) -> List[Chest]:
        if player_tag is None:
            player_tag = self.player_tag

        resp = requests.get(self.api_url + '/players/' + quote(player_tag) +
                            '/upcomingchests',
                            headers=self.auth)
        resp.raise_for_status()
        return resp.json(object_hook=self._player_json_hook)['items']

    def get_player_battle_log(self, player_tag: Optional[str]=None
                              ) -> List[BattleLog]:
        if player_tag is None:
            player_tag = self.player_tag

        resp = requests.get(self.api_url + '/players/' + quote(player_tag) +
                            '/battlelog',
                            headers=self.auth)
        resp.raise_for_status()
        return resp.json(object_hook=self._player_json_hook)

    def list_card(self) -> List[Card]:
        resp = requests.get(self.api_url + '/cards', headers=self.auth)
        resp.raise_for_status()
        return resp.json(object_hook=self._player_json_hook)['items']


