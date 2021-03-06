import random as r
import pymorphy2 as mrph

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

morpher = mrph.MorphAnalyzer()


def count(lst):
    res = 0
    for x in lst:
        for _ in x:
            res+=1
    return res


def summa_POS(lst):
    res = 0
    for x in lst:
        for y in lst:
            res += weig_bank[word_bank.index(y)]
    return res


def contain(a,lst):
    for x in lst:
        for y in x:
            if a == y:
                return True
    return False

def lastword(wrd):
    return wrd.split()[-1]

NOUN_bank = [x for x in word_bank if morpher.parse(x)[0].tag.POS == 'NOUN']  # имя существительное	            хомяк
ADJF_bank = [x for x in word_bank if morpher.parse(x)[0].tag.POS == 'ADJF']  # имя прилагательное (полное)	    хороший
ADJS_bank = [x for x in word_bank if morpher.parse(x)[0].tag.POS == 'ADJS']  # имя прилагательное (краткое)	    хорош
COMP_bank = [x for x in word_bank if morpher.parse(x)[0].tag.POS == 'COMP']  # компаратив	                    лучше, получше, выше
VERB_bank = [x for x in word_bank if morpher.parse(x)[0].tag.POS == 'VERB']  # глагол (личная форма)	        говорю, говорит, говорил
INFN_bank = [x for x in word_bank if morpher.parse(x)[0].tag.POS == 'INFN']  # глагол (инфинитив)	            говорить, сказать
PRTF_bank = [x for x in word_bank if morpher.parse(x)[0].tag.POS == 'PRTF']  # причастие (полное)	            прочитавший, прочитанная
PRTS_bank = [x for x in word_bank if morpher.parse(x)[0].tag.POS == 'PRTS']  # причастие (краткое)	            прочитана
GRND_bank = [x for x in word_bank if morpher.parse(x)[0].tag.POS == 'GRND']  # деепричастие	                    прочитав, рассказывая
NUMR_bank = [x for x in word_bank if morpher.parse(x)[0].tag.POS == 'NUMR']  # числительное	                    три, пятьдесят
ADVB_bank = [x for x in word_bank if morpher.parse(x)[0].tag.POS == 'ADVB']  # наречие	                        круто
NPRO_bank = [x for x in word_bank if morpher.parse(x)[0].tag.POS == 'NPRO']  # местоимение-существительное	    он
PRED_bank = [x for x in word_bank if morpher.parse(x)[0].tag.POS == 'PRED']  # предикатив	                    некогда
PREP_bank = [x for x in word_bank if morpher.parse(x)[0].tag.POS == 'PREP']  # предлог	                        в
CONJ_bank = [x for x in word_bank if morpher.parse(x)[0].tag.POS == 'CONJ']  # союз	                            и
PRCL_bank = [x for x in word_bank if morpher.parse(x)[0].tag.POS == 'PRCL']  # частица	                        бы, же, лишь
INTJ_bank = [x for x in word_bank if morpher.parse(x)[0].tag.POS == 'INTJ']  # междометие	                    ой

nouns_bank = NOUN_bank + NPRO_bank # предмет (существительное, местоимение)
nouns_bank_weight = [weig_bank[word_bank.index(x)] for x in nouns_bank]

adjfs_bank = ADJF_bank + ADJS_bank + PRTF_bank + PRTS_bank # признак (прилагательное (полное, краткое), причастие (полное, краткое))
adjfs_bank_weight = [weig_bank[word_bank.index(x)] for x in adjfs_bank]

verbs_bank = VERB_bank + INFN_bank + GRND_bank # действие (глагол, инфинитив, деепричастие)
verbs_bank_weight = [weig_bank[word_bank.index(x)] for x in verbs_bank]

advbs_bank = COMP_bank + ADVB_bank # степени (компаратив, наречие) (вопрос: как?)
advbs_bank_weight = [weig_bank[word_bank.index(x)] for x in advbs_bank]

numbs_bank = NUMR_bank # числительные
numbs_bank_weight = [weig_bank[word_bank.index(x)] for x in numbs_bank]

npros_bank = PRED_bank # неопределенная форма
npros_bank_weight = [weig_bank[word_bank.index(x)] for x in npros_bank]

preps_bank = PREP_bank # предлоги
preps_bank_weight = [weig_bank[word_bank.index(x)] for x in preps_bank]

prcls_bank = PRCL_bank + INTJ_bank # частицы
prcls_bank_weight = [weig_bank[word_bank.index(x)] for x in prcls_bank]

parts_of_speech = [nouns_bank,adjfs_bank,verbs_bank,advbs_bank,numbs_bank,npros_bank,preps_bank,prcls_bank]
POSes_weights = [nouns_bank_weight,adjfs_bank_weight,verbs_bank_weight,advbs_bank_weight,numbs_bank_weight,
                 npros_bank_weight,preps_bank_weight,prcls_bank_weight]
POSes_weights = [sum(x) for x in POSes_weights]

def fill(inp):
    res = ''
    for i in inp:
        res+=' ' + i
    return res

"""
def generate_sample_phrase():
    res = ''
    temp = ''
    temp_pos = ''
    temp = r.choices(parts_of_speech,weights=POSes_weights)[0]
    temp_pos = morpher.parse(temp[0])[0].tag.POS
    while temp_pos == 'PRCL' or temp_pos == 'INTJ':
        temp = r.choices(parts_of_speech, weights=POSes_weights)[0]
        temp_pos = morpher.parse(temp[0])[0].tag.POS
    res += r.choices(temp,weights=[weig_bank[word_bank.index(x)] for x in temp])[0]
    #print(res,temp_pos)
    if temp_pos in ['NOUN', 'NPRO']:
        if temp_pos == 'PREP':
            temp = preps_bank
            res += ' ' + r.choices(temp,weights=[weig_bank[word_bank.index(x)] for x in temp])[0]
            temp = nouns_bank
            res += ' ' + r.choices(temp,weights=[weig_bank[word_bank.index(x)] for x in temp])[0]
        else:
            temp = verbs_bank+adjfs_bank
            res += ' ' + r.choices(temp,weights=[weig_bank[word_bank.index(x)] for x in temp])[0]
    elif temp_pos in ['ADJF', 'ADJS', 'PRTF', 'PRTS']:
        temp = nouns_bank
        res += ' ' + r.choices(temp, weights=[weig_bank[word_bank.index(x)] for x in temp])[0]
    elif temp_pos in ['VERB', 'INFN', 'GRND']:
        temp = nouns_bank + advbs_bank + preps_bank
        res += ' ' + r.choices(temp, weights=[weig_bank[word_bank.index(x)] for x in temp])[0]
        if morpher.parse(lastword(res))[0].tag.POS == 'PREP':
            temp = nouns_bank
            res += ' ' + r.choices(temp, weights=[weig_bank[word_bank.index(x)] for x in temp])[0]
    elif temp_pos in ['PREP']:
        temp_pos = nouns_bank+adjfs_bank
        res += ' ' + r.choices(temp, weights=[weig_bank[word_bank.index(x)] for x in temp])[0]
        res += ' ' + r.choices(temp, weights=[weig_bank[word_bank.index(x)] for x in temp])[0]
    #print(res)
    return res"""
#print('checkpoint')
def soglas_phrase(main_word = ''):
    #print('incheck 0')
    if main_word == '':
        res = ''
        temp = adjfs_bank
        last_word = r.choices(temp, weights=[weig_bank[word_bank.index(x)] for x in temp])[0]
        res += ' ' + last_word
        #print('incheck 1',res)
    else:
        last_word = main_word
        res = ' ' + last_word
    temp = nouns_bank + preps_bank
    last_word = r.choices(temp, weights=[weig_bank[word_bank.index(x)] for x in temp])[0]
    res += ' ' + last_word

    #print('incheck 2',res)
    if morpher.parse(last_word)[0].tag.POS == 'PREP':
        temp = nouns_bank
        res += ' ' + r.choices(temp, weights=[weig_bank[word_bank.index(x)] for x in temp])[0]
        #print('incheck (3)')
    res = res.upper()
    temp = res.split()
    last_word = temp[-1]
    morfed = morpher.parse(temp[0])[0]
    try:
        temp[0] = morfed.inflect({morpher.parse(last_word)[0].tag.number, morpher.parse(last_word)[0].tag.gender, morpher.parse(last_word)[0].tag.case})[0]
        res = ''
        for i in temp:
            res += i + ' '
        return res.upper()
    except:
        return res.lstrip(' ').upper()


def uprav_phrase(main_word = ''):
    if main_word == '':
        temp = verbs_bank+nouns_bank+advbs_bank+numbs_bank
        res = ''
        last_word = r.choices(temp, weights=[weig_bank[word_bank.index(x)] for x in temp])[0]
        res += last_word
    else:
        last_word = main_word
        res = main_word
    if morpher.parse(last_word)[0].tag.POS in ['INFN', 'VERB']:
        temp = preps_bank + prcls_bank+ nouns_bank
        last_word = r.choices(temp, weights=[weig_bank[word_bank.index(x)] for x in temp])[0]
        res += ' ' + last_word
        if morpher.parse(last_word)[0].tag.POS in ['PREP','PRCL','INTJ']:
            temp = nouns_bank
            last_word = r.choices(temp, weights=[weig_bank[word_bank.index(x)] for x in temp])[0]
            res += ' ' + last_word
        brkn = res.split()
        res = ''
        temp = morpher.parse(brkn[-1])[0]
        last_word = temp.inflect({r.choice(['ablt','accs']), morpher.parse(last_word)[0].tag.number})[0]
        brkn[-1] = last_word
        res == ''
        for i in brkn:
            res += i + ' '
    elif morpher.parse(last_word)[0].tag.POS in ['NOUN','NPRO','NUMR']:
        temp = nouns_bank + preps_bank
        last_word = r.choices(temp, weights=[weig_bank[word_bank.index(x)] for x in temp])[0]
        res += ' ' + last_word
        if morpher.parse(last_word)[0].tag.POS == 'PREP':
            temp = nouns_bank
            last_word = r.choices(temp, weights=[weig_bank[word_bank.index(x)] for x in temp])[0]
            res += ' ' + last_word
        brkn = res.split()
        res = ''
        temp = morpher.parse(brkn[-1])[0]
        brkn[-1] = temp.inflect({'gent'})[0]
        for i in brkn:
            res += i + ' '
    elif morpher.parse(last_word)[0].tag.POS in ['COMP','ADVB']:
        temp = nouns_bank + preps_bank + verbs_bank + prcls_bank
        last_word = r.choices(temp, weights=[weig_bank[word_bank.index(x)] for x in temp])[0]
        res += ' ' + last_word
        if morpher.parse(last_word)[0].tag.POS in ['PRCL','INTJ','PREP']:
            temp = nouns_bank + verbs_bank
            last_word = r.choices(temp, weights=[weig_bank[word_bank.index(x)] for x in temp])[0]
            res += ' ' + last_word
        brkn = res.split()
        res = ''
        temp = morpher.parse(brkn[-1])[0]
        try:
            brkn[-1] = temp.inflect({'gent'})[0]
        except: None
        for i in brkn:
            res += i + ' '
    return res.upper()


def primik_phrase(main_word = ''):
    res = ''
    if main_word == '':
        temp = nouns_bank + verbs_bank
        last_word = ''
        last_word = r.choices(temp, weights=[weig_bank[word_bank.index(x)] for x in temp])[0]
        res += last_word
    else:
        last_word = main_word
        res = last_word
    if last_word in nouns_bank:
        temp = verbs_bank + advbs_bank
        last_word = r.choices(temp, weights=[weig_bank[word_bank.index(x)] for x in temp])[0]
        res += ' ' + last_word
    else:
        temp = nouns_bank + advbs_bank
        last_word = r.choices(temp, weights=[weig_bank[word_bank.index(x)] for x in temp])[0]
        res += ' ' + last_word
    return res

def generate_simple_sentence():
    temp = VERB_bank + nouns_bank
    res = ''
    last_word = r.choices(temp, weights=[weig_bank[word_bank.index(x)] for x in temp])[0]
    res += last_word
    if last_word in nouns_bank:
        temp = VERB_bank
        morfed = morpher.parse(last_word)[0]
        last_word = r.choices(temp, weights=[weig_bank[word_bank.index(x)] for x in temp])[0]
        try:
            res = morfed.inflect({'nomn',morpher.parse(last_word)[0].tag.number})[0]
        except: res = morfed[0]
        res += ' ' + last_word
    else:
        temp = nouns_bank
        last_word = r.choices(temp, weights=[weig_bank[word_bank.index(x)] for x in temp])[0]
        morfed = morpher.parse(last_word)[0]
        try:
            last_word = morfed.inflect({morpher.parse(res)[0].tag.number,'nomn'})[0]
        except: last_word = morfed[0]
        res += ' ' + last_word
    return res.upper()


def generate_full_sentense(leng):
    mores = [primik_phrase,uprav_phrase,soglas_phrase]
    res = generate_simple_sentence().split()
    cnt = 0
    while cnt<leng:
        for i in range(len(res)):
            if r.choice([True,False]):
                res[i] = r.choices(mores,weights=[10,8,6])[0](res[i])
                mdl = []
                for i in res:
                    mdl+=i.split()
                res = mdl
        cnt = len(res)
    return fill(res).upper().lstrip(' ')


def fix_sentense(snt):
    temp = snt.split()
    for i in range(1,len(temp)):
        try:
            temp[i] = morpher.parse(temp[i])[0].inflect({morpher.parse(temp[i-1])[0].tag.case})[0]
        except: None
        try:
            temp[i] = morpher.parse(temp[i])[0].inflect({morpher.parse(temp[i-1])[0].tag.number})[0]
        except: None
        try:
            temp[i] = morpher.parse(temp[i])[0].inflect({morpher.parse(temp[i-1])[0].tag.gender})[0]
        except: None
        try:
            temp[i] = morpher.parse(temp[i])[0].inflect({morpher.parse(temp[i-1])[0].tag.case})[0]
        except: None
        if temp[i-1].upper() in ["НА","О","В","ОБ","ОБО","ПРИ","ПО"]:
            try:
                temp[i] = morpher.parse(temp[i])[0].inflect({'loct'})[0]
            except: None
        elif temp[i-1].upper() in ["ЗА","НАД","ПОД","ПЕРЕД","С"]:
            try:
                temp[i] = morpher.parse(temp[i])[0].inflect({'ablt'})[0]
            except: None
    return fill(temp)

size = r.randint(5,10)
for m in range(size):
    sntns = generate_full_sentense(r.randint(1,7))
    sntns = fix_sentense(sntns).upper()
    sidsnts = sntns.split()
    for i in range(len(sidsnts)):
        if morpher.parse(sidsnts[i])[0].tag.POS == 'CONJ':
            sidsnts[i-1] += ','
    print(fill(sidsnts).lstrip(' '))
    if m != size-1:
        print('@')
