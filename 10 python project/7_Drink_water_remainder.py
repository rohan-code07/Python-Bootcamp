import time
from plyer import notification
from colorama import Fore, init
init(autoreset=True)

print('='*40)
print(Fore.BLUE + "         DRINK WATER REMAINDER")
print('='*40)

minutes = int(input("Reminder every how many minutes? "))

try:
    while True:
        notification.notify(title = "Please drink some water", message = "You need to drink some wate")
        time.sleep(minutes*60)

except KeyboardInterrupt:
    print("Water Remainder Stopped!")

