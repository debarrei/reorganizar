from pprint import pprint
from pruebasPython.module.mimodulo import generar_saludo

pprint(locals())

print("--------------------------------")
from datetime import datetime
pprint(locals())




datos_persona = {"nombre": "Paquita", "genero": 1}
saludo = generar_saludo(datos_persona)
print(saludo)