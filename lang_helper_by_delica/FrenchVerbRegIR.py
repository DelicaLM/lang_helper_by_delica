from lang_helper_by_delica.FrenchVerb import FrenchVerb
from lang_constants import *

class FrenchVerbRegIR(FrenchVerb):
    FIRST_PER_SING_END = "is"
    SECOND_PER_SING_END = "is"
    THIRD_PER_SING_END = "it"
    FIRST_PER_PLUR_END = "issons"
    SECOND_PER_PLUR_END = "issez"
    THIRD_PER_PLUR_END = "issent"
    def __init__(self, verb, english_def=""):
        assert len(verb) > 2
        verb_root = verb[:-2]
        first_per_sing_form = verb_root + self.FIRST_PER_SING_END
        second_per_sing_form = verb_root + self.SECOND_PER_SING_END
        third_per_sing_form = verb_root + self.THIRD_PER_SING_END
        first_per_plur_form = verb_root + self.FIRST_PER_PLUR_END
        second_per_plur_form = verb_root + self.SECOND_PER_PLUR_END
        third_per_plur_form = verb_root + self.THIRD_PER_PLUR_END
        super().__init__(verb, english_def=english_def, verb_type=FRENCH_REG_IR_VERB_TYPE,
                         first_per_sing=first_per_sing_form, second_per_sing=second_per_sing_form,
                         third_per_sing=third_per_sing_form, first_per_plur=first_per_plur_form,
                         second_per_plur=second_per_plur_form, third_per_plur=third_per_plur_form,)

    #
    # @staticmethod
    # def get_first_sing_person_ending():
    #     return "is"
    #
    # @staticmethod
    # def get_second_sing_person_ending():
    #     return "is"
    #
    # @staticmethod
    # def get_third_sing_person_ending():
    #     return "it"
    #
    # @staticmethod
    # def get_first_plur_person_ending():
    #     return "issons"
    #
    # @staticmethod
    # def get_second_plur_person_ending():
    #     return "issez"
    #
    # @staticmethod
    # def get_third_plur_person_ending():
    #     return "issent"