from lang_constants import *
from FrenchGreeting import FrenchGreeting
class FrenchGreeter:
    BONJOUR = FrenchGreeting("Bonjour", is_formal=True, times_of_day=[MORNING, AFTERNOON])
    BONSOIR = FrenchGreeting("Bonsoir", is_formal=True, times_of_day=[EVENING])
    SALUT = FrenchGreeting("Salut", is_formal=False, times_of_day=ALL_TIMES)
    AU_REVOIR = FrenchGreeting("Au revoir", is_formal=False, times_of_day=ALL_TIMES)

    def __init__(self):
        pass

    def say_hello(self, time_of_day=None, is_formal=True, spk_gender=None, recp_gender=None, recp_num=None):
        bonjour = self.BONJOUR.get_greeting()
        salut = self.SALUT.get_greeting()
        result = bonjour
        if not is_formal:
            result = salut
        return result
