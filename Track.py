import tkinter as tk
import json

class Track:
    def __init__(self, canvas, config):
        self.canvas = canvas
        self.name = config['name']
        self.track_data = config['track']
        self.create_track()

    def create_track(self):
        for line in self.track_data:
            self.canvas.create_line(line['x1'], line['y1'], line['x2'], line['y2'], fill='black', width=5)

    @staticmethod
    def load_from_json(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("AI Drifting Project")
    root.geometry("800x600")
    root.configure(bg='gray')

    canvas = tk.Canvas(root, width=800, height=600, bg='gray')
    canvas.pack()

    # Load track configuration from JSON file
    config = Track.load_from_json('track_config.json')
    track = Track(canvas, config)

    root.mainloop()