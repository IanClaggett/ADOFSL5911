#Author: Ian Claggett
from obspy import UTCDateTime, read
from obspy.clients.fdsn import Client
from obspy.signal.cross_correlation import correlation_detector

def collect_templates(filepaths):
    templates = []
    for path in filepaths:
        template = read(path)
        templates.append(template)
    return templates

def cross_correlate(network,station,location,channel, client_code, startTime,endTime, templates, min_freq, max_freq):
    client = Client(client_code) #For California
    try:
        stream = client.get_waveforms(network, station, location, channel, startTime, endTime, attach_response=True)
    except:
        print(f"Error requesting data: {network}, {station}. Time: {startTime}")
    else:
        stream.remove_response(output = "VEL")
        stream.filter('bandpass', freqmin=min_freq, freqmax=max_freq)
        height = 0.35  # similarity threshold
        distance = 10  # distance between detections in seconds
        detections, sims = correlation_detector(stream, templates, height, distance, plot=stream)
        if(len(detections)!=0):
            for detection in detections:
                print("Detection similarity: "+ str(detection['similarity']*200) + "%")
        else:
            print("No launches detected at " + network)