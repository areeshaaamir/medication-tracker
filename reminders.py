import time
from datetime import datetime
from win10toast import ToastNotifier
from backend import getAllReminders 

toaster = ToastNotifier()

def check_reminders():
    while True:
        now = datetime.now().strftime("%I:%M%p").lstrip('0')  
        reminders = getAllReminders() 

        for medName, remind_time, username in reminders:
            if remind_time.strip().upper() == now.upper():
                toaster.show_toast(
                    f"Reminder for {username}",
                    f"It's time to take your medicine: {medName}",
                    duration=10
                )

        time.sleep(60)

check_reminders()
