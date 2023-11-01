print(f"__debug__ * {__debug__}")

if __debug__:
    print("Execução em modo Normal")
else:
    print("Execução em modo otimizado")
    # modo otimizado ignora diversos features da linguagem
    # que facilitam e melhoram a programação, mas não devem
    # ser passados para o cliente final do código
    # executar python em modo otimizado: python -O <file.py>