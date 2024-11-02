import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_no_matching_name(self):
        name = "Owen"
        self.assertEqual(None, self.stats.search(name))

    def test_name_match(self):
        name = "Semenko"
        player = Player("Semenko", "EDM", 4, 12)
        self.assertEqual(str(player), str(self.stats.search(name)))

    def test_players_team(self):
        team_name = "EDM"
        players = [Player("Semenko", "EDM", 4, 12),
                   Player("Kurri",   "EDM", 37, 53),
                   Player("Gretzky", "EDM", 35, 89)]
        players_on_team = self.stats.team(team_name)
        
        self.assertEqual(len(players), len(players_on_team))

        for i in range(0, len(players)):
            self.assertEqual(str(players[i]), str(players_on_team[i]))

    def test_sort_by_points(self):
        top_players = self.stats.top(2, SortBy.POINTS)
        expected_players = [
            Player("Gretzky", "EDM", 35, 89),
            Player("Lemieux", "PIT", 45, 54),
            Player("Yzerman", "DET", 42, 56)
        ]
        print(top_players)
        self.assertEqual(len(top_players), len(expected_players))

        for i in range(0, len(top_players)):
            self.assertEqual(str(top_players[i]), str(expected_players[i]))

    def test_sort_by_goals(self):
        top_players = self.stats.top(2, SortBy.GOALS)
        expected_players = [
            Player("Lemieux", "PIT", 45, 54),
            Player("Yzerman", "DET", 42, 56),
            Player("Kurri",   "EDM", 37, 53)
        ]
        print(top_players)
        self.assertEqual(len(top_players), len(expected_players))

        for i in range(0, len(top_players)):
            self.assertEqual(str(top_players[i]), str(expected_players[i]))

    def test_sort_by_assists(self):
        top_players = self.stats.top(2, SortBy.ASSISTS)
        expected_players = [
            Player("Gretzky", "EDM", 35, 89),
            Player("Yzerman", "DET", 42, 56),
            Player("Lemieux", "PIT", 45, 54)
        ]
        print(top_players)
        self.assertEqual(len(top_players), len(expected_players))

        for i in range(0, len(top_players)):
            self.assertEqual(str(top_players[i]), str(expected_players[i]))