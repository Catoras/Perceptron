import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import *
import perceptron

X = []
p = perceptron.Perceptron()

def plot_point(event):
    ix, iy = event.xdata, event.ydata

    X.append((ix, iy))
    ax.plot(ix,iy, marker='.',color ='#84b6f4')
    canvas.draw()

def print_axis():
    global ax
    ejeX = [-10,10]
    ejeY = [-10,10]
    zeros = [0,0]

    ax.plot(ejeX, zeros, color ='#3c3c3c')
    ax.plot(zeros, ejeY, color ='#3c3c3c')

def print_line():
    global w1, w2, theta

    p.establecerValores(float(w1.get()),float(w2.get()),float(theta.get()))

    seniales, m, b = p.funcionDeActivacion(X)

    ax.cla()
    print_axis()

    for i in range(len(X)):
        if seniales[i]:
            ax.plot(X[i][0],X[i][1], marker='.',color ='#77dd77')
        else:
            ax.plot(X[i][0],X[i][1], marker='.',color ='#ff6961')

    plt.axline((X[0][0], (X[0][0]*m)+b), slope=m, color='#84b6f4')
    canvas.draw()

def clean_screen():
    global X
    ax.cla()
    print_axis()
    canvas.draw()
    X = []


fig, ax= plt.subplots(facecolor='#c5c6c8')
fig.canvas.mpl_connect('button_press_event', plot_point)

print_axis()

mainwindow = Tk()
mainwindow.geometry('800x800')
mainwindow.wm_title('Practica 1')

w1 = StringVar(mainwindow, 0)
w2 = StringVar(mainwindow, 0)
theta = StringVar(mainwindow, 0)

canvas = FigureCanvasTkAgg(fig, master = mainwindow)
canvas.get_tk_widget().pack(padx=5, pady=5, expand=1, fill='both')

Label(mainwindow, text='w1', width=7).pack(pady=5, side='left', expand=1)
Entry(mainwindow, width=15, textvariable=w1).pack(pady=5, side='left', expand=1)

Label(mainwindow, text='w2', width=7).pack(pady=5, side='left', expand=1)
Entry(mainwindow, width=15, textvariable=w2).pack(pady=5, side='left', expand=1)

Label(mainwindow, text='θ theta', width=10).pack(pady=5, side='left', expand=1)
Entry(mainwindow, width=15, textvariable=theta).pack(pady=5, side='left', expand=1)

Button(mainwindow, text='Correr', width=10, command=print_line).pack(pady=5, side='left', expand=2)

mainwindow.mainloop()
