#!/bin/bash

# Automated Project Runner
# Copyright (C) 2024 Eduardo Aguilar AST
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

# Source the .bashrc file to ensure that the PROJECT_DIR variable is loaded
#source ~/.bashrc

# Obtiene la ubicación del script autorun.sh y navega a la carpeta Scripts
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

echo $PROJECT_DIR
# Source the necessary scripts using the PROJECT_DIR variable
source "lib/run_java.sh"
source "lib/run_node.sh"

# Check if the route.txt file exists
if [ ! -f "routes.txt" ]; then
    echo "Error: File 'routes.txt' not found."
    echo "Add routes.txt file."
    exit 1
fi

# Read the paths and ports from the file routes.txt, ignoring lines that start with #
mapfile -t routes < <(grep -v '^#' routes.txt)

echo "************ Automated Project Runner ************"

# Iterate over the routes and ports
for route in "${routes[@]}"; do
    # Remove quotes from the route and port
route="${route//\"}"
    # Get the route and port
    IFS=', ' read -r -a parts <<< "$route"
    project="${parts[0]}"
    port="${parts[1]}"

    # Change to the project directory
    cd "$project" || {
    echo "Error: Failed to change directory to '$project'."
    continue
    }


    # Check if it's a Java (Maven) project
    if [ -f "pom.xml" ]; then
        run_java "$project"
    # Check if it's a React project
    elif [ -f "package.json" ]; then
        run_node "$project"
    else
        echo "Unknown application type: $project"
    fi
done

echo "************ Automated Project Runner Finished ************"
echo "************ All services ran successfully ************"