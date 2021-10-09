class Player:
    """A code template for a player of HiLo game. The responsibility of this 
      class of objects is to guess if the next card is higher or lower than the current card, 
      keep track of score, and determine whether or not it can play again.

      Attributes:
          guess (char): A character h/H or l/L.
          score (int): keeping track of current score
          will_play(char): A yes or no input from user
      """

    def __init__(self):
        self.guess = ""
        self.score = 0
        self.will_play = True

    # setters
    def set_guess(self):
        self.guess = input()

    def set_score(self, s):
        self.score = s

    def set_will_play(self):
        if (input().lower() == 'y'):
            self.will_play = True
        else:
            self.will_play = False

    # getters
    def get_guess(self):
        return self.guess

    def get_score(self):
        return self.score

    def get_will_play(self):
        return self.will_play
