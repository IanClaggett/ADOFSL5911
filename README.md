# ADOFSL5911 - Automatic Detection of Foreign Space Launches

**Authors**: Ian Claggett, Luke Rako, Klay Shukla, Divyang Prajapati, John Paul Beli

## Project Abstract

ADOFSL5911 is a seismic data analysis system designed to automatically detect foreign space launches by comparing live seismic data to known rocket launch templates using cross-correlation techniques and machine learning. The system collects waveform data from seismic stations like CI BUE, CI LOC, and NZ BKZ to match against historical templates and identify potential launch events.

---

# For Users

This application allows you to analyze seismic data and determine whether it matches patterns associated with known rocket launches. It’s built to be used by people with light technical familiarity—no programming experience is required.

### Using the Application

#### Step 1: Launch the App

Open a terminal or command prompt and run:

```bash
python main.py
```

This opens the main interface.

#### Step 2: Start Seismic Analysis

Click the **"Analyze Seismic Data"** button to begin. This will start checking the data against known launch signatures.

#### Step 3: View Results in Test Viewer

After analysis starts, a new window opens:

- Click **"Next"** to go through each test case.
- Close the plot window after viewing to proceed.
- When all test cases are completed, the application will close automatically.

#### What You'll See

- A scrollable log showing what the system is doing.
- Graphs showing vibration patterns and whether a match was found.

#### Example Screenshots

Step 1: Analyze Seismic Data

![Analyze](image.png)

Step 2: Begin Testing

![Testing](image-1.png)

---

# For Developers

## Project Structure

```
ADOFSL5911
├── Template_Traces       # Stored seismic templates from known launches
├── Cartopy.py            # Map visualization of seismic events
├── correlation_testing.py# GUI for running cross-correlation tests
├── Correlator.py         # Core cross-correlation logic
├── main.py               # Main script for automated launch detection
├── RealTime.py           # Continuous real-time detection
├── SeismicStations.py    # Manage seismic station data
├── stations.txt          # Text file with seismic station info
├── template_loader.py    # Generates and saves new waveform templates
├── test.py               # Basic ObsPy installation test
└── README.md             # Project documentation
```

## Dependencies

- ObsPy
- NumPy, SciPy
- Matplotlib
- Cartopy
- Tkinter

## Installation

Install required libraries:

```bash
pip install numpy scipy matplotlib lxml sqlalchemy pyreadline ipython obspy
```

For Windows help, see [ObsPy Installation Guide](<https://github.com/obspy/obspy/wiki/Installation-on-windows-using-a-pre-build-package-(pypi)>).

## Running the Code

Run the main script:

```bash
python main.py
```

## Getting Started

### 1. Load Templates

```bash
python template_loader.py
```

### 2. Run Cross-Correlation Tests

```bash
python correlation_testing.py
```

### 3. Real-Time Monitoring

```bash
python RealTime.py
```

### 4. Visualization

```bash
python Cartopy.py
```

### 5. Station Management

```bash
python SeismicStations.py
```

## Adding and Testing a New Launch Template

### 1. Identify Launch Details

- Launch time: `2025-04-01T10:30:00`
- Network: `CI`, Station: `LOC`, Channels: `BHZ,BLZ`

### 2. Generate the Template

Add this to `template_loader.py`:

```python
#New Launch - Example
try:
    launchTime = UTCDateTime("2025-04-01T10:30:00")
    startTime = launchTime - 60
    endTime = launchTime + 210
    template = client.get_waveforms("CI", "LOC", "*", "BHZ,BLZ", startTime, endTime, attach_response=True)
    template.remove_response(output="VEL")
    template.filter('bandpass', freqmin=0.25, freqmax=1.5)
    pick = UTCDateTime("2025-04-01T10:30:30")
    template.trim(pick, pick + 90)
    template.write(TEMPLATE_FILE_PATH + "/01-04-2025_CI_LOC_NewRocket", format="MSEED")
    print("Saved template: 01-04-2025_CI_LOC_NewRocket")
except Exception as e:
    print(f"Failed to generate 01-04-2025_CI_LOC_NewRocket: {e}")
```

Run:

```bash
python template_loader.py
```

### 3. Add to the Test Suite

In `correlation_testing.py`:

```python
ci_loc_templates = collect_templates([
    "Template_Traces/24-11-2024_CI_LOC_Rocket",
    "Template_Traces/15-03-2025_CI_LOC_SpaceX",
    "Template_Traces/11-03-2025_CI_LOC_SpaceX",
    "Template_Traces/01-04-2025_CI_LOC_NewRocket"
])
```

```python
launch_events = [
    ...,
    ("2025-04-01T10:30:00", 60, 240)
]
```

### 4. Run Tests

```bash
python correlation_testing.py
```

## Logger

We use Python’s `logging` module to track events and errors across scripts. Logs are saved to:

```
logs/system.log
```

- Avoid pushing this file to Git. Add to your `.gitignore`:

```gitignore
logs/system.log
```

Each developer should maintain their own log file locally.

## How Cross-Correlation Works

- Load known launch templates.
- Download waveform data from remote stations.
- Preprocess waveforms (e.g., filtering, trimming).
- Match data to templates using correlation.
- Display results and detections in GUI.

## Output

- Waveform plots with detections
- Match similarity scores (e.g., "Detection similarity: 72.3%")
- Logs available inside the GUI and `logs/system.log`

## Example: Test ObsPy Setup

```python
from obspy import read
st = read()
st.filter(type='highpass', freq=3.0)
st = st.select(component='Z')
st.plot()
```

## Troubleshooting

- Templates must exist in `Template_Traces`
- `stations.txt` should have correct station codes
- Matplotlib and GUI must be supported by your OS

---

For help, contact the project maintainers.
