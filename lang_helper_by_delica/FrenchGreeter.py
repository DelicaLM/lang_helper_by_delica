from lang_constants import *
from FrenchGreeting import FrenchGreeting
class FrenchGreeter:
    BONJOUR = FrenchGreeting("Bonjour")
    SALUT = FrenchGreeting("Salut")
    AU_REVOIR = FrenchGreeting("Au revoir")

    def __init__(self):
        pass

    def say_hello(self, is_formal=True, spk_gender=None, recp_gender=None, recp_num=None):
        bonjour = self.BONJOUR.get_greeting()
        salut = self.SALUT.get_greeting()
        result = bonjour
        if not is_formal:
            result = salut
        return result
