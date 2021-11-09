class Computador:
    def __init__(self, fabricante, modelo, processador, memoriaRam, tamanhoHD, espacoHD, ligado=False):
        self.fabricante = fabricante
        self.modelo = modelo
        self.processador = processador 
        self.memoriaRam = memoriaRam
        self.tamanhoHD = tamanhoHD
        self.espacoHD = espacoHD
        self.ligado = ligado
    
    
    # Ligar ou desligar
    def ligarDesligar (self):
        if self.ligado == "ligado":
            return True
        self.ligado = False
    


    # Limpar o HD 
    def limpaHD (self,valor):
        if valor  <= self.tamanhoHD:
            self.espacoHD -= valor
            return True
        return False       


    # ocupar o HD 
    def ocupaHD (self,valor):
        if valor  <= self.tamanhoHD:
            self.espacoHD = valor
            return True
        return False    