from lang_helper_by_delica.FrenchWord import FrenchWord
from lang_constants import *

import error_helper_by_delica as error_lib

class FrenchNoun(FrenchWord):
    def __init__(self, noun, gender, english_def="", is_plural=False, is_aspirated=False):
        error_lib.check_type(noun, str, "french noun")
        error_lib.check_value_is_in_set(gender, FRENCH_WORD_GENDERS, "french noun gender")
        error_lib.check_type(english_def, str, "french noun english definition")
        super().__init__(noun, english_def)
        assert len(noun) > 0
        self.noun = noun.lower()
        self.gender = gender
        self.eng = english_def
        self.is_plural = is_plural
        self.is_aspirated = is_aspirated
        self.indef_article = "un"
        if self.gender == FEMININE:
            self.indef_article = "une"
        if is_plural:
            self.indef_article = "des"
        self.def_article = "le"
        if self.gender == FEMININE:
            self.def_article = "la"
        first_char = self.noun[0]
        if first_char in FRENCH_VOWELS or first_char == "h" and is_aspirated:
            self.def_article = "l\'"
        if is_plural:
            self.def_article = "les"

    def get_noun_with_indef_article(self):
        return self.indef_article + " " + self.noun

    def get_noun_with_def_article(self):
        result = self.def_article + " " + self.noun
        if self.def_article == "l\'":
            result = self.def_article + self.noun
        return result






