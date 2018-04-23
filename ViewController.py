# зовнішній вигляд
from tkinter import *


class PaintViewController(Frame):
    def __init__(self, model, config, parent=None):
        Frame.__init__(self, parent)

        self.model = model
        self.parent = parent
        self.color = config.default_color
        self.brush_size = config.default_brush_size
        self.setUI()

    def draw(self, event):
        self.canv.create_oval(event.x - self.brush_size,
                              event.y - self.brush_size,
                              event.x + self.brush_size,
                              event.y + self.brush_size,
                              fill=self.color, outline=self.color)

    def setUI(self):
        self.parent.title("Paint")  # Устанавливаем название окна
        self.pack(fill=BOTH, expand=1)  # Размещаем активные элементы на родительском окне

        self.columnconfigure(6, weight=1)  # Даем седьмому столбцу возможность растягиваться, благодаря чему кнопки не будут разъезжаться при ресайзе
        self.rowconfigure(2, weight=1)  # То же самое для третьего ряда

        # Создаем поле для рисования, устанавливаем белый фон
        self.canv = Canvas(self, bg="white")
        self.canv.grid(row=2, column=0, columnspan=7,
                       padx=5, pady=5,
                       sticky=E + W + S + N)  # Прикрепляем канвас методом grid. Он будет находится в 3м ряду, первой колонке, и будет занимать 7 колонок, задаем отступы по X и Y в 5 пикселей, и заставляем растягиваться при растягивании всего окна
        self.canv.bind("<B1-Motion>",
                       self.draw)  # Привязываем обработчик к канвасу. <B1-Motion> означает "при движении зажатой левой кнопки мыши" вызывать функцию draw

        color_lab = Label(self, text="Color: ")  # Создаем метку для кнопок изменения цвета кисти
        color_lab.grid(row=0, column=0,
                       padx=6)  # Устанавливаем созданную метку в первый ряд и первую колонку, задаем горизонтальный отступ в 6 пикселей

        red_btn = Button(self, width=2, bg="red",
                         command=lambda: self.model.set_color(self, "red"))  # Создание кнопки:  Установка текста кнопки, задание ширины кнопки (10 символов), функция вызываемая при нажатии кнопки.
        red_btn.grid(row=0, column=1)  # Устанавливаем кнопку

        # Создание остальных кнопок повторяет ту же логику, что и создание
        # кнопки установки красного цвета, отличаются лишь аргументы.

        green_btn = Button(self, width=2, bg="green",
                           command=lambda: self.model.set_color(self, "green"))
        green_btn.grid(row=0, column=2)

        blue_btn = Button(self, width=2, bg="blue",
                          command=lambda: self.model.set_color(self, "blue"))
        blue_btn.grid(row=0, column=3)

        black_btn = Button(self, width=2, bg="black",
                           command=lambda: self.model.set_color(self, "black"))
        black_btn.grid(row=0, column=4)

        white_btn = Button(self, width=2, bg="white",
                           command=lambda: self.model.set_color(self, "white"))
        white_btn.grid(row=0, column=5)

        clear_btn = Button(self, text="Clear all", width=10,
                           command=lambda: self.canv.delete("all"))
        clear_btn.grid(row=0, column=6, sticky=W)

        size_lab = Label(self, text="Brush size: ")
        size_lab.grid(row=1, column=0, padx=5)
        one_btn = Button(self, text="Two", width=10,
                         command=lambda: self.model.set_brush_size(self, 2))
        one_btn.grid(row=1, column=1)

        two_btn = Button(self, text="Five", width=10,
                         command=lambda: self.model.set_brush_size(self, 5))
        two_btn.grid(row=1, column=2)

        five_btn = Button(self, text="Seven", width=10,
                          command=lambda: self.model.set_brush_size(self, 7))
        five_btn.grid(row=1, column=3)

        seven_btn = Button(self, text="Ten", width=10,
                           command=lambda: self.model.set_brush_size(self, 10))
        seven_btn.grid(row=1, column=4)

        ten_btn = Button(self, text="Twenty", width=10,
                         command=lambda: self.model.set_brush_size(self, 20))
        ten_btn.grid(row=1, column=5)

        twenty_btn = Button(self, text="Fifty", width=10,
                            command=lambda: self.model.set_brush_size(self, 50))
        twenty_btn.grid(row=1, column=6, sticky=W)

        #Spinbox(self.parent, from=0, to=50, width=5).pack()

