from lang_helper_by_delica.FrenchVerbRegER import FrenchVerbRegER
from lang_constants import FIRST_PERSON, SECOND_PERSON, THIRD_PERSON, PERSON_OPTIONS

class FrenchVerbRegELER(FrenchVerbRegER):
    def __init__(self, verb, english_def=""):
        super().__init__(verb, english_def)

    def conjugate(self, person, is_plural=False):
        result = super().conjugate(person, is_plural)
        if not is_plural or person == THIRD_PERSON:
            assert len(self.verb) > 3
            result = self.verb[:-2]
            if person == FIRST_PERSON:
                result += self.get_first_sing_person_ending()
            elif person == SECOND_PERSON:
                result += self.get_second_sing_person_ending()
            elif person == THIRD_PERSON:
                if not is_plural:
                    result += self.get_third_sing_person_ending()
                else:
                    result += self.get_third_plur_person_ending()
        return result

    @staticmethod
    def get_first_sing_person_ending():
        return "le"

    @staticmethod
    def get_second_sing_person_ending():
        return "les"

    @staticmethod
    def get_third_sing_person_ending():
        return "le"

    @staticmethod
    def get_third_plur_person_ending():
        return "lent"

