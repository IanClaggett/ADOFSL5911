# Author: Ian Claggett
from datetime import datetime, timezone
from obspy import UTCDateTime, read
from obspy.clients.fdsn import Client
from Correlator import collect_templates, cross_correlate
from pathlib import Path

# Test file of the New Zealand Rocket Lab spaceport

TEMPLATE_FILE_PATH = str(Path.cwd().__str__() + "/Template_Traces")
launchTime1 = UTCDateTime("2024-11-25T03:55:00") #Mahia Peninsula New Zealand
network = "NZ"
station = "BKZ"
location = "*"
channel = "HNZ"
client = Client("IRIS")
startTime= launchTime1 - 30
endTime= launchTime1 + 270


template = client.get_waveforms(network, station, location, channel, startTime, endTime, attach_response=True)
template.remove_response(output = "VEL")
template.filter('bandpass', freqmin=0.5, freqmax=1.2)
pick = UTCDateTime("2024-11-25T03:55:00")
template.trim(pick, pick + 90)
#template.plot()
#template.write(TEMPLATE_FILE_PATH + "/25-11-2024_NZ_BKZ_OldLaunch", format = "MSEED")"


launchTime1 = UTCDateTime("2025-03-17T01:30:00") #Mahia Peninsula New Zealand "High Five" Rocket
network = "NZ"
station = "BKZ"
location = "*"
channel = "HNZ"
min_freq = 0.5
max_freq = 1.2
client = Client("IRIS")
startTime= launchTime1 - 30
endTime= launchTime1 + 270
#template = client.get_waveforms(network, station, location, channel, startTime, endTime, attach_response=True)
#template.remove_response(output = "VEL")
#template.filter('bandpass', freqmin=min_freq, freqmax=max_freq)
#template.plot()

cross_correlate(network,station,location,channel, "IRIS",startTime,endTime, template, min_freq, max_freq)

launchTime1 = UTCDateTime("2025-03-17T02:50:30") #Mahia Peninsula New Zealand 4.4 M Earthquake
network = "NZ"
station = "BKZ"
location = "*"
channel = "HNZ"
min_freq = 0.5
max_freq = 1.2
client = Client("IRIS")
startTime= launchTime1 - 30
endTime= launchTime1 + 270

cross_correlate(network,station,location,channel, "IRIS",startTime,endTime, template, min_freq, max_freq)