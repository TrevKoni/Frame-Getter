import os
import tkinter as tk
from tkinter import filedialog

import cv2


def extract_frames(video_path, output_folder, num_frames):
    cap = cv2.VideoCapture(video_path)

    # Get video properties
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_interval = total_frames // num_frames

    # Create output folder if not exists
    os.makedirs(output_folder, exist_ok=True)

    # Extract frames
    for i in range(0, total_frames, frame_interval):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)
        ret, frame = cap.read()

        if ret:
            frame_filename = os.path.join(output_folder, f"frame_{i}.jpg")
            cv2.imwrite(frame_filename, frame)

    cap.release()


def select_video():
    video_path = filedialog.askopenfilename(
        title="Select Video File", filetypes=[("Video files", "*.mp4;*avi;*.mkv")]
    )
    video_entry.delete(0, tk.END)
    video_entry.insert(0, video_path)


def select_output_folder():
    output_folder = filedialog.askdirectory(title="Select Output Folder")
    output_entry.delete(0, tk.END)
    output_entry.insert(0, output_folder)


def start_extraction():
    video_path = video_entry.get()
    output_folder = output_entry.get()
    num_frames = int(num_frames_entry.get())

    extract_frames(video_path, output_folder, num_frames)
    status_label.config(text="Frames extracted successfully!")


# Create main window
window = tk.Tk()
window.title("Video Frame Extractor")

# Create and place widgets
video_label = tk.Label(window, text="Select Video:")
video_label.pack()

video_entry = tk.Entry(window, width=40)
video_entry.pack()

video_button = tk.Button(window, text="Browse", command=select_video)
video_button.pack()

output_label = tk.Label(window, text="Select Output Folder:")
output_label.pack()

output_entry = tk.Entry(window, width=40)
output_entry.pack()

output_button = tk.Button(window, text="Browse", command=select_output_folder)
output_button.pack()

num_frames_label = tk.Label(window, text="Number of Frames:")
num_frames_label.pack()

num_frames_entry = tk.Entry(window, width=10)
num_frames_entry.pack()

start_button = tk.Button(window, text="Start Extraction", command=start_extraction)
start_button.pack()

status_label = tk.Label(window, text="")
status_label.pack()

# Start the GUI ecent loop
window.mainloop()

