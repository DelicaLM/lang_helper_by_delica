from FrenchNoun import FrenchNoun
from lang_constants import *

school_nouns = [FrenchNoun("bureau", MASCULINE, "desk"),
                FrenchNoun("chaise", FEMININE, "chair"),
                FrenchNoun("stylo", MASCULINE, "pen"),
                FrenchNoun("crayon", MASCULINE, "pencil"),
                FrenchNoun("école", FEMININE, "school"),
                FrenchNoun("livre", MASCULINE, "book"),
                ]

for school_noun in school_nouns:
    print(school_noun.get_noun_with_indef_article(), "[" + school_noun.gender + "]", "(" + school_noun.get_english() +")")