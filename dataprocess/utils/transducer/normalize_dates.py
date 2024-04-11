from pyformlang.fst import FST

def normalize_dates_info(extracted_info):

    transducer = FST()

    def string_number(number):
        if number == 1:
            return 'Uno'
        elif number == 2:
            return 'Dos'
        elif number == 3:
            return 'Tres'
        elif number == 4:
            return 'Cuatro'
        elif number == 5:
            return 'Cinco'
        elif number == 6:
            return 'Seis'
        elif number == 7:
            return 'Siete'
        elif number == 8:
            return 'Ocho'
        elif number == 9:
            return 'Nueve'
        else:
            return 'Cero'

    transducer.add_transitions([
        # DAY
        ('q0', '0', 'q1', ['']),
        ('q5', 'epsilon', 'q9', [' de ']),

        ('q0', '1', 'q2', ['']),
        ('q2', '0', 'q6', ['Diez']),
        ('q2', '1', 'q6', ['Once']),
        ('q2', '2', 'q6', ['Doce']),
        ('q2', '3', 'q6', ['Trece']),
        ('q2', '4', 'q6', ['Catorce']),
        ('q2', '5', 'q6', ['Quince']),
        ('q6', 'epsilon', 'q9', [' de ']),
        
        ('q0', '2', 'q3', ['Veinte']),
        ('q3', 'epsilon', 'q7', [' y ']),

        ('q0', '3', 'q4', ['Treinta']),
        ('q4', 'epsilon', 'q7', [' y ']),

        ('q8', 'epsilon', 'q9', [' de ']),

        ('q9', '/', 'q9', ['']),
        ('q9', '0', 'q10', ['']),
        ('q10', '1', 'q11', ['Enero']),
        ('q10', '2', 'q11', ['Febrero']),
        ('q10', '3', 'q11', ['Marzo']),
        ('q10', '4', 'q11', ['Abril']),
        ('q10', '5', 'q11', ['Mayo']),
        ('q10', '6', 'q11', ['Junio']),
        ('q10', '7', 'q11', ['Julio']),
        ('q10', '8', 'q11', ['Agosto']),
        ('q10', '9', 'q11', ['Septiembre']),
        ('q9', '1', 'q12', ['']),
        ('q12', '0', 'q11', ['Octubre']),
        ('q12', '1', 'q11', ['Noviembre']),
        ('q12', '2', 'q11', ['Diciembre']),

        ('q13', '/', 'q13', ['']),
        ('q11', 'epsilon', 'q13', [' del ']),
      ])

    for i in range(10):
      transducer.add_transitions([
        ('q1', str(i), 'q5', [str(string_number(i))]),
        ('q7', str(i), 'q8', [str(string_number(i))]),
        ('q7', str(i), 'q8', [str(string_number(i))]),
        ('q13', str(i), 'q13', [str(i)]),
      ])

    transducer.add_start_state('q0')
    transducer.add_final_state('q13')

    normalized_dates = []
    for date in extracted_info:
        normalized_date = ''.join(list(transducer.translate(date))[0])
        normalized_dates.append(normalized_date)

    normalized_info = {
        'dates': normalized_dates
    }

    return normalized_dates