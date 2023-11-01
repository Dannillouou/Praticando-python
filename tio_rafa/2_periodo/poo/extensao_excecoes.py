class DeuRuimError(ZeroDivisionError):
    def __init__(self, message="Deu ruim, mané!") -> None:
        self.message = message
        super().__init__(self.message)
        
def teste():
    raise DeuRuimError

try:
    teste()
except DeuRuimError:
    print("Pelo menos tentamos 2...")