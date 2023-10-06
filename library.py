import random

class Library():
    def __init__(self, card=''):
        self.card = card
    
    def generate_card(self):
        cardnum = []
        for i in range(0, 8):
            num = random.randint(0, 9)
            cardnum.append(str(num))
            card = ''.join(cardnum)
        return card
        
    def get_access(self, card):
        if card:
            return True