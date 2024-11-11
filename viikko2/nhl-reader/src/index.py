import requests
from player import Player
from rich import print as rich_print
from rich.prompt import Prompt
from rich.table import Table
from rich.console import Console

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

    rich_print("NHL statistics by nationality")

    while True:
        season = Prompt.ask("Select season [2018-19/2019-20/0220-21/2021-22/2022-23/2023-24/2024-25/]")
        if season == "":
            break

        while True:
            nationality = Prompt.ask("Select nationality [AUT/CZE/AUS/SWE/GER/DEN/SUI/SVK/NOR/RUS/CAN/LAT/BLR/SLO/USA/FIN/GBR/]")
            if nationality == "":
                break

            table = Table(title=f'Top scorers of {nationality} season {season}')
            table.add_column('name')
            table.add_column('team')
            table.add_column('goals')
            table.add_column('assists')
            table.add_column('points')

            players = PlayerStats(reader).top_scorers_by_nation(nationality)

            for player in players:
                table.add_row(player.name, player.team, str(player.goals), str(player.assists),
                              str(player.goals + player.assists))
                
            rich_print(table)

if __name__ == "__main__":
    main()