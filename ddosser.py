# This is a fake DDOS software
from colorama import Fore, Back, Style
import os
import PySimpleGUI as sg
from pyfiglet import Figlet
import os
import random
import time

f = Figlet(font='slant')
counter = int(0)

print(f.renderText("DDOS Manager"))

def create_dashes():
    terminal_width = os.get_terminal_size().columns
    dashes = '-' * terminal_width
    print(Fore.RED + dashes + Style.RESET_ALL)

create_dashes()

print(Fore.RED + "Format of Database File: (ip/server url/ngrok url):(ssh port)/(username)@(password)" + Style.RESET_ALL)
print("")
file = sg.popup_get_file('Pick a file!')

import os.path
# Check if the file exists
if os.path.isfile(file) and file.endswith(".txt"):
    print(Fore.RED + "✅ File valid, importing list of ips" + Style.RESET_ALL)
    
    try:
        with open(file, 'r') as file:
            # Read all lines from the file and split each line by space to get the first part (IP)
            ips = [line.split()[0] for line in file.readlines()]
            
            # Calculate the number of elements
            num_elements = len(ips)

        # Print the IPs and the number of elements
        print(Fore.RED + "✅ IPs Imported:" + Style.RESET_ALL)

    except FileNotFoundError:
        print(Fore.RED + "❌ File not found!" + Style.RESET_ALL)

else:
    print(Fore.RED + "❌ Invalid file or file format. Please select a valid .txt file." + Style.RESET_ALL)

num_elements = len(ips)
randarraynumb = random.randint(1, num_elements-1)
print(ips)
mswait = random.randint(1, 3)

time.sleep(mswait)
randip = ips[randarraynumb]

# Start attack

nonworkingips = []
print("")
print(Fore.RED + "⚒️ Checking IPs" + Style.RESET_ALL)
print("")
print(Fore.RED + "-------" + Style.RESET_ALL)
print("")
print(Fore.RED + "Some IP's are not working. They have been removed" + Style.RESET_ALL) 
for i in range(3):
    num_elements = len(ips)-1
    ips.pop(randarraynumb)
    print("1 IP Removed")
    time.sleep(1)
print("")
print(f"Finalized IP List:")
print(ips)
num_elements = len(ips)
print(f"{num_elements} IPs left.")

# Ask IP
toPing = input(Fore.RED + "What IP/URL would you like to ping? " + Style.RESET_ALL)
toPingPort = input(Fore.RED + "What port would you like to ping (80 = HTTP, 21 = FTP, 25 = SMTP, 22 = SSH, 443 = HTTPS, 53 = DNS, 3306 = MySQL DB, 5432 = PostgresSQL DB), 8080 = HTTP Proxy? " + Style.RESET_ALL)

# Simulate pinging

for i in range(random.randint(1, 784)):
    chanceOfFailed = random.randint(1, 50)
    if chanceOfFailed == 29:
        print(Fore.RED + f"❌ {ips[random.randint(1, num_elements-1)]} was not able to ping {toPing}:{toPingPort}. Retrying with different IP" + Style.RESET_ALL)
    else:
        print(Fore.GREEN + ips[random.randint(1, num_elements-1)] + f" has pinged {toPing}:{toPingPort}" + Style.RESET_ALL)
        time.sleep(random.randint(300, 684) / 1000)
