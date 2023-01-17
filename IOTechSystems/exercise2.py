import json
import base64
import time

# Load data from data.json
with open("exercises/exercise-02/data/data.json", "r") as json_file:
    data = json.load(json_file)

# Get current time
current_time = int(time.time())

# Initialize variables for storing total value and uuids
valueTotal = 0
uuids = []

# Iterate through devices array
for device in data["Devices"]:
    # Get timestamp and check if it's before current time
    if int(device["timestamp"]) < current_time:
        continue

    # Get value and add it to total
    val = base64.b64decode(device["value"]).decode()
    valueTotal += int(val)

    # Get uuid from info and add it to uuids list
    uuid = device["Info"].split(":")[-1]
    uuid = str(uuid).split(",")[0]
    uuids.append(uuid)

# Create dictionary with total and uuids; according to the output-schema
output = {"ValueTotal": valueTotal, "UUIDS": uuids}

# Write output to file
with open("exercise2_output.json", "w") as json_file:
    json.dump(output, json_file)
