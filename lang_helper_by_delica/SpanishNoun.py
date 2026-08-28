from lang_helper_by_delica.SpanishWord import SpanishWord
from lang_constants import *

import error_helper_by_delica as error_lib

class SpanishNoun(SpanishWord):
    def __init__(self, noun, gender, english_def="", is_plural=False, starts_with_stressed_a=False):
        error_lib.check_type(noun, str, "spanish noun")
        error_lib.check_value_is_in_set(gender, SPANISH_WORD_GENDERS, "spanish noun gender")
        error_lib.check_type(english_def, str, "spanish noun english definition")
        super().__init__(noun, english_def)
        assert len(noun) > 0
        self.noun = noun.lower()
        self.gender = gender
        self.eng = english_def
        self.is_plural = is_plural
        self.starts_with_stressed_a = starts_with_stressed_a
        self.indef_article = "un"
        if self.gender == FEMININE:
            self.indef_article = "una"
        if is_plural:
            if self.gender == MASCULINE:
                self.indef_article = "unos"
            else:
                self.indef_article = "unas"
        self.def_article = "el"
        if self.gender == FEMININE and not starts_with_stressed_a:
            self.def_article = "la"
        if is_plural:
            if self.gender == MASCULINE:
                self.def_article = "los"
            else:
                self.def_article = "las"

    def get_noun_with_indef_article(self):
        return self.indef_article + " " + self.noun

    def get_noun_with_def_article(self):
        return self.def_article + " " + self.noun







