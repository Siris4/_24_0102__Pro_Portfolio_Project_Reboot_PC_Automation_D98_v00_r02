import subprocess
import os

# function to terminate processes by their names
def kill_processes(process_names):
    for process_name in process_names:
        try:
            subprocess.run(f'taskkill /IM {process_name} /F', shell=True, check=True)
            print(f"Terminated {process_name}")
        except subprocess.CalledProcessError as e:
            print(f"Failed to terminate {process_name}: {e}")

# function to connect to a specific WiFi network
def connect_to_wifi(ssid):
    try:
        subprocess.run(f'netsh wlan connect name="{ssid}"', shell=True, check=True)
        print(f"Connected to WiFi: {ssid}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to connect to WiFi: {ssid}, Error: {e}")

# paths to the executables of the programs you want to launch
apps_to_open = [
    r"C:\C Drive - Downloads and Installations\Capture2Text\Capture2Text\Capture2Text.exe",  # Update with the actual path
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",  # Path to Chrome
    r"C:\C Drive - Downloads and Installations\ClipAngel - Copy Clipboard\ClipAngel.exe",    # Update with the actual path
    r"C:\Users\Siris\AppData\Local\electron\Rize.exe",          # Update with the actual path
    r"C:\Users\Siris\AppData\Local\Programs\Notion\Notion.exe"  # Update with the actual path
]

# function to launch each application
def launch_applications(apps):
    for app in apps:
        try:
            subprocess.Popen(app)
            print(f"Started {app}")
        except Exception as e:
            print(f"Error starting {app}: {e}")

# First, terminate Bitdefender VPN App, Service, and ShareX
processes_to_kill = ["BitdefenderVpnApp.exe", "BitdefenderVpnService.exe", "ShareX.exe"]  # Replace with actual process names if different
kill_processes(processes_to_kill)

# Then, connect to the specific WiFi network
connect_to_wifi("Totalplay-829F")

# Finally, launch the apps
launch_applications(apps_to_open)
