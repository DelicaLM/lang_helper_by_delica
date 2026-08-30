import random
from lang_constants import *
from FrenchGreeting import FrenchGreeting

class FrenchGreeter:
    BONJOUR = FrenchGreeting("Bonjour", is_formal=True, is_also_informal=True, times_of_day=[MORNING, AFTERNOON])
    BONSOIR = FrenchGreeting("Bonsoir", is_formal=True, is_also_informal=True, times_of_day=[EVENING, NIGHT])
    BONNE_NUIT = FrenchGreeting("Bonne nuit", times_of_day=[LATE_EVENING, NIGHT])
    SALUT = FrenchGreeting("Salut", is_formal=False, times_of_day=ALL_TIMES)
    AU_REVOIR = FrenchGreeting("Au revoir", is_formal=False, times_of_day=ALL_TIMES)
    COUCOU = FrenchGreeting("Coucou", is_formal=False, times_of_day=ALL_TIMES)

    def __init__(self):
        pass

    def say_hello(self, time_of_day=None, is_formal=True, spk_gender=None, recp_gender=None, recp_num=None):
        bonjour = self.BONJOUR.get_greeting()
        bonsoir = self.BONSOIR.get_greeting()
        salut = self.SALUT.get_greeting()
        coucou = self.COUCOU.get_greeting()
        result_options = []
        if time_of_day in MORNING_TIMES or time_of_day in AFTERNOON_TIMES:
            result_options.append(bonjour)
        else:
            result_options.append(bonsoir)
        if not is_formal:
            result_options.append(salut)
            result_options.append(coucou)
        assert len(result_options) > 0
        result = random.choice(result_options)
        return result
