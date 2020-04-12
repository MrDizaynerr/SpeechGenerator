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
