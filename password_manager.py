import csv

from caesar import caesar_encrypt


def encrypt_single_pass(filename: str) -> None:
    """TODO: Parte 1."""
    with open(filename, "r") as archivo: 
        password = archivo.read().strip()
    call = caesar_encrypt(password)
    with open(filename, "w") as documento: 
        documento.write(call)

def encrypt_passwords_in_file(filename: str) -> None:
    filas = []
    with open(filename, "r") as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            if fila:
                filas.append(fila)
    for i in range(len(filas)):
        if i != 0:
            password = filas[i][2]
            filas[i][2] = caesar_encrypt(password)
    with open(filename, "w", newline="") as archivo:
        escritor = csv.writer(archivo)
        for fila in filas:
            escritor.writerow(fila)

def change_password(filename: str, website: str, password: str) -> bool:
    filas = []
    with open(filename, "r") as archivo:
        lector = csv.reader(archivo)
        for fila in lector:
            if fila:
                filas.append(fila)
    encontrado = False
    for i in range(len(filas)):
        if filas[i][0] == website:
            filas[i][2] = caesar_encrypt(password)
            encontrado = True
    if not encontrado:
        return False
    with open(filename, "w", newline="") as archivo:
        escritor = csv.writer(archivo)
        for fila in filas:
            escritor.writerow(fila)
    return True

def add_login(filename: str, website_name: str, username: str, password: str) -> None:
    password_encriptada = caesar_encrypt(password)
    with open(filename, "a", newline="") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow([website_name, username, password_encriptada])
