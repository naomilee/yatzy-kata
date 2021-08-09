class Yatzy:
    """ This is a class for computing the Yatzy score for a given dice roll in a given category """

    def __init__(self, d1, d2, d3, d4, d5):
        self.dice = [0] * 5
        self.dice[0] = d1
        self.dice[1] = d2
        self.dice[2] = d3
        self.dice[3] = d4
        self.dice[4] = d5

    # Helper methods:

    def _sum_single_value(self, value):
        """ Helper for scoring: "Ones", "Twos", "Threes", "Fours", "Fives", "Sixes"

        Sums each of the dice which have the specified value """
        total = 0
        for die in self.dice:
            if die == value:
                total += value

        return total

    def _get_die_counts(self):
        """ Helper method: Computes a counts dictionary for the dice values

         The counts dictionary is 0-indexed and therefore stores the count
         for value x at index x - 1 """
        counts = [0] * 6
        for die in self.dice:
            counts[die - 1] += 1

        return counts

    def _score_x_of_a_kind(self, x):
        """ Helper for scoring: "Three of a Kind", "Four of a Kind" """
        counts = self._get_die_counts()

        for i in range(6):
            if counts[i] >= x:
                return (i + 1) * x
        return 0

    # Score computers:

    def chance(self):
        return sum(self.dice)

    def yatzy(self):
        # This method could be implemented using self._score_x_of_a_kind(5) for consistency
        # with the related scores ("Three of a Kind", "Four of a Kind") and therefore improved
        # maintainability, but this is intentionally implemented in a different way as the
        # purpose of this assignment is to generate a conversation about code
        if len(set(self.dice)) == 1:
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

        # Looking for the highest pair, so walk backwards
        for i in range(5, -1, -1):
            if counts[i] == 2:
                return (i + 1) * 2
        return 0

    def two_pair(self):
        counts = self._get_die_counts()

        pairs_found = 0
        score = 0
        # We want the highest two-pair possible, but it is not necessary to walk
        # backwards because there are at most 2 two-pairs in our 5 total dice
        for i in range(6):
            # Check for case where there are two doubles of different values
            if counts[i] in [2, 3]:
                pairs_found += 1
                score += 2 * (i + 1)
            # Check for the case where there are two doubles of the same value
            elif counts[i] == 4:
                pairs_found = 2
                score = 4 * (i + 1)

        if pairs_found == 2:
            return score
        else:
            return 0

    def four_of_a_kind(self):
        return self._score_x_of_a_kind(4)

    def three_of_a_kind(self):
        return self._score_x_of_a_kind(3)

    def small_straight(self):
        counts = self._get_die_counts()

        score = 30
        # There are 3 ways to get a small straight: 1-4, 2-5, 3-6
        # Note that the counts don't necessarily have to be 1's
        if counts[0] and counts[1] and counts[2] and counts[3]:
            return score
        if counts[1] and counts[2] and counts[3] and counts[4]:
            return score
        if counts[2] and counts[3] and counts[4] and counts[5]:
            return score
        # We could remove some redundant work in this function, but it would add code complexity
        # disproportionally to the amount of performance gain we would get

        return 0

    def large_straight(self):
        counts = self._get_die_counts()

        # If values 2 through 5 were each gotten exactly once, then the last die must be either a 1 or a 6
        if (counts[1] == 1 and
                counts[2] == 1 and
                counts[3] == 1 and
                counts[4] == 1):
            return 40
        return 0

    def full_house(self):
        counts = self._get_die_counts()

        if 2 in counts and 3 in counts:
            return 25
        else:
            return 0
