import requests

def infoRequest():
    qtd = 3
    info = requests.get('https://uinames.com/api/?ext&amount='+ str(qtd) +'&region=Brazil',timeout=5.0).json()
    frases = []
    for i in range(0,qtd):
        frase = "My name is {} {} and the PIN on my card is {}.".format(info[i]['name'],info[i]['surname'],info[i]['credit_card']['pin']) 
        frases.append(frase)   
    return frases

if __name__ == '__main__':
    print(infoRequest())