from pyformlang.fst import FST

def normalize_dates_info(extracted_info):

    transducer = FST()

    for i in range(10):
      transducer.add_transitions([
          # YEAR
          ('q1', str(i), 'q2', [str(i)]),
          ('q2', str(i), 'q3', [str(i)]),
          ('q3', str(i), 'q4', [str(i)]),
          ('q4', str(i), 'q5', [str(i) + ' - ']),

          # MONTH
          ('q6', str(i), 'q7', [str(i)]),
          ('q7', str(i), 'q8', [str(i) + ' - ']),

          # DAY
          ('q9', str(i), 'q10', [str(i)]),
          ('q10', str(i), 'q11', [str(i)]),
      ])

    transducer.add_transitions([
        ('q0', 'epsilon', 'q1', ['Year: ']),
        ('q5', 'epsilon', 'q6', ['Month: ']),
        ('q8', 'epsilon', 'q9', ['Day: ']),

        ('q6', '/', 'q6', ['']),
        ('q9', '/', 'q9', ['']),
    ])

    transducer.add_start_state('q0')
    transducer.add_final_state('q11')

    normalized_dates = []
    for date in extracted_info:
        normalized_date = ''.join(list(transducer.translate(date))[0])
        normalized_dates.append(normalized_date)

    normalized_info = {
        'dates': normalized_dates
    }

    return normalized_info