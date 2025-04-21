# Authors: Ian Claggett, Klay Shukla

from obspy import UTCDateTime
from obspy.clients.fdsn import Client
import os
from pathlib import Path
from logger import logger

# Check if the template folder has been created, and if not create one
TEMPLATE_FILE_PATH = str(Path.cwd().__str__() + "/Template_Traces")

if not os.path.exists(TEMPLATE_FILE_PATH):
    os.makedirs(TEMPLATE_FILE_PATH)
    logger.info("Created Template_Traces directory.")

# -------------------------(CI LOC Station)-------------------------

# Last year launch 
try:
    client = Client("SCEDC")  # For California
    logger.info("Connected to SCEDC client.")
    
    launchTime1 = UTCDateTime("2024-11-24T05:25:00")  # Vanderberg CA
    startTime1 = launchTime1 - 60
    endTime1 = launchTime1 + 210
    network = "CI"
    station = "LOC"
    template = client.get_waveforms(network, station, "*", "BHZ,BLZ", startTime1, endTime1, attach_response=True)
    template.remove_response(output="VEL")
    template.filter('bandpass', freqmin=0.25, freqmax=1.5)
    pick = UTCDateTime("2024-11-24T05:25:30")
    template.trim(pick, pick + 90)
    template.write(TEMPLATE_FILE_PATH + "/24-11-2024_CI_LOC_Rocket", format="MSEED")
    logger.info("Saved template: 24-11-2024_CI_LOC_Rocket")
except Exception as e:
    logger.error(f"Failed to generate 24-11-2024_CI_LOC_Rocket: {e}")

# SpaceX Launch 3/15 
try:
    launchTime1 = UTCDateTime("2025-03-15T06:42:00")
    startTime1 = launchTime1 - 60
    endTime1 = launchTime1 + 210
    template = client.get_waveforms("CI", "LOC", "*", "BHZ,BLZ", startTime1, endTime1, attach_response=True)
    template.remove_response(output="VEL")
    template.filter('bandpass', freqmin=0.25, freqmax=1.5)
    pick = UTCDateTime("2025-03-15T06:42:30")
    template.trim(pick, pick + 90)
    template.write(TEMPLATE_FILE_PATH + "/15-03-2025_CI_LOC_SpaceX", format="MSEED")
    logger.info("Saved template: 15-03-2025_CI_LOC_SpaceX")
except Exception as e:
    logger.error(f"Failed to generate 15-03-2025_CI_LOC_SpaceX: {e}")

# SpaceX Launch 3/11
try:
    launchTime1 = UTCDateTime("2025-03-11T03:09:00")
    startTime1 = launchTime1 - 60
    endTime1 = launchTime1 + 210
    template = client.get_waveforms("CI", "LOC", "*", "BHZ,BLZ", startTime1, endTime1, attach_response=True)
    template.remove_response(output="VEL")
    template.filter('bandpass', freqmin=0.25, freqmax=1.5)
    pick = UTCDateTime("2025-03-11T03:09:30")
    template.trim(pick, pick + 90)
    template.write(TEMPLATE_FILE_PATH + "/11-03-2025_CI_LOC_SpaceX", format="MSEED")
    logger.info("Saved template: 11-03-2025_CI_LOC_SpaceX")
except Exception as e:
    logger.error(f"Failed to generate 11-03-2025_CI_LOC_SpaceX: {e}")

# -------------------------(CI LOC Station)-------------------------

# -------------------------(CI BUE Station)-------------------------

# Last year launch 
try:
    launchTime1 = UTCDateTime("2024-11-24T05:25:00")  # Vanderberg CA
    startTime1 = launchTime1 - 60
    endTime1 = launchTime1 + 210
    network = "CI"
    station = "BUE"
    template = client.get_waveforms(network, station, "*", "BHZ,BLZ", startTime1, endTime1, attach_response=True)
    template.remove_response(output="VEL")
    template.filter('bandpass', freqmin=0.20, freqmax=1.4)
    pick = UTCDateTime("2024-11-24T05:25:30")
    template.trim(pick, pick + 90)
    template.write(TEMPLATE_FILE_PATH + "/24-11-2024_CI_BUE_Rocket", format="MSEED")
    logger.info("Saved template: 24-11-2024_CI_BUE_Rocket")
except Exception as e:
    logger.error(f"Failed to generate 24-11-2024_CI_BUE_Rocket: {e}")

# SpaceX Launch 3/15 
try:
    launchTime1 = UTCDateTime("2025-03-15T06:42:00")
    startTime1 = launchTime1 - 60
    endTime1 = launchTime1 + 210
    template = client.get_waveforms("CI", "BUE", "*", "BHZ,BLZ", startTime1, endTime1, attach_response=True)
    template.remove_response(output="VEL")
    template.filter('bandpass', freqmin=0.20, freqmax=1.4)
    pick = UTCDateTime("2025-03-15T06:42:30")
    template.trim(pick, pick + 90)
    template.write(TEMPLATE_FILE_PATH + "/15-03-2025_CI_BUE_SpaceX", format="MSEED")
    logger.info("Saved template: 15-03-2025_CI_BUE_SpaceX")
except Exception as e:
    logger.error(f"Failed to generate 15-03-2025_CI_BUE_SpaceX: {e}")

# SpaceX Launch 3/11
try:
    launchTime1 = UTCDateTime("2025-03-11T03:09:00")
    startTime1 = launchTime1 - 60
    endTime1 = launchTime1 + 210
    template = client.get_waveforms("CI", "BUE", "*", "BHZ,BLZ", startTime1, endTime1, attach_response=True)
    template.remove_response(output="VEL")
    template.filter('bandpass', freqmin=0.20, freqmax=1.4)
    pick = UTCDateTime("2025-03-11T03:09:30")
    template.trim(pick, pick + 90)
    template.write(TEMPLATE_FILE_PATH + "/11-03-2025_CI_BUE_SpaceX", format="MSEED")
    logger.info("Saved template: 11-03-2025_CI_BUE_SpaceX")
except Exception as e:
    logger.error(f"Failed to generate 11-03-2025_CI_BUE_SpaceX: {e}")

# -------------------------(CI BUE Station)-------------------------
