#Author: Ian Claggett
from obspy import UTCDateTime, read
from obspy.clients.fdsn import Client
from Correlator import collect_templates, cross_correlate


#-------------------------(CI LOC Station)-------------------------
template_paths = ["Template_Traces/24-11-2024_CI_LOC_Rocket", "Template_Traces/15-03-2025_CI_LOC_SpaceX", "Template_Traces/11-03-2025_CI_LOC_SpaceX"]
CI_LOC_Templates = collect_templates(template_paths)
network = "CI"
station = "LOC"
location = "*"
channel = "BHZ,BLZ"
min_freq = 0.25
max_freq = 1.5

#4.5 MAGNITUDE EARTHQUAKE
launchTime2 = UTCDateTime("2025-02-14T00:17:04") #Vanderberg CA
startTime2 = launchTime2 - 30
endTime2 = launchTime2 + 240

print("Testing: 4.5 Magnitude Earthquake")
cross_correlate(network,station,location,channel, "SCEDC", startTime2,endTime2, CI_LOC_Templates, min_freq, max_freq)

#Recent Launch
print("Testing: Rocket Launch")
launchtime3 = UTCDateTime("2025-02-10T21:13:00")
startTime3 = launchtime3 - 30
endTime3 = launchtime3 + 240

cross_correlate(network,station,location,channel, "SCEDC",startTime3,endTime3, CI_LOC_Templates, min_freq, max_freq)

print("Testing: 7.1 Magnitude Earthquake")
#7.1 MAGNITUDE EARTHQUAKE
launchtime4 = UTCDateTime("2019-07-06T03:19:53")
startTime4 = launchtime4 - 30
endTime4 = launchtime4 + 240

cross_correlate(network,station,location,channel, "SCEDC",startTime4,endTime4, CI_LOC_Templates, min_freq, max_freq)

#Template (template)
print("Testing: Rocket Launch Template")
launchTime1 = UTCDateTime("2024-11-24T05:25:00") #Vanderberg CA
startTime1 = launchTime1 - 60
endTime1 = launchTime1 + 210

cross_correlate(network,station,location,channel, "SCEDC",startTime1,endTime1, CI_LOC_Templates, min_freq, max_freq)

#Random spaceX launch (template)

print("Testing: Rocket Launch Template")
launchTime1 = UTCDateTime("2025-03-11T03:10:00") #Vanderberg CA
startTime1 = launchTime1 - 60
endTime1 = launchTime1 + 210

cross_correlate(network,station,location,channel, "SCEDC",startTime1,endTime1, CI_LOC_Templates, min_freq, max_freq)

#Spacex (template)
print("Testing: Rocket Launch Template")
client = Client("SCEDC") #For California
launchTime1 = UTCDateTime("2025-03-15T06:50:00") #Vanderberg CA
startTime1 = launchTime1 - 60
endTime1 = launchTime1 + 240

cross_correlate(network,station,location,channel, "SCEDC",startTime1,endTime1, CI_LOC_Templates, min_freq, max_freq)

#Spacex Thuraya 4-NGS (PASS)
print("Testing: Rocket Launch")
client = Client("SCEDC") #For California
launchTime1 = UTCDateTime("2025-01-03T16:30:00") #Vanderberg CA
startTime1 = launchTime1 - 60
endTime1 = launchTime1 + 240

cross_correlate(network,station,location,channel, "SCEDC",startTime1,endTime1, CI_LOC_Templates, min_freq, max_freq)

#-------------------------(CI BUE Station)-------------------------
template_paths = ["Template_Traces/24-11-2024_CI_BUE_Rocket", "Template_Traces/15-03-2025_CI_BUE_SpaceX", "Template_Traces/11-03-2025_CI_BUE_SpaceX"]
CI_BUE_Templates = collect_templates(template_paths)
network = "CI"
station = "BUE"
location = "*"
channel = "BHZ,BLZ"
min_freq = 0.3
max_freq = 1.5

#4.5 MAGNITUDE EARTHQUAKE 
print("Testing: 4.5 Magnitude Earthquake")
launchTime2 = UTCDateTime("2025-02-14T00:17:04") #Vanderberg CA
startTime2 = launchTime2 - 30
endTime2 = launchTime2 + 240


cross_correlate(network,station,location,channel, "SCEDC",startTime2,endTime2, CI_BUE_Templates, min_freq, max_freq)

#Recent Launch
print("Testing: Rocket Launch Template")
launchtime3 = UTCDateTime("2025-02-10T21:13:00")
startTime3 = launchtime3 - 30
endTime3 = launchtime3 + 240

cross_correlate(network,station,location,channel, "SCEDC",startTime3,endTime3, CI_BUE_Templates, min_freq, max_freq)

#7.1 MAGNITUDE EARTHQUAKE
print("Testing: 7.1 Magnitude Earthquake")
launchtime4 = UTCDateTime("2019-07-06T03:19:53")
startTime4 = launchtime4 - 30
endTime4 = launchtime4 + 240

cross_correlate(network,station,location,channel, "SCEDC",startTime4,endTime4, CI_BUE_Templates, min_freq, max_freq)

#Template (template)
print("Testing: Rocket Launch Template")
launchTime1 = UTCDateTime("2024-11-24T05:25:00") #Vanderberg CA
startTime1 = launchTime1 - 60
endTime1 = launchTime1 + 210

cross_correlate(network,station,location,channel, "SCEDC",startTime1,endTime1, CI_BUE_Templates, min_freq, max_freq)

#Random spaceX launch (template)
print("Testing: Rocket Launch Template")
launchTime1 = UTCDateTime("2025-03-11T03:10:00") #Vanderberg CA
startTime1 = launchTime1 - 60
endTime1 = launchTime1 + 210

cross_correlate(network,station,location,channel, "SCEDC",startTime1,endTime1, CI_BUE_Templates, min_freq, max_freq)

#Spacex (template)
print("Testing: Rocket Launch Template")
client = Client("SCEDC") #For California
launchTime1 = UTCDateTime("2025-03-15T06:50:00") #Vanderberg CA
startTime1 = launchTime1 - 60
endTime1 = launchTime1 + 240

cross_correlate(network,station,location,channel, "SCEDC",startTime1,endTime1, CI_BUE_Templates, min_freq, max_freq)

#Spacex Thuraya 4-NGS 
print("Testing: Rocket Launch")
client = Client("SCEDC") #For California
launchTime1 = UTCDateTime("2025-01-03T16:30:00") #Vanderberg CA
startTime1 = launchTime1 - 60
endTime1 = launchTime1 + 240

cross_correlate(network,station,location,channel, "SCEDC",startTime1,endTime1, CI_BUE_Templates, min_freq, max_freq)