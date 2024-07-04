import re
import subprocess
import os
from terminate_ports import PortTerminator
from run_java import RunJava
from run_node import RunNode

class ProjectRunner:
    def __init__(self, filename):
        self.filename = filename

    def read_projects(self):
        projects = []
        with open(self.filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                match = re.match(r'^"([^"]+)",\s*(\d+),\s*(java|react)', line)
                if match:
                    projects.append({
                        'path': match.group(1),
                        'port': match.group(2),
                        'type': match.group(3)
                    })
        return projects

    def run_projects(self, projects):
        for project in projects:
            project_path = project['path']
            project_type = project['type']
            print(f"Ejecutando proyecto en {project_path} de tipo {project_type}")

            if project_type == 'java':
                java_runner = RunJava(project_path)
                java_runner.find_and_run_jar()
            elif project_type == 'react':
                node_runner = RunNode(project_path)
                node_runner.run_server_js()

def main():
    # Terminar procesos
    terminator = PortTerminator('routes.txt')
    terminator.read_ports()
    terminator.terminate_processes()

    # Leer y ejecutar proyectos
    project_runner = ProjectRunner('routes.txt')
    projects = project_runner.read_projects()
    project_runner.run_projects(projects)

if __name__ == "__main__":
    main()
