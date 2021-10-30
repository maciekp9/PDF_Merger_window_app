import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfFileMerger


class pdfmerger:

    def __init__(self, window_width, window_height):
        self.root = tk.Tk()
        self.root.title("PDF merger")
        center_x = int(self.root.winfo_screenwidth() / 2 - window_width / 2)
        center_y = int(self.root.winfo_screenheight() / 2 - window_height / 2)
        self.root.resizable(False, False)
        self.filenames= []
        self.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


    def UI(self):
        self.listbox = tk.Listbox(self.root)
        self.listbox.pack()
        self.choose_button = tk.Button(self.root, text="Choose Files", command=self.choose_files)
        self.choose_button.pack()
        self.merge_button = tk.Button(self.root, text="Merge Files", command=self.merge_files)
        self.merge_button.pack()


    def choose_files(self):
        FILEOPENOPTIONS = dict(defaultextension=".pdf", initialdir="/Users/maciejprzydatek/Desktop",
                               filetypes=[('pdf file', '*.pdf')])
        self.filenames = filedialog.askopenfilenames(**FILEOPENOPTIONS)
        for i in range(0,len(self.filenames)):
            self.listbox.insert(i,self.filenames[i])

        print(self.filenames)




    def merge_files(self):
        pass


    def program_start(self):
        self.UI()
        self.root.mainloop()

