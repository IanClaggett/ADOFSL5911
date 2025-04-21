import json

# Enter location names and associated data with the station into the tunings, to be used in the future as tuning packages
# meant for creating a single point of control over the system
tunings = {
    "Vandenberg_5_miles" : {
        "network" : "CI",
        "station" : "LOC",
        "location": "*",
        "channel" : "BHZ,BLZ",
        "client_code" : "SCEDC",
        "min_freq" : 0.25,
        "max_freq" : 1.5
    },
    "Vandenberg_40_miles" : {
        "network" : "CI",
        "station" : "BUE",
        "location": "*",
        "channel" : "BHZ,BLZ",
        "client_code" : "SCEDC",
        "min_freq" : 0.20,
        "max_freq" : 1.4
    },
    "New_Zealand" : {
        "network" : "NZ",
        "station" : "BKZ",
        "location" : "*",
        "channel" : "HNZ",
        "client_code" : "IRIS",
        "min_freq" : 0.5,
        "max_freq" : 1.2
    }
}

output = json.dumps(tunings, indent=4)

#Outputs the generated JSON tree back to user to check for correctness
try:
    with open("tunings.json", "w") as text_file:
        text_file.write(output)
except Exception as e:
    print(e)

