import json

# Load the data form devices.json
with open('exercises/exercise-01/data/devices.json') as f:
    data = json.load(f)

# Iterate through devices array
for device in data['Devices']:
    # Extract the information from each device
    info_str = device['Info']

    # Get uuid from info and add it to uuids list
    uuid = info_str.split(':')[-1]
    uuid = str(uuid).split(",")[0]

    #Creating a "Uuid" field in the JSON file
    device['Uuid'] = uuid
    
    # For each device, calculate sum of the sensor payloads
    payload_total = sum(sensor['Payload'] for sensor in device['Sensors'])
    device['PayloadTotal'] = payload_total

    #Removing the "Sensors" key to make it according to the output schema
    del device['Sensors']

# Order the reformatted data by Name (ascending)
data['Devices'] = sorted(data['Devices'], key=lambda x: x['Name'])

# Write the reformatted data to a new file in JSON format
with open('exercise1_output.json', 'w') as f:
    json.dump(data, f)