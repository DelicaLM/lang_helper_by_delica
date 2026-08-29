from FrenchNoun import FrenchNoun
from lang_constants import *

fr_school_nouns = [FrenchNoun("bureau", MASCULINE, "desk"),
                   FrenchNoun("chaise", FEMININE, "chair"),
                   FrenchNoun("stylo", MASCULINE, "pen"),
                   FrenchNoun("crayon", MASCULINE, "pencil"),
                   FrenchNoun("école", FEMININE, "school"),
                   FrenchNoun("livre", MASCULINE, "book"),
                   FrenchNoun("lycée", MASCULINE, "high school"),
                   FrenchNoun("collège", MASCULINE, "middle school"),
                   FrenchNoun("sac à dos", MASCULINE, "backpack"),
                   FrenchNoun("calculatrice", FEMININE, "calculator"),
                   FrenchNoun("tableau", MASCULINE, "chalkboard/blackboard"),
                   FrenchNoun("salle de classe", FEMININE, "classroom"),
                   FrenchNoun("classe", FEMININE, "class"),
                   FrenchNoun("cours", MASCULINE, "course"),
                   FrenchNoun("ordinateur", MASCULINE, "computer"),
                   FrenchNoun("portable", MASCULINE, "laptop"),
                   FrenchNoun("dictionnaire", MASCULINE, "dictionary"),
                   FrenchNoun("gomme", FEMININE, "eraser"),
                   FrenchNoun("cahier", MASCULINE, "notebook"),
                   FrenchNoun("examen", MASCULINE, "test/exam"),
                   FrenchNoun("papier", MASCULINE, "paper"),
                ]


fr_aspirated_h_nouns = [FrenchNoun("hache", FEMININE, "axe", is_aspirated=True),
                     FrenchNoun("haie", FEMININE, "hedge", is_aspirated=True),
                     FrenchNoun("haïku", MASCULINE, "haiku", is_aspirated=True),
                     FrenchNoun("haine", FEMININE, "hate", is_aspirated=True),
                     FrenchNoun("hamac", MASCULINE, "hammock", is_aspirated=True),
                     FrenchNoun("hamburger", MASCULINE, "hamburger", is_aspirated=True),
                     FrenchNoun("hamster", MASCULINE, "hamster", is_aspirated=True),
                     ]

fr_unaspirated_h_nouns = [FrenchNoun("homme", MASCULINE, "man"),
                       FrenchNoun("hiver", MASCULINE, "winter"),
                       FrenchNoun("honneur", MASCULINE, "honour"),
                       FrenchNoun("habitude", FEMININE, "habit"),
                       FrenchNoun("harmonie", FEMININE, "harmony"),
                       FrenchNoun("hélicoptère", MASCULINE, "helicopter"),
                       FrenchNoun("herbe", FEMININE, "grass"),
                       FrenchNoun("heure", FEMININE, "hour"),
                       FrenchNoun("histoire", FEMININE, "story/history"),
                       FrenchNoun("hôpital", MASCULINE, "hospital"),
                       FrenchNoun("huile", FEMININE, "oil"),
                       FrenchNoun("humain", MASCULINE, "human"),
                       ]

fr_season_nouns = [FrenchNoun("printemps", MASCULINE, "spring"),
                FrenchNoun("été", MASCULINE, "summer"),
                FrenchNoun("automne", MASCULINE, "autumn"),
                FrenchNoun("hiver", MASCULINE, "winter"),]

fr_days_of_week_nouns = [FrenchNoun("jour", MASCULINE, "day"),
                      FrenchNoun("semaine", FEMININE, "week"),
                      FrenchNoun("lundi", MASCULINE, "Monday"),
                      FrenchNoun("mardi", MASCULINE, "Tuesday"),
                      FrenchNoun("mercredi", MASCULINE, "Wednesday"),
                      FrenchNoun("jeudi", MASCULINE, "Thursday"),
                      FrenchNoun("vendredi", MASCULINE, "Friday"),
                      FrenchNoun("samedi", MASCULINE, "Saturday"),
                      FrenchNoun("dimanche", MASCULINE, "Sunday"),]

fr_months_nouns = [FrenchNoun("janvier", MASCULINE, "January"),
                   FrenchNoun("février", MASCULINE, "February"),
                   FrenchNoun("mars", MASCULINE, "March"),
                   FrenchNoun("avril", MASCULINE, "April"),
                   FrenchNoun("mai", MASCULINE, "May"),
                   FrenchNoun("juin", MASCULINE, "June"),
                   FrenchNoun("juillet", MASCULINE, "July"),
                   FrenchNoun("août", MASCULINE, "August"),
                   FrenchNoun("septembre", MASCULINE, "September"),
                   FrenchNoun("octobre", MASCULINE, "October"),
                   FrenchNoun("janvier", MASCULINE, "january"),
                   FrenchNoun("janvier", MASCULINE, "january"),
                   ]
for noun in fr_months_nouns:
    print(noun.get_noun_with_def_article(), "[" + noun.gender + "]", "(" + noun.get_english() +")")