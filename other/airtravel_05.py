"""Model for aircraft flights."""
from pprint import pprint as pp

class Flight:
    
    def __init__(self, number):
        self._number = number
        
    def number(self):
        return self._number

rows, seats = (range(0, 23), 'ABCDEF')
x = [None] + [{letter: None for letter in seats} for _ in rows]
pp(x)
