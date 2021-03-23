from tkinter import *
from tkinter import filedialog
from get_info import get_info


def UploadAction(event=None):
    # принимаем путь к файлу
    filename = filedialog.askopenfilename()
    if str(filename).split('.')[1] in ['xlsx', 'xls']:
        get_info(filename)
        notif = Label(frame, text="Награды сделаны!", bg="red")
        notif.pack()
    else:
        notif = Label(frame, text="Данный тип файла не соответствует формату xlsx или xls :(", bg="red")
        notif.pack()


# загрузка файлов в приложение


def HelpAction():
    root = Tk()
    root['bg'] = '#fafafa'
    root.title("Автоматические документы")
    root.geometry('600x300')
    root.resizable(width=False, height=False)
    canvas = Canvas(root, height=600, width=300)
    canvas.pack()

    frame = Frame(root, bg='light blue')
    frame.place(relwidth=1, relheight=1)

    title = Label(frame, text="Помощь", bg="light blue", font=40)
    title.pack()
    lbl1 = Label(frame, text="1). Загрузите с помощью кнопки 'Загрузить 1-ый файл' книгу Excel c расширением .xlsx")
    lbl1.pack()
    lbl2 = Label(frame, text="2). Загрузите с помощью кнопки 'Загрузить 2-ой файл' документ Word с расширением .docx")
    lbl2.pack()


def UploadAction1(event=None):
    # принимаем путь к файлу
    filename = filedialog.askopenfilename()
    if str(filename).split('.')[1] in ['xlsx', 'xls']:
        get_info(filename)
        notif = Label(frame, text="Награды сделаны!", bg="red")
        notif.pack()
    else:
        notif = Label(frame, text="Данный тип файла не соответствует формату xlsx или xls :(", bg="red")
        notif.pack()


def UploadAction2(event=None):
    filename2 = filedialog.askopenfilename()
    if str(filename2).split('.')[1] in ['docx']:
        print(0)
    else:
        print(1)


root = Tk()
root['bg'] = '#fafafa'
root.title("Автоматические документы")
root.geometry('600x300')
root.resizable(width=False, height=False)
canvas = Canvas(root, height=600, width=300)
canvas.pack()

frame = Frame(root, bg='light blue')
frame.place(relwidth=1, relheight=1)
# создание текста в окне
title = Label(frame, text="Автоматические документы", bg="light blue", font=40)
title.pack()

# кнопки
btn = Button(frame, text="Загрузить 1-ый файл", bg="white", command=UploadAction1)
btn.place(x=320, y=270)

btn2 = Button(frame, text="Загрузить 2-ой файл", bg="white", command=UploadAction2)
btn2.place(x=470, y=270)

btn3 = Button(frame, text="Помощь", bg="white", command=HelpAction)
btn3.place(x=4, y=270)

root.mainloop()