from lang_helper_by_delica.FrenchVerb import FrenchVerb
from lang_constants import FIRST_PERSON, SECOND_PERSON, THIRD_PERSON, PERSON_OPTIONS

class FrenchVerbRegER(FrenchVerb):
    def __init__(self, verb):
        super().__init__(verb)

    def conjugate(self, person, is_plural=False):
        assert len(self.verb) > 2
        assert person in PERSON_OPTIONS
        result = self.verb[:-2]
        if not person.is_plural:
            if person == FIRST_PERSON:
                result += "e"
            elif person == SECOND_PERSON:
                result += "es"
            else:
                result += "e"
        else:
            if person == FIRST_PERSON:
                result += "ons"
            elif person == SECOND_PERSON:
                result += "ez"
            else:
                result += "ent"