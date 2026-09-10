from lang_helper_by_delica.Verb import Verb
from lang_helper_by_delica.lang_constants import *

class IrregularVerb(Verb):
    def __init__(self, irreg_verb, irreg_verb_type=IRREGULAR_VERB_TYPE, first_per_sing=None, second_per_sing=None,
                 third_per_sing=None, first_per_plur=None, second_per_plur=None, third_per_plur=None):
        super().__init__(irreg_verb, first_per_sing=first_per_sing, second_per_sing=second_per_sing,
                         third_per_sing=third_per_sing, first_per_plur=first_per_plur, second_per_plur=second_per_plur,
                         third_per_plur=third_per_plur)