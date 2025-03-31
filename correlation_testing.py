# Authors: Ian Claggett, Luke Rako

import sys
import tkinter as tk
from tkinter import ttk
from obspy import UTCDateTime, read
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Correlator import collect_templates, cross_correlate

class TextRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, text):
        self.text_widget.insert(tk.END, text)
        self.text_widget.see(tk.END)

    def flush(self):
        pass

class SeismicGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Seismic Test Viewer")

        self.test_cases = self.build_test_cases()
        self.test_index = 0
        self.canvas = None

        self.status_label = ttk.Label(root, text="Click 'Next' to begin testing...")
        self.status_label.pack(pady=10)

        self.output_box = tk.Text(root, height=8, wrap="word")
        self.output_box.pack(fill="both", expand=True, padx=10, pady=10)

        sys.stdout = TextRedirector(self.output_box)

        self.plot_frame = ttk.Frame(root)
        self.plot_frame.pack(fill="both", expand=True)

        self.next_button = ttk.Button(root, text="Next", command=self.run_next_test)
        self.next_button.pack(pady=10)

    def build_test_cases(self):
        test_cases = []

        ci_loc_templates = collect_templates([
            "Template_Traces/24-11-2024_CI_LOC_Rocket",
            "Template_Traces/15-03-2025_CI_LOC_SpaceX",
            "Template_Traces/11-03-2025_CI_LOC_SpaceX",
        ])

        ci_bue_templates = collect_templates([
            "Template_Traces/24-11-2024_CI_BUE_Rocket",
            "Template_Traces/15-03-2025_CI_BUE_SpaceX",
            "Template_Traces/11-03-2025_CI_BUE_SpaceX",
        ])

        launch_events = [
            ("2025-02-14T00:17:04", 30, 240),
            ("2025-02-10T21:13:00", 30, 240),
            ("2019-07-06T03:19:53", 30, 240),
            ("2024-11-24T05:25:00", 60, 210),
            ("2025-03-11T03:10:00", 60, 210),
            ("2025-03-15T06:50:00", 60, 240),
            ("2025-01-03T16:30:00", 60, 240),
        ]

        for time_str, pre, post in launch_events:
            launch_time = UTCDateTime(time_str)
            start_time = launch_time - pre
            end_time = launch_time + post

            test_cases.append(("CI", "LOC", ci_loc_templates, start_time, end_time))
            test_cases.append(("CI", "BUE", ci_bue_templates, start_time, end_time))

        return test_cases

    def run_next_test(self):
        self.output_box.delete("1.0", tk.END)

        if self.test_index >= len(self.test_cases):
            self.status_label.config(text="All tests completed.")
            return

        # Clear previous plot
        for widget in self.plot_frame.winfo_children():
            widget.destroy()
        plt.close('all')

        # Get current test
        network, station, templates, start, end = self.test_cases[self.test_index]
        test_label = f"Test {self.test_index + 1}/{len(self.test_cases)} for {station}"
        self.status_label.config(text=f" Running {test_label}...")

        # Run correlation
        fig, detections = cross_correlate(
            network=network,
            station=station,
            location="*",
            channel="BHZ,BLZ",
            client_code="SCEDC",
            startTime=start,
            endTime=end,
            templates=templates,
            min_freq=0.25,
            max_freq=1.5
        )

        # Display plot in GUI
        if fig:
            self.canvas = FigureCanvasTkAgg(fig, master=self.plot_frame)
            self.canvas.get_tk_widget().pack(fill="both", expand=True)
            self.canvas.draw()
            self.status_label.config(
                text=f"{test_label} completed — Detections: {len(detections)}"
            )
        else:
            self.status_label.config(text=f"⚠️ {test_label} returned no figure.")

        self.test_index += 1
        if self.test_index >= len(self.test_cases):
            self.root.after(2000, self.root.destroy)


if __name__ == "__main__":
    root = tk.Tk()
    app = SeismicGUI(root)
    root.mainloop()
