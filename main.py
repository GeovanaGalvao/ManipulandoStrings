from ExtratorArgumentosUrl import ExtratorArgumentosUrl

'''
------------------------------------------------------------------------------------------------------------------------
argumento = "www.bytebank.com/cambio?moedaorigem=real&moedadestino=dolar&valor=1500"
substring = argumento[4:12]
print("\n{}\n".format(substring))
------------------------------------------------------------------------------------------------------------------------
argumento = "moedaorigem=real"
listadeargumentos = argumento.split("=")
print(listadeargumentos)
------------------------------------------------------------------------------------------------------------------------
url = "www.bytebank.com/cambio?moedaorigem=real&moedadestino=dolar&valor=1500"
argumento = ExtratorArgumentosUrl(url)
print("\nEssa url é válida? {}".format(ExtratorArgumentosUrl.valida_url(url)))
print("\n{}".format(argumento))
moeda_origem, moeda_destino, valor = argumento.extrai_argumentos()
print("\nSerá convertido {} de {} para {}".format(valor, moeda_origem, moeda_destino))
------------------------------------------------------------------------------------------------------------------------
# Teste da nova implementação na validação da URL; Essa linha vai crashar o programa e indicar que a URL está incorreta.
url = "https://www.bitebank.com/cambio?MoedaOrigem=MoedaDestino&MoedaDestino=dolar&valor=1500"
argumento = ExtratorArgumentosUrl(url)
------------------------------------------------------------------------------------------------------------------------
'''

url = "https://www.bytebank.com/cambio?MoedaOrigem=MoedaDestino&MoedaDestino=dolar&valor=1500"
argumento = ExtratorArgumentosUrl(url)
moeda_origem, moeda_destino, valor = argumento.extrai_argumentos()
print("\nSerá convertido o valor de {} da moeda {} para {}".format(valor, moeda_origem, moeda_destino))
