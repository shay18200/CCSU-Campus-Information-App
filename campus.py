from tkinter import *
from PIL import ImageTk, Image
import pandas as pd

#window setup
window = Tk()
window.title("CCSU Moblie App")
window.geometry("600x600")
window.resizable(width = 0, height = 0)
window.configure(bg="#a3b9db")



img= Image.open ('logo1.png')
try:
    img=img.resize((100,100), Image.Resampling.LANCZOS)
except AttributeError:
    img=img.resize((100,100),Image.ANTIALIAS)

img = img.convert("RGBA")
data = img.getdata()

newData = []
for item in data:

    if item[:3] == (255, 255, 255):
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)
img.putdata(newData)
img.save("transparent.png")

logo = Image.open("transparent.png")
logo = ImageTk.PhotoImage(logo)
logoLabel = Label(window, image=logo, bg="#a3b9db")
logoLabel.place(x=1, y=1)

data = pd.read_csv("CCSU_Fall_2026_Academic_Calendar.csv")

lb = Label(window, justify="left", bg="#a3b9db", anchor="w", font=("Arial", 12))
lb.place(x=130, y=235)


def calender():
    df = pd.DataFrame(data, columns=['CalendarDate'])
    selected_rows = df[~df['CalendarDate'].isnull()]
    lb.config(text=selected_rows.to_string(index=False))
    lb.place(x=130, y=235)    # CHANGED: y


def building():
    df = pd.DataFrame(data, columns=['Buildings'])
    selected_rows = df[~df['Buildings'].isnull()]
    lb.config(text=selected_rows.to_string(index=False))
    lb.place(x=130, y=235)


def faculty():
    df = pd.DataFrame(data, columns=['FacultyName'])
    selected_rows = df[~df['FacultyName'].isnull()]
    lb.config(text=selected_rows.to_string(index=False))
    lb.place(x=130, y=235)

#school of business
def business():
    if lb.cget("text") == "":
        lb.config(text="School of Business Departments:\n"
                       "- Accounting\n"
                       "- Finance\n"
                       "- Management & Organization\n"
                       "- Marketing\n"
                       "- Management Information Systems (MIS)\n"
                       "- Business Analytics")
    else:
        lb.config(text="")

#MIS Department
def mis():
    if lb.cget("text") == "":
        lb.config(text="MIS Department Core Courses:\n"
                       "- Intro to MIS\n"
                       "- Database Management\n"
                       "- Systems Analysis & Design\n"
                       "- Business Analytics / Data Visualization\n"
                       "- Networks & Information Security\n"
                       "- Project Management\n"
                       "- Python for Business Applications")
    else:
        lb.config(text="")

button1 = Button(window, text='Calendar', command=calender, highlightbackground="dark blue", fg="black")
button1.place(x=50, y=110)

button2 = Button(window, text='Buildings', command=building, highlightbackground="dark blue", fg="black")
button2.place(x=150, y=110)

button3 = Button(window, text='Faculty', command=faculty, highlightbackground="dark blue", fg="black")
button3.place(x=250, y=110)

button4 = Button(window, text='School of Business', command=business, highlightbackground="dark blue", fg="black")
button4.place(x=45, y=185)

button5 = Button(window, text='MIS Department', command=mis, highlightbackground="dark blue", fg="black")
button5.place(x=200, y=185)
window.mainloop()
