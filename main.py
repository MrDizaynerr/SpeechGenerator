import random as r

# import pymorphy2 as morpher

sft_letters = ['а', 'и', 'о', 'э', 'у', 'я', 'е', 'ё', 'ы', 'ю']
str_letters = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п',
               'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']

sft_weighs = [801, 735, 1097, 32, 262, 201, 845, 4, 190, 64]
str_weighs = [159, 454, 170, 298, 94, 165, 121, 349, 440, 321, 670, 281, 473,
              547, 626, 26, 97, 48, 144, 73, 36]

all_letters = (str_letters, sft_letters)
all_weighs = (str_weighs, sft_weighs)

prepositions = [', a', ', но', ', да', ' и']


def generate_syllable():
    lengh = r.randint(2, 3)
    begfrom = r.choices([0, 1], weights=[275, 145])[0]
    res = ''
    res += r.choices(all_letters[begfrom], weights=all_weighs[begfrom])[0]
    if lengh == 2 and res[0] in str_letters:
        res += r.choices(sft_letters, weights=sft_weighs)[0]
    elif lengh == 2 and res[0] in sft_letters:
        res += r.choices(str_letters, weights=str_weighs)[0]
    elif lengh == 3 and res[0] in str_letters:
        res += r.choices(sft_letters, weights=sft_weighs)[0]
        res += r.choices(str_letters, weights=str_weighs)[0]
    else:
        res += r.choices(str_letters, weights=str_weighs)[0]
        res += r.choices(sft_letters, weights=sft_weighs)[0]
    return res


def generate_word(big):
    lengh = r.randint(1, 5)
    res = ''
    res += generate_syllable()
    while res[0] == 'ы':
        res = generate_syllable()
    for _ in range(lengh - 1):
        res += generate_syllable()
    #   mrph = morpher.MorphAnalyzer()
    #   res = mrph.parse(res)[0].normal_form
    if big is True:
        res = res.title()
    return res


def generate_sentence():
    lengh = r.randint(2, 20)
    res = ''
    res += generate_word(True)
    for _ in range(lengh):
        if r.randint(0, 10) == 1:
            res += r.choice(prepositions)
        res += ' ' + generate_word(False)
    res += '. '
    return res


def generate_paragraph():
    lengh = r.randint(3, 20)
    res = ''
    for _ in range(lengh):
        res += generate_sentence()
    res += '\n'
    return res


print(generate_paragraph())
