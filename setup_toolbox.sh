#!/bin/bash
# Setup script to create a toolbox and install tkinter

echo "Creating toolbox container..."
toolbox create bioinformatics -y

echo "Installing python3-tkinter in toolbox..."
toolbox run -c bioinformatics sudo dnf install -y python3-tkinter

echo ""
echo "Setup complete! To run the app:"
echo "  toolbox run -c bioinformatics python3 app.py"
echo ""
echo "Or enter the toolbox:"
echo "  toolbox enter bioinformatics"
echo "  python3 app.py"
