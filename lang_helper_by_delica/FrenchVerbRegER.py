from lang_helper_by_delica.FrenchVerb import FrenchVerb
from lang_constants import FIRST_PERSON, SECOND_PERSON, THIRD_PERSON, PERSON_OPTIONS

class FrenchVerbRegER(FrenchVerb):
    def __init__(self, verb, english_def=""):
        super().__init__(verb, english_def)

    def conjugate(self, person, is_plural=False):
        assert len(self.verb) > 2
        assert person in PERSON_OPTIONS
        result = self.verb[:-2]
        if not is_plural:
            if person == FIRST_PERSON:
                result += self.get_first_sing_person_ending()
            elif person == SECOND_PERSON:
                result += self.get_second_sing_person_ending()
            else:
                result += self.get_third_sing_person_ending()
        else:
            if person == FIRST_PERSON:
                result += self.get_first_plur_person_ending()
            elif person == SECOND_PERSON:
                result += self.get_second_plur_person_ending()
            else:
                result += self.get_third_plur_person_ending()
        return result

    @staticmethod
    def get_first_sing_person_ending():
        return "e"

    @staticmethod
    def get_second_sing_person_ending():
        return "es"

    @staticmethod
    def get_third_sing_person_ending():
        return "e"

    @staticmethod
    def get_first_plur_person_ending():
        return "ons"

    @staticmethod
    def get_second_plur_person_ending():
        return "ez"

    @staticmethod
    def get_third_plur_person_ending():
        return "ent"