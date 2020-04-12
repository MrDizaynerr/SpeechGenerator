import random as r

word_bank = []
weig_bank = []

try:
    with open('wrdBank', 'r') as dat:
        word_bank = dat.read().split()
    with open('wgtBank', 'r') as dat:
        for i in dat.read().split():
            try:
                weig_bank.append(int(i))
            except:
                continue
    dat.close()
except:
    print("НЕ СЧИТАНО")


def teaching():
    buh = ''
    while True:
        x = input()
        if x:
            buh += x + ' '
        else:
            break
    wrd = ''
    buh += ' '

    for i in buh:
        if i.isalpha():
            wrd += i
        else:
            if wrd not in word_bank:
                word_bank.append(wrd)
                wrd = ''
                weig_bank.append(1)
            else:
                weig_bank[word_bank.index(wrd)] += 1
                wrd = ''
    if '' in word_bank:
        del weig_bank[word_bank.index('')]
        del word_bank[word_bank.index('')]


while True:
    x = input("Continue? y/n\n")
    if x == 'y':
        teaching()
    else:
        break

with open('wrdBank', 'w') as dat1:
    for x in word_bank:
        dat1.write('%s ' % x)
with open('wgtBank', 'w') as dat2:
    for x in weig_bank:
        dat2.write('%s ' % x)
dat1.close()
dat2.close()

# print(word_bank)
print(len(word_bank))
# print(weig_bank)
print(len(weig_bank))
