from lang_helper_by_delica.Word import Word
from lang_constants import *


class Verb(Word):
    def __init__(self, verb, verb_type=BASIC_VERB_TYPE, first_per_sing=None, second_per_sing=None, third_per_sing=None,
                 first_per_plur=None, second_per_plur=None, third_per_plur=None,):
        super().__init__(verb)
        self.verb = verb
        self.verb_type = verb_type
        self.first_per_sing = first_per_sing
        self.second_per_sing = second_per_sing
        self.third_per_sing = third_per_sing
        self.first_per_plur = first_per_plur
        self.second_per_plur = second_per_plur
        self.third_per_plur = third_per_plur

    def get_verb(self):
        return self.verb

    def conjugate(self, person, is_plural=False):
        result = self.verb
        if not is_plural:
            if person == FIRST_PERSON:
                result = self.first_per_sing
            elif person == SECOND_PERSON:
                result = self.second_per_sing
            else:
                result = self.third_per_sing
        else:
            if person == FIRST_PERSON:
                result = self.first_per_plur
            elif person == SECOND_PERSON:
                result = self.second_per_plur
            else:
                result = self.third_per_plur
        return result