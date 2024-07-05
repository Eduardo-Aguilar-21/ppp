#!/bin/bash

# Definir la clase RunJava equivalente en shell

# Función para ejecutar un archivo JAR en segundo plano
run_java() {
    project_directory="$1"
    target_directory="$project_directory/target"
    
    if [ ! -d "$target_directory" ]; then
        echo "El directorio $target_directory no existe."
        return
    fi
    
    # Buscar archivos .jar en el directorio target
    jar_files=$(find "$target_directory" -name "*.jar")
    
    if [ -z "$jar_files" ]; then
        echo "No se encontraron archivos .jar en $target_directory."
        return
    fi
    
    # Tomar el primer archivo .jar encontrado
    jar_file=$(echo "$jar_files" | head -n 1)
    
    # Ejecutar el archivo .jar en segundo plano
    echo "Ejecutando $jar_file en segundo plano."
    sudo java -jar "$jar_file" &
    
    # Obtener el PID del proceso JAR
    JAR_PID=$!
    
    # Esperar a que el proceso JAR termine
    wait $JAR_PID
    
    # Continuar con el resto del script
    echo "El archivo JAR ha terminado de ejecutarse. Continuando con el script..."
}

