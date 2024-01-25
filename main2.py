import argparse
import json
import datetime
import time

import calls as C
import calculation
import helper as H

# Argparsing all day baybbeeee

# Test Function to be used later
"""
def timeSetting():

    while True:
        Start = int(input("Start Time (epoch): "))
        print(convert_epoch_to_date(Start))
        #response = input('y/n')
        if input("Is this start time correct? (y/n): ").lower() == 'y':
            break
        
    while True:
        End = int(input("End Time (epoch): "))
        print(convert_epoch_to_date(End))
        if input("Is this end time correct? (y/n): ").lower() == 'y':
            break
            
    return Start, End
    """
    
def convert_epoch_to_date(epoch_time):
    local_time = datetime.datetime.fromtimestamp(epoch_time, tz=datetime.timezone.utc).astimezone()
    # Format to m/d/y
    return local_time.strftime('%m/%d/%y %H:%M:%S')

def validate_time(value):
    if len(value) != 10:
        raise argparse.ArgumentTypeError("Epoch Time must be INT len of 10")
    return value

def parse_arguments():
    parser = argparse.ArgumentParser(description="Variables required. UNIX Start Time. UNIX end time. Device ID. Org ID This script will also require the cookies, and the x-verkada-token in the headers of the request. Make sure to set the times 5 seconds before and after the analysis period.")
    parser.add_argument('--start', '-S', required=True, type=validate_time, help='Unix start time of event')
    parser.add_argument('--end', '-E', required=True, type=validate_time, help='UNIX end time of the event')
    parser.add_argument('--deviceid', '-D', required=True, type=str, help='Device ID of the sensor')
    parser.add_argument('--orgid', '-O', required=True, type=str, help='Org ID hosting the sensor')
    parser.add_argument('--cookie', '-C', required=True, type=str, help="the cookie from the request header. Hint: POST 'https://vsensor.command.verkada.com/query'. You may need to refresh your browser with dev tools open on the Network Tab:")
    parser.add_argument('--token', '-T', required=True, type=str, help="***MUST USE '' AROUND THE COOKIE***\nPlease locate the x-verkada-token. It's located in the headers just like the Cookie")
    return parser.parse_args()

args = parse_arguments()
Start = args.start
End = args.end
DeviceId = args.deviceid
OrgId = args.orgid
Cookie = args.cookie
xverkadatoken = args.token    

#startTime = convert_epoch_to_date(int(Start))
#endTime = convert_epoch_to_date(int(End))
#print(f"Start: {startTime}\nEnd: {endTime}")

#data = C.Sensor_Readings(Cookie, xverkadatoken, Start, End, DeviceId, OrgId)
#json_data = json.loads(data)
"""
json_data = [
{"_time": 1705515976, "motion": 0, "noflux": True, "pm_2_5": 0.10127705335617065, "tvoc": 490, "vape_index": 0, "ethanol": 10},
{"_time": 1705515977, "motion": 0, "noflux": True, "pm_2_5": 0.63454534535534534, "tvoc": 400, "vape_index": 0, "ethanol": 10},
{"_time": 1705515978, "motion": 0, "noflux": True, "pm_2_5": 1, "tvoc": 400, "vape_index": 0, "ethanol": 10},
{"_time": 1705515979, "motion": 0, "noflux": True, "pm_2_5": 7, "tvoc": 400, "vape_index": 0, "ethanol": 100},
{"_time": 1705515980, "motion": 0, "noflux": True, "pm_2_5": 0.10127705335617065, "tvoc": 400, "vape_index": 0, "ethanol": 100},
{"_time": 1705515981, "motion": 0, "noflux": True, "pm_2_5": 0.10127705335617065, "tvoc": 400, "vape_index": 0, "ethanol": 100},
{"_time": 1705515982, "motion": 0, "noflux": True, "pm_2_5": 0.10127705335617065, "tvoc": 400, "vape_index": 0, "ethanol": 100},
{"_time": 1705515983, "motion": 0, "noflux": True, "pm_2_5": 0.10127705335617065, "tvoc": 400, "vape_index": 0, "ethanol": 100},
{"_time": 1705515984, "motion": 0, "noflux": True, "pm_2_5": 16, "tvoc": 400, "vape_index": 0, "ethanol": 100},
{"_time": 1705515985, "motion": 0, "noflux": True, "pm_2_5": 0.10127705335617065, "tvoc": 400, "vape_index": 0, "ethanol": 100},
{"_time": 1705515986, "motion": 0, "noflux": True, "pm_2_5": 0.10127705335617065, "tvoc": 400, "vape_index": 0, "ethanol": 100},
{"_time": 1705515987, "motion": 0, "noflux": True, "pm_2_5": 0.10127705335617065, "tvoc": 400, "vape_index": 0, "ethanol": 100},
{"_time": 1705515988, "motion": 0, "noflux": True, "pm_2_5": 0.10127705335617065, "tvoc": 400, "vape_index": 0, "ethanol": 100},
{"_time": 1705515989, "motion": 0, "noflux": True, "pm_2_5": 30, "tvoc": 400, "vape_index": 0, "ethanol": 100},
{"_time": 1705515990, "motion": 0, "noflux": True, "pm_2_5": 0.10127705335617065, "tvoc": 400, "vape_index": 0, "ethanol": 100},
{"_time": 1705515991, "motion": 0, "noflux": True, "pm_2_5": 0.10127705335617065, "tvoc": 400, "vape_index": 0, "ethanol": 100},
{"_time": 1705515992, "motion": 0, "noflux": True, "pm_2_5": 0.10127705335617065, "tvoc": 400, "vape_index": 0, "ethanol": 100},
]
"""
# Defining functions for menu options

def option1(json_data):
    print("Low Sensitivity Selected")
    H.Low_Sensitivity(json_data)

def option2(json_data):
    print("Medium Sensitivity Selected")
    H.Medium_Sensitivity(json_data)
    
def option3(json_data):
    print("High Sensitivity Selected")
    H.High_Sensitivity(json_data)

def option4(json_data):
    print("Configure custom settings")
    H.Custom_Senstivity(json_data)

def option5(json_data):
    """Adding a method so we can adjust the time of the sensor"""
    #timeSetting()
    print("Test")


    
menu = {
    '1': option1,
    '2': option2,
    '3': option3,
    '4': option4,
    '5': option5,
    'q': exit
}

def main():
    args = parse_arguments()
    Start = args.start
    End = args.end
    DeviceId = args.deviceid
    OrgId = args.orgid
    Cookie = args.cookie
    xverkadatoken = args.token    
    data = C.Sensor_Readings(Cookie, xverkadatoken, Start, End, DeviceId, OrgId)
    json_data = json.loads(data)
    print("\n\n")
    while True:
        if input(f"Is Start: {Start}\nEnd: {End} correct? \n(y/n): ").lower() in ['y', '']:
            print("Displaying Menu:\n")
            
        else:
            Start = input("Start: ")
            End = input("End: ")
            data = C.Sensor_Readings(Cookie, xverkadatoken, Start, End, DeviceId, OrgId)
            json_data = json.loads(data)
        
        # Display menu options to the user
        print("Menu:")
        print("1. Low Sensitivity")
        print("2. Medium Sensitivity")
        print("3. High Sensitivity")
        print("4. Custom Sensitivity")
        print("5. Test DateTime")
        print("q. Quit")

        # Get user input
        choice = input("Enter your choice: ")

        # Check if the choice is in the menu dictionary
        if choice in menu:
            # Call the corresponding function based on the user's choice
            menu[choice](json_data)
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == '__main__':
    main()