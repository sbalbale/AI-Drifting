import tkinter as tk
from tkinter import simpledialog
import json

class Track:
    def __init__(self, canvas):
        self.canvas = canvas
        self.track_data = []
        self.current_line = None
        self.line_id = None
        self.canvas.bind("<Button-1>", self.start_line)
        self.canvas.bind("<B1-Motion>", self.draw_line)
        self.canvas.bind("<ButtonRelease-1>", self.end_line)
        self.canvas.bind("<Return>", self.connect_lines)

    def start_line(self, event):
        self.current_line = {'x1': event.x, 'y1': event.y, 'x2': event.x, 'y2': event.y}
        self.line_id = self.canvas.create_line(self.current_line['x1'], self.current_line['y1'], self.current_line['x2'], self.current_line['y2'], fill='black', width=5)

    def draw_line(self, event):
        self.current_line['x2'] = event.x
        self.current_line['y2'] = event.y
        if self.line_id:
            self.canvas.coords(self.line_id, self.current_line['x1'], self.current_line['y1'], self.current_line['x2'], self.current_line['y2'])

    def end_line(self, event):
        self.current_line['x2'] = event.x
        self.current_line['y2'] = event.y
        if self.line_id:
            self.canvas.coords(self.line_id, self.current_line['x1'], self.current_line['y1'], self.current_line['x2'], self.current_line['y2'])
        self.track_data.append(self.current_line)
        self.current_line = None
        self.line_id = None

    def connect_lines(self, event):
        points = []
        for line in self.track_data:
            points.extend([line['x1'], line['y1'], line['x2'], line['y2']])
        self.canvas.create_line(points, fill='red', width=3, smooth=True)

    def save_to_json(self, file_path):
        with open(file_path, 'w') as file:
            json.dump({'name': 'Custom Track', 'track': self.track_data}, file)

    @classmethod
    def load_from_json(cls, file_path):
        with open(file_path, 'r') as file:
            data = json.load(file)
            return data

def save_track(track):
    track_name = simpledialog.askstring("Input", "Enter the track name:")
    if track_name:
        file_path = f'gameData/track_config_{track_name}.json'
        track.save_to_json(file_path)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Track Drawing Tool")
    root.geometry("800x600")
    root.configure(bg='gray')

    canvas = tk.Canvas(root, width=800, height=600, bg='white')
    canvas.pack()

    track = Track(canvas)

    save_button = tk.Button(root, text="Save Track", command=lambda: save_track(track))
    save_button.pack()

    root.mainloop()