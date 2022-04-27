# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# generar un scrip que cambie el dominio de los email,de @test.com a @newemail.com,
# cuando el cambio se ejecute generar un csv con el nombre completo y el email sacado de la informacion del email

# ejemplo:
# email, name
# Ricardo Valbuena, ricardo.valbuena@test.com

from os import replace

import names
import csv

def generated_name():
    generated_email_list = []
    for _ in range(50):
        name = names.get_full_name()
        name = name.replace(" ", ".")
        name = name.lower()
        name = name + "@test.com"
        generated_email_list.append(name)
    return generated_email_list

def cambiodominio(value):
    email_list = []

    for correo in value:
        correo = correo.replace('@test.com','@newemail.com')
        email_list.append(correo)

    archivo = 'correos.csv'

    with open(archivo,'w') as csvarchivo:
        fields = ['email', 'name']
        writer = csv.DictWriter(csvarchivo, fieldnames=fields)
        writer.writeheader()
        for n in email_list:
            nombre = n.replace('@newemail.com', '')
            nombre = nombre.replace('.', ' ')
            nombre = nombre.title()
            writer.writerow({'email': '{}'.format(n), 'name': '{}'.format(nombre)})


cambiodominio(generated_name())