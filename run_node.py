import re
import subprocess
import os

class RunNode:
    def __init__(self, project_directory):
        self.project_directory = project_directory

    def run_server_js(self):
        server_js_path = os.path.join(self.project_directory, 'server.js')
        
        if not os.path.isfile(server_js_path):
            print(f"El archivo {server_js_path} no existe.")
            return
        
        # Ejecutar el archivo server.js en segundo plano
        try:
            subprocess.Popen(['sudo', 'node', server_js_path], check=True)
            print(f"Ejecutando {server_js_path} en segundo plano.")
        except subprocess.CalledProcessError as e:
            print(f"Error al ejecutar {server_js_path}: {e}")