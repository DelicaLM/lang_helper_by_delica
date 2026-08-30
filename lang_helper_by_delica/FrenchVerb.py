from lang_helper_by_delica.Verb import Verb
from lang_constants import *

class FrenchVerb(Verb):
    def __init__(self, verb, english_def="", verb_type=BASIC_VERB_TYPE,
                 first_per_sing=None, second_per_sing=None, third_per_sing=None,
                 first_per_plur=None, second_per_plur=None, third_per_plur=None):
        super().__init__(verb, verb_type)
        self.eng = english_def



