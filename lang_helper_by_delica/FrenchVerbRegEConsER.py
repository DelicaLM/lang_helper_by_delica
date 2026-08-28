from lang_helper_by_delica.FrenchVerbRegER import FrenchVerbRegER
from lang_constants import FIRST_PERSON, SECOND_PERSON, THIRD_PERSON, PERSON_OPTIONS

class FrenchVerbRegEConsER(FrenchVerbRegER):
    def __init__(self, verb, english_def=""):
        super().__init__(verb, english_def)

    def conjugate(self, person, is_plural=False):
        result = super().conjugate(person, is_plural)
        if not is_plural or person == THIRD_PERSON:
            assert len(result) > 3
            verb_len = len(self.verb)
            result = result[:verb_len-4] + "è" + result[verb_len-3:]
        return result



