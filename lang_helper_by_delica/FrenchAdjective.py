from lang_helper_by_delica.Adjective import Adjective


class FrenchAdjective(Adjective):
    def __init__(self, adj : str, english_def : str = "", before_verb : bool = False, masc_plur_form : str = "",
                 fem_sing_form : str ="", fem_plur_form : str = ""):
        masc_sing_form = adj
        if fem_sing_form == "":
            if adj.endswith("f"):
                fem_sing_form = masc_sing_form[:-1] + "ve"
            elif adj.endswith("x"):
                fem_sing_form = masc_sing_form[:-1] + "se"
            elif adj.endswith("el"):
                fem_sing_form = masc_sing_form + "le"
            elif adj.endswith("en") or adj.endswith("on"):
                fem_sing_form = masc_sing_form + "ne"
            elif adj.endswith("et"):
                fem_sing_form = masc_sing_form + "te"
            elif adj.endswith("e"):
                fem_sing_form = masc_sing_form
            elif adj.endswith("eau"):
                fem_sing_form = masc_sing_form[:-2] + "lle"
            else:
                fem_sing_form = adj + "e"
        if fem_plur_form == "":
            fem_plur_form = fem_sing_form + "s"
        if masc_plur_form == "":
            if masc_sing_form.endswith("x") or masc_sing_form.endswith("s"):
                masc_plur_form = masc_sing_form
            elif adj.endswith("eau"):
                masc_plur_form = masc_sing_form + "x"
            elif adj.endswith("al"):
                masc_plur_form = masc_sing_form[:-1] + "ux"
            else:
                masc_plur_form = masc_sing_form + "s"
        super().__init__(masc_sing_form, english_def=english_def, before_verb=before_verb, fem_sing_form=fem_sing_form,
                         fem_plur_form=fem_plur_form, masc_sing_form=masc_sing_form, masc_plur_form=masc_plur_form)

    def print_forms(self):
        print(self.adj, f"({self.eng})")
        print("Masculin Singulier:", self.masc_sing_form, "(e.g., Il est", self.masc_sing_form)
        print("Féminin Singulier:", self.fem_sing_form)
        print("Masculin Pluriel:", self.masc_plur_form)
        print("Féminin Pluriel:", self.fem_plur_form)