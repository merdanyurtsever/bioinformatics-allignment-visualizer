"""Entry point for the application.

This module starts the Flask-based web GUI.
"""

def run():
    from gui.web_server import start
    start()


if __name__ == "__main__":
    run()
