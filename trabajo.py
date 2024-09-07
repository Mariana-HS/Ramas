def verificar_nombre(nombre):
    # Verifica que el nombre no esté vacío y solo contenga letras
    if nombre.isalpha():
        return True
    else:
        return False

def pedir_nombre():
    nombre = input("Introduce tu nombre: ")
    
    if verificar_nombre(nombre):
        print(f"Hola, {nombre}. ¡Tu nombre es válido!")
    else:
        print("Error: El nombre debe contener solo letras y no estar vacío.")

if __name__ == "__main__":
    pedir_nombre()
