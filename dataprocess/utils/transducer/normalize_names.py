from pyformlang.fst import FST

def normalize_names_info(extracted_info):
    transducer = FST()

    for i in range(26):
        upper_case_letter = chr(ord('a') + i).upper()
        lower_case_letter = chr(ord('a') + i).lower()
        transducer.add_transitions([
            ('q0', lower_case_letter, 'q1', [upper_case_letter]),
            ('q0', upper_case_letter, 'q1', [upper_case_letter]),
            ('q1', lower_case_letter, 'q1', [lower_case_letter]),
            ('q1', upper_case_letter, 'q1', [lower_case_letter]),
            ('q2', lower_case_letter, 'q1', [upper_case_letter]),
            ('q2', upper_case_letter, 'q1', [upper_case_letter]),
        ])

    transducer.add_transitions([
        ('q1', ' ', 'q2', [' ']),
    ])
    transducer.add_start_state('q0')
    transducer.add_final_state('q1')

    normalized_names = []
    for name in extracted_info:
        normalized_name = ''.join(list(transducer.translate(name))[0])
        normalized_names.append(normalized_name)

    normalized_info = {
        'names': normalized_names
    }

    return normalized_info