import Word
from lang_constants import *

class Greeting(Word):
    def __init__(self, greeting, is_formal=True):
        super().__init__(greeting)
        self.is_formal = is_formal

    def get_greeting(self):
        return self.greeting
