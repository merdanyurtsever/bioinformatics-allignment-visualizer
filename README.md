# Bioinformatics Alignment Visualizer

A web-based tool for visualizing sequence alignment algorithms (Needleman-Wunsch and Smith-Waterman).

## Features

- **Global Alignment** (Needleman-Wunsch algorithm)
- **Local Alignment** (Smith-Waterman algorithm)
- Interactive web interface
- Matrix visualization with traceback path highlighting
- Alignment score calculation

## Requirements

- Python 3.x
- Flask

## Installation

### On Aurora/Fedora (using toolbox)

```bash
# Create and enter toolbox
toolbox create bioinformatics
toolbox enter bioinformatics

# Install Flask
sudo dnf install python3-flask

# Navigate to project directory
cd /var/home/merdan/Desktop/bioinformatics/bioinformatics-allignment-visualizer

# Run the application
python3 app.py
```

### On other systems

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
python3 app.py
```

## Usage

1. Start the application:
   ```bash
   python3 app.py
   ```

2. Open your web browser and navigate to:
   ```
   http://127.0.0.1:5000
   ```

3. Enter your sequences in the input fields

4. Select the alignment algorithm:
   - **Global (Needleman-Wunsch)**: Aligns entire sequences
   - **Local (Smith-Waterman)**: Finds best local alignment

5. Click **Calculate Alignment** to see results

## Project Structure

```
bioinformatics-allignment-visualizer/
├── app.py                    # Application entry point
├── requirements.txt          # Python dependencies
├── test_alignment.py         # Test script for core algorithms
├── core/                     # Core alignment algorithms
│   ├── __init__.py
│   ├── alignment_global.py  # Needleman-Wunsch implementation
│   ├── alignment_local.py   # Smith-Waterman implementation
│   └── scoring.py           # Scoring functions
├── gui/                      # Web interface
│   ├── __init__.py
│   ├── web_server.py        # Flask server
│   └── templates/
│       └── index.html       # Web UI
└── utils/                    # Utility functions
    ├── __init__.py
    └── matrix_ops.py
```

## Testing

Run the test suite to verify core algorithms:

```bash
python3 test_alignment.py
```

## Algorithms

### Global Alignment (Needleman-Wunsch)
- Aligns complete sequences from end to end
- Optimal for sequences of similar length
- Uses dynamic programming to find optimal global alignment

### Local Alignment (Smith-Waterman)
- Finds best matching subsequences
- Optimal for finding conserved regions
- Uses dynamic programming with 0 as minimum score

## Scoring

Default scoring parameters:
- Match: +1
- Mismatch: -1
- Gap: -2

These can be modified in `core/scoring.py`.

## License

This project is for educational purposes.

## Author

Created for bioinformatics sequence alignment visualization.
