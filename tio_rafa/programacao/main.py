from modulo_criptografas import *

print(cifra_reversa("Eu adoro a EMAp"))
mensagem_criptografada = cifra_de_cesar("Eu adoro a EMAp", "encriptar", 3)
print(mensagem_criptografada)
print(cifra_de_cesar(mensagem_criptografada, "decriptar", 3))