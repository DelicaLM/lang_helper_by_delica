from lang_helper_by_delica.SpanishVerb import SpanishVerb
from lang_constants import *

class SpanishIrregularVerb(SpanishVerb):
    def __init__(self, verb, english_def="", verb_type=SPANISH_IRREGULAR_VERB_TYPE,
                 first_per_sing=None, second_per_sing=None, third_per_sing=None,
                 first_per_plur=None, second_per_plur=None, third_per_plur=None):
        super().__init__(verb, english_def=english_def, verb_type=verb_type, first_per_sing=first_per_sing,
                         second_per_sing=second_per_sing, third_per_sing=third_per_sing, first_per_plur=first_per_plur,
                         second_per_plur=second_per_plur, third_per_plur=third_per_plur)
        self.eng = english_def
