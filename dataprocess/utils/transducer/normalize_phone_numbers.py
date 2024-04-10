from pyformlang.fst import FST

def normalize_phone_number_info(extracted_info):

    transducer = FST()

    for i in range(10):
      transducer.add_transitions([
          ('q0', str(i), 'q1', [str(i)]),
          ('q2', str(i), 'q8', [str(i)]),
          ('q8', str(i), 'q9', [str(i)]),
          ('q9', str(i), 'q10', [str(i)]),
          ('q3', str(i), 'q4', [str(i)]),
          ('q4', str(i), 'q5', [str(i)]),
          ('q5', str(i), 'q6', [str(i)]),
          ('q7', str(i), 'q7', [str(i)]),
          ('q1', str(i), 'q12', [str(i)]),
          ('q12', str(i), 'q13', [str(i)]),
      ])

    transducer.add_transitions([
        ('q0', '+', 'q1', ['+']),
        ('q6', 'epsilon', 'q7', ['-']),
        ('q10', 'epsilon', 'q11', ['-']),
        ('q10', ' ', 'q3', ['-']),
        ('q11', 'epsilon', 'q7', ['']),
        ('q13', 'epsilon', 'q2', ['-']),
        ('q13', ' ', 'q2', ['-']),
    ])

    transducer.add_start_state('q0')
    transducer.add_final_state('q7')

    normalized_phones = []
    for phone in extracted_info:
        normalized_phone_number = ''.join(list(transducer.translate(phone))[0])
        normalized_phones.append(normalized_phone_number)

    normalized_info = {
        'phone_number': normalized_phones
    }

    return normalized_phones