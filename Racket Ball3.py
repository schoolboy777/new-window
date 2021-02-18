from tkinter import * #импортирование <из> модуля ткинтер.
import random #имрортируем модуль рандом.
import time #импортируем модуль время.
print(time.asctime())
class Ball:#класс мяч-состовление класса.
    def __init__(self, canvas, paddle, color,):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False
       #имя        #аргумент   
    def hit_paddle(self, pos):#всё,что записано после def и вниз Тело функции
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
            return False

    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3
        print(self.canvas.coords(self.id))

class Paddle:#ракетка
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0
    
    def turn_left(self, evt):
        self.x = -3

    def turn_right(self, evt):
        self.x = 3

def knopka():
    print(time.asctime())
    time.sleep(10)
    
tk = Tk()#создаёт холст-это класс встроенный в ткинтер.
btn1 = Button(tk, text="вход", command=knopka)#создание кнопки с аргументами tk и text.
btn1.pack()#btn переменная,pack команда для работы с граффическими элементами в ткинтер ст,163.
tk.title("Игра")
tk.resizable(1000, 1000)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bg="blue", bd=0, highlightthickness=0)
canvas.pack()
tk.update()

paddle = Paddle(canvas, 'red')#объект
ball = Ball(canvas, paddle, 'green')#объект

while 1:
    if ball.hit_bottom == False:
        ball.draw()
        paddle.draw()
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)
root.mainloop()
