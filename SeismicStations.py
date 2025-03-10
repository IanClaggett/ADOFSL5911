from obspy import UTCDateTime
from obspy import read_inventory
from obspy.clients.fdsn import Client

client = Client("IRIS")

#US located at lat 37.09024 (center) and -95.712891 long (center)
minlatitude = 24.40
maxlatitude = 50.0
minlongitude = -125.0
maxlongitude = -67.0

#US
stations = client.get_stations(minlatitude=minlatitude, maxlatitude=maxlatitude,
                            minlongitude=minlongitude, maxlongitude=maxlongitude,
                            channel="BHZ")
for network in stations:
    for station in network:
        #print(f"Network: {network.code}, Station: {station.code}, Location: {station.latitude}, {station.longitude}, Location Name: {station.site.name}")
        print(f"Location Name: {station.site.name}")
