"""Flask web server for alignment visualizer GUI."""
from flask import Flask, render_template, request, jsonify
from core.alignment_global import AlignmentGlobal
from core.alignment_local import AlignmentLocal

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    
    seqA = data.get('seqA', '').strip().upper()
    seqB = data.get('seqB', '').strip().upper()
    algorithm = data.get('algorithm', 'global')
    
    if not seqA or not seqB:
        return jsonify({'error': 'Please enter both sequences'}), 400
    
    try:
        if algorithm == 'global':
            aligner = AlignmentGlobal(seqA, seqB)
        else:
            aligner = AlignmentLocal(seqA, seqB)
        
        result = aligner.compute()
        matrix = result['matrix']
        traceback = result['traceback']
        
        if algorithm == 'global':
            score = matrix[-1][-1]
        else:
            score = max(max(row) for row in matrix) if matrix else 0
        
        return jsonify({
            'score': score,
            'matrix': matrix,
            'traceback': traceback,
            'seqA': seqA,
            'seqB': seqB
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


def start(host='127.0.0.1', port=5000, debug=False):
    """Start the Flask web server."""
    print(f"\n{'='*60}")
    print("Bioinformatics Alignment Visualizer - Web Interface")
    print(f"{'='*60}")
    print(f"\nOpen your browser and navigate to:")
    print(f"  http://{host}:{port}")
    print(f"\nPress Ctrl+C to stop the server")
    print(f"{'='*60}\n")
    
    app.run(host=host, port=port, debug=debug)
