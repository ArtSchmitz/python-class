import urllib.request, urllib.error, urllib.parse
from functools import reduce
from collections import defaultdict
from collections import Counter
from operator import add
import sys

def listaPalavrasPFreqDici(lista_palavras):
    freq_palavras = [lista_palavras.count(p) for p in lista_palavras]
    return dict(list(zip(lista_palavras,freq_palavras)))

def ordenaDicionario(freq_dicionario):
    aux = [(freq_dicionario[key], key) for key in freq_dicionario]
    aux.sort()
    aux.reverse()
    return aux

def removeStopwords(lista_palavras, stopwords):
    return [w for w in lista_palavras if w not in stopwords]

def stripTags(pageContents):
    pageContents = str(pageContents)
    startLoc = pageContents.find("<p>")
    endLoc = pageContents.rfind("<br/>")

    pageContents = pageContents[startLoc:endLoc]

    inside = 0
    text = ''

    for char in pageContents:
        if char == '<':
            inside = 1
        elif (inside == 1 and char == '>'):
            inside = 0
        elif inside == 1:
            continue
        else:
            text += char

    return text

url_001 = 'https://pt.wikipedia.org/wiki/COBOL'
url_002 = 'https://pt.wikipedia.org/wiki/Linguagem_assembly'
url_003 = 'https://pt.wikipedia.org/wiki/C'

response_001 = urllib.request.urlopen(url_001)
response_002 = urllib.request.urlopen(url_002)
response_003 = urllib.request.urlopen(url_003)

html_001 = response_001.read().decode('UTF-8')
html_002 = response_002.read().decode('UTF-8')
html_003 = response_003.read().decode('UTF-8')

stopwords = ['a','agora','ainda','alguém','algum','alguma','algumas','alguns','ampla','amplas','amplo',
             'amplos','ante','antes','ao','aos','após','aquela','aquelas','aquele','aqueles','aquilo',
             'as','até','através','cada','coisa','coisas','com','como','contra','contudo','da','daquele',
             'daqueles','das','de','dela','delas','dele','deles','depois','dessa','dessas','desse',
             'desses','desta','destas','deste','deste','destes','deve','devem','devendo','dever',
             'deverá','deverão','deveria','deveriam','devia','deviam','disse','disso','disto','dito',
             'diz','dizem','do','dos','e','é','ela','elas','ele','eles','em','enquanto','entre','era',
             'essa','essas','esse','esses','esta','está','estamos','estão','estas','estava','estavam',
             'estávamos','este','estes','estou','eu','fazendo','fazer','feita','feitas','feito','feitos',
             'foi','for','foram','fosse','fossem','grande','grandes','há','isso','isto','já','la','lá',
             'lhe','lhes','lo','mas','me','mesma','mesmas','mesmo','mesmos','meu','meus','minha',
             'minhas','muita','muitas','muito','muitos','na','não','nas','nem','nenhum','nessa',
             'nessas','nesta','nestas','ninguém','no','nos','nós','nossa','nossas','nosso','nossos',
             'num','numa','nunca','o','os','ou','outra','outras','outro','outros','para','pela','pelas',
             'pelo','pelos','pequena','pequenas','pequeno','pequenos','per','perante','pode','pude',
             'podendo','poder','poderia','poderiam','podia','podiam','pois','por','porém','porque',
             'posso','pouca','poucas','pouco','poucos','primeiro','primeiros','própria','próprias',
             'próprio','próprios','quais','qual','quando','quanto','quantos','que','quem','são','se',
             'seja','sejam','sem','sempre','sendo','será','serão','seu','seus','si','sido','só','sob',
             'sobre','sua','suas','talvez','também','tampouco','te','tem','tendo','tenha','ter','teu',
             'teus','ti','tido','tinha','tinham','toda','todas','todavia','todo','todos','tu','tua',
             'tuas','tudo','última','últimas','último','últimos','um','uma','umas','uns','vendo','ver',
             'vez','vindo','vir','vos','vós', '/', '|', '1', '&#x27e8;ch&#x27e9;', '/k/.', '/ʃ/', ';',
             'isbn&#160;0-471-80461-4&#160;', '&#x27e8;c&#x27e9;','2021&#160;', '7', '&#x27e8;c&#x27e9;']

response_001 = urllib.request.urlopen(url_001)
html_001 = response_001.read().decode('UTF-8')
texto_001 = stripTags(html_001).lower()

lista_palavras_001 = texto_001.split()
lista_palavras_001 = removeStopwords(lista_palavras_001, stopwords)
dicionario_001 = listaPalavrasPFreqDici(lista_palavras_001)
dicionario_filtrado_001 = {key: val for key, val in dicionario_001.items() if val > 2}
ordenacao_dicionario_001 = ordenaDicionario(dicionario_filtrado_001)

response_002 = urllib.request.urlopen(url_002)
html_002 = response_002.read().decode('UTF-8')
texto_002 = stripTags(html_002).lower()

lista_palavras_002 = texto_002.split()
lista_palavras_002 = removeStopwords(lista_palavras_002, stopwords)
dicionario_002 = listaPalavrasPFreqDici(lista_palavras_002)
dicionario_filtrado_002 = {key: val for key, val in dicionario_002.items() if val > 2}
ordenacao_dicionario_002 = ordenaDicionario(dicionario_filtrado_002)

response_003 = urllib.request.urlopen(url_003)
html_003 = response_003.read().decode('UTF-8')
texto_003 = stripTags(html_003).lower()

lista_palavras_003 = texto_003.split()
lista_palavras_003 = removeStopwords(lista_palavras_003, stopwords)
dicionario_003 = listaPalavrasPFreqDici(lista_palavras_003)
dicionario_filtrado_003 = {key: val for key, val in dicionario_003.items() if val > 2}
ordenacao_dicionario_003 = ordenaDicionario(dicionario_filtrado_003)

print("\n\nDicionário mapeados e reduzidos:\n")

sys.stdout.reconfigure(encoding='utf-8')

dict_list = [ordenacao_dicionario_001, ordenacao_dicionario_002, ordenacao_dicionario_003]
sum_dict = reduce(add, (map(Counter, dict_list)))
print(sum_dict)