#Author: Ian Claggett
from datetime import datetime, timezone
from obspy import UTCDateTime, read
from obspy.clients.fdsn import Client
from Correlator import collect_templates, cross_correlate

time = UTCDateTime(datetime.now(timezone.utc))
print(time)

while True:
    if(time.second % 10 == 0):
        print("Read now")
        template_paths = ["Template_Traces/24-11-2024_CI_LOC_Rocket", "Template_Traces/15-03-2025_CI_LOC_SpaceX", "Template_Traces/11-03-2025_CI_LOC_SpaceX"]
        CI_LOC_Templates = collect_templates(template_paths)
        network = "CI"
        station = "LOC"
        location = "*"
        channel = "BHZ,BLZ"
        min_freq = 0.5
        max_freq = 1.2
        startTime = time - 120
        endTime = time

        cross_correlate(network,station,location,channel, "SCEDC", startTime,endTime, CI_LOC_Templates, min_freq, max_freq)
    
    time = UTCDateTime(datetime.now(timezone.utc))