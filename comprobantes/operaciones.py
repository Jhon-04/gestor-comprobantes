import json
import os
from comprobantes.modelo import Comprobante

RUTA_ARCHIVO = "data/comprobantes.json"

def cargar_comprobantes():
    if not os.path.exists(RUTA_ARCHIVO):
        return []
    with open(RUTA_ARCHIVO, "r") as archivo:
        try:
            return json.load(archivo)
        except json.JSONDecodeError:
            return []

def guardar_comprobantes(comprobantes):
    with open(RUTA_ARCHIVO, "w") as archivo:
        json.dump(comprobantes, archivo, indent=4)

def registrar_comprobante():
    tipo = input("Tipo de comprobante (Factura/Boleta): ")
    proveedor = input("Nombre del proveedor: ")
    monto = float(input("Monto del comprobante: "))

    comprobante = Comprobante(tipo, proveedor, monto)
    comprobantes = cargar_comprobantes()
    comprobantes.append(comprobante.to_dict())
    guardar_comprobantes(comprobantes)

    print("✅ Comprobante registrado correctamente.")

def listar_comprobantes():
    comprobantes = cargar_comprobantes()
    if not comprobantes:
        print("No hay comprobantes registrados.")
        return

    print("\n📄 Lista de Comprobantes:")
    for c in comprobantes:
        print(f"{c['fecha']} - {c['tipo']} - {c['proveedor']} - S/ {c['monto']}")
