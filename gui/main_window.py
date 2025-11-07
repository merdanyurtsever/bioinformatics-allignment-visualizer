#değişkenler: seqA_input:str, seqB_input:str, algorithm:str, matrixView:MatrixView

import dearpygui.dearpygui as dpg
from core.alignment_global import AlignmentGlobal
from core.alignment_local import AlignmentLocal
from gui.matrix_view import MatrixView

#metotlar: render():void, on_calculate_click():void, get_user_input(): tuple[str, str, str]

# main window class for the alignment visualizer GUI
class MainWindow:
    def __init__(self):
        # initialize GUI components
        self.seqA_input = ""
        self.seqB_input = ""
        self.algorithm = "global"
        self.matrix_view = None
        self.result_data = None

    def render(self) -> None:
        # render the main window
        with dpg.window(label="Bioinformatics Alignment Visualizer", tag="main_window", 
                       width=1200, height=800, no_close=True):
            
            # Input section
            with dpg.group(horizontal=False):
                dpg.add_text("Sequence Alignment Tool", color=(100, 200, 255))
                dpg.add_separator()
                
                dpg.add_text("Sequence A:")
                dpg.add_input_text(tag="seq_a_input", default_value="ACGTACGT", 
                                  width=400, multiline=False)
                
                dpg.add_text("Sequence B:")
                dpg.add_input_text(tag="seq_b_input", default_value="ACGACG", 
                                  width=400, multiline=False)
                
                dpg.add_separator()
                
                # Algorithm selection
                dpg.add_text("Algorithm:")
                dpg.add_radio_button(["Global (Needleman-Wunsch)", "Local (Smith-Waterman)"], 
                                    tag="algorithm_radio", default_value="Global (Needleman-Wunsch)",
                                    horizontal=True)
                
                dpg.add_separator()
                
                # Calculate button
                dpg.add_button(label="Calculate Alignment", callback=self.on_calculate_click,
                             width=200, height=40)
                
                dpg.add_separator()
            
            # Results section
            with dpg.group(horizontal=False):
                dpg.add_text("Results:", tag="results_header", show=False, color=(100, 255, 100))
                dpg.add_text("", tag="alignment_score", show=False)
                dpg.add_separator()
                
            # Matrix view section
            with dpg.child_window(tag="matrix_container", height=-1, border=True):
                dpg.add_text("Matrix visualization will appear here after calculation")

    def on_calculate_click(self) -> None:
        # handle calculate button click
        seqA, seqB, algorithm = self.get_user_input()
        
        if not seqA or not seqB:
            dpg.set_value("alignment_score", "Error: Please enter both sequences")
            dpg.configure_item("alignment_score", show=True, color=(255, 100, 100))
            return
        
        # perform alignment calculation
        try:
            if algorithm == "global":
                aligner = AlignmentGlobal(seqA, seqB)
            else:
                aligner = AlignmentLocal(seqA, seqB)
            
            result = aligner.compute()
            self.result_data = result
            
            # Get alignment score
            matrix = result["matrix"]
            if algorithm == "global":
                score = matrix[-1][-1]
            else:
                score = max(max(row) for row in matrix)
            
            # Update UI
            dpg.configure_item("results_header", show=True)
            dpg.set_value("alignment_score", f"Alignment Score: {score}")
            dpg.configure_item("alignment_score", show=True, color=(100, 255, 100))
            
            # Draw matrix
            if self.matrix_view is None:
                self.matrix_view = MatrixView("matrix_container", seqA, seqB)
            
            self.matrix_view.update_sequences(seqA, seqB)
            self.matrix_view.draw_matrix(result["matrix"], result["traceback"])
            
        except Exception as e:
            dpg.set_value("alignment_score", f"Error: {str(e)}")
            dpg.configure_item("alignment_score", show=True, color=(255, 100, 100))

    def get_user_input(self) -> tuple[str, str, str]:
        # retrieve user input from GUI fields
        seqA_input = dpg.get_value("seq_a_input").strip().upper()
        seqB_input = dpg.get_value("seq_b_input").strip().upper()
        
        algorithm_choice = dpg.get_value("algorithm_radio")
        algorithm = "global" if "Global" in algorithm_choice else "local"
        
        return seqA_input, seqB_input, algorithm
    
    def start(self) -> None:
        """Initialize and start the DearPyGUI application"""
        dpg.create_context()
        
        # Setup viewport
        dpg.create_viewport(title="Bioinformatics Alignment Visualizer", 
                           width=1200, height=800)
        
        # Render the main window
        self.render()
        
        # Setup and show viewport
        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.set_primary_window("main_window", True)
        
        # Start render loop
        dpg.start_dearpygui()
        
        # Cleanup
        dpg.destroy_context()

