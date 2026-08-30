import Word
from lang_constants import *

class Greeting(Word):
    def __init__(self, greeting):
        super().__init__(greeting)

    def get_greeting(self):
        return self.greeting
