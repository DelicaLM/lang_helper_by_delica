from lang_helper_by_delica.Adjective import Adjective


class FrenchAdjective(Adjective):
    def __init__(self, adj : str, english_def : str = "", before_noun : bool = False, is_invariable : bool = False,
                 is_loan_word : bool = False, masc_plur_form : str = "",
                 fem_sing_form : str ="", fem_plur_form : str = "", masc_sing_before_vowel : str = ""):
        masc_sing_form = adj
        self.masc_sing_before_vowel = masc_sing_form
        if masc_sing_before_vowel != "":
            self.masc_sing_before_vowel = masc_sing_before_vowel
        if is_invariable:
            masc_plur_form = masc_sing_form
            fem_sing_form = masc_sing_form
            fem_plur_form = masc_sing_form
        else:
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
                elif adj.endswith("eur"):
                    fem_sing_form = masc_sing_form[:-1] + "se"
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
        super().__init__(masc_sing_form, english_def=english_def, before_noun=before_noun, is_invariable=is_invariable,
                         is_loan_word=is_loan_word, fem_sing_form=fem_sing_form, fem_plur_form=fem_plur_form,
                         masc_sing_form=masc_sing_form, masc_plur_form=masc_plur_form)

    def print_forms(self):
        print(self.adj, f"({self.eng})")
        if self.is_invariable or self.is_loan_word:
            special_string = "Special Characteristics: "
            if self.is_invariable:
                special_string += "invariable"
            if self.is_loan_word:
                if self.is_invariable:
                    special_string += ", "
                special_string += "loan word"
            print(special_string)
        if self.before_noun:
            if self.masc_sing_before_vowel == self.masc_sing_form:
                print("Masculin Singulier:", self.masc_sing_form, "(e.g., Il est un", self.masc_sing_form, "homme.)")
            else:
                print("Masculin Singulier:", f"{self.masc_sing_form}/{self.masc_sing_before_vowel}","(e.g., Il est un",
                      self.masc_sing_form, "mari. Il est un", self.masc_sing_before_vowel, "homme.)")
        else:
            print("Masculin Singulier:", self.masc_sing_form, "(e.g., Il est un homme", f"{self.masc_sing_form}.)")
        if self.before_noun:
            print("Féminin Singulier:", self.fem_sing_form, "(e.g., Elle est une", self.fem_sing_form, "femme.)")
        else:
            print("Féminin Singulier:", self.fem_sing_form, "(e.g., Elle est une femme", f"{self.fem_sing_form}.)")
        if self.before_noun:
            print("Masculin Pluriel:", self.masc_plur_form, "(e.g., Ils sont des", self.masc_plur_form, "hommes.)")
        else:
            print("Masculin Pluriel:", self.masc_plur_form, "(e.g., Ils sont des hommes", f"{self.masc_plur_form}.)")
        if self.before_noun:
            print("Féminin Pluriel:", self.fem_plur_form, "(e.g., Elles sont des", self.fem_plur_form, "femmes.)")
        else:
            print("Féminin Pluriel:", self.fem_plur_form, "(e.g., Elles sont des femmes", f"{self.fem_plur_form}.)")