from lang_helper_by_delica.SpanishVerb import SpanishVerb
from lang_constants import *

class SpanishVerbRegAR(SpanishVerb):
    FIRST_PER_SING_END = "o"
    SECOND_PER_SING_END = "as"
    THIRD_PER_SING_END = "a"
    FIRST_PER_PLUR_END = "amos"
    SECOND_PER_PLUR_END = "áis"
    THIRD_PER_PLUR_END = "an"
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
#
# from lang_helper_by_delica.SpanishVerb import SpanishVerb
# from lang_constants import *
#
# class SpanishVerbRegAR(SpanishVerb):
#     def __init__(self, verb, english_def=""):
#         super().__init__(verb, english_def)
#
#     def conjugate(self, person, is_plural=False):
#         assert len(self.verb) > 2
#         assert person in PERSON_OPTIONS
#         result = self.verb[:-2]
#         if not is_plural:
#             if person == FIRST_PERSON:
#                 result += self.get_first_sing_person_ending()
#             elif person == SECOND_PERSON:
#                 result += self.get_second_sing_person_ending()
#             else:
#                 result += self.get_third_sing_person_ending()
#         else:
#             if person == FIRST_PERSON:
#                 result += self.get_first_plur_person_ending()
#             elif person == SECOND_PERSON:
#                 result += self.get_second_plur_person_ending()
#             else:
#                 result += self.get_third_plur_person_ending()
#         return result
#
#     @staticmethod
#     def get_first_sing_person_ending():
#         return "o"
#
#     @staticmethod
#     def get_second_sing_person_ending():
#         return "as"
#
#     @staticmethod
#     def get_third_sing_person_ending():
#         return "a"
#
#     @staticmethod
#     def get_first_plur_person_ending():
#         return "amos"
#
#     @staticmethod
#     def get_second_plur_person_ending():
#         return "áis"
#
#     @staticmethod
#     def get_third_plur_person_ending():
#         return "an"