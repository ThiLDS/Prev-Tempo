import requests
from bs4 import BeautifulSoup
import pyttsx3

cidade = input('Digite a cidade qua quer saber a previsão do tempo: ')
busca =f"A Previsão do tempo em {cidade} é de "
url = f"https://www.google.com/search?q={busca}"
r = requests.get(url)
s= BeautifulSoup(r.text, "html.parser")
update = s.find("div",class_="BNeawe").text
a = (busca + update)
print(a)
engine = pyttsx3.init()
engine.say(a)
engine.runAndWait()