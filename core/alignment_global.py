#değişkenler: scoring: Scoring

#metotlar: compute(seqA: str, seqB: str) -> dict returns { "matrix": [...], "traceback": [...]},
#build_matrix(): list[list[int]], traceback_path(): list[tuple[int,int]]

from core.scoring import score, gap

class AlignmentGlobal:
    def __init__(self, seqA: str, seqB: str):
        self.seqA = seqA
        self.seqB = seqB
        self.matrix = []
        self.traceback = []

    def build_matrix(self) -> list[list[int]]:
        rows = len(self.seqA) + 1
        cols = len(self.seqB) + 1
        self.matrix = [[0 for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            self.matrix[i][0] = i * gap()
        for j in range(cols):
            self.matrix[0][j] = j * gap()

        for i in range(1, rows):
            for j in range(1, cols):
                match = self.matrix[i-1][j-1] + score(self.seqA[i-1], self.seqB[j-1])
                delete = self.matrix[i-1][j] + gap()
                insert = self.matrix[i][j-1] + gap()
                self.matrix[i][j] = max(match, delete, insert)

        return self.matrix

    def traceback_path(self) -> list[tuple[int,int]]:
        i, j = len(self.seqA), len(self.seqB)
        path = []

        while i > 0 or j > 0:
            current_score = self.matrix[i][j]
            if i > 0 and j > 0 and current_score == self.matrix[i-1][j-1] + score(self.seqA[i-1], self.seqB[j-1]):
                path.append((i-1, j-1))
                i -= 1
                j -= 1
            elif i > 0 and current_score == self.matrix[i-1][j] + gap():
                path.append((i-1, j))
                i -= 1
            else:
                path.append((i, j-1))
                j -= 1

        path.reverse()
        self.traceback = path
        return path

    def compute(self) -> dict:
        self.build_matrix()
        self.traceback_path()
        return {
            "matrix": self.matrix,
            "traceback": self.traceback
        }