
def first(word):
    return word[0]

def acronym(words):
    acro = ''
    acro = acro.join(list(map(first,words))).upper()
    return acro

words = ['Situation', 'normal', 'all', 'fucked', 'up']

#acro = list(map(first,words))

acro = acronym(words)
print(acro)
