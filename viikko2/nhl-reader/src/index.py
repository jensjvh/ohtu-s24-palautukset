import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self._url = url

    def get_players(self):
        response = requests.get(self._url).json()
        return [Player(player_dict) for player_dict in response]
    
class PlayerStats:
    def __init__(self, reader):
        self._reader = reader
    
    def top_scorers_by_nation(self, nationality):
        players = self._reader.get_players()
        filtered_players = [player for player in players
                            if player.nationality == nationality]
        filtered_players.sort(reverse=True, key=lambda player: player.points)
        return filtered_players

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    reader = PlayerReader(url)
    nationality = "FIN"
    players = PlayerStats(reader).top_scorers_by_nation(nationality)

    print("Players from FIN:")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()