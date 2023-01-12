import os
import datetime
from tkinter import *
from tkinter import messagebox

directory = "C:/Users/donegin/Desktop/m_hair_ep2_western_01"




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


flag = False
if directory == "":
    messagebox.showerror('Error', 'Please check the path')
else:
    res = ""
    for root, dirs, files in os.walk(directory):                                                                #берем один элемент, проверяем его
        f = open('str.txt', 'r')
        structure = f.readlines()
        f.close()
        for structural_element in structure:
            if structural_element != "\n":
                folder_name_s = structural_element.find("Folder name: ") + len("Folder name: ")
                folder_name_e = structural_element.find(" File format: ")
                file_names_s = structural_element.find("File format:") + len("File format: ")
                file_names_e = structural_element.find("Folders:")
                folder_names_s = structural_element.find("Folders:") + len("Folders:")
                folder_names_e = structural_element.find("Image size:")
                folder_name = structural_element[folder_name_s:folder_name_e]
                file_names = structural_element[file_names_s:file_names_e].replace(' ', '').split(',')
                folder_names = structural_element[folder_names_s:folder_names_e].replace(' ', '').split(',')
                if root == directory:
                    if folder_name == "!MainFolder!":
                        res = res + (Check_Folder_Name(root, dirs, folder_names))
                if os.path.basename(root) == folder_name:
                    if folder_names != [""]:
                        res = res + (Check_Folder_Name(root, dirs, folder_names))
                if os.path.basename(root) not in os.path.basename(directory):
                    if folder_name == os.path.basename(root):
                        if file_names[0]:
                            res = res + (Check_File_Name(directory, root, files, file_names))

    print(res)






        # if directory == root:
        #     res = res + Check_Folder_Name(root, dirs, check_folder)
        # elif directory != root:
        #     if os.path.basename(root) in check_folder:
        #         res = res + Check_Folder_Name(root, dirs, check_folder[os.path.basename(root)])

