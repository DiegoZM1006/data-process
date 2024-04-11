from pyparsing import Word, Literal, ZeroOrMore, Group, Suppress, alphanums, printables, OneOrMore
import re

# Definición de los componentes de una URL
protocol = Literal("http://") | Literal("https://")
#subdominio = Word(alphanums + "-") + Literal(".")
domain_name = Word(alphanums + "-") + Literal(".")
tld = (Literal("com") | Literal("org") | Literal("net") | Literal("edu") | Literal("gov"))
route = Word(printables)
parameters = Group(Word(printables) + "=" + Word(printables))
parameters_separator = Suppress("&")

# Definición de la CFG para la URL
url = protocol + OneOrMore(domain_name) + tld + ZeroOrMore("/" + route) + ZeroOrMore(parameters_separator + parameters)

def validate_url(url_ejemplo):
    try:
        resultado = url.parseString(url_ejemplo)
        # print("URL válida:", url_ejemplo)
        return True
    except Exception as e:
        # print("URL no válida:", url_ejemplo)
        return False

def validate_urls_in_text(texto):
    urls_encontradas = re.findall(r'http[s]?://(?:[^\s]+)', texto)
    correct_urls = []
    for url in urls_encontradas:
        if validate_url(url):
            correct_urls.append(url)
    return correct_urls