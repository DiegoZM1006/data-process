from pyformlang.fst import FST

def normalize_names_info(extracted_info):
    transducer = FST()

    for i in range(26):
        upper_case_letter = chr(ord('a') + i).upper()
        lower_case_letter = chr(ord('a') + i).lower()
        lower_binary_letter = "{0:08b}".format(ord(lower_case_letter))
        upper_binary_letter = "{0:08b}".format(ord(upper_case_letter))
        transducer.add_transitions([
            ('q0', lower_case_letter, 'q0', [lower_binary_letter]),
            ('q0', upper_case_letter, 'q0', [upper_binary_letter]),
            # ('q0', lower_case_letter, 'q1', [chinise_letter]),
            # ('q0', upper_case_letter, 'q1', [chinise_letter]),
            # ('q1', lower_case_letter, 'q1', [chinise_letter]),
            # ('q1', upper_case_letter, 'q1', [chinise_letter]),
            # ('q2', lower_case_letter, 'q1', [chinise_letter]),
            # ('q2', upper_case_letter, 'q1', [chinise_letter]),
        ])

    transducer.add_transitions([
        ('q0', ' ', 'q0', [' ']),
    ])
    transducer.add_start_state('q0')
    transducer.add_final_state('q0')

    normalized_names = []
    for name in extracted_info:
        normalized_name = ''.join(list(transducer.translate(name))[0])
        normalized_names.append(normalized_name)

    normalized_info = {
        'names': normalized_names
    }

    return normalized_names