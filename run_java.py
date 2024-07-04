import re
import subprocess
import os

class RunJava:
    def __init__(self, project_directory):
        self.project_directory = project_directory

    def find_and_run_jar(self):
        target_directory = os.path.join(self.project_directory, 'target')
        
        if not os.path.isdir(target_directory):
            print(f"El directorio {target_directory} no existe.")
            return
        
        # Buscar archivos .jar en el directorio target
        jar_files = [f for f in os.listdir(target_directory) if f.endswith('.jar')]
        
        if not jar_files:
            print(f"No se encontraron archivos .jar en {target_directory}.")
            return
        
        # Tomar el primer archivo .jar encontrado
        jar_file = jar_files[0]
        jar_path = os.path.join(target_directory, jar_file)
        
        # Ejecutar el archivo .jar en segundo plano
        try:
            subprocess.Popen(['sudo', 'java', '-jar', jar_path], check=True)
            print(f"Ejecutando {jar_path} en segundo plano.")
        except subprocess.CalledProcessError as e:
            print(f"Error al ejecutar {jar_path}: {e}")