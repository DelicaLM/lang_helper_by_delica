from lang_helper_by_delica.SpanishIrregularVerb import SpanishIrregularVerb
from lang_helper_by_delica.SpanishIrregularARVerb import SpanishIrregularARVerb
from lang_helper_by_delica.SpanishIrregularERVerb import SpanishIrregularERVerb
from lang_helper_by_delica.SpanishIrregularIRVerb import SpanishIrregularIRVerb



ser = SpanishIrregularVerb("ser", "to be",
                           first_per_sing="soy", second_per_sing="eres", third_per_sing="es",
                           first_per_plur="somos", second_per_plur="sois", third_per_plur="son",)
ir = SpanishIrregularVerb("ir", "to go",
                          first_per_sing="voy", second_per_sing="vas", third_per_sing="va",
                          first_per_plur="vamos", second_per_plur="vais", third_per_plur="van",)
dar = SpanishIrregularARVerb("dar", "to give", first_per_sing="doy", second_per_plur="dais")
estar = SpanishIrregularARVerb("estar", "to be (temporary states, locations)",
                               first_per_sing="estoy", second_per_sing="estás", third_per_sing="está",
                               third_per_plur="están")

caber = SpanishIrregularERVerb("caber", "to fit", first_per_sing="quepo")
caer = SpanishIrregularERVerb("caer", "to fit", first_per_sing="caigo")
haber = SpanishIrregularERVerb("haber", "to have (e.g., to have done/to exist)", first_per_sing="he",
                               second_per_sing="has", third_per_sing="ha", first_per_plur="hemos",
                               third_per_plur="han",)

conducir = SpanishIrregularIRVerb("conducir", "to drive", first_per_sing="conduzco")

haber.print_conjugations()