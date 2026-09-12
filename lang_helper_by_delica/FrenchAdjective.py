from lang_helper_by_delica.Adjective import Adjective


class FrenchAdjective(Adjective):
    def __init__(self, adj : str, english_def : str = "", before_verb : bool = False):
        super().__init__(adj, english_def=english_def, before_verb=before_verb)
