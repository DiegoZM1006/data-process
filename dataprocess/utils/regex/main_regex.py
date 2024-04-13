import re
from pyformlang.regular_expression import Regex

name_regex = r"([A-ZÁÉÍÓÚÜÑ][a-záéíóúüñ]+)( [A-ZÁÉÍÓÚÜÑ][a-záéíóúüñ]+)"
date_regex = r"\b\d{1,2}/\d{1,2}/\d{2,4}\b"
address_regex = r"\b(?:Carrera|Calle|Transversal|Diagonal|Circular|Avenida)\s+\d+\s*(?:#?\s*\d+-?\d*)?,?\s*\w+\b(?:\s+[A-Za-záéíóúüñÁÉÍÓÚÜÑ]+\b){1,},?\s*[A-Za-záéíóúüñÁÉÍÓÚÜÑ]+\b"
phone_number_regex = r"(?:\+57\s?)?(?:3(?:0[0-5]|[1-5]\d|6[0-7])\s?\d{7})" 
email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
adf_formmat_possibles_numbers = r"\+([0-9][0-9]?)\s?(3(?:0[0-5]|[1-5]\d|6[0-7])\s?\d{7})"

def search_names(texto):
    return re.findall(name_regex, texto)

def search_dates(texto):
    return re.findall(date_regex, texto)

def search_addresses(texto):
    return re.findall(address_regex, texto)

def search_phone_numbers(texto):
    return re.findall(phone_number_regex, texto)

def search_emails(texto):
    return re.findall(email_regex, texto)

def search_adf_formmat_possibles_numbers(texto):
    return re.findall(adf_formmat_possibles_numbers, texto)