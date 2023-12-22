import cv2
import tkinter as tk
from PIL import Image, ImageTk

class VideoGUI:
    def __init__(self, video_source=0):
        self.window = tk.Tk()
        self.window.title("Video Feed")
        self.video_source = video_source

        self.canvas = tk.Canvas(self.window, width=640, height=480)
        self.canvas.pack()

        self.start_button = tk.Button(self.window, text="Start", command=self.start_video)
        self.start_button.pack()

        self.stop_button = tk.Button(self.window, text="Stop", command=self.stop_video, state="disabled")
        self.stop_button.pack()

        self.video_capture = cv2.VideoCapture(self.video_source)
        self.video_frame = None

    def start_video(self):
        self.video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        self.update_video()
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")

    def stop_video(self):
        self.video_capture.release()
        self.video_frame = None
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")

    def update_video(self):
        ret, frame = self.video_capture.read()
        if ret:
            self.video_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            self.photo = ImageTk.PhotoImage(Image.fromarray(self.video_frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        self.window.after(10, self.update_video)

if __name__ == "__main__":
    gui = VideoGUI()
    gui.window.mainloop()
