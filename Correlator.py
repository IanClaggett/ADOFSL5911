#Author: Ian Claggett
from obspy import UTCDateTime
from obspy.clients.fdsn import Client
from obspy.signal.cross_correlation import correlation_detector

class Correllator:
    def collect_templates():
        #Last year launch
        client = Client("SCEDC") #For California
        launchTime1 = UTCDateTime("2024-11-24T05:25:00") #Vanderberg CA
        startTime1 = launchTime1 - 60
        endTime1 = launchTime1 + 210
        network = "CI"
        station = "LOC"
        template = client.get_waveforms(network, station, "*", "BHZ,BLZ,MHZ,MLZ", startTime1, endTime1, attach_response=True)
        template.remove_response(output = "VEL")
        template.filter('bandpass', freqmin=0.25, freqmax=1.5)
        pick = UTCDateTime("2024-11-24T05:25:30")
        template.trim(pick, pick + 90)
        return template
    
    def cross_correlate(network,station,location,channel,startTime,endTime):
        templates = Correllator.collect_templates()
        client = Client("SCEDC") #For California
        stream = client.get_waveforms(network, station, location, channel, startTime, endTime, attach_response=True)
        stream.remove_response(output = "VEL")
        stream.filter('bandpass', freqmin=0.25, freqmax=1.5)
        height = 0.35  # similarity threshold
        distance = 10  # distance between detections in seconds
        detections, sims = correlation_detector(stream, templates, height, distance, plot=stream)
        if(len(detections)!=0):
            for detection in detections:
                print("Detection similarity: "+ str(detection['similarity']*200) + "%")
        else:
            print("No launches detected at " + network)


#4.5 MAGNITUDE EARTHQUAKE
launchTime2 = UTCDateTime("2025-02-14T00:17:04") #Vanderberg CA
startTime2 = launchTime2 - 30
endTime2 = launchTime2 + 240
network = "CI"
station = "LOC"
location = "*"
channel = "BHZ,BLZ,MHZ,MLZ"

Correllator.cross_correlate(network,station,location,channel,startTime2,endTime2)

#Recent Launch
launchtime3 = UTCDateTime("2025-02-10T21:13:00")
startTime3 = launchtime3 - 30
endTime3 = launchtime3 + 240
network = "CI"
station = "LOC"
location = "*"
channel = "BHZ,BLZ,MHZ,MLZ"

Correllator.cross_correlate(network,station,location,channel,startTime3,endTime3)

#7.1 MAGNITUDE EARTHQUAKE
launchtime4 = UTCDateTime("2019-07-06T03:19:53")
startTime4 = launchtime4 - 30
endTime4 = launchtime4 + 240
network = "CI"
station = "LOC"
location = "*"
channel = "BHZ,BLZ,MHZ,MLZ"

Correllator.cross_correlate(network,station,location,channel,startTime4,endTime4)