class Yatzy:

    def __init__(self, d1, d2, d3, d4, d5):
        self.dice = [0] * 5
        self.dice[0] = d1
        self.dice[1] = d2
        self.dice[2] = d3
        self.dice[3] = d4
        self.dice[4] = d5

    # Helper methods:

    def _sum_single_value(self, value):
        """ Helper for scoring: "Ones", "Twos", "Threes", "Fours", "Fives", "Sixes" """
        total = 0
        for die in self.dice:
            if die == value:
                total += value

        return total

    def _get_die_counts(self):
        """ Helper method: Computes a counts dictionary for the dice values """
        counts = [0] * 6
        for die in self.dice:
            counts[die - 1] += 1

        return counts

    # Score computers:

    def chance(self):
        return sum(self.dice)

    def yatzy(self):
        counts = self._get_die_counts()
        for i in range(len(counts)):
            if counts[i] == 5:
                return 50
        return 0

    def ones(self):
        return self._sum_single_value(1)

    def twos(self):
        return self._sum_single_value(2)

    def threes(self):
        return self._sum_single_value(3)

    def fours(self):
        return self._sum_single_value(4)

    def fives(self):
        return self._sum_single_value(5)

    def sixes(self):
        return self._sum_single_value(6)

    def score_pair(self):
        counts = self._get_die_counts()

        for at in range(6):
            if counts[6 - at - 1] == 2:
                return (6 - at) * 2
        return 0

    def two_pair(self):
        counts = self._get_die_counts()

        n = 0
        score = 0
        for i in range(6):
            if counts[6 - i - 1] >= 2:
                n = n + 1
                score += (6 - i)

        if n == 2:
            return score * 2
        else:
            return 0

    def four_of_a_kind(self):
        counts = self._get_die_counts()

        for i in range(6):
            if counts[i] >= 4:
                return (i + 1) * 4
        return 0

    def three_of_a_kind(self):
        counts = self._get_die_counts()

        for i in range(6):
            if counts[i] >= 3:
                return (i + 1) * 3
        return 0

    def small_straight(self):
        counts = self._get_die_counts()

        if (counts[1] == 1 and
                counts[2] == 1 and
                counts[3] == 1 and
                counts[4] == 1):
            if counts[0] == 1 or counts[5] == 1:
                return 30
        return 0

    def large_straight(self):
        counts = self._get_die_counts()

        if (counts[1] == 1 and
                counts[2] == 1 and
                counts[3] == 1 and
                counts[4] == 1
                and counts[5] == 1):
            return 40
        return 0

    def full_house(self):
        _2 = False
        _2_at = 0
        _3 = False
        _3_at = 0

        counts = self._get_die_counts()

        for i in range(6):
            if counts[i] == 2:
                _2 = True
                _2_at = i + 1

        for i in range(6):
            if counts[i] == 3:
                _3 = True
                _3_at = i + 1

        if _2 and _3:
            return 25
        else:
            return 0
