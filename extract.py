import re
import subprocess

# Leer el archivo routes.txt
with open('routes.txt', 'r') as file:
    data = file.read()

# Utilizar una expresión regular para encontrar todos los puertos
puertos = re.findall(r', (\d+),', data)

# Imprimir los puertos
for puerto in puertos:
    print(f"Proceso en el puerto {puerto}:")

    # Usar lsof para encontrar el proceso que escucha en el puerto
    try:
        proceso = subprocess.check_output(['sudo', 'lsof', '-i', f':{puerto}']).decode('utf-8')
        print(proceso)

        # Extraer el PID del proceso
        pid = proceso.split()[9]  # Ajustar el índice según el resultado de lsof

        # Matar el proceso usando kill -9
        subprocess.run(['sudo', 'kill', '-9', pid])
        print(f"Proceso con PID {pid} terminado.")
    except subprocess.CalledProcessError:
        print(f"No se encontró ningún proceso escuchando en el puerto {puerto}.")
    except IndexError:
        print(f"No se pudo obtener el PID del proceso escuchando en el puerto {puerto}.")
