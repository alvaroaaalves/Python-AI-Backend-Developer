class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, aro=18):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
    def buzinar(self):
        print("Plim plim...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmm...")

    def trocar_marcha(self, nro_marcha):
        print ("Trocando marcha")

        def trocar_marcha():
            print("ok")
            if (nro_marcha > _self.marcha):
                print ("Marcha trocada")
            else:
                print ("Não foi possível trocar de marcha")


b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
b1._trocar_marcha(19)
print ('\n',b1)


