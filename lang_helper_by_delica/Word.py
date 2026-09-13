class Word:
    def __init__(self, word, english_def=""):
        self.word = word
        self.eng = english_def
        self.eng_meanings = english_def.split("/")
        self.is_perfect_cognate = self.word == self.eng
        if not self.is_perfect_cognate and len(self.eng_meanings) > 1:
            eng_word_index = 0
            while not self.is_perfect_cognate and eng_word_index < len(self.eng_meanings):
                curr_eng_word = self.eng_meanings[eng_word_index]
                self.is_perfect_cognate = self.word == curr_eng_word
                eng_word_index += 1

    def __str__(self):
        return self.word

    def get_word(self):
        return self.word

    def print_word(self):
        print(self.word)

    def get_english(self):
        return self.eng