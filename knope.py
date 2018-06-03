#!/usr/bin/python3

import random

adjectives=[
    'poetic',
    'noble',
    'beautiful',
    'perfect',
    'cunning',
    'pliable',
    'chestnut-haired',
    'tricky',
    'rule-breaking',
    'thoughtful',
    'talented',
    'brilliant',
    'glowing',
    'coy'
]

nouns=[
    'land mermaid',
    'spinster',
    'sunflower',
    'sunfish',
    'minx',
    'moth',
    'unicorn-nurse',
    'musk-ox',
    'tropical fish',
    'sun goddess',
    'bastard'
]

def complimenter():
    adjective1 = random.choice(adjectives)
    adjective2 = random.choice(adjectives)
    noun = random.choice(nouns)
    compliment = 'Ann, you {}, {} {}!'.format(adjective1, adjective2, noun)
    return compliment

for i in range(20):
        print(complimenter())

