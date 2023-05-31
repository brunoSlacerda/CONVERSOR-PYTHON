import requests #Importa a biblioteca requests para poder pegar a api da cotação
import json

def moedas():
    moeda = input("Informe a moeda a ser utilizada (Euro,Dólar,Bitcoin) : ").upper() #Uper foi utilizado para não haver erros do usuario de digitação
    return moeda

def valores():
    while True:
        try:
            print("="*60)
            valor = float(input("Informe a quantidade do valor que deseja conveter : "))
            break
        except ValueError:
            print("Valor inválido! TENTE NOVAMENTE.")
    return valor

cotacoes = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacoes = cotacoes.json()

dollar = cotacoes['USDBRL'] ['bid'] #Recebe o valor do dólar da api
euro = cotacoes['EURBRL'] ['bid'] #Recebe o valor do euro da api
bitcoin = cotacoes['BTCBRL'] ['bid'] #Recebe o valor do bitcoin da api


valor = valores() #Chama as funções e recebe seu valor
moeda = moedas() #Chama as funções e recebe seu valor


if moeda == 'EURO':  #Calcula euro
    conversao = valor * float(euro)
    print("="*60)
    print(f"Hoje, {valor}€ são aproximadamente {conversao:.2f}R$")
        

elif moeda == 'DOLLAR': #Calcula dólar
    conversao = valor * float(dollar)
    print("="*60)
    print(f"Hoje, {valor} US$ são aproximadamente {conversao:.2f}R$")
        

elif moeda == 'BITCOIN': #Calcula bitcoin
    conversao = valor * float(bitcoin)
    print("="*60)
    print(f"Hoje, {valor} US$ são aproximadamente {conversao:.2f}R$")
               
else: 
    print("MOEDA NÃO ENCONTRADA. ENCERRANDO PROGRAMA!")
        
   
