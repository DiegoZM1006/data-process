from pyformlang.finite_automaton import EpsilonNFA, NondeterministicFiniteAutomaton, DeterministicFiniteAutomaton, State, Symbol
import re
import string

def automataNoD_mstcd():
  q0 = State('q0')
  q1 = State('q1')
  q2 = State('q2')
  q3 = State('q3')
  q4 = State('q4')
  q5 = State('q5')
  q6 = State('q6')
  q7 = State('q7')
  q8 = State('q8')
  q9 = State('q9')
  q10 = State('q10')
  q11 = State('q11')
  q12 = State('q12')
  q13 = State('q13')
  q14 = State('q14')
  q15 = State('q15')
  q16 = State('q16')
  q17 = State('q17')
  q18 = State('q18')
  q19 = State('q19')


  # Obtener todos los caracteres de la a a la z
  input_symbols2 = set(string.ascii_letters)

  # Agregar otros símbolos necesarios
  input_symbols2.update({'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', ' ', ':' , 'ñ' , 'Ñ', 'á', 'é', 'í', 'ó', 'ú', 'Á', 'É', 'Í', 'Ó', 'Ú' ,'+'})


  # Configurar el Automata Deterministico para Visa
  nfa_mstcd = NondeterministicFiniteAutomaton()

  # Colocamos las transición

  nfa_mstcd.add_transitions([
        (q0, '5', q1),
    ])


  # Este for me ayuda en poder rellenar mucho más rapido las transiciones.

  for digit in string.digits:
      nfa_mstcd.add_transition(q0, digit, q0)
      nfa_mstcd.add_transition(q1, digit, q2)
      nfa_mstcd.add_transition(q2, digit, q3)
      nfa_mstcd.add_transition(q3, digit, q4)

      nfa_mstcd.add_transition(q5, digit, q6)
      nfa_mstcd.add_transition(q6, digit, q7)
      nfa_mstcd.add_transition(q7, digit, q8)
      nfa_mstcd.add_transition(q8, digit, q9)

      nfa_mstcd.add_transition(q10, digit, q11)
      nfa_mstcd.add_transition(q11, digit, q12)
      nfa_mstcd.add_transition(q12, digit, q13)
      nfa_mstcd.add_transition(q13, digit, q14)

      nfa_mstcd.add_transition(q15, digit, q16)
      nfa_mstcd.add_transition(q16, digit, q17)
      nfa_mstcd.add_transition(q17, digit, q18)
      nfa_mstcd.add_transition(q18, digit, q19)


  # Añado las trasiciones faltantes (los espacios/-)
  nfa_mstcd.add_transition(q4, '-' , q5)
  nfa_mstcd.add_transition(q9, '-' , q10)
  nfa_mstcd.add_transition(q14, '-' , q15)

  nfa_mstcd.add_transition(q4, ' ' , q5)
  nfa_mstcd.add_transition(q9, ' ' , q10)
  nfa_mstcd.add_transition(q14, ' ' , q15)



  # Agregar transición de cualquier símbolo que no necesito vuelva al estado inicial - solo para digitos.
  for symbol in input_symbols2:
      if symbol not in {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}:
          nfa_mstcd.add_transition(q0, symbol, q0)
          nfa_mstcd.add_transition(q1, symbol, q0)
          nfa_mstcd.add_transition(q2, symbol, q0)
          nfa_mstcd.add_transition(q3, symbol, q0)
          nfa_mstcd.add_transition(q5, symbol, q0)
          nfa_mstcd.add_transition(q6, symbol, q0)
          nfa_mstcd.add_transition(q7, symbol, q0)
          nfa_mstcd.add_transition(q8, symbol, q0)
          nfa_mstcd.add_transition(q10, symbol, q0)
          nfa_mstcd.add_transition(q11, symbol, q0)
          nfa_mstcd.add_transition(q12, symbol, q0)
          nfa_mstcd.add_transition(q13, symbol, q0)
          nfa_mstcd.add_transition(q15, symbol, q0)
          nfa_mstcd.add_transition(q16, symbol, q0)
          nfa_mstcd.add_transition(q17, symbol, q0)
          nfa_mstcd.add_transition(q18, symbol, q0)
          #Falta ver lo de q19 que al final debe de darme como cierto entonces no deberia de ponerlo.


  # Agregar transición de cualquier símbolo que no necesito vuelva al estado inicial - solo para espacios entre números.
  for symbol in input_symbols2:
      if symbol not in {'-', ' '}:
        nfa_mstcd.add_transition(q4, symbol, q0)
        nfa_mstcd.add_transition(q9, symbol, q0)
        nfa_mstcd.add_transition(q14, symbol, q0)


  nfa_mstcd.add_start_state('q0')
  nfa_mstcd.add_final_state('q19')

  return nfa_mstcd