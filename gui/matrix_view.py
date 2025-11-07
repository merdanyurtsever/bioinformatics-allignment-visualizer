# Matrix view for Tkinter GUI
import tkinter as tk
from tkinter import ttk


class MatrixView:
    def __init__(self, parent):
        self.parent = parent
        self.text = tk.Text(parent, wrap=tk.NONE, font=("Courier", 10))
        self.v_scroll = tk.Scrollbar(parent, orient=tk.VERTICAL, command=self.text.yview)
        self.h_scroll = tk.Scrollbar(parent, orient=tk.HORIZONTAL, command=self.text.xview)
        self.text.configure(yscrollcommand=self.v_scroll.set, xscrollcommand=self.h_scroll.set)

        self.v_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.h_scroll.pack(side=tk.BOTTOM, fill=tk.X)
        self.text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def draw_matrix(self, matrix, traceback, seqA, seqB):
        self.clear()
        if not matrix:
            return

        rows = len(matrix)
        cols = len(matrix[0])

        traceback_set = set(traceback) if traceback else set()

        col_width = 6
        def cell(val, mark=False):
            s = str(val)
            if mark:
                s = f"[{s}]"
            return s.rjust(col_width)

        # Header row
        header = "".ljust(col_width) + cell("-")
        for ch in seqB:
            header += cell(ch)
        self.text.insert(tk.END, header + "\n")

        # Rows
        for i in range(rows):
            if i == 0:
                row_label = "-"
            else:
                row_label = seqA[i-1] if i-1 < len(seqA) else ""
            line = row_label.rjust(col_width)
            for j in range(cols):
                is_mark = (i, j) in traceback_set
                line += cell(matrix[i][j], mark=is_mark)
            self.text.insert(tk.END, line + "\n")

    def clear(self):
        self.text.delete("1.0", tk.END)