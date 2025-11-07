# entrance point for the application for visualization of genome alignments matrix calculations
# the application uses dearpygui for the GUI
# the application is structured in a modular way to separate the GUI from the backend logic
# the application will be built using PyInstaller for distribution

# değişkenler: window: MainWindow

# metotlar: run()

def run():
    from gui.main_window import MainWindow
    window = MainWindow()
    window.start()

if __name__ == "__main__":
    run()