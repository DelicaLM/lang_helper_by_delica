from lang_helper_by_delica.Word import Word

class Noun(Word):
    def __init__(self, noun, english_def=""):
        super().__init__(noun, english_def)
        self.noun = noun


