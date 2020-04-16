# Pasos para la instalación de la app de star wars

#1) Moverse al directorio "api" dentro del directorio "star_wars".

#2) Ejecutar el comando "docker-compose build".

#3) Ejecutar el comando "docker-compose up".

# Pasos para la instalación de la app de The Mandalorian

#1) Ir al directorio "api" dentro del directorio "the_mandalorian".

#2) Ejecutar el comando "pip install redis flask".

#3) Iniciar el contenedor de redis de Docker.

#4) Verificar con el comando docker inspect "id_del_contenedor" si la ipAddress coincide con el valor del host ubicado en la línea 7 de app.py; en caso contrario, modificarlo.

#5) Ejecutar el comando "flask run".

