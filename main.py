import json
import tkinter as tk
import pyperclip as ppc
import customtkinter as ctk

class App():
    def __init__(self, root, json_file) -> None:
        self.root = root
        self.data = json_file
        
        self.frame_main = ctk.CTkFrame(self.root, fg_color= 'transparent')
        self.frame_main.pack(expand= True)

        self.label_list = []
        self.btn_list = []

        self.arrow_left = ctk.CTkButton(self.frame_main, text= '<-', width= 20, height= 298, command= lambda: self.scroll(dir= -1))
        self.arrow_left.grid(column = 0, rowspan= 10)

        self.arrow_right = ctk.CTkButton(self.frame_main, text= '->', width= 20, height= 298, command= lambda: self.scroll(dir= 1))
        self.arrow_right.grid(column = 4, row = 0, rowspan= 10)

        self.btn_add = ctk.CTkButton(self.frame_main, text= 'Add', width = 290, command = self.input_info)
        self.btn_add.grid(row = 10, columnspan = 5, pady = 1)

        self.marker = '0'

        #creating btns
        self.generate_btns()

    def load_json(self):
        with open('info.json', 'r') as file:
            self.data = json.load(file)

    def get(self, c):
        #example of two lists
        shuffled_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=', '-', '0', '9', '8', '7', '6', '5', '4', '3', '2', '1', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\', '|', '}', '{', 'P', 'O', 'I', 'U', 'Y', 'T', 'R', 'E', 'W', 'Q', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', ';', 'z', 'x', 'c', 'v', '', 'b', 'n', 'm', ',', '.', '/', '?', '>', '<', 'M', 'N', 'B', 'V', 'C', 'X', 'Z', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        main_list = ['q', 't', 'u', '>', 'K', 'U', 'b', ']', 'Z', '|', 'f', '9', 'G', 'A', 'h', 'B', 'n', 'a', '5', 'E', 's', '1', '4', ',', '@', 'w', 'X', '/', 'z', '?', 'g', 'v', ';', '{', 'k', '[', 'y', 'l', 'i', '(', 'm', 'F', '$', 'p', 'L', '^', '2', 'd', '+', 'c', '-', 'e', 'j', 'x', 'N', 'J', 'W', '!', 'I', '*', 'T', 'S', '}', '=', '7', '3', '#', 'D', 'r', '\\', 'Q', '%', 'O', '8', 'Y', 'H', ' ', '<', 'M', 'o', 'P', '&', '_', ')', 'V', '0', 'R', '6', ':', 'C', '.']
        sub = ''

        for symbol in self.data[self.marker][c]:
            sub += main_list[shuffled_list.index(symbol)]
        ppc.copy(sub)


    def add_new(self, c):
        #better to rewrite to not repeat init lists
        shuffled_list = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=', '-', '0', '9', '8', '7', '6', '5', '4', '3', '2', '1', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', '\\', '|', '}', '{', 'P', 'O', 'I', 'U', 'Y', 'T', 'R', 'E', 'W', 'Q', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', ';', 'z', 'x', 'c', 'v', '', 'b', 'n', 'm', ',', '.', '/', '?', '>', '<', 'M', 'N', 'B', 'V', 'C', 'X', 'Z', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']
        main_list = ['q', 't', 'u', '>', 'K', 'U', 'b', ']', 'Z', '|', 'f', '9', 'G', 'A', 'h', 'B', 'n', 'a', '5', 'E', 's', '1', '4', ',', '@', 'w', 'X', '/', 'z', '?', 'g', 'v', ';', '{', 'k', '[', 'y', 'l', 'i', '(', 'm', 'F', '$', 'p', 'L', '^', '2', 'd', '+', 'c', '-', 'e', 'j', 'x', 'N', 'J', 'W', '!', 'I', '*', 'T', 'S', '}', '=', '7', '3', '#', 'D', 'r', '\\', 'Q', '%', 'O', '8', 'Y', 'H', ' ', '<', 'M', 'o', 'P', '&', '_', ')', 'V', '0', 'R', '6', ':', 'C', '.']
        
        from objdict import ObjDict
        new_data = ObjDict(self.data)

        name = c.split(' ')[0]
        info = c.split(' ')[1]

        new = ''
        for symbol in info:
            new += shuffled_list[main_list.index(symbol)]

        true_marker = self.marker
        
        while self.marker in list(new_data.keys()) and len(new_data[self.marker]) >= 30:
            self.marker = str(int(self.marker) + 1)

        try:
            help_data = ObjDict(self.data[self.marker])
        except KeyError:
            help_data = ObjDict()

        help_data[name] = new
        new_data[self.marker] = help_data

        with open("info.json",'w+') as file:
            json.dump(new_data, file, indent=4)

        self.marker = true_marker

        self.load_json()

        for btn in self.btn_list:
            btn.grid_forget()
        self.generate_btns()
        
        self.window.destroy()


    def scroll(self, dir):
        if dir == -1:
            if self.marker == '0':
                return 0
            else: self.marker = str(int(self.marker) - 1)
        else:
            if self.marker == list(self.data)[-1]:
                return 0
            else: self.marker = str(int(self.marker) + 1)
        
        for btn in self.btn_list:
            btn.grid_forget()
        self.generate_btns()

    def generate_btns(self):
        self.btn_list = []

        for i, info in enumerate(self.data[self.marker]):
            self.btn_list.append(ctk.CTkButton(self.frame_main, 
                                   text= info,
                                   width= 200,
                                   hover_color= '#275918',
                                   command= lambda c=info:  self.get(c)))
            
            self.btn_list[i].grid(row = i - (i//10)*10, column = i//10 + 1, pady = 1, padx = 1)

    def input_info(self):
        self.window = ctk.CTkToplevel(self.root)

        main_frame = ctk.CTkFrame(self.window, fg_color= 'transparent')
        main_frame.pack(expand= True)

        entry_info = ctk.CTkEntry(main_frame, width = 200)
        entry_info.pack(side= 'top')

        btn_create = ctk.CTkButton(main_frame, text= 'add', width = 200, command = lambda: self.add_new(c= entry_info.get()))
        btn_create.pack(side= 'bottom')



def main():
    ctk.set_default_color_theme('green')

    root = ctk.CTk()
    root.geometry('900x500')
    root.resizable(0, 0)

    with open('info.json', 'r') as file:
        data = json.load(file)

    App(root= root, json_file= data)

    root.mainloop()

main()