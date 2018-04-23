from tkinter import *
import Model
import ViewController
import config


def main():
    root = Tk()
    root.geometry("850x500+300+300")
    ViewController.PaintViewController(model=Model.PaintModel, config=config, parent=root)
    root.mainloop()


if __name__ == '__main__':
    main()
