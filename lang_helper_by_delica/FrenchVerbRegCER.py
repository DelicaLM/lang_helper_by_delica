from lang_helper_by_delica.FrenchVerb import FrenchVerb
from lang_constants import *

class FrenchVerbRegCER(FrenchVerb):
    FIRST_PER_SING_END = "e"
    SECOND_PER_SING_END = "es"
    THIRD_PER_SING_END = "e"
    FIRST_PER_PLUR_END = "çons"
    SECOND_PER_PLUR_END = "ez"
    THIRD_PER_PLUR_END = "ent"
    def __init__(self, verb, english_def=""):
        assert len(verb) > 3
        verb_root = verb[:-2]
        first_per_sing_form = verb_root + self.FIRST_PER_SING_END
        second_per_sing_form = verb_root + self.SECOND_PER_SING_END
        third_per_sing_form = verb_root + self.THIRD_PER_SING_END
        first_per_plur_form = verb_root + self.FIRST_PER_PLUR_END
        second_per_plur_form = verb_root + self.SECOND_PER_PLUR_END
        third_per_plur_form = verb_root + self.THIRD_PER_PLUR_END
        super().__init__(verb, english_def=english_def, verb_type=FRENCH_REG_CER_VERB_TYPE,
                         first_per_sing=first_per_sing_form, second_per_sing=second_per_sing_form,
                         third_per_sing=third_per_sing_form, first_per_plur=first_per_plur_form,
                         second_per_plur=second_per_plur_form, third_per_plur=third_per_plur_form)


