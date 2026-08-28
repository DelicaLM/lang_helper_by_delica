from lang_helper_by_delica.FrenchWord import FrenchWord


class FrenchVerb(FrenchWord):
    def __init__(self, verb, english_def=""):
        super().__init__(verb, english_def)
        self.verb = verb
        self.eng = english_def

    def conjugate(self, person, is_plural=False):
        return self.verb


