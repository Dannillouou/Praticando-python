class Foo:
    def __init__(self) -> None:
        self.public = "Public"
        self._protected = "_Protected"
        self.__private = "__Private"

    def public_method(self):
        print("Metodo publico")
        self._protected_method()

    def _protected_method(self):
        print("Método protegido")

    def __private_method(self):
        print("Método privado")        

class Bar(Foo):
    def using_parent_public_method_and_attribute(self):
        print("OK invocar métodos públicos e acessar atributos públicos")
        super().public_method()
        print(self.public)

    def using_parent_protected_method_and_attribute(self):
        print("OK invocar métodos públicos e acessar atributos protegidos")
        super().public_method()
        print(self.public)

    def using_private_protected_method_and_attribute(self):
        print("OK invocar métodos públicos e acessar atributos privado")
        super().public_method()
        print(self.public)


print("="*80)
object_ = Foo()
print(object_.public)
object_.public_method()

print("="*80)
print("ERRO SEMÂNTICO")
print(object_._protected)
object_._protected_method()

print("="*80)
print("ERRO SEMÂNTICO")
print(object_.__private)
object_.__private_method()