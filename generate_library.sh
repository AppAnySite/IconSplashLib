#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Remove any previous builds
echo "Cleaning up previous builds..."
rm -rf build dist IconSplashLib.spec

# Generate the initial spec file
echo "Generating initial spec file..."
pyinstaller --name=IconSplashLib main.py

# Modify the spec file to include additional files and directories
echo "Modifying spec file to include additional files and directories..."
cat <<EOL > IconSplashLib.spec
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['main.py'],
    pathex=['.'],
    binaries=[],
    datas=[
        ('plugins', 'plugins'),
        ('utils', 'utils'),
        ('config', 'config'),
        ('requirements.txt', '.'),
        ('docs', 'docs')
    ],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='IconSplashLib',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='IconSplashLib',
)
EOL

# Build the executable
echo "Building the executable..."
pyinstaller -y IconSplashLib.spec

echo "Build completed. The executable is in the 'dist/IconSplashLib' directory."
