from tkinter import *
import webbrowser
import datetime
import copy

date = datetime.datetime.now()
today = 'Today\'s topic'

def on_click(keyword):
    URL = "https://search.naver.com/search.naver?where=news&query=" + keyword + "&sm=tab_tmr&nso=so:r,p:all,a:all&sort=0"
    webbrowser.open(URL)

def UI_tk(topic_list):
    topic=copy.deepcopy(topic_list)
    window = Tk()
    window.title(today)
    window.geometry("300x675")

    buttons = []
    labels = []

    ibuttons = []
    ilabels = []

    buttonCnt = 10

    label = Label(window, text=datetime.datetime.now().strftime('%Y-%m-07 23시'))
    label.grid(row=0, column=0)
    bFont = ("Courier", 15, "bold")
    max_line = 18

    for x in range(0, buttonCnt):
        
        label = Label(window, text=(x+1,'위'))
        labels.append(label)
        labels[x].grid(row=(x % max_line)+2, column= int(x / max_line)*2 + 0)
        labels[x].config(height=2, width=3)

        button = Button(window)
        buttons.append(button)
        buttons[x].grid(row=(x % max_line) + 2, column= int(x / max_line)*2 + 1)
        button_text = StringVar()
        button_text.set(topic[x])
        buttons[x].config(height=2, width=15, textvariable=button_text, command=lambda i=x: on_click(topic[i]), font = bFont)

        
    
    mainloop()

