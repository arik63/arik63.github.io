import time
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText
from pynput.keyboard import Key, Listener, Controller

# Define replay_count as a Tkinter IntVar
replay_count = tk.IntVar(value=1)

# Function to record key presses
def on_key_press(key):
    recorded_keys.append(key)
    log_monitor.configure(state="normal")
    log_monitor.insert("end", f"Key Pressed: {key}\n")
    log_monitor.see("end")
    log_monitor.configure(state="disabled")

# Function to clear recorded keys and log monitor
def clear_recorded_keys():
    global recorded_keys
    recorded_keys = []
    log_monitor.configure(state="normal")
    log_monitor.delete("1.0", "end")
    log_monitor.configure(state="disabled")

# Function to replay recorded keys with a countdown
def replay_keys():
    global replay_count, recorded_keys
    replay_count_val = replay_count.get()
    for count in range(3, 0, -1):
        log_monitor.configure(state="normal")
        log_monitor.insert("end", f"Starting replay in {count}...\n")
        log_monitor.see("end")
        log_monitor.configure(state="disabled")
        time.sleep(1)
    for _ in range(replay_count_val):
        for key in recorded_keys:
            if key == Key.enter:
                log_monitor.configure(state="normal")
                log_monitor.insert("end", "Replaying Enter key\n")
                log_monitor.see("end")
                log_monitor.configure(state="disabled")
                keyboard_controller.press(Key.enter)
                keyboard_controller.release(Key.enter)
            elif key == Key.space:
                log_monitor.configure(state="normal")
                log_monitor.insert("end", "Replaying Space key\n")
                log_monitor.see("end")
                log_monitor.configure(state="disabled")
                keyboard_controller.press(Key.space)
                keyboard_controller.release(Key.space)
            elif key != Key.space:
                log_monitor.configure(state="normal")
                log_monitor.insert("end", f"Replaying key: {key}\n")
                log_monitor.see("end")
                log_monitor.configure(state="disabled")
                keyboard_controller.press(key)
                keyboard_controller.release(key)
            time.sleep(replay_interval.get())

# Function to start recording
def start_recording():
    global listener, replay_count
    clear_recorded_keys()
    listener = Listener(on_press=on_key_press)
    listener.start()
    replay_count_val = replay_count.get()
    start_button["state"] = "disabled"
    replay_count_entry["state"] = "disabled"
    replay_button["state"] = "disabled"
    stop_button["state"] = "normal"
    cancel_button["state"] = "normal"

# Function to stop recording
def stop_recording():
    global listener
    if listener:
        listener.stop()
    start_button["state"] = "normal"
    replay_count_entry["state"] = "normal"
    replay_button["state"] = "normal"
    stop_button["state"] = "disabled"
    cancel_button["state"] = "normal"

# Function to cancel recording
def cancel_recording():
    global listener, recorded_keys
    if listener:
        listener.stop()
    recorded_keys = []
    clear_recorded_keys()
    start_button["state"] = "normal"
    replay_count_entry["state"] = "normal"
    replay_button["state"] = "normal"
    stop_button["state"] = "disabled"
    cancel_button["state"] = "disabled"

# Create the main application window
app = tk.Tk()
app.title("Keyboard Recorder and Replayer")
app.configure(bg="#333333")

# Create and configure the GUI elements
start_button = ttk.Button(app, text="Start Recording", command=start_recording)
replay_count_label = ttk.Label(app, text="Replay Count:")
replay_count_entry = ttk.Entry(app, textvariable=replay_count)
replay_button = ttk.Button(app, text="Replay Recorded Keys", command=replay_keys)
stop_button = ttk.Button(app, text="Stop Recording", command=stop_recording)
cancel_button = ttk.Button(app, text="Cancel Recording", command=cancel_recording)

# Create a log monitor using a scrolled text widget
log_monitor = ScrolledText(app, wrap=tk.WORD, width=40, height=15)
log_monitor.configure(state="disabled", bg="#1E1E1E", fg="white")

# Create a keyboard controller
keyboard_controller = Controller()

# Default replay interval in seconds
replay_interval = tk.DoubleVar(value=0.2)

# Place the GUI elements in the window
start_button.pack(pady=10)
replay_count_label.pack(pady=10)
replay_count_entry.pack(pady=10)
replay_button.pack(pady=10)
stop_button.pack(pady=10)
cancel_button.pack(pady=10)
log_monitor.pack(pady=10)

# Start the GUI application
app.mainloop()
