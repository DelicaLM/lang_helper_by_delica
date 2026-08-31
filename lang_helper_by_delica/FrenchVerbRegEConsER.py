from lang_helper_by_delica.FrenchVerb import FrenchVerb
from lang_constants import *

class FrenchVerbRegEConsER(FrenchVerb):
    FIRST_PER_SING_END = "e"
    SECOND_PER_SING_END = "es"
    THIRD_PER_SING_END = "e"
    FIRST_PER_PLUR_END = "ons"
    SECOND_PER_PLUR_END = "ez"
    THIRD_PER_PLUR_END = "ent"
    def __init__(self, verb, english_def=""):
        assert len(verb) > 4
        verb_cons = verb[-3]
        verb_root = verb[:-4]
        first_per_sing_form = verb_root + "è"  + verb_cons + self.FIRST_PER_SING_END
        second_per_sing_form = verb_root + "è"  + verb_cons + self.SECOND_PER_SING_END
        third_per_sing_form = verb_root + "è"  + verb_cons + self.THIRD_PER_SING_END
        first_per_plur_form = verb_root + verb[-4] + verb_cons + self.FIRST_PER_PLUR_END
        second_per_plur_form = verb_root + verb[-4] + verb_cons + self.SECOND_PER_PLUR_END
        third_per_plur_form = verb_root + "è"  + verb_cons + self.THIRD_PER_PLUR_END
        super().__init__(verb, english_def=english_def, verb_type=FRENCH_REG_E_CONS_ER_VERB_TYPE,
                         first_per_sing=first_per_sing_form, second_per_sing=second_per_sing_form,
                         third_per_sing=third_per_sing_form, first_per_plur=first_per_plur_form,
                         second_per_plur=second_per_plur_form, third_per_plur=third_per_plur_form,)

#
# from lang_helper_by_delica.FrenchVerbRegER import FrenchVerbRegER
# from lang_constants import FIRST_PERSON, SECOND_PERSON, THIRD_PERSON, PERSON_OPTIONS
#
# class FrenchVerbRegEConsER(FrenchVerbRegER):
#     def __init__(self, verb, english_def=""):
#         super().__init__(verb, english_def)
#
#     def conjugate(self, person, is_plural=False):
#         result = super().conjugate(person, is_plural)
#         if not is_plural or person == THIRD_PERSON:
#             assert len(result) > 3
#             verb_len = len(self.verb)
#             result = result[:verb_len-4] + "è" + result[verb_len-3:]
#         return result
#
#
#
