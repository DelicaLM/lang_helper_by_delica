from lang_helper_by_delica.Word import Word

class Adjective(Word):
    def __init__(self, adj, english_def="", before_verb=True, fem_sing_form="", fem_plur_form="",
                 masc_sing_form="", masc_plur_form=""):
        super().__init__(adj, english_def)
        self.adj = adj
        self.before_verb = before_verb
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




