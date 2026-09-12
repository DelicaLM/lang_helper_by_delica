from lang_helper_by_delica.Word import Word

class Adjective(Word):
    def __init__(self, adj, english_def="", before_verb=True, fem_sing_form="", fem_plur_form="",
                 masc_sing_form=""):
        super().__init__(adj, english_def)
        self.adj = adj
        self.before_verb = before_verb



