from lang_helper_by_delica.SpanishVerbRegIR import SpanishVerbRegIR
from lang_constants import *

class SpanishIrregularIRVerb(SpanishVerbRegIR):
    def __init__(self, verb, english_def="", verb_type=SPANISH_IRREGULAR_IR_VERB_TYPE,
                 first_per_sing=None, second_per_sing=None, third_per_sing=None,
                 first_per_plur=None, second_per_plur=None, third_per_plur=None):
        super().__init__(verb, english_def=english_def)
        if first_per_sing is not None:
            self.first_per_sing = first_per_sing
        if second_per_sing is not None:
            self.second_per_sing = second_per_sing
        if third_per_sing is not None:
            self.third_per_sing = third_per_sing
        if first_per_plur is not None:
            self.first_per_plur = first_per_plur
        if second_per_plur is not None:
            self.second_per_plur = second_per_plur
        if third_per_plur is not None:
            self.third_per_plur = third_per_plur
