import Word
from lang_constants import *

class Greeting(Word):
    def __init__(self, greeting, is_formal=True, is_also_informal=False, times_of_day=None):
        super().__init__(greeting)
        self.is_formal = is_formal
        self.is_also_informal = is_also_informal
        self.times_of_day = times_of_day

    def get_greeting(self):
        return self.greeting
