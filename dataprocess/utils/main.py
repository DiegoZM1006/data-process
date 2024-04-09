import re
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import os

def clear_documents_directory():
    files = os.listdir('documents')
    for file_name in files:
        file_path = os.path.join('documents', file_name)
        os.remove(file_path)

def read_text_file(file_path):
    text = []
    with open('documents/' + file_path, 'r') as file:
        for linea in file:
            text.append(linea.strip())
    return text

def parse_text(text):
    name_pattern = re.compile(r'[A-Z][a-z]+ [A-Z][a-z]+')
    date_pattern = re.compile(r'\d{4}-\d{2}-\d{2}')
    location_pattern = re.compile(r'[A-Z][a-z]+, [A-Z]{2}')

    extracted_info = {
        'names': name_pattern.findall(text),
        'dates': date_pattern.findall(text),
        'locations': location_pattern.findall(text)
    }

    return extracted_info

def main(myfile):
   
    data = []

    fs = FileSystemStorage(location='documents/')
    filename = fs.save(myfile.name, myfile)

    # Change the next lines of the files to the correct processing of the file

    extracted_info = read_text_file(filename)
    data = extracted_info

    # continue...

    clear_documents_directory()
    return data