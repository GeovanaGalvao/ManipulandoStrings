class ExtratorArgumentosUrl:

    def __init__(self, url):
        if self.valida_url(url):
            self.__url = url.lower()
        else:
            raise LookupError("\nUrl inválida!")

    def __len__(self):
        return len(self.__url)

    def __str__(self):
        moeda_origem, moeda_destino, valor = self.extrai_argumentos()
        return "\n{}\nA url tem {} caracteres.\n\nSerá convertido o valor de {} da moeda {} para {}"\
            .format(self.url, len(self.url), valor, moeda_origem, moeda_destino)

    def __eq__(self, other):
        return self.url == other.url

    @property
    def url(self):
        return self.__url

    @staticmethod
    def valida_url(url):
        return True if url and url.startswith("https://www.bytebank.com") else False

    def obtem_indice_inicial(self, argumento_buscado):
        return self.url.find(argumento_buscado) + len(argumento_buscado) + 1

    def obtem_indice_final(self, argumento_buscado, indice_argumento_inicial):
        # O argumento inicial é necessário para não buscar a informação errada.
        return self.url.find(argumento_buscado, indice_argumento_inicial)

    def troca_moeda_origem(self):
        self.__url = self.__url.replace("moedadestino", "real", 1)

    def extrai_argumentos(self):
        # O primeiro argumento é o string/caractere desejado e o segundo argumento indica
        # a partir de qual índice será iniciada a busca pelo caractere desejado.
        moeda_origem = self.url[self.obtem_indice_inicial("moedaorigem"):
                                self.obtem_indice_final("&", self.obtem_indice_inicial("moedaorigem"))]

        if moeda_origem == "moedadestino":
            self.troca_moeda_origem()
            moeda_origem = self.url[self.obtem_indice_inicial("moedaorigem"):
                                    self.obtem_indice_final("&", self.obtem_indice_inicial("moedaorigem"))]

        moeda_destino = self.url[self.obtem_indice_inicial("moedadestino"):
                                 self.obtem_indice_final("&", self.obtem_indice_inicial("moedadestino"))]
        valor = self.url[self.obtem_indice_inicial("valor"):]
        return moeda_origem, moeda_destino, valor
