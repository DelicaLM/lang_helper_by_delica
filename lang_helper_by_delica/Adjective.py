from lang_helper_by_delica.Word import Word

class Adjective(Word):
    def __init__(self, adj, english_def=""):
        super().__init__(adj, english_def)
        self.adj = adj


