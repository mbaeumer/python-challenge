import subprocess

def is_connected():
    command = "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -I".split()
    cmd = subprocess.run(
        command, stdout=subprocess.PIPE
    )
    output = cmd.stdout.decode()
    print(cmd.stdout)
    print(output)

    return "SSID:" in output

if __name__ == '__main__':
    print(is_connected())