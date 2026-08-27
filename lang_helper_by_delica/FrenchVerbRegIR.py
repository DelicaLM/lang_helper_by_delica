from lang_helper_by_delica.FrenchVerb import FrenchVerb
from lang_constants import FIRST_PERSON, SECOND_PERSON, THIRD_PERSON, PERSON_OPTIONS

class FrenchVerbRegIR(FrenchVerb):
    def __init__(self, verb):
        super().__init__(verb)

    def conjugate(self, person, is_plural=False):
        assert len(self.verb) > 2
        assert person in PERSON_OPTIONS
        result = self.verb[:-2]
        if not person.is_plural:
            if person == FIRST_PERSON:
                result += "is"
            elif person == SECOND_PERSON:
                result += "is"
            else:
                result += "it"
        else:
            if person == FIRST_PERSON:
                result += "issons"
            elif person == SECOND_PERSON:
                result += "issez"
            else:
                result += "issent"
        return result