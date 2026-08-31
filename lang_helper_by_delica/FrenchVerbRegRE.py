from lang_helper_by_delica.FrenchVerb import FrenchVerb
from lang_constants import *

class FrenchVerbRegRE(FrenchVerb):
    FIRST_PER_SING_END = "s"
    SECOND_PER_SING_END = "s"
    THIRD_PER_SING_END = ""
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
        super().__init__(verb, english_def=english_def, verb_type=FRENCH_REG_RE_VERB_TYPE,
                         first_per_sing=first_per_sing_form, second_per_sing=second_per_sing_form,
                         third_per_sing=third_per_sing_form, first_per_plur=first_per_plur_form,
                         second_per_plur=second_per_plur_form, third_per_plur=third_per_plur_form,)

    #
    # @staticmethod
    # def get_first_sing_person_ending():
    #     return "s"
    #
    # @staticmethod
    # def get_second_sing_person_ending():
    #     return "s"
    #
    # @staticmethod
    # def get_third_sing_person_ending():
    #     return ""
    #
    # @staticmethod
    # def get_first_plur_person_ending():
    #     return "ons"
    #
    # @staticmethod
    # def get_second_plur_person_ending():
    #     return "ez"
    #
    # @staticmethod
    # def get_third_plur_person_ending():
    #     return "ent"