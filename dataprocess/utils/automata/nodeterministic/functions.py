import re
from dataprocess.utils.automata.nodeterministic.jcb import *
from dataprocess.utils.automata.nodeterministic.america_express import *
from dataprocess.utils.automata.nodeterministic.visa import *
from dataprocess.utils.automata.nodeterministic.unionpay import *
from dataprocess.utils.automata.nodeterministic.mastercard import *
from django.core.files.storage import FileSystemStorage

def load_content(filename):

    fs = FileSystemStorage(location='documents/')
    filename = fs.save(filename.name, filename)

    with open('documents/' + filename, 'r') as file:
        lines = file.read().splitlines()
        s = ' '.join(lines)

    return split_text(s)

def accepts_visa(nfa_visa,pattern_request):
  return nfa_visa.accepts(pattern_request)

def accepts_mstcd(nfa_mstcd,pattern_request):
  return nfa_mstcd.accepts(pattern_request)

def accepts_up(nfa_up,pattern_request):
  return nfa_up.accepts(pattern_request)

def accepts_jcb(nfa_jcb,pattern_request):
  return nfa_jcb.accepts(pattern_request)

def accepts_ae(nfa_ae,pattern_request):
  return nfa_ae.accepts(pattern_request)

def generated_words(list_string, n, partitions):
    message = ''
    pivot_list = []
    try:
        for word in range(n, n + partitions, 1):
            if n < len(list_string):
                pivot_list.append(list_string[word])

        message = ' '.join(pivot_list)
        return message
    except IndexError:
        pivot_list.append('')
    message = ' '.join(pivot_list)
    return message

def split_text(s):
    #Defino los automatas.
    nfa_visa = automataNoD_Visa()
    nfa_mstcd = automataNoD_mstcd()
    nfa_up = automataNoD_Unionpay()
    nfa_jcb = automataNoD_jcb()
    nfa_ae = automataNoD_ae()

    card_list = {
      'Visa': [],
      'Mastercard': [],
      'UnionPay': [],
      'JCB': [],
      'AmericanExpress': []
      }

    message = ''
    list_string = re.split(r'[: ,.-]', s)
    for n in range(0,len(list_string)):
        new_word = generated_words(list_string, n, 4)
        if accepts_visa(nfa_visa,new_word) == True:
          card_list['Visa'].append(new_word)
        if accepts_mstcd(nfa_mstcd,new_word) == True:
          card_list['Mastercard'].append(new_word)
        if accepts_up(nfa_up,new_word) == True:
          card_list['UnionPay'].append(new_word)
        if accepts_jcb(nfa_jcb,new_word) == True:
          card_list['JCB'].append(new_word)
        new_word = generated_words(list_string, n, 3)
        if accepts_ae(nfa_ae,new_word) == True:
          card_list['AmericanExpress'].append(new_word)

    return card_list