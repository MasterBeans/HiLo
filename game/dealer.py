import random
from game.player import Player


class Dealer:

    def __init__(self):
        self.card = 0
        self.player = Player()
        self.player.set_score(300)
        self.draw_card()

    def draw_card(self):
        self.card = random.randint(1, 13)

    def is_Lower(self, card1, card2):
        if card1 > card2:
            return True

    def calculate_score(self, card1, card2):
        if self.is_Lower(card1, card2) and self.player.get_guess().lower() == 'l':
            self.player.set_score(self.player.get_score() + 100)
        elif not(self.is_Lower(card1, card2)) and self.player.get_guess().lower() == 'h':
            self.player.set_score(self.player.get_score() + 100)
        else:
            self.player.set_score(self.player.get_score() - 75)

    def can_play(self):
        if self.player.get_score() > 0 and self.player.get_will_play():
            return True
        else:
            return False

    def play(self):
        while self.can_play():
            prev_card = self.card
            print(f'This card is {prev_card}')
            print(f'Higher or lower [h/l] ', end='')
            self.player.set_guess()
            self.draw_card()
            next_card = self.card
            print(f'Next card was : {next_card}')
            self.calculate_score(prev_card, next_card)
            print(f"Your score is: {self.player.get_score()}")
            if self.player.get_score() > 0:
                print(f'Keep playing? [y/n] ', end='')
                self.player.set_will_play()
            print()
        print(f'GAME OVER')
        print(f'Thank you for playing!')
