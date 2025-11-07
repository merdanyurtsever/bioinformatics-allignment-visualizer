"""Entry point for the application.

This module starts the Tkinter-based GUI.
"""

def run():
    from gui.main_window import MainWindow
    window = MainWindow()
    window.start()


if __name__ == "__main__":
    run()