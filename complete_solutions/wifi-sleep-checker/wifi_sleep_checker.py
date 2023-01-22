import datetime
import time
import subprocess

def get_airport_status():
    command = "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I".split()
    cmd = subprocess.run(
        command, stdout=subprocess.PIPE
    )
    output = cmd.stdout.decode()
    
    return output
  

#def get_wifi_name():
    

def get_wifi_status():
    airport_status = get_airport_status()
    key_index = airport_status.find("SSID")
    if key_index == -1:
        return "not connected"

    rows = airport_status.split("\n")
    stripped_rows = [str(row).strip() for row in rows]
    ssids = [row for row in stripped_rows if str(row).startswith("SSID:")]
    row_with_ssid = ssids[0]
    ssid_key_value = str(row_with_ssid).split(":")
    ssid_value = ssid_key_value[1].strip()

    return "connected to " + ssid_value
    
def is_time_to_sleep(date):
    #date = datetime.datetime.now()
    return date.hour >= 22 and date.minute >= 30

if __name__ == '__main__':
    while True:
        time.sleep(5)
        print(get_wifi_status())
        break