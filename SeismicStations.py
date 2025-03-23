from obspy import UTCDateTime
from obspy import read_inventory
from obspy.clients.fdsn import Client

client = Client("IRIS")

#US located at lat 37.09024 (center) and -95.712891 long (center)
minlatitude = 24.40
maxlatitude = 50.0
minlongitude = -125.0
maxlongitude = -67.0

# US
stations = client.get_stations(minlatitude=minlatitude, maxlatitude=maxlatitude,
                            minlongitude=minlongitude, maxlongitude=maxlongitude,
                            channel="BHZ")

def get_stations(filename):
    stations = {}
    with open(filename, "r") as file:
        return {line.strip().split(": ")[0]: line.strip().split(": ")[1] for line in file}
    

# Print stations
def print_stations(station_dict):
    print("Currently registered stations and their locations: ")
    for station, location in station_dict.items():
        print(f"{station} - {location}")
        
def add_stations(curr_stations, station_dict):
    user_input = input("Write station name (ENTER to exit): ")
    while user_input != "":
        if user_input == "":
            break
        if user_input in station_dict:
            print("Station already exists.\n")
        elif user_input not in curr_stations:
            print("Station does not exist.")
        elif user_input in curr_stations and user_input not in station_dict:
            station_dict[user_input] = curr_stations.get(user_input)
            print(f"Station {user_input} added.\n")
        user_input = input("Write station name (ENTER to exit): ")

# Delete stations        
def delete_stations(station_dict):
    words_per_line = 0
    list = []
    
    # 5 stations per line for readability
    for station in station_dict.keys():
        words_per_line += 1
        list.append(station)
        if words_per_line % 5 == 0:
            words_per_line = 0
            print(', '.join(list))
            list.clear()
            
    # Specify which station to delete
    user_input = "1"
    while user_input != "":
        user_input = input("Which stations would you want to delete (ENTER to exit): ")
        if user_input != "":
            if user_input in station_dict:
                del station_dict[user_input]
                print("Successfully deleted station.\n")
            else:
                print("Invalid station name, try again.")
                
                
# Save into txt file
def save_stations(station_dict):
    with open("stations.txt", "w") as file:
        for stations, location in station_dict.items():
            # for station in network:
            #     #print(f"Network: {network.code}, Station: {station.code}, Location: {station.latitude}, {station.longitude}, Location Name: {station.site.name}")
            try:
                file.write(f"{stations}: {location}\n")
            except:
                print("Error writing to the file")
                break
    print("Saved changes into stations.txt\n")
    
        

# # Call the function and store the result in station_dict
# with open("stations.txt", "w") as file:
#     for network in stations:
#         for station in network:
#             #print(f"Network: {network.code}, Station: {station.code}, Location: {station.latitude}, {station.longitude}, Location Name: {station.site.name}")
#             file.write(f"{station.code}: {station.site.name}\n")

current_iris_stations = {}
for network in stations:
    for station in network:
        current_iris_stations[station.code] = station.site.name
        
station_dict = get_stations("stations.txt")

user_input = "-1"
print("What do you wish to do?")
while user_input != "7":
    user_input = input("1. View current station list\n2. Add a station\n3. Delete a station\n4. Save changes\n7. Exit\n\n(Type a number): ")

    if user_input == "1":
        print_stations(station_dict)
    elif user_input == "2":
        add_stations(current_iris_stations, station_dict)
    elif user_input == "3":
        delete_stations(station_dict)
    elif user_input == "4":
        save_stations(station_dict)
    elif user_input != "7":
        print("\nWhat do you wish to do next?")
    




