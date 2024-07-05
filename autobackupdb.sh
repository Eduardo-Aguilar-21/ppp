#!/bin/bash

# Ruta donde se guardarán los backups
backup_dir="/etc/automation/mysql_backups"

# Obtener la fecha actual en el formato deseado (dd-mm-yyyy)
current_date=$(date +"%d-%m-%Y")

# Crear la carpeta con el nombre del día actual
backup_folder="$backup_dir/$current_date"
mkdir -p "$backup_folder"

# Leer el archivo db_list.txt línea por línea
while IFS= read -r database
do
    # Generar el nombre del archivo de backup
    backup_file="$backup_folder/${database}-${current_date}.sql"

    # Crear el backup de la base de datos actual
    mysqldump -u tu_usuario -pcontraseña --databases "$database" > "$backup_file"

    # Comprobar si el backup se realizó correctamente
    if [ $? -eq 0 ]; then
        echo "Backup de $database realizado correctamente en $backup_file"
    else
        echo "Error al realizar el backup de $database"
    fi
done < "db_list.txt"
