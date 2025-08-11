Simple Keylogger: Create a basic Keylogger program that records and logs keystrokes. Focus on logging the keys pressed and saving them to a file. Note: Ethical considerations and permissions are crucial for projects involving keyloggers.
pynput captures keyboard events.

Every key press is appended to key_log.txt.

ESC stops the program.

Installation:
bash
pip install pynput
Usage:
bash
python keylogger.py
It will create/update key_log.csv in the same folder.

CSV Output – Creates a file like:

Timestamp,Key

Special Keys – Stored in square brackets for clarity.

Stop with ESC – Cleanly ends the program.
