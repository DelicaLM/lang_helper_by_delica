from lang_helper_by_delica.Verb import Verb


class FrenchVerb(Verb):
    def __init__(self, verb, english_def=""):
        super().__init__(verb)
        self.eng = english_def
