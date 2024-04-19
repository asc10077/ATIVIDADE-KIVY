class Veiculo:
def __init__(self, marca, modelo):
    self.marca = marca
    self.modelo = modelo

def frear (self):
    return(f"{self.marca} {self.modelo} o veiculo está freando")

def acelerar (self):
    return(f"{self.marca} {self.modelo} o veiculo está acelerando")

class Carro(Veiculo):
    def __init__ (self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor
    def abrir_porta(self):
        return (f" as portas do {self.marca} {self.modelo} {self.cor} estão abertas")
class Moto (Veiculo):
    def __init__ (self, marca, modelo, cilindrada):
        super().__init__(marca,modelo)
        self.cilindrada = cilindrada
    def empinar(self):
        return(f"{self.marca} {self.modelo} {self.cilindrada} está empinando")
    
if __name__ == "__main__":
    carro = Carro("fiat", "palio", "branco")
    print(carro.frear())
    print(carro.acelerar())
    print(carro.abrir_porta())

    moto = Moto("honda", "titan", "160")
    print(moto.frear())
    print(moto.acelerar())
    print(moto.empinar())
    