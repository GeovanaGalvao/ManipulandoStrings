from ExtratorArgumentosUrl import ExtratorArgumentosUrl

'''
argumento = "www.bytebank.com/cambio?moedaorigem=real&moedadestino=dolar&valor=1500"
substring = argumento[4:12]
print("\n{}\n".format(substring))
------------------------------------------------------------------------------------
argumento = "moedaorigem=real"
listadeargumentos = argumento.split("=")
print(listadeargumentos)
'''

url = "www.bytebank.com/cambio?moedaorigem=real&moedadestino=dolar&valor=1500"
argumento = ExtratorArgumentosUrl(url)
print("\nEssa url é válida? {}".format(ExtratorArgumentosUrl.valida_url(url)))
print("\n{}".format(argumento))
moeda_origem, moeda_destino, valor = argumento.extrai_argumentos()
print("\nSerá convertido {} de {} para {}".format(valor, moeda_origem, moeda_destino))
