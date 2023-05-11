#bob = {'nombre': 'Bob', 'apellidos': 'Esponja', 'edad': 4}

def create_person(nombre, apellido, edad):
    return {'nombre': nombre.capitalize(), 'apellidos': apellido.capitalize(), 'edad': edad}




bob = create_person('bob', 'esponja', 4)
patricio = create_person('patricio', 'estrella', 3)

print(patricio)
print(bob)


def get_birth_date(persona):
    return 2023 - persona['edad']


def print_person_birth_date(pers):
        print(f"The person {pers['nombre']} was born in {str(get_birth_date(pers))}")

print_person_birth_date(bob)

#another change