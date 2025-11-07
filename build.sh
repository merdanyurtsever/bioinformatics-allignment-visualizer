#!/bin/bash
# Build script for creating standalone executable

echo "Building Bioinformatics Alignment Visualizer..."
echo "=============================================="
echo ""

# Check if we're in toolbox
if [ -f /run/.containerenv ]; then
    echo "Running inside toolbox - good!"
else
    echo "Not in toolbox. Run this script with:"
    echo "  toolbox run -c bioinformatics ./build.sh"
    exit 1
fi

# Install dependencies
echo "Installing build dependencies..."
pip3 install --user pyinstaller flask

# Clean previous builds
echo "Cleaning previous builds..."
rm -rf build dist

# Build with PyInstaller
echo "Building executable with PyInstaller..."
pyinstaller --clean bioinformatics-visualizer.spec

# Check if build succeeded
if [ -f "dist/bioinformatics-visualizer" ]; then
    echo ""
    echo "=============================================="
    echo "✓ Build successful!"
    echo "=============================================="
    echo ""
    echo "Executable location:"
    echo "  dist/bioinformatics-visualizer"
    echo ""
    echo "To run the application:"
    echo "  ./dist/bioinformatics-visualizer"
    echo ""
    echo "Then open your browser to:"
    echo "  http://127.0.0.1:5000"
    echo ""
else
    echo ""
    echo "✗ Build failed. Check the output above for errors."
    exit 1
fi
