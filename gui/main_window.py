# Simple Tkinter-based GUI for the alignment visualizer
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkfont

from core.alignment_global import AlignmentGlobal
from core.alignment_local import AlignmentLocal
from gui.matrix_view import MatrixView


class MainWindow:
    def __init__(self):
        self.root = None
        self.seq_a_var = None
        self.seq_b_var = None
        self.algorithm_var = None
        self.matrix_view = None

    def build(self):
        self.root = tk.Tk()
        self.root.title("Bioinformatics Alignment Visualizer")
        self.root.geometry("1000x700")
        
        # Create StringVars after root window exists
        self.seq_a_var = tk.StringVar(value="ACGTACGT")
        self.seq_b_var = tk.StringVar(value="ACGACG")
        self.algorithm_var = tk.StringVar(value="global")

        title = tk.Label(self.root, text="Sequence Alignment Tool", fg="#64C8FF", font=("Helvetica", 14, "bold"))
        title.pack(pady=8)

        frame = tk.Frame(self.root)
        frame.pack(fill=tk.X, padx=12)

        left = tk.Frame(frame)
        left.pack(side=tk.LEFT, fill=tk.Y)

        tk.Label(left, text="Sequence A:").pack(anchor=tk.W)
        tk.Entry(left, textvariable=self.seq_a_var, width=50).pack(pady=4)

        tk.Label(left, text="Sequence B:").pack(anchor=tk.W)
        tk.Entry(left, textvariable=self.seq_b_var, width=50).pack(pady=4)

        tk.Label(left, text="Algorithm:").pack(anchor=tk.W, pady=(8,0))
        algo_frame = tk.Frame(left)
        algo_frame.pack(anchor=tk.W)
        tk.Radiobutton(algo_frame, text="Global (Needleman-Wunsch)", variable=self.algorithm_var, value="global").pack(side=tk.LEFT)
        tk.Radiobutton(algo_frame, text="Local (Smith-Waterman)", variable=self.algorithm_var, value="local").pack(side=tk.LEFT)

        tk.Button(left, text="Calculate Alignment", command=self.on_calculate_click, width=20).pack(pady=10)

        self.score_label = tk.Label(left, text="", fg="#64FF64", font=("Helvetica", 12))
        self.score_label.pack(pady=4)

        # Matrix view on the right
        right = tk.Frame(frame)
        right.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(12,0))

        self.matrix_view = MatrixView(right)

    def on_calculate_click(self):
        seqA = self.seq_a_var.get().strip().upper()
        seqB = self.seq_b_var.get().strip().upper()
        if not seqA or not seqB:
            self.score_label.config(text="Error: please enter both sequences", fg="#FF6464")
            return

        try:
            if self.algorithm_var.get() == "global":
                aligner = AlignmentGlobal(seqA, seqB)
            else:
                aligner = AlignmentLocal(seqA, seqB)

            result = aligner.compute()
            matrix = result["matrix"]
            traceback = result["traceback"]

            if self.algorithm_var.get() == "global":
                score = matrix[-1][-1]
            else:
                score = max(max(row) for row in matrix)

            self.score_label.config(text=f"Alignment Score: {score}", fg="#64FF64")
            self.matrix_view.draw_matrix(matrix, traceback, seqA, seqB)
        except Exception as e:
            self.score_label.config(text=f"Error: {e}", fg="#FF6464")

    def start(self):
        self.build()
        self.root.mainloop()

