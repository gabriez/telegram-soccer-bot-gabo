import httpx
from constants import get_settings

class FootballAPIClient:
    def __init__(self):
        self.settings = get_settings()
        self.base_url = "https://v3.football.api-sports.io"
        self.headers = {
            'x-apisports-key': self.settings.football_token
        }

    def get_team_info(self, team_name: str):
        url = f"{self.base_url}/teams?search={team_name}"
        response = httpx.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def get_player_info(self, player_name: str):
        url = f"{self.base_url}/players/profiles?search={player_name}"
        response = httpx.get(url, headers=self.headers)
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()
