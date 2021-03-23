from tkinter import *
from tkinter import filedialog
from get_info import get_info


def UploadAction(event=None):
    # принимаем путь к файлу
    filename = filedialog.askopenfilename()
    if str(filename).split('.')[1] in ['xlsx']:
        get_info(filename)
    else:
        print(1)


# загрузка файлов в приложение


root = Tk()
root['bg'] = '#fafafa'
root.title("Автоматические документы")
root.geometry('500x250')
canvas = Canvas(root, height=500, width=250)
canvas.pack()

frame = Frame(root, bg='red')
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)
# создание текста в окне

title = Label(frame, text="Автоматические документы", bg="gray", font=40)
title.pack()

# кнопки

btn = Button(frame, text="Загрузить файл", bg="white", command=UploadAction)
btn.pack()

root.mainloop()
