import re
import subprocess

class PortTerminator:
    def __init__(self, filename):
        self.filename = filename
        self.ports = []

    def read_ports(self):
        # Leer el archivo routes.txt
        with open(self.filename, 'r') as file:
            data = file.read()
        
        # Utilizar una expresión regular para encontrar todos los puertos
        self.ports = re.findall(r', (\d+),', data)

    def terminate_processes(self): 
        # Imprimir los puertos
        for puerto in self.ports:
            print(f"Proceso en el puerto {puerto}:")

            # Usar lsof para encontrar el proceso que escucha en el puerto
            try:
                # Ejecutar lsof y obtener la salida
                proceso = subprocess.check_output(['sudo', 'lsof', '-i', f':{puerto}']).decode('utf-8')
                
                # Dividir la salida en líneas y filtrar por la que contiene 'LISTEN'
                lineas = proceso.splitlines()
                linea_listen = [linea for linea in lineas if 'LISTEN' in linea]

                if not linea_listen:
                    print(f"No se encontró ningún proceso escuchando en el puerto {puerto}.")
                    continue
                
                # Extraer el PID del proceso de la línea 'LISTEN'
                pid = linea_listen[0].split()[1]
                
                # Matar el proceso usando kill -9
                subprocess.run(['sudo', 'kill', '-9', pid])
                print(f"Proceso con PID {pid} terminado.")
            except subprocess.CalledProcessError:
                print(f"No se encontró ningún proceso escuchando en el puerto {puerto}.")
            except IndexError:
                print(f"No se pudo obtener el PID del proceso escuchando en el puerto {puerto}.")

