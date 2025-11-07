#değişkenler: seqA_input:str, seqB_input:str, algorithm:str, matrixView:MatrixView



#metotlar: render():void, on_calculate_click():void, get_user_input(): tuple[str, str, str]

# main window class for the alignment visualizer GUI
class MainWindow:
    def __init__(self):
        # initialize GUI components
        pass

    def render(self) -> None:
        # render the main window
        pass

    def on_calculate_click(self) -> None:
        # handle calculate button click
        seqA, seqB, algorithm = self.get_user_input()
        # perform alignment calculation
        pass

    def get_user_input(self) -> tuple[str, str, str]:
        # retrieve user input from GUI fields
        seqA_input = ""  # get from input field
        seqB_input = ""  # get from input field
        algorithm = ""   # get from selection field
        return seqA_input, seqB_input, algorithm

