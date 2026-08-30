from lang_helper_by_delica.Verb import Verb


class IrregularVerb(Verb):
    def __init__(self, irreg_verb, first_per_sing, second_per_sing, third_per_sing,
                 first_per_plur, second_per_plur, third_per_plur):
        super().__init__(irreg_verb)