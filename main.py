import argparse
import json

import calls as C
import helper as H

# Argparsing all day baybbeeee


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

def secretOption():
    print("Just RMA their building...")

    
menu = {
    '1': option1,
    '2': option2,
    '3': option3,
    '4': option4,
    '6062': secretOption,
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
        if input(f"Is Start: \033[1m{Start}\033[0m | End: \033[1m{End}\033[0m correct? \n(y/n): ").lower() in ['y', '']:
            print("Displaying Menu:\n")
        else:
            try:
                Start = validate_time(input("Start: "))
            except:
                print("Time must be given in epoch, and must be 10 characters..")
                continue
            try:
                End = validate_time(input("End: "))
            except:
                print("Time must be given in epoch, and must be 10 characters..")
                continue
            data = C.Sensor_Readings(Cookie, xverkadatoken, Start, End, DeviceId, OrgId)
            json_data = json.loads(data)
        
        # Display menu options to the user
        print("Menu:")
        print("1. Low Sensitivity")
        print("2. Medium Sensitivity")
        print("3. High Sensitivity")
        print("4. Custom Sensitivity")
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