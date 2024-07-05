#!/bin/bash

# Definir la clase RunNode equivalente en shell

# Función para ejecutar server.js en segundo plano
run_node() {
    project_directory="$1"
    server_js_path="$project_directory/server.js"

    if [ ! -f "$server_js_path" ]; then
        echo "El archivo $server_js_path no existe."
        return
    fi

    # Ejecutar server.js en segundo plano
    echo "Ejecutando $server_js_path en segundo plano."
    sudo node "$server_js_path" &
}


