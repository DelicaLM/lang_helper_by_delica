from lang_helper_by_delica.FrenchVerb import FrenchVerb
from lang_constants import *

class FrenchVerbRegER(FrenchVerb):
    FIRST_PER_SING_END = "e"
    SECOND_PER_SING_END = "es"
    THIRD_PER_SING_END = "e"
    FIRST_PER_PLUR_END = "ons"
    SECOND_PER_PLUR_END = "ez"
    THIRD_PER_PLUR_END = "ent"
    def __init__(self, verb, english_def=""):
        assert len(verb) > 2
        verb_root = verb[:-2]
        first_per_sing_form = verb_root + self.FIRST_PER_SING_END
        second_per_sing_form = verb_root + self.SECOND_PER_SING_END
        third_per_sing_form = verb_root + self.THIRD_PER_SING_END
        first_per_plur_form = verb_root + self.FIRST_PER_PLUR_END
        second_per_plur_form = verb_root + self.SECOND_PER_PLUR_END
        third_per_plur_form = verb_root + self.THIRD_PER_PLUR_END
        super().__init__(verb, english_def=english_def, verb_type=FRENCH_REG_ER_VERB_TYPE,
                         first_per_sing=first_per_sing_form, second_per_sing=second_per_sing_form,
                         third_per_sing=third_per_sing_form, first_per_plur=first_per_plur_form,
                         second_per_plur=second_per_plur_form, third_per_plur=third_per_plur_form,)

    # def conjugate(self, person, is_plural=False):
    #     assert len(self.verb) > 2
    #     assert person in PERSON_OPTIONS
    #     result = self.verb[:-2]
    #     if not is_plural:
    #         if person == FIRST_PERSON:
    #             result += self.get_first_sing_person_ending()
    #         elif person == SECOND_PERSON:
    #             result += self.get_second_sing_person_ending()
    #         else:
    #             result += self.get_third_sing_person_ending()
    #     else:
    #         if person == FIRST_PERSON:
    #             result += self.get_first_plur_person_ending()
    #         elif person == SECOND_PERSON:
    #             result += self.get_second_plur_person_ending()
    #         else:
    #             result += self.get_third_plur_person_ending()
    #     return result
    #
    # @staticmethod
    # def get_first_sing_person_ending():
    #     return FrenchVerbRegER.FIRST_PER_SING_END
    #
    # @staticmethod
    # def get_second_sing_person_ending():
    #     return FrenchVerbRegER.SECOND_PER_SING_END
    #
    # @staticmethod
    # def get_third_sing_person_ending():
    #     return FrenchVerbRegER.THIRD_PER_SING_END
    #
    # @staticmethod
    # def get_first_plur_person_ending():
    #     return FrenchVerbRegER.FIRST_PER_PLUR_END
    #
    # @staticmethod
    # def get_second_plur_person_ending():
    #     return FrenchVerbRegER.SECOND_PER_PLUR_END
    #
    # @staticmethod
    # def get_third_plur_person_ending():
    #     return FrenchVerbRegER.THIRD_PER_PLUR_END