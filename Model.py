# всі дані
from tkinter import Canvas, Tk


class PaintModel():
    def __init__(self):
        self.canv = Canvas(self, bg="white")

    def setCursor(self, place):
        pass

    def set_color(self, new_color):
        self.color = new_color

    def set_brush_size(self, new_size):
        self.brush_size = new_size

    def draw(self, event):
        self.canv.create_oval(event.x - self.brush_size,
                              event.y - self.brush_size,
                              event.x + self.brush_size,
                              event.y + self.brush_size,
                              fill=self.color, outline=self.color)
