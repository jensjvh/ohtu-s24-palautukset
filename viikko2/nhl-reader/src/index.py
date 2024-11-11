import requests
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2023-24/players"
    response = requests.get(url).json()

    players = [Player(player_dict) for player_dict in response if player_dict['nationality'] == 'FIN']

    players.sort(reverse=True,key=lambda player: player.points)

    print("Players from FIN:")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()