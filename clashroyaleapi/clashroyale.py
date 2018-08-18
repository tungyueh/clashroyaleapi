from dataclasses import dataclass
import requests

from typing import Any, Dict, List

JsonDict = Dict[str, Any]


@dataclass
class Card:
    name: str
    id: str
    max_level: str

    def __init__(self, mapping):
        self._raw: JsonDict = mapping
        self.name: str = self._raw['name']
        self.id: int = self._raw['id']
        self.max_level: int = self._raw['maxLevel']
        self.icon_url: Dict[str, str] = self._raw['iconUrls']


class ClashRoyaleClient:
    def __init__(self, token: str):
        self.token = token
        self.auth = {'Authorization': 'Bearer ' + self.token}
        self.api_version = 'v1'
        self.base_url = 'https://api.clashroyale.com/'
        self.api_url = self.base_url + self.api_version

        def json_card_hook(dct: JsonDict):
            if 'name' in dct:
                return Card(dct)
            return dct
        self._json_card_hook = json_card_hook

    def list_card(self) -> List[Card]:
        resp = requests.get(self.api_url + '/cards', headers=self.auth)
        resp.raise_for_status()
        return resp.json(object_hook=self._json_card_hook)['items']


