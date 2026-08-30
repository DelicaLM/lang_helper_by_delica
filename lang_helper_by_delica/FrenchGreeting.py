import Greeting
from lang_constants import *


class FrenchGreeting(Greeting):
    def __init__(self, greeting, is_formal=True, is_also_informal=False, times_of_day=None, gender=None, is_plural=False, masc_form=None, fem_form=None):
        super().__init__(greeting, is_formal, is_also_informal, times_of_day)
        self.is_plural = is_plural
        self.masc_form = masc_form
        self.fem_form = fem_form
        self.gender = gender
        if self.fem_form is None and self.masc_form is None and gender is None:
            self.gender = NO_GENDER


    def get_greeting(self):
        return self.greeting