Medication Tracker App - README
===============================

This is a desktop GUI-based Medication Tracker application built using:
- Python 3.10+
- Tkinter (GUI)
- SQLite3 (Database)
- Plyer (for desktop notifications)

----------------------------------------
🗂 Project Structure & File Description
----------------------------------------

1. login_gui.py           -> Main GUI logic (login, signup, dashboard, forms)
2. backend.py             -> Database and logic for users, medicines, reminders
3. reminder_notifier.py   -> Background task that checks and sends medicine reminders
4. med_tracker.db         -> SQLite database (auto-created if not found)
5. README.txt             -> This file

----------------------------------------
💻 System Requirements
----------------------------------------

✔ Python 3.10+ (check using: python --version)
✔ pip installed (Python package manager)
✔ Required libraries installed:
   Run this command in terminal:
     pip install plyer

----------------------------------------
🚀 How to Run the Project
----------------------------------------

1. Place all the project files in a single folder.

2. Open a terminal in that folder and run:
     python login_gui.py

   This will open the main GUI.

3. Open a second terminal in the same folder and run:
     python reminder_notifier.py

   This will enable reminder notifications in the background.

----------------------------------------
🛠 Common Issues & Fixes
----------------------------------------

- "No module named plyer":
  Make sure you installed it using: pip install plyer

- GUI doesn't open:
  Ensure Tkinter is available (comes by default with most Python installations).

- Notifications don't show up:
  Make sure system notifications are enabled in Windows settings.

----------------------------------------
🧠 Developer Notes & Problems Faced
----------------------------------------

- Designed complete user auth and medicine management logic.
- Integrated SQLite3 to persist medicine and reminder data.
- Faced challenges with sending reminders when GUI is closed – solved it using a separate Python process.
- Tried converting to .exe but reverted to Python version to keep it simple and editable.

----------------------------------------
💬 Final Notes
----------------------------------------

This is a working medication tracker with full CRUD operations, reminders, and a multi-screen GUI. If you need help running it, follow the instructions above.

-- Thank you! :)