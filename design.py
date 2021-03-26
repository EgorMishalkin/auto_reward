from tkinter import *
from tkinter import filedialog
from get_info import get_info


def UploadAction(event=None):
    # принимаем путь к файлу
    filename = filedialog.askopenfilename()
    filename2 = filedialog.askopenfilename()
    if str(filename).split('.')[1] in ['xlsx', 'xls']:
        if str(filename2).split('.')[1] in ['docx']:
            get_info(filename, filename2)
            notif = Label(frame, text="Награды сделаны!", bg="red")
            notif.pack()
        else:
            notif = Label(frame, text="Данный тип файла не соответствует формату docx :(", bg="red")
            notif.pack()
    else:
        notif = Label(frame, text="Данный тип файла не соответствует формату xlsx или xls :(", bg="red")
        notif.pack()


# загрузка файлов в приложение


def UploadAction1(event=None):
    # принимаем путь к файлу
    filename = filedialog.askopenfilename()
    if str(filename).split('.')[1] in ['xlsx', 'xls']:
        if get_info(filename) == 'ok':
            notif = Label(frame, text="Награды сделаны!", bg="red")
            notif.pack()
        else:
            notif = Label(frame, text="Возникли проблемы с таблицей. Проверьте правильность введеных данных", bg="red")
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
root.geometry('700x400')
root.resizable(width=False, height=False)
canvas = Canvas(root, height=600, width=300)
canvas.pack()

frame = Frame(root, bg='light blue')
frame.place(relwidth=1, relheight=1)
# создание текста в окне
title = Label(frame, text="Автоматические документы", bg="light blue", font=40)
title.pack()
lbl1 = Label(frame, text="1). Нажмите на кнопку 'Загрузить' и выберите файл в формате .xlsx")
lbl1.pack()
lbl2 = Label(frame, text="2). Ожидайте повторного открытия диалогового окна и выберите файл с расширением .docx")
lbl2.pack()
lbl3 = Label(frame, text="3). После появления надписи 'Награды готовы!', откройте созданную "
                         "автоматически папку и пользуйтесь документами!")
lbl3.pack()
# кнопки
btn = Button(frame, text="Загрузить файлы", bg="white", height=5, width=13, command=UploadAction)
btn.place(x=300, y=200)


root.mainloop()
