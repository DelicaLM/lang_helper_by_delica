from lang_helper_by_delica.SpanishIrregularVerb import SpanishIrregularVerb



ser = SpanishIrregularVerb("ser", "to be",
                           first_per_sing="soy", second_per_sing="eres", third_per_sing="es",
                           first_per_plur="somos", second_per_plur="sois", third_per_plur="son",)
ir = SpanishIrregularVerb("ir", "to go",
                          first_per_sing="voy", second_per_sing="vas", third_per_sing="va",
                          first_per_plur="vamos", second_per_plur="vais", third_per_plur="van",)
ir.print_conjugations()