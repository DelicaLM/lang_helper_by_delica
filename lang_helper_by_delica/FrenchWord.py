from lang_helper_by_delica.Word import Word

class FrenchWord(Word):
    def __init__(self, word, english_def):
        super().__init__(word)
        self.word = word
        self.eng = english_def

    def get_english(self):
        return self.eng

    def print_english(self):
        print(self.eng)