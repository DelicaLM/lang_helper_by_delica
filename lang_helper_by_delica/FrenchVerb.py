from lang_helper_by_delica.Verb import Verb
from lang_constants import *

class FrenchVerb(Verb):
    def __init__(self, verb, english_def="", verb_type=BASIC_VERB_TYPE,
                 first_per_sing=None, second_per_sing=None, third_per_sing=None,
                 first_per_plur=None, second_per_plur=None, third_per_plur=None):
        super().__init__(verb, english_def=english_def, verb_type=verb_type, first_per_sing=first_per_sing,
                         second_per_sing=second_per_sing, third_per_sing=third_per_sing, first_per_plur=first_per_plur,
                         second_per_plur=second_per_plur, third_per_plur=third_per_plur)
        self.eng = english_def

    def print_conjugations(self):
        print(self.verb, f"({self.eng})")
        print("Je", " "*7, self.first_per_sing)
        print("Tu", " "*7, self.second_per_sing)
        print("Il/Elle/On", self.third_per_sing)
        print("Nous", " "*5, self.first_per_plur)
        print("Vous", " "*5, self.second_per_plur)
        print("Ils/Elles ", self.third_per_plur)
        print("")