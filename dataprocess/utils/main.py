import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from dataprocess.utils.regex.main_regex import *
from dataprocess.utils.transducer.normalize_names import *
from dataprocess.utils.transducer.normalize_dates import *
from dataprocess.utils.transducer.normalize_address import *
from dataprocess.utils.transducer.normalize_emails import *
from dataprocess.utils.transducer.normalize_phone_numbers import *
from dataprocess.utils.automata.deterministic.functions import *
from dataprocess.utils.automata.nodeterministic.functions import *
from dataprocess.utils.grammar.cfg import *

def clear_documents_directory():
    files = os.listdir('documents')
    for file_name in files:
        file_path = os.path.join('documents', file_name)
        os.remove(file_path)

def read_text_file(file_path):
    with open('documents/' + file_path, 'r') as file:
        return file.read()

def main(myfile, options):
   
    extracted_info = []

    fs = FileSystemStorage(location='documents/')
    filename = fs.save(myfile.name, myfile)

    # Change the next lines of the files to the correct processing of the file

    content = read_text_file(filename)

    # Use the regex for names, address, locations, phone numbers and emails
    names = search_names(content)
    dates = search_dates(content)
    address = search_addresses(content)
    phone_numbers = search_phone_numbers(content)
    adf_formmat_possibles_numbers = search_adf_formmat_possibles_numbers(content)
    emails = search_emails(content)


    # Use transducer for normalize the extracted information
        
    merge_names = [f"{nombre} {apellido}" for nombre, apellido in names]

    normalize_names = normalize_names_info(merge_names)
    normalize_dates = normalize_dates_info(dates)
    normalize_address = normalize_address_info(address)
    normalize_phone_numbers = normalize_phone_number_info(phone_numbers)
    # normalize_emails = normalize_mail_info(emails)

    # Use automata to validate the extracted information
    validate_cards = load_content(myfile)
    validate_phone_numbers = extract_text_info(adf_formmat_possibles_numbers)

    # Use CFG to validate the extracted information
    cfg_urls = validate_urls_in_text(content)

    extracted_info = {
        'regex_names': names,
        'regex_dates': dates,
        'regex_addd': address,
        'regex_phone_numbers': phone_numbers,
        'regex_emails': emails,
        'normalize_names': normalize_names,
        'normalize_dates': normalize_dates,
        'normalize_address': normalize_address,
        'normalize_phone_numbers': normalize_phone_numbers,
        # 'normalize_emails': normalize_emails,
        'validate_cards': validate_cards,
        'validate_phone_numbers': validate_phone_numbers,
        'cfg_urls': cfg_urls,
    }

    # continue...

    clear_documents_directory()
    return extracted_info