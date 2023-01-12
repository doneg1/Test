import os
import datetime
from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext

# directory = "C:/Users/donegin/Desktop/m_hair_ep2_western_01"
check_main_folder = ["2.HP", "1.WB_Pattern", "3.Texturing", "4.Final_delivery"]                                         #главные папки
check_folder = {
    "1.WB_Pattern": ["work"],
    "2.HP": "",
    "3.Texturing": ["baking", "substance_painter", "work_files"],
    "4.Final_delivery": ["baking", "substance_painter", "work_files"]
}

check_folder_WB_HP = [".jpg", ".ztl"]                                                                                   #проверка по файлам и папкам
check_folder_Tex_Fin = [".asset", ".jpg", ".mb", ".mesh", ".ztl", "_diffuse.dds", "_normal.dds", "_properties.dds",
                        "_screenshot.png"]
check_folder_baking = [".fbx", ".tbscene", "_ao.png", "_curve.png", "_normal.png", "_normalobj.png", "_position.png",
                       "_thickness.png", "_vertexcolor.png"]
check_folder_substance_painter = [".meta", ".spp", "_BaseColor.png", "_Color1.png", "_Metallic.png", "_Normal.png",
                                  "_Opacity.png", "_Roughness.png"]


def btn_save_click(txt):
    sv = f"{datetime.datetime.now().strftime('%d-%m-%Y %H:%M')}\n{txt.get('1.0', END)}"                                 #сохраняем в файл
    Check_issues = open('check.txt', "a", encoding='utf-8')
    Check_issues.write(sv)
    Check_issues.close()
    messagebox.showinfo("Save", "Save complete")


def btn_click():
    try:
        directory = directoryInput.get()#.replace('\\', '/')                                                            #получаем путь
        flag = False
        if directory == "":
            messagebox.showerror('Error', 'Please check the path')
        else:
            res = ""
            for root, dirs, files in os.walk(directory):                                                                #берем один элемент, проверяем его
                if directory == root:
                    res = res + Check_Folder_Name(root, dirs, check_folder)
                elif directory != root:
                    if os.path.basename(root) in check_folder:
                        res = res + Check_Folder_Name(root, dirs, check_folder[os.path.basename(root)])
                if os.path.basename(root) not in os.path.basename(directory):
                    if os.path.basename(root) == "1.WB_Pattern" or os.path.basename(root) == "2.HP":
                        res = res + (Check_File_Name(directory, root, files, check_folder_WB_HP))
                        flag = True
                    elif os.path.basename(root) == "3.Texturing" or os.path.basename(root) == "4.Final_delivery":
                        res = res + (Check_File_Name(directory, root, files, check_folder_Tex_Fin))
                        flag = True
                    elif os.path.basename(root) == "baking":
                        res = res + Check_File_Name(directory, root, files, check_folder_baking)
                        flag = True
                    elif os.path.basename(root) == "substance_painter":
                        res = res + Check_File_Name(directory, root, files, check_folder_substance_painter)
                        flag = True

            if res == "" and flag:                                                                                      #проверка на ввод
                res = "OK\n\n"
            elif res == "" and not flag:
                messagebox.showerror('Error', 'Please check the path')

            if res != "":
                window.geometry('620x415')                                                                              #обновляем окно Tk
                txt = scrolledtext.ScrolledText(window, width=65, height=19, wrap="word")
                txt.place(x=45, y=65)
                txt.insert(INSERT, res)
                txt.configure(state=DISABLED)
                btn_save = Button(frame, text='Save', command=lambda: btn_save_click(txt), width=10, height=1)
                btn_save.place(x=507, y=380)

    except:
        messagebox.showerror('Error', 'Please check the path')                                                          #ловим ошибку


def Check_File_Name(directory, root, files, check_file):                                                                #деф проверка на имя файла и формат
    merge_name = []
    report = ""
    for f in check_file:
        merge_name.append(os.path.basename(directory) + f)
    check_files = []
    if len(files) < len(check_file):
        report = f"{report}#FILE-IS-MISSING: {list(set(merge_name) - set(files))}\n"

    elif len(files) > len(check_file):
        report = f"{report}#UNNECESSARY-FILE: {len(files) - len(merge_name)}\n"
    for file in files:
        flag = True
        for mname in merge_name:
            if mname == file:
                flag = False
                break
        if flag:
            check_files.append(file)

    for f in check_files:
        index = f.index('.')                                                                                            #разделяю название файла и формат
        flag = True
        for ff in merge_name:
            index1 = ff.index('.')
            if f[:index] == ff[:index1]:#проверяем формат
                flag = False
                break
        if flag:
            report = f"{report}#WRONG-NAME: {f[:index]}\n"

        flag = True
        for ff in check_file:
            index1 = ff.index('.')                                                                                      #разделяю название файла и формат
            if f[index:] == ff[index1:]:
                flag = False
                break
        if flag:
            report = f"{report}#WRONG-FORMAT: {f} => {f[index:]}\n"

    if report:
        report = f"{report}\n"
        report = f"{root}\n{report}"
    return report


def Check_Folder_Name(root, dirs, check_folder):                                                                        #деф проверка на название папки
    report = ""
    for f in dirs:
        flag = True
        for ff in check_folder:#проверяем название папки
            if f == ff:
                flag = False
                break
        if flag:
            report = f"{report}#WRONG-FOLDER-NAME: {f}\n"

    if len(check_folder) < len(dirs):#сравниваем количество папок
        report = f"{report}#UNNECESSARY-FOLDER: {len(dirs) - len(check_folder)}\n"

    elif len(check_folder) != len(dirs):
        for f in list(set(check_folder) - set(dirs)):#проверяем на отсуствие папки
            report = f"{report}#FOLDER-IS-MISSING: {f}\n"
    if report:
        report = f"{report}\n"
        report = f"{root}\n{report}"

    return report


window = Tk()
window.title('Paradox')
window.geometry('620x100')                                                                                              #создаем окно
window.resizable(width=False, height=False)#нельзя изменять размер окна
canvas = Canvas(window, height=500, width=100)
canvas.pack()
frame = Frame(window, bg='#808080')
frame.place(relwidth=1, relheight=1)

title = Label(frame, text='Path:', bg='#808080')                                                                        #текст
title.place(x=10, y=10)                                                                                                 #расположение текста
directoryInput = Entry(frame, width=90)                                                                                 #форма
folder_path = directoryInput.get().replace('\\', '/')
directoryInput.place(x=45, y=10)                                                                                        #расположение формы
btn = Button(frame, text='Check', command=btn_click, width=10, height=1)                                                #кнопка
btn.place(x=45, y=35)                                                                                                   #расположение кнопка
btn_close = Button(frame, text='Close', command=window.destroy, width=10, height=1)
btn_close.place(x=130, y=35)
window.mainloop()