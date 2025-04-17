from comprobantes.operaciones import registrar_comprobante, listar_comprobantes

def menu():
    while True:
        print("\n--- Gestor de Comprobantes ---")
        print("1. Registrar comprobante")
        print("2. Listar comprobantes")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == '1':
            registrar_comprobante()
        elif opcion == '2':
            listar_comprobantes()
        elif opcion == '3':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
