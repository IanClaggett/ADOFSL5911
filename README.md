# ADOFSL5911 - Automatic Detection of Foreign Space Launches

**Authors**: Ian Claggett, Luke Rako, Klay Shukla, Divyang Prajapati, John Paul Beli

## Project Abstract

ADOFSL5911 (Automatic Detection of Foreign Space Launches) is a seismic data analysis system designed to automatically detect foreign space launches by leveraging cross-correlation techniques and machine learning. It uses seismic waveform templates from known rocket launches to identify similar seismic events corresponding to new launches, helping enhance situational awareness and support national security efforts.

This project focuses on correlating seismic data collected from seismic stations (e.g., CI BUE, CI LOC, NZ BKZ) with known rocket launch templates, enabling real-time identification and validation based on seismic signatures.

## Project Structure

```
ADOFSL5911
├── Template_Traces       # Stored seismic templates from known launches
│   ├── 11-03-2025_CI_BUE_SpaceX
│   ├── 11-03-2025_CI_LOC_SpaceX
│   ├── 15-03-2025_CI_BUE_SpaceX
│   ├── 15-03-2025_CI_LOC_SpaceX
│   ├── 24-11-2024_CI_BUE_Rocket
│   ├── 24-11-2024_CI_LOC_Rocket
│   └── 25-11-2024_NZ_BKZ_OldLaunch
├── Cartopy.py              # Map visualization of seismic events
├── correlation_testing.py  # GUI for running cross-correlation tests
├── Correlator.py           # Core cross-correlation algorithms
├── main.py                 # Main script for automated detection workflow
├── NZ_BKZ.py               # Seismic analysis script for NZ BKZ station
├── RealTime.py             # Continuous real-time analysis script
├── SeismicStations.py      # Tool to manage seismic station data
├── stations.txt            # Text file with seismic station information
├── template_loader.py      # Preprocess and load seismic templates
├── test.py                 # Basic ObsPy test script
└── README.md               # Documentation
```

## Installation

Libraries being used:

- obspy
- pyreadline ipython 
- lxml sqlalchemy
- Numpy
- SciPy
- matplotlib

Install required Python libraries with:

```bash
pip install numpy scipy matplotlib lxml sqlalchemy pyreadline ipython obspy
```

OR

```bash
pip install Numpy
pip install SciPy
pip install matplotlib
pip install lxml sqlalchemy
pip install pyreadline ipython 
pip install obspy
```

For detailed Windows installation instructions, see [ObsPy Installation](<https://github.com/obspy/obspy/wiki/Installation-on-windows-using-a-pre-build-package-(pypi)>).

## Getting Started

### Step 1: Load Templates

Download and preprocess seismic waveform templates:

```bash
python template_loader.py
```

### Step 2: Run Cross-Correlation Tests

Use the GUI to run tests and visualize results:

```bash
python correlation_testing.py
```

Close each plot window after a test to move to the next.

### Step 3: Continuous Real-Time Detection

For continuous monitoring, run:

```bash
python RealTime.py
```

## Visualization

The project includes geographical visualization using Cartopy. Run:

```bash
python Cartopy.py
```

## Managing Seismic Stations

Update seismic stations using:

```bash
python SeismicStations.py
```

## Example: Test ObsPy Setup

Check ObsPy setup quickly run `test.py` file

## Project Dependencies

- **ObsPy**: Seismic data handling
- **NumPy & SciPy**: Data processing
- **Matplotlib**: Data visualization
- **Cartopy**: Geographic plotting
- **Tkinter**: GUI development

## Workflow Overview

- **Handler Script**: Coordinates data retrieval and processing.
- **Selector Script**: Queries ObsPy and collects seismic data.
- **Reader Script**: Processes seismic data and filters noise.
- **Machine Learning Model (AWS SageMaker)**: Classifies seismic data to detect launches.

## How Cross-Correlation Works

- Preprocess seismic waveforms (bandpass filtering, response removal).
- Compare waveforms to known templates.
- Identify events with high similarity.
- Display detection results visually.

## Output

The system generates detailed waveform plots, similarity scores, and identifies seismic events indicating possible launches.

---

### Troubleshooting

Make sure:

- Templates are loaded correctly in `Template_Traces`.
- `stations.txt` station IDs match ObsPy IDs.
- GUI operations and plotting are supported by your system.

---

For questions or issues, reach out to the project team.
