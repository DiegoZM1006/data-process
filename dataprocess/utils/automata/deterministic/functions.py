from pyformlang.finite_automaton import EpsilonNFA, NondeterministicFiniteAutomaton, DeterministicFiniteAutomaton, State, Symbol
import re

def load_content(nombre_archivo):
  with open(nombre_archivo, 'r') as file:
    return file.read()

def possibles_numbers(content):
  take_possibles_numbers = r"\+([0-9][0-9]?)\s?(3(?:0[0-5]|[1-5]\d|6[0-7])\s?\d{7})"
  return re.findall(take_possibles_numbers, content)

def dfa_Eeuu():
  dfa_eeuu = DeterministicFiniteAutomaton()
  dfa_eeuu.add_transition('q0', '+', 'q1')
  dfa_eeuu.add_transition('q1', '1', 'q2')

  dfa_eeuu.add_start_state('q0')
  dfa_eeuu.add_final_state('q2')

  return dfa_eeuu

def eeuu_accepts(dfa, number_prefijo):
  prefijo = number_prefijo[0]
  new_prefijo = '+' + prefijo
  return dfa.accepts(new_prefijo)

def dfa_accepts(dfa, number_prefijo):
  return dfa.accepts(number_prefijo)

def dfa_Argentina():
  dfa_argentina = DeterministicFiniteAutomaton()
  dfa_argentina.add_transition('q0', '5', 'q1')
  dfa_argentina.add_transition('q1', '4', 'q2')

  dfa_argentina.add_start_state('q0')
  dfa_argentina.add_final_state('q2')

  return dfa_argentina


def dfa_Colombia():
  dfa_colombia = DeterministicFiniteAutomaton()
  dfa_colombia.add_transition('q0', '5', 'q1')
  dfa_colombia.add_transition('q1', '7', 'q2')

  dfa_colombia.add_start_state('q0')
  dfa_colombia.add_final_state('q2')

  return dfa_colombia

def dfa_Mexico():
  dfa_mexico = DeterministicFiniteAutomaton()
  dfa_mexico.add_transition('q0', '5', 'q1')
  dfa_mexico.add_transition('q1', '2', 'q2')

  dfa_mexico.add_start_state('q0')
  dfa_mexico.add_final_state('q2')

  return dfa_mexico

def dfa_Vnz():
  dfa_vnz = DeterministicFiniteAutomaton()
  dfa_vnz.add_transition('q0', '5', 'q1')
  dfa_vnz.add_transition('q1', '8', 'q2')

  dfa_vnz.add_start_state('q0')
  dfa_vnz.add_final_state('q2')

  return dfa_vnz

def extract_text_info(phone_numbers):
    dfa_eeuu = dfa_Eeuu()
    dfa_argentina = dfa_Argentina()
    dfa_colombia = dfa_Colombia()
    dfa_mexico = dfa_Mexico()
    dfa_vnz = dfa_Vnz()

    #   content = load_content(nombre_archivo)
    #   list_possibles_numbers = possibles_numbers(content)
    list_possibles_numbers = phone_numbers
    list_numbers = {
        'Estados Unidos': [],
        'Argentina' : [],
        'Colombia' : [],
        'México' : [],
        'Venezuela' : []
        }

    for n in range( 0, len(list_possibles_numbers)):
        if eeuu_accepts(dfa_eeuu, list_possibles_numbers[n]) == True:
            list_numbers['Estados Unidos'].append(list_possibles_numbers[n][1])
        if dfa_accepts(dfa_argentina, list_possibles_numbers[n][0]) == True:
            list_numbers['Argentina'].append(list_possibles_numbers[n][1])
        if dfa_accepts(dfa_colombia, list_possibles_numbers[n][0]) == True:
            list_numbers['Colombia'].append(list_possibles_numbers[n][1])
        if dfa_accepts(dfa_mexico, list_possibles_numbers[n][0]) == True:
            list_numbers['México'].append(list_possibles_numbers[n][1])
        if dfa_accepts(dfa_vnz, list_possibles_numbers[n][0]) == True:
            list_numbers['Venezuela'].append(list_possibles_numbers[n][1])

    return list_numbers