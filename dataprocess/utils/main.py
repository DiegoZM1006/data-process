import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from dataprocess.utils.regex.main_regex import *
from dataprocess.utils.transducer.normalize_names import *
from dataprocess.utils.transducer.normalize_dates import *
from dataprocess.utils.transducer.normalize_address import *
from dataprocess.utils.transducer.normalize_emails import *
from dataprocess.utils.transducer.normalize_phone_numbers import *

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
    emails = search_emails(content)

    # Use transducer for normalize the extracted information
    # normalize_names = normalize_names_info(names)
    # normalize_dates = normalize_dates_info(dates)
    normalize_address = normalize_address_info(address)
    normalize_phone_numbers = normalize_phone_number_info(phone_numbers)
    normalize_emails = normalize_mail_info(emails)

    extracted_info = {
        'regex_names': names,
        'regex_dates': dates,
        'regex_addd': address,
        'regex_phone_numbers': phone_numbers,
        'regex_emails': emails,
        # 'normalize_names': normalize_names,
        # 'normalize_dates': normalize_dates,
        'normalize_address': normalize_address,
        'normalize_phone_numbers': normalize_phone_numbers,
        'normalize_emails': normalize_emails,
    }

    # continue...

    clear_documents_directory()
    return extracted_info