import modulo_criptografas

print(modulo_criptografas.cifra_reversa("Eu adoro a EMAp"))
mensagem_criptografada = modulo_criptografas.cifra_de_cesar("Eu adoro a EMAp", "encriptar", 3)
print(mensagem_criptografada)
print(modulo_criptografas.cifra_de_cesar(mensagem_criptografada, "decriptar", 3))