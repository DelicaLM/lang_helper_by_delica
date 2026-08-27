from lang_helper_by_delica.FrenchVerbRegER import FrenchVerbRegER
from lang_constants import FIRST_PERSON, SECOND_PERSON, THIRD_PERSON, PERSON_OPTIONS

class FrenchVerbRegGER(FrenchVerbRegER):
    def __init__(self, verb, english_def):
        super().__init__(verb, english_def)

    def conjugate(self, person, is_plural=False):
        result = super().conjugate(person, is_plural)
        if person == FIRST_PERSON and is_plural:
            assert len(self.verb) > 3
            result = self.verb[:-1] + self.get_first_plur_person_ending()
        return result

    @staticmethod
    def get_first_plur_person_ending():
        return "çons"

