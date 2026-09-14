from lang_helper_by_delica.Word import Word

class Adjective(Word):
    def __init__(self, adj : str = "adjective", english_def : str = "", before_noun : bool = True,
                 is_invariable : bool = False, is_loan_word : bool = False, fem_sing_form="", fem_plur_form="",
                 masc_sing_form="", masc_plur_form=""):
        super().__init__(adj, english_def)
        self.adj = adj
        self.before_noun = before_noun
        self.is_invariable = is_invariable
        self.is_loan_word = is_loan_word
        if is_invariable:
            self.masc_sing_form = self.adj
            self.fem_sing_form = self.adj
            self.masc_plur_form = self.adj
            self.fem_plur_form = self.adj
        else:
            if fem_sing_form != "":
                self.fem_sing_form = fem_sing_form
            else:
                self.fem_sing_form = adj
            if fem_plur_form != "":
                self.fem_plur_form = fem_plur_form
            else:
                self.fem_plur_form = adj
            if masc_sing_form != "":
                self.masc_sing_form = masc_sing_form
            else:
                self.masc_sing_form = adj
            if masc_plur_form != "":
                self.masc_plur_form = masc_plur_form
            else:
                self.masc_plur_form = adj




