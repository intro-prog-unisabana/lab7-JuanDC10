from password_manager import add_login, change_password, encrypt_passwords_in_file

def main() -> None:
    print("Enter the CSV file name:")
    filename = input()
    encrypt_passwords_in_file(filename)
    while True:
        print("Options: (1) Change Password, (2) Add Password, (3) Quit:")
        opcion = input()
        if opcion == "1":
            print("Enter the website and the new password:")
            entrada = input()
            partes = entrada.split()
            if len(partes) < 2:
                print("Input is in the wrong format!")
                continue
            website = partes[0]
            password = partes[1]
            if len(password) < 12:
                print("Password is too short!")
                continue
            resultado = change_password(filename, website, password)
            if resultado:
                print("Password changed.")
            else:
                print("Website not found! Operation failed.")
        elif opcion == "2":
            print("Enter the website, username, and password:")
            entrada = input()
            partes = entrada.split()
            if len(partes) < 3:
                print("Input is in the wrong format!")
                continue
            website = partes[0]
            username = partes[1]
            password = partes[2]
            if len(password) < 12:
                print("Password is too short!")
                continue
            add_login(filename, website, username, password)
            print("Login added.")
        elif opcion == "3":
            break
        else:
            print("Invalid option selected!")


if __name__ == "__main__":
    main()
