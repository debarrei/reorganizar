

def generar_saludo(persona):
    if persona["genero"] == 0:
        return f"Hola Señor {persona['nombre']}"
    else:
        return f"Hola Señora {persona['nombre']}"




if __name__ == "__main__":
    datos_persona = {"nombre": "Paquito", "genero": 0}
    saludo = generar_saludo(datos_persona)
    assert saludo == "Hola Señor Paquito"
    print(saludo)


    datos_persona = {"nombre": "Paquita", "genero": 1}
    saludo = generar_saludo(datos_persona)
    assert saludo == "Hola Señora Paquita"
    print(saludo)