import requests
import json

def Sensor_Readings(cookie, xVerkadaToken, start, end, deviceId, organizationId):
    """
    This requires access to the user organization. 
    startTime in epoc, end time in epoc.
    
    The cookie will need to be pasted in. You can find this by inspecting the
    POST: https://vsensor.command.verkada.com/query in the headers
    """
    
    url = "https://vsensor.command.verkada.com/query"
    
    payload = f'{{"deviceId":"{deviceId}","organizationId":"{organizationId}","dashboardId":"","start":{start},"end":{end},"shouldCache":false,"aggregateInterval":"1s","fields":["vape_index","tvoc","pm_2_5","motion","ethanol"],"fillPrevious":false,"isPageDefaultQuery":false}}'    
    headers = {
    'x-verkada-token': xVerkadaToken,
    'Cookie': cookie,
    'Content-Type': 'text/plain'
    }

    try:
        response = requests.post(url, headers=headers, data=payload)
        response.raise_for_status() # Raise an error for a bad response
    except requests.exceptions.RequestException as e:
        # Handle request related errors
        print(f"Request error: {e}")
        return None # Or raise an exception log
    
    try:
        response_data = response.json()
    except ValueError as e:
        print(f"JSON decoding error: {e}")

    return response.text
