argumento = "www.bytebank.com/cambio?moedaorigem=real&moedadestino=dolar&valor=1500"
substring = argumento[4:12]
print("\n{}\n".format(substring))
argumento = "moedaorigem=real"
listadeargumentos = argumento.split("=")
print(listadeargumentos)
