# IconSplashLib

IconSplashLib is a tool for generating icons and splash screens for React Native projects. It supports both Android and iOS platforms.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Setup](#setup)
- [Usage](#usage)
  - [Generating Android Icons](#generating-android-icons)
    - [Generate All Android Icons](#generate-all-android-icons)
    - [Generate Android Icons by Category](#generate-android-icons-by-category)
    - [Generate Android Icons by Type and Category](#generate-android-icons-by-type-and-category)
    - [Generate Android Icons in Dev Mode](#generate-android-icons-in-dev-mode)
    - [Generate Android Icons with Library](#generate-android-icons-with-library)
    - [Generate Android Icons with Library and Dev Mode](#generate-android-icons-with-library-and-dev-mode)
    - [Generate Android Icons Inside a React Native Project](#generate-android-icons-inside-a-react-native-project)
  - [Generating iOS Icons](#generating-ios-icons)
    - [Generate All iOS Icons](#generate-all-ios-icons)
    - [Generate iOS Icons by Category](#generate-ios-icons-by-category)
    - [Generate iOS Icons in Dev Mode](#generate-ios-icons-in-dev-mode)
    - [Generate iOS Icons with Library](#generate-ios-icons-with-library)
    - [Generate iOS Icons with Library and Dev Mode](#generate-ios-icons-with-library-and-dev-mode)
    - [Generate iOS Icons Inside a React Native Project](#generate-ios-icons-inside-a-react-native-project)
  - [Generating Splash Screen](#generating-splash-screen)
    - [Generate Splash Screen Images](#generate-splash-screen-images)
    - [Generate Splash Screen Images with Dev Mode](#generate-splash-screen-images-with-dev-mode)
    - [Generate Splash Screen Images with Library](#generate-splash-screen-images-with-library)
    - [Generate Splash Screen Images with Library and Dev Mode](#generate-splash-screen-images-with-library-and-dev-mode)
  - [Generate Library](#generate-library)
  - [Generating Documentation](#generating-documentation)

## Prerequisites
- Python 3.x
- Virtualenv
- PIL (Pillow)
- Sphinx (for generating documentation)
- PyInstaller (for generating executables)

## Setup

1. **Clone the repository:**
    ```bash
    git clone https://github.com/AppAnySite/AppAnySite.git
    cd AppAnySite/Utils/tools/
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv IconSplashLib
    cd IconSplashLib
    source bin/activate # For MacOSX/Linux
    source Scripts/activate # For Windows 
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Generating Android Icons

#### Generate All Android Icons
```bash
./generate_assets.sh -i IMAGE_PATH --platform android
```

#### Generate Android Icons by Category
```bash
./generate_assets.sh -i IMAGE_PATH --platform android --folder ICON_FOLDER
```

#### Generate Android Icons by Type and Category
```bash
./generate_assets.sh -i IMAGE_PATH --platform android --folder ICON_FOLDER --icon-type ICON_TYPE
```

### Generate Android Icons in Dev Mode

#### Generate All Android Icons
```bash
./generate_assets.sh -i IMAGE_PATH --platform android --dev
```

#### Generate Android Icons by Category
```bash
./generate_assets.sh -i IMAGE_PATH --platform android --folder ICON_FOLDER --dev
```

#### Generate Android Icons by Type and Category
```bash
./generate_assets.sh -i IMAGE_PATH --platform android --folder ICON_FOLDER --icon-type ICON_TYPE --dev
```

### Generate Android Icons with Library

#### Generate All Android Icons with Library
```bash
./generate_assets.sh -i IMAGE_PATH --platform android -l
```

#### Generate Android Icons by Category with Library
```bash
./generate_assets.sh -i IMAGE_PATH --platform android --folder ICON_FOLDER -l
```

#### Generate Android Icons by Type and Category with Library
```bash
./generate_assets.sh -i IMAGE_PATH --platform android --folder ICON_FOLDER --icon-type ICON_TYPE -l
```

### Generate Android Icons with Library and Dev Mode

#### Generate All Android Icons with Library and Dev Mode
```bash
./generate_assets.sh -i IMAGE_PATH --platform android -l --dev
```

#### Generate Android Icons by Category with Library and Dev Mode
```bash
./generate_assets.sh -i IMAGE_PATH --platform android --folder ICON_FOLDER -l --dev
```

#### Generate Android Icons by Type and Category with Library and Dev Mode
```bash
./generate_assets.sh -i IMAGE_PATH --platform android --folder ICON_FOLDER --icon-type ICON_TYPE -l --dev
```

### Generate Android Icons Inside a React Native Project
```bash
./generate_assets.sh -p PROJECT_PATH -i IMAGE_PATH --platform android
```

### Generating iOS Icons

#### Generate All iOS Icons
```bash
./generate_assets.sh -i IMAGE_PATH --platform ios
```

#### Generate iOS Icons by Category
```bash
./generate_assets.sh -i IMAGE_PATH --platform ios --folder ICON_TYPE
```

### Generate iOS Icons in Dev Mode

#### Generate All iOS Icons with Dev Mode
```bash
./generate_assets.sh -i IMAGE_PATH --platform ios --dev
```

#### Generate iOS Icons by Category with Dev Mode
```bash
./generate_assets.sh -i IMAGE_PATH --platform ios --folder ICON_TYPE --dev
```

### Generate iOS Icons with Library

#### Generate All iOS Icons with Library
```bash
./generate_assets.sh -i IMAGE_PATH --platform ios -l
```

#### Generate iOS Icons by Category with Library
```bash
./generate_assets.sh -i IMAGE_PATH --platform ios --folder ICON_TYPE -l
```

### Generate iOS Icons with Library and Dev Mode

#### Generate All iOS Icons with Library and Dev Mode
```bash
./generate_assets.sh -i IMAGE_PATH --platform ios -l --dev
```

#### Generate iOS Icons by Category with Library and Dev Mode
```bash
./generate_assets.sh -i IMAGE_PATH --platform ios --folder ICON_TYPE -l --dev
```

### Generate iOS Icons Inside a React Native Project
```bash
./generate_assets.sh -p PROJECT_PATH -i IMAGE_PATH --platform ios
```

### Generating Splash Screen

#### Generate Splash Screen Images
```bash
./generate_assets.sh -p PROJECT_DIR -s SPLASH_PATH_SVG
```

### Generate Splash Screen Images with Dev Mode
```bash
./generate_assets.sh -p PROJECT_DIR -s SPLASH_PATH_SVG --dev
```

### Generate Splash Screen Images with Library
```bash
./generate_assets.sh -p PROJECT_DIR -s SPLASH_PATH_SVG -l
```

### Generate Splash Screen Images with Library and Dev Mode
```bash
./generate_assets.sh -p PROJECT_DIR -s SPLASH_PATH_SVG -l --dev
```

### Generate Library
```bash
./generate_library.sh
```

### Generating Documentation
```bash
./generate_docs.sh
```
