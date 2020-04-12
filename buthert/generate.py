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
    res = 0;
    for x in lst:
        for _ in x:
            res+=1
    return res



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

nouns_bank = [NOUN_bank, NPRO_bank] # предмет (существительное, местоимение)
adjfs_bank = [ADJF_bank, ADJS_bank, PRTF_bank, PRTS_bank] # признак (прилагательное (полное, краткое), причастие (полное, краткое))
verbs_bank = [VERB_bank, INFN_bank, GRND_bank] # действие (глагол, инфинитив, деепричастие)
advbs_bank = [COMP_bank, ADVB_bank] # степени (компаратив, наречие) (вопрос: как?)
numbs_bank = [NUMR_bank] # числительные
npros_bank = [PRED_bank] # неопределенная форма
preps_bank = [PREP_bank] # предлоги
prcls_bank = [PRCL_bank, INTJ_bank] # частицы

parts_of_speech = [nouns_bank,adjfs_bank,verbs_bank,advbs_bank,numbs_bank,npros_bank,preps_bank,prcls_bank]

poses_weights = [count(x) for x in parts_of_speech]

def generate_phrase():
    res = ''
    prev_word = ''
    temp = r.choice(r.choices(parts_of_speech,poses_weights)[0])
    prev_word += r.choices(temp,[weig_bank[word_bank.index(x)] for x in temp])[0]
    prev_POS = morpher.parse(prev_word)[0].tag.POS
    print(prev_word,prev_POS)

