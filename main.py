# Author: Luke Rako

import tkinter as tk
from tkinter import ttk
from obspy import UTCDateTime
import subprocess
import sys

class SeismicGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Seismic Launch Detection")

        welcome = (
            "Welcome to the Automatic Detection of Foreign Space Launches Capstone Project!\n\n"
            "Press the 'Analyze Seismic Data' button to use cross-correlation to detect "
            "if a space launch occurred at an input location."
        )
        self.welcome_label = ttk.Label(root, text=welcome, wraplength=400, justify="center", font=("Helvetica", 11))
        self.welcome_label.grid(row=0, column=0, padx=20, pady=15)

        self.datetime_label = ttk.Label(root, text="", font=("Helvetica", 10))
        self.datetime_label.grid(row=1, column=0, padx=10, pady=5)
        self.update_datetime()

        self.analyze_button = ttk.Button(root, text="Analyze Seismic Data", command=self.run_analysis)
        self.analyze_button.grid(row=2, column=0, padx=10, pady=20)

    def update_datetime(self):
        now = UTCDateTime().strftime("%Y-%m-%d %H:%M:%S (UTC)")
        self.datetime_label.config(text=f"Current Date and Time: {now}")
        self.root.after(1000, self.update_datetime)

    def run_analysis(self):
        subprocess.Popen([sys.executable, "correlation_testing.py"])
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = SeismicGUI(root)
    root.mainloop()
