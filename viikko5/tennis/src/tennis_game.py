DEUCE_SCORE = 4
SCORE_NAMES = ["Love", "Fifteen", "Thirty", "Forty"]

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score += 1
        else:
            self.player2_score += 1
    
    def get_equal_score(self):
        score = self.player1_score

        if score >= 3:
            return "Deuce"
        return f"{SCORE_NAMES[score]}-All"
    
    def get_advantage_score(self):
        score_difference = self.player1_score - self.player2_score
        if score_difference == 1:
            return f"Advantage {self.player1_name}"
        elif score_difference == -1:
            return f"Advantage {self.player2_name}"
        elif score_difference >= 2:
            return f"Win for {self.player1_name}"
        else:
            return f"Win for {self.player2_name}"

    def get_normal_score(self):
        return f"{SCORE_NAMES[self.player1_score]}-{SCORE_NAMES[self.player2_score]}"

    def get_score(self):
        score = ""

        if self.player1_score == self.player2_score:
            score = self.get_equal_score()

        elif self.player1_score >= DEUCE_SCORE or self.player2_score >= DEUCE_SCORE:
            score = self.get_advantage_score()

        else:
            score = self.get_normal_score()

        return score
