from lang_helper_by_delica.FrenchVerbRegER import FrenchVerbRegER
from lang_helper_by_delica.FrenchVerbRegCER import FrenchVerbRegCER
from lang_helper_by_delica.FrenchVerbRegCER import FrenchVerbRegCER

test_verb = FrenchVerbRegCER("commencer", "to sing")
conj1_je = test_verb.conjugate(1, False)
conj2_tu = test_verb.conjugate(2, False)
conj3_on = test_verb.conjugate(3, False)
conj4_nous = test_verb.conjugate(1, True)
conj5_vous = test_verb.conjugate(2, True)
conj6_ils = test_verb.conjugate(3, True)
test = 0