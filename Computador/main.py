from Computador import Computador

# Entradas do usuário
espacoHD = int(input("Qual o espaço do HD (gb)? "))
ligado = input("O PC está ligado ou desligado?: ")




# instanciando o objeto
pc1 = Computador("Dell", "Dell Inspiron", "Intel Core i9", "16", 1000, espacoHD, ligado)

print ("Modelo do computador: ", pc1.modelo)
print ("Fabricante do computador: ", pc1.fabricante)

pc1.ligarDesligar()
if (pc1.ligado):
    print ("O computador está ligado.")
else:
    print ("O computador está desligado.") 






ligarOcupar = input("você deseja limpar ou ocupar o HD? ")

if ligarOcupar == "limpar":
    if pc1.limpaHD (500):
         print ("O HD foi limpo, sobrando: ", pc1.espacoHD)
    else:
        print ("O HD não pode ser limpo") 
if ligarOcupar == "ocupar":
    if pc1.ocupaHD (500):
        print ("O HD foi ocupado com: ", pc1.espacoHD)
    else:
        print ("O HD não pode ser limpo") 