from lang_helper_by_delica import Word


class Verb(Word):
    def __init__(self, verb):
        super().__init__(verb)
        self.verb = verb
        self.verb_type = None

    def get_word(self):
        return self.verb

    def conjugate(self, person, is_plural=False):
        return self.verb