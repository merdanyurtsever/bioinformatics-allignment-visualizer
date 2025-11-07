#değişkenler: matrix: list[list[int]], traceback: list[tuple[int,int]]
#metotlar: draw_matrix(matrix): void, clear(): void

import dearpygui.dearpygui as dpg

# matrix view class for displaying alignment matrices in the GUI
class MatrixView:
    def __init__(self, parent_tag: str, seqA: str, seqB: str):
        # initialize matrix view components
        self.parent_tag = parent_tag
        self.seqA = seqA
        self.seqB = seqB
        self.table_tag = "matrix_table"
        
    def update_sequences(self, seqA: str, seqB: str):
        """Update the sequences for the matrix view"""
        self.seqA = seqA
        self.seqB = seqB

    def draw_matrix(self, matrix: list[list[int]], traceback: list[tuple[int,int]]) -> None:
        # draw the alignment matrix in the GUI
        self.clear()
        
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0
        
        if rows == 0 or cols == 0:
            return
        
        # Convert traceback to set for quick lookup
        traceback_set = set(traceback) if traceback else set()
        
        # Create table
        with dpg.table(header_row=True, tag=self.table_tag, parent=self.parent_tag,
                      borders_innerH=True, borders_outerH=True,
                      borders_innerV=True, borders_outerV=True,
                      row_background=True, scrollY=True, scrollX=True,
                      policy=dpg.mvTable_SizingFixedFit):
            
            # Add columns
            dpg.add_table_column(label="", width_fixed=True)  # Row header
            dpg.add_table_column(label="-", width_fixed=True)  # Gap column
            for j, char in enumerate(self.seqB):
                dpg.add_table_column(label=char, width_fixed=True)
            
            # Add gap row
            with dpg.table_row():
                dpg.add_text("-")
                for j in range(cols):
                    cell_value = matrix[0][j]
                    is_traceback = (0, j) in traceback_set
                    
                    if is_traceback:
                        dpg.add_text(f"{cell_value}", color=(255, 255, 100))
                    else:
                        dpg.add_text(f"{cell_value}")
            
            # Add sequence rows
            for i in range(1, rows):
                with dpg.table_row():
                    # Row header with sequence character
                    if i - 1 < len(self.seqA):
                        dpg.add_text(self.seqA[i-1])
                    else:
                        dpg.add_text("")
                    
                    # Matrix values
                    for j in range(cols):
                        cell_value = matrix[i][j]
                        is_traceback = (i, j) in traceback_set
                        
                        if is_traceback:
                            dpg.add_text(f"{cell_value}", color=(255, 255, 100))
                        else:
                            dpg.add_text(f"{cell_value}")

    def clear(self) -> None:
        # clear the matrix view
        if dpg.does_item_exist(self.table_tag):
            dpg.delete_item(self.table_tag)