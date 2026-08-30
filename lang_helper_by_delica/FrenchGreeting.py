import Greeting
from lang_constants import *


class FrenchGreeting(Greeting):
    def __init__(self, greeting, gender=None, is_plural=False, masc_form=None, fem_form=None):
        super().__init__(greeting)
        self.is_plural = is_plural
        self.masc_form = masc_form
        self.fem_form = fem_form
        self.gender = gender
        if self.fem_form is None and self.masc_form is None and gender is None:
            self.gender = NO_GENDER

    def get_greeting(self):
        return self.greeting