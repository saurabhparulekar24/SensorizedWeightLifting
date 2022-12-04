import tkinter as tk
import tkinter.ttk as ttk

variable = {"W":None,"I":None,"T":None}

class NewprojectWidget(ttk.Frame):
    def __init__(self, master=None, **kw):
        super(NewprojectWidget, self).__init__(master, **kw)
        self.weght = tk.Message(self)
        self.W = tk.StringVar(value='weight')
        self.weght.configure(
            font="{5} 12 {}",
            justify="right",
            text='weight',
            textvariable=self.W,
            width=200)
        self.weght.pack(ipadx=50, ipady=50, padx=50, pady=50, side="right")
        self.Iteration = tk.Message(self)
        self.I = tk.StringVar(value='Iteration')
        self.Iteration.configure(
            font="{5} 12 {}",
            justify="right",
            text='Iteration',
            textvariable=self.I,
            width=200)
        self.Iteration.pack(ipadx=50, ipady=50, padx=50, pady=50, side="left")
        label2 = ttk.Label(self)
        self.img_ttt = tk.PhotoImage(file="ttt.png")
        label2.configure(image=self.img_ttt, text='label2')
        label2.pack(side="top")
        progressbar1 = ttk.Progressbar(self)
        self.T = tk.StringVar(value='80')
        progressbar1.configure(
            mode="determinate",
            orient="horizontal",
            value=80,
            variable=self.T)
        progressbar1.pack(ipadx=5, ipady=5, padx=5, pady=5, side="bottom")
        self.configure(height=500, relief="groove", width=400)
        self.pack(side="top")
        global variable
        variable["W"]= self.W
        variable["I"]= self.I
        variable["T"]= self.T





