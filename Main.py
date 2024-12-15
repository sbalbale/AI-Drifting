import tkinter as tk
import pyglet
from Track import Track

# Initialize Tkinter window
root = tk.Tk()
root.title("AI Drifting Project")
root.geometry("800x600")
root.configure(bg='gray')

# Create a canvas
canvas = tk.Canvas(root, width=800, height=600, bg='gray')
canvas.pack()

# Load track configuration from JSON file
config = Track.load_from_json('gameData/track_config.json')
track = Track(canvas, config)

# # Load a Pyglet font (optional)
# pyglet.font.add_file('path_to_your_font.ttf')
# custom_font = pyglet.font.load('YourFontName')

# Run the Tkinter main loop
root.mainloop()