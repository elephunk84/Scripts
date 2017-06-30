#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as Tk
import math, base64, os, subprocess

from lib.gui.private import *

privateTEXTFile='/home/iainstott/GitRepo/Scripts/lib/gui/data/privatefile.txt'
GLOBALBGCOLOR="grey86"
GLOBALBGCOLOR2="grey92"

def StrEncode():
    STRroot = Tk.Tk()
    app = STRINGENCODE(STRroot)
    STRroot.title("Encode & Decode")
    STRroot.geometry('600x200+50+50')
    STRroot.mainloop()

class STRINGENCODE(Tk.Frame):

    def __init__(self, parent):
        Tk.Frame.__init__(self, parent)
        self.master = parent
        self.StringEncode()

    def StringEncode(self):
        self.StringEncode_entry1 = Tk.Entry(self.master, width=70)
        self.StringEncode_entry1.pack()
        self.StringEncode_entry1.place(x=20, y=30)
        self.StringEncode_label1 = Tk.Label(self.master, text="Encode & Decode text...", height=0, width=100)
        self.StringEncode_label1.pack()
        self.StringEncode_button1 = Tk.Button(self.master, text="Encode",  command=lambda :self.STRencode(), justify=Tk.LEFT)
        self.StringEncode_button1.pack()
        self.StringEncode_button1.place(x=20, y=60)
        self.StringEncode_button2 = Tk.Button(self.master, text="Decode",  command=lambda :self.STRdecode(), justify=Tk.LEFT)
        self.StringEncode_button2.pack()
        self.StringEncode_button2.place(x=100, y=60)
        self.StringEncode_button3 = Tk.Button(self.master, text="Clear File",  command=lambda :self.CLRPRVFile(), justify=Tk.LEFT)
        self.StringEncode_button3.pack()
        self.StringEncode_button3.place(x=480, y=60)
        self.StringEncode_EncodedString=Tk.StringVar()
        self.StringEncode_EncodedStringLabel=Tk.Label(self.master, textvariable=self.StringEncode_EncodedString, font=('helvetica', 24), fg='green')
        self.StringEncode_EncodedStringLabel.pack()
        self.StringEncode_EncodedStringLabel.place(x=20, y=100)


    def STRencode(self):
        self.OrigString=self.StringEncode_entry1.get()
        encoded_string=STRencode(self.OrigString)
        with open(privateTEXTFile, "a") as f:
            encoded_string=str(encoded_string)
            encoded_string=encoded_string[:-1]
            encoded_string=encoded_string[2:]
            f.write(self.OrigString+" = "+encoded_string+'\n')
        self.StringEncode_EncodedString.set(encoded_string)
        print("String = "+self.OrigString+" Encoded = "+encoded_string)

    def STRdecode(self):
        self.OrigString=self.StringEncode_entry1.get()
        decoded_string=STRdecode(self.OrigString)
        self.StringEncode_EncodedString.set(str(decoded_string))

    def CLRPRVFile(self):
        os.remove(privateTEXTFile)
        subprocess.call(['touch', privateTEXTFile])

if __name__ == "__main__":
    StrEncode()
