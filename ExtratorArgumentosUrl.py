class ExtratorArgumentosUrl:

    def __init__(self, url):
        if self.valida_url(url):
            self.__url = url
        else:
            raise LookupError("\nUrl inválida!")

    @property
    def url(self):
        return self.__url

    @staticmethod
    def valida_url(url):
        return True if url else False

    def obtem_indice_inicial(self, argumento_buscado):
        return self.url.find(argumento_buscado) + len(argumento_buscado) + 1

    def obtem_indice_final(self, argumento_buscado, indice_argumento_inicial):
        # O argumento inicial é necessário para não buscar a informação errada.
        return self.url.find(argumento_buscado, indice_argumento_inicial)

    def extrai_argumentos(self):
        # O primeiro argumento é o string/caractere desejado e o segundo argumento indica
        # a partir de qual índice será iniciada a busca pelo caractere desejado.
        moeda_origem = self.url[self.obtem_indice_inicial("moedaorigem"):
                                self.obtem_indice_final("&", self.obtem_indice_inicial("moedaorigem"))]
        moeda_destino = self.url[self.obtem_indice_inicial("moedadestino"):
                                 self.obtem_indice_final("&", self.obtem_indice_inicial("moedadestino"))]
        valor = self.url[self.obtem_indice_inicial("valor"):]
        return moeda_origem, moeda_destino, valor
