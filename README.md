# Command-Line Interface using Official API of Clash Royale 
[![Build Status](https://api.travis-ci.com/tungyueh/clashroyaleapi.svg?branch=master)](https://travis-ci.com/tungyueh/clashroyaleapi)
[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)

CLI using Clash Royale Official API

## How to use CLI
1. Go to https://developer.clashroyale.com/#/ to create a key
2. Fill in token, player_tag and clan_tag in auth file
3. `pip install .`
3. `cr-cli -a [file_path] [-v]`

## Auth File Format
Please refer sample_auth.json

```
{
    "player_tag": "",
    "clan_tag": "",
    "token": ""
}
```

## How to use ClashRoyaleClient
``` python
from clashroyaleapi import ClashRoyaleClient
cr_client = ClashRoyaleClient(TOKEN, PLAYER_TAG, CLAN_TAG)
```
## Methods
`get_clan(self, clan_tag: Optional[str] = None) -> Clan`

`list_clan_member(self, clan_tag: Optional[str] = None) -> List[ClanMember]`

`list_clan_war_log(self, clan_tag: Optional[str] = None) -> List[WarLog]`

`get_clan_current_war(self, clan_tag: Optional[str] = None) -> CurrentWar`

`get_player(self, player_tag: Optional[str] = None) -> Player`

`get_player_upcoming_chest(self, player_tag: Optional[str] = None) -> List[Chest]`

`get_player_battle_log(self, player_tag: Optional[str] = None) -> List[BattleLog]`

`list_card(self) -> List[Card]`
