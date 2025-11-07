#metotlar: create_empty(rows: int, cols: int) -> list[list[int]], normalize(matrix) -> list[list[float]], pad_sequences(seqA, seqB) -> tuple[str, str]

def create_empty(rows: int, cols: int) -> list[list[int]]:
    """Creates an empty matrix with given number of rows and columns."""
    return [[0 for _ in range(cols)] for _ in range(rows)]

def normalize(matrix: list[list[int]]) -> list[list[float]]:
    """Normalizes the matrix values to a range of 0 to 1."""
    max_val = max(max(row) for row in matrix) if matrix else 1
    return [[val / max_val for val in row] for row in matrix]

def pad_sequences(seqA: str, seqB: str) -> tuple[str, str]:
    """Pads the sequences to the same length with gaps."""
    max_len = max(len(seqA), len(seqB))
    return seqA.ljust(max_len, '-'), seqB.ljust(max_len, '-')