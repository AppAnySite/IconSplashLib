#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Function to display usage
usage() {
  echo "Usage: $0 [-p <PROJECT_DIR>] [-i <ICON_PATH>] [-s <SPLASH_LOGO_PATH>] [-l] [--platform PLATFORM] [--folder FOLDER] [--icon-type ICON_TYPE] [--config CONFIG] [--dev]"
  echo "Provide either -i for icon generation, -s for splash screen generation, or both."
  echo "Use -l to generate and use the library."
  echo "Use --platform to specify the platform (android or ios)."
  echo "Use --folder to specify specific folders to generate icons for."
  echo "Use --icon-type to specify the type of icon to generate."
  echo "Use --config to specify a custom configuration file."
  echo "Use --dev to enable tqdm progress bar for development."
  exit 1
}

# Parse arguments
USE_LIBRARY=false
PROJECT_DIR="output"
ICON_PATH=""
SPLASH_LOGO_PATH=""
SIZES=()
PLATFORM=""
FOLDERS=()
ICON_TYPE=""
CONFIG=""
DEV_MODE=false

while [[ "$#" -gt 0 ]]; do
  case $1 in
    -p) PROJECT_DIR="$2"; shift ;;
    -i) ICON_PATH="$2"; shift ;;
    -s) SPLASH_LOGO_PATH="$2"; shift ;;
    -l) USE_LIBRARY=true ;;
    --size) SIZES+=("$2" "$3"); shift 2 ;;
    --platform) PLATFORM="$2"; shift ;;
    --folder) FOLDERS+=("$2"); shift ;;
    --icon-type) ICON_TYPE="$2"; shift ;;
    --config) CONFIG="$2"; shift ;;
    --dev) DEV_MODE=true ;;
    *) usage ;;
  esac
  shift
done

# Ensure at least one of the required arguments is provided
if [[ -z "$ICON_PATH" && -z "$SPLASH_LOGO_PATH" ]]; then
  usage
fi

# Ensure the output directory exists if PROJECT_DIR is not provided
mkdir -p "$PROJECT_DIR"

# Generate the library if -l is provided
if $USE_LIBRARY; then
  echo "Generating library..."
  ./generate_library.sh
  LIBRARY_PATH="./dist/IconSplashLib/IconSplashLib"
else
  LIBRARY_PATH="python3 main.py"
fi

# Construct the command
CMD="$LIBRARY_PATH $PROJECT_DIR"
[[ -n "$ICON_PATH" ]] && CMD+=" --icon $ICON_PATH"
[[ -n "$SPLASH_LOGO_PATH" ]] && CMD+=" --splash $SPLASH_LOGO_PATH"
for (( i=0; i<${#SIZES[@]}; i+=2 )); do CMD+=" --size ${SIZES[i]} ${SIZES[i+1]}"; done
[[ -n "$PLATFORM" ]] && CMD+=" --platform $PLATFORM"
for FOLDER in "${FOLDERS[@]}"; do CMD+=" --folder $FOLDER"; done
[[ -n "$ICON_TYPE" ]] && CMD+=" --icon-type $ICON_TYPE"
[[ -n "$CONFIG" ]] && CMD+=" --config $CONFIG"
$DEV_MODE && CMD+=" --dev"

# Execute the command
echo "Running script to generate icons..."
eval $CMD

echo "All operations completed successfully."
