from pyformlang.fst import FST

def normalize_address_info(extracted_info):

    transducer = FST()

    transducer.add_transitions([

         # STATES FOR CALLE -> STREET
        ('q0', 'C', 'q1', ['S']),
        ('q1', 'a', 'q2', ['t']),
        ('q2', 'l', 'q3', ['r']),
        ('q3', 'l', 'q4', ['e']),
        ('q4', 'e', 'q5', ['e']),
        ('q5', 'epsilon', 'q6', ['t']),

        # STATES FOR CARRERA -> CAREER
        ('q0', 'C', 'q7', ['C']),
        ('q7', 'a', 'q8', ['a']),
        ('q8', 'r', 'q9', ['r']),
        ('q9', 'r', 'q10', ['e']),
        ('q10', 'e', 'q11', ['e']),
        ('q11', 'r', 'q12', ['']),
        ('q12', 'a', 'q13', ['']),
        ('q13', 'epsilon', 'q6', ['r']),

        # STATES FOR AVENIDA -> AVENUE
        ('q0', 'A', 'q14', ['A']),
        ('q14', 'v', 'q15', ['v']),
        ('q15', 'e', 'q16', ['e']),
        ('q16', 'n', 'q17', ['n']),
        ('q17', 'i', 'q18', ['u']),
        ('q18', 'd', 'q19', ['']),
        ('q19', 'a', 'q20', ['']),
        ('q20', 'epsilon', 'q6', ['e']),

        # STATE FOR TRANSVERSAL -> CROSS
        ('q0', 'T', 'q21', ['C']),
        ('q21', 'r', 'q22', ['r']),
        ('q22', 'a', 'q23', ['o']),
        ('q23', 'n', 'q24', ['s']),
        ('q24', 's', 'q25', ['']),
        ('q25', 'v', 'q26', ['']),
        ('q26', 'e', 'q27', ['']),
        ('q27', 'r', 'q28', ['']),
        ('q28', 's', 'q29', ['']),
        ('q29', 'a', 'q46', ['']),
        ('q46', 'l', 'q47', ['']),
        ('q47', 'epsilon', 'q6', ['s']),

        # STATES FOR CIRCULAR -> CIRCULAR
        ('q0', 'C', 'q30', ['C']),
        ('q30', 'i', 'q31', ['i']),
        ('q31', 'r', 'q32', ['r']),
        ('q32', 'c', 'q33', ['c']),
        ('q33', 'u', 'q34', ['u']),
        ('q34', 'l', 'q35', ['l']),
        ('q35', 'a', 'q36', ['a']),
        ('q36', 'r', 'q37', ['']),
        ('q37', 'epsilon', 'q6', ['r']),

        # STATES FOR DIAGONAL -> DIAGONAL
         ('q0', 'D', 'q38', ['D']),
        ('q38', 'i', 'q39', ['i']),
        ('q39', 'a', 'q40', ['a']),
        ('q40', 'g', 'q41', ['g']),
        ('q41', 'o', 'q42', ['o']),
        ('q42', 'n', 'q43', ['n']),
        ('q43', 'a', 'q44', ['a']),
        ('q44', 'l', 'q45', ['']),
        ('q45', 'epsilon', 'q6', ['l']),

        ('q6', ' ', 'q6', [' ']),
        ('q6', ',', 'q6', [',']),
        ('q6', '-', 'q6', ['-']),
        ('q6', '#', 'q6', ['#']),
    ])

    for i in range(26):
        upper_case_letter = chr(ord('a') + i).upper()
        lower_case_letter = chr(ord('a') + i).lower()
        transducer.add_transitions([
            ('q6', lower_case_letter, 'q6', [lower_case_letter]),
            ('q6', upper_case_letter, 'q6', [upper_case_letter]),
        ])

    for i in range(10):
      transducer.add_transitions([
          ('q6', str(i), 'q6', [str(i)]),
      ])

    transducer.add_start_state('q0')
    transducer.add_final_state('q6')

    normalized_address_info = []
    for address in extracted_info:
        normalized_address = ''.join(list(transducer.translate(address))[0])
        normalized_address_info.append(normalized_address)

    normalized_info = {
        'address': normalized_address_info
    }

    return normalized_address_info