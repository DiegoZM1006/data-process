from pyformlang.fst import FST

def normalize_mail_info(extracted_info):
    transducer = FST()

    for i in range(26):
        upper_case_letter = chr(ord('a') + i).upper()
        lower_case_letter = chr(ord('a') + i).lower()
        transducer.add_transitions([
            ('q0', lower_case_letter, 'q0', [lower_case_letter]),
            ('q0', upper_case_letter, 'q0', [upper_case_letter]),
            ('q1', lower_case_letter, 'q1', [lower_case_letter]),
            ('q1', upper_case_letter, 'q1', [lower_case_letter]),
            ('q2', lower_case_letter, 'q2', [lower_case_letter]),
            ('q2', upper_case_letter, 'q2', [lower_case_letter]),
        ])

    transducer.add_transitions([
        ('q1', '.', 'q2', ['.']),
        ('q0', '@', 'q1', ['@']),
    ])

    transducer.add_start_state('q0')
    transducer.add_final_state('q2')

    normalized_mails = []
    for email in extracted_info:
        normalized_email = ''.join(list(transducer.translate(email))[0])
        normalized_mails.append(normalized_email)

    normalized_info = {
        'mails': normalized_mails
    }

    return normalized_mails