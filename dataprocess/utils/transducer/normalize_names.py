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
        ('q0', 'Á', 'q0', ['11000011 10000001']),
        ('q0', 'á', 'q0', ['11000011 10100001']), 
        ('q0', 'É', 'q0', ['11000011 10001001']), 
        ('q0', 'é', 'q0', ['11000011 10101001']), 
        ('q0', 'Í', 'q0', ['11000011 10001101']),  
        ('q0', 'í', 'q0', ['11000011 10101101']),  
        ('q0', 'Ó', 'q0', ['11000011 10010011']), 
        ('q0', 'ó', 'q0', ['11000011 10110011']),  
        ('q0', 'Ú', 'q0', ['11000011 10011010']), 
        ('q0', 'ú', 'q0', ['11000011 10111010']),
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