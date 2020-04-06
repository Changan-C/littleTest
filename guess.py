class Solution:
    def game(self, guess , answer):
        """
        :type guess : list[int]
        :type answer: list[int]
        rtype: int
        """
        return sum(guess[i]==answer[i] for i in range(len(guess)))
