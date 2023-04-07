import datetime
import time
import subprocess
from wifi_status import WifiStatus
import re
import sys


def handle_cli_args(argv):
    if len(argv) != 2:
        print("Not enough arguments")
        return False

    return bool(re.search(r"^(0[1-9]|1[0-2]):([0-5][0-9])$", argv[1]))

def get_airport_status():
    command = "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I".split()
    cmd = subprocess.run(
        command, stdout=subprocess.PIPE
    )
    output = cmd.stdout.decode()
    
    return output
  

def get_wifi_status():
    airport_status = get_airport_status()
    key_index = airport_status.find("SSID")
    if key_index == -1:
        return WifiStatus(False,"")

    rows = airport_status.split("\n")
    stripped_rows = [str(row).strip() for row in rows]
    ssids = [row for row in stripped_rows if str(row).startswith("SSID:")]
    row_with_ssid = ssids[0]
    ssid_key_value = str(row_with_ssid).split(":")
    ssid_value = ssid_key_value[1].strip()

    return WifiStatus(True, ssid_value)

def get_sleep_datetime(now, sleep_timestamp):
    hour = str(sleep_timestamp).split(":")[0]
    minute = str(sleep_timestamp).split(":")[1]
    sleep_datetime_string = str(now.year) + "-" + str(now.month) + "-" + str(now.day) + " " + str(hour) + ":" + str(minute)
    sleep_datetime = datetime.datetime.strptime(sleep_datetime_string, "%Y-%m-%d %H:%M")

    if now > sleep_datetime:
        sleep_datetime = sleep_datetime + datetime.timedelta(days=1)

    return sleep_datetime
    
def is_time_to_sleep(date, sleep_time):
    return date > sleep_time

def disconnect_from_wifi():
    command = "networksetup -setnetworkserviceenabled Wi-Fi off".split()
    cmd = subprocess.run(
        command, stdout=subprocess.PIPE
    )

if __name__ == '__main__':
    if not handle_cli_args(sys.argv):
        exit(1)
    sleep_time = sys.argv[1]
    while True:
        time.sleep(5)
        wifi_status = get_wifi_status()
        print(wifi_status.is_connected)
        print(wifi_status.ssid)
        if is_time_to_sleep(datetime.datetime.now()):
            print("now it is time to go to bed!")
            disconnect_from_wifi()

        break

