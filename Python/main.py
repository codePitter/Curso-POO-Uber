from car import Car
from account import Account
from uberX import UberX
from user import User

if __name__ == "__main__":
    print("Inicializando la info de los autos")
    print("Car")
    car = Car("AMS546", Account("Andres Herrera", "AND123"));
    print(vars(car))
    print(vars(car.driver))

    print("UberX")
    uberX = UberX("ASD156", Account("Marcelo Lois", "FD421", "jose@gamil.com", 4658))
    print(vars(uberX))
    print(vars(uberX.driver))

    print("User")
    user = User("Marcela Perez", "HJG421", "mar@gamil.com", 1234)
    print(vars(user))