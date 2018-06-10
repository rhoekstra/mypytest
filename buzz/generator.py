from __future__ import print_function
import random

#buzz = ('continuous testing', 'continuous integration',
#    'continuous deployment', 'continuous improvement', 'devops')
buzz = ('schoenlepel', 'vaag', 'computers', 'fietssleutel', 'variatie')
#adjectives = ('complete', 'modern', 'self-service', 'integrated', 'end-to-end')
adjectives = ('gedaan', 'glimmend', 'voltooid' 'geintegreerd', 'volledig')
#adverbs = ('remarkably', 'enormously', 'substantially', 'significantly',
#    'seriously')
adverbs = ('bijzonder', 'gigantisch', 'enorm', 'extreem',
    'grappig')
#verbs = ('accelerates', 'improves', 'enhances', 'revamps', 'boosts')
verbs = ('harder', 'beter', 'mooier', 'herbouwd', 'sneller')

def sample(l, n = 1):
    result = random.sample(l, n)
    if n == 1:
        return result[0]
    return result

def generate_buzz():
    buzz_terms = sample(buzz, 2)
    phrase = ' '.join([sample(adjectives), buzz_terms[0], sample(adverbs),
        sample(verbs), buzz_terms[1]])
    return phrase.title()

if __name__ == "__main__":
    print(generate_buzz())
