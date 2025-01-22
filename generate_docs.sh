#!/bin/bash

# Define variables
PROJECT_DIR=$(pwd)
DOCS_DIR="$PROJECT_DIR/docs"
SOURCE_DIR="$DOCS_DIR/source"
BUILD_DIR="$DOCS_DIR/build"
VERSION="0.2"

# Function to update the version in conf.py
update_version() {
    CONF_FILE="$SOURCE_DIR/conf.py"
    sed -i '' "s/^release = .*/release = '$VERSION'/g" $CONF_FILE
    echo "Updated version in conf.py to $VERSION"
}

# Function to generate new reStructuredText files
generate_rst() {
    sphinx-apidoc -o $SOURCE_DIR $PROJECT_DIR
    echo "Generated new reStructuredText files"
}

# Function to build HTML documentation
build_html() {
    cd $DOCS_DIR
    make html
    echo "Built HTML documentation"
}

# Function to clean old build files
clean_build() {
    rm -rf $BUILD_DIR/*
    echo "Cleaned old build files"
}

# Main script
main() {
    update_version
    clean_build
    generate_rst
    build_html
    echo "Documentation generation complete. Open $BUILD_DIR/html/index.html to view the documentation."
}

main
