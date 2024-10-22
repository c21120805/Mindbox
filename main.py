from Menu.menu import Menu
from ZOO.zoo import Zoo
import bcrypt

def main():
    zoo = Zoo()
    menu = Menu(zoo)
    try:
        menu.login()
    except ValueError as ve:
        print(f"Error de validación: {ve}")
    except bcrypt.exceptions.BcryptError as be:
        print(f"Error de bcrypt: {be}")
    except Exception as e:
        print(f"Error inesperado durante la ejecución del programa: {e}")

if __name__ == "__main__":
    main()