#!/bin/bash

# Function to start the dashboard
start_dashboard() {
    echo "Starting dashboard..."
    python ./yuukaDash/manage.py runserver
    # Add your code to start the dashboard here
}

# Function to make migrations
make_migrations() {
    echo "Making migrations..."
    python ./yuukaDash/manage.py makemigrations
    # Add your code to make migrations here
}

migrate() {
    echo "Migrating..."
    python ./yuukaDash/manage.py migrate
    # Add your code to migrate here
}

# Main script
while getopts "sab" opt; do
    case $opt in
        s)
            start_dashboard
            ;;
        a)
            make_migrations
            ;;
        b)
            migrate
            ;;
        *)
            echo "Invalid option. Please try again."
            ;;
    esac
done
