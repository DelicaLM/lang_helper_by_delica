class Word:
    def __init__(self, word, english_def=""):
        self.word = word
        self.eng = english_def

    def __str__(self):
        return self.word

    def get_word(self):
        return self.word

    def print_word(self):
        print(self.word)

    def get_english(self):
        return self.eng