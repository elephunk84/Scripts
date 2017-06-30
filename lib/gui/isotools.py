#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, subprocess, shutil
from pubsub import pub
from glob import glob

discsDIR='/mnt/NFS/Data/template/iso'
discDIRContents=os.listdir(discsDIR)
discDIRContents=sorted(discDIRContents, reverse=True)

import tkinter as Tk

drives=subprocess.Popen(['ls /dev/disk/by-id/usb-*'], shell=True, stdout=subprocess.PIPE)
drives_stdout, drives_stderr = drives.communicate()

DRIVES=drives_stdout.splitlines()

CHOICE1={
        'USB/SD Card':['usbsdChoice'],
        'CD/DVD Media':['cddvdChoice'],
        'Mount ISO':['mountChoice'],
        'Extract ISO':['exctractChoice']
        }

def ISOmain():
    root = Tk.Tk()
    root.geometry("400x200+300+300")
    app = ISOTOOLS(root)
    img = Tk.PhotoImage(file = '/home/iainstott/GitRepo/Scripts/lib/gui/data/images/isoicon.png')
    root.call('wm', 'iconphoto', root, img)
    root.mainloop()

class ISOTOOLS(Tk.Frame):
    def __init__(self, parent):
        """Constructor"""
        pub.subscribe(self.listener, "mainListener")
        self.root = parent
        self.root.title("Iso Tool Menu")
        self.frame = Tk.Frame(parent)
        self.frame.pack()
        self.Page1_text=Tk.StringVar()
        self.Page1_text.set("None")
        self.Page1_label=Tk.Label(self.frame, text="Please choose a mode").pack(pady=10)
        for choice, command in CHOICE1.items():
            Page1_radio=Tk.Radiobutton(self.frame, variable=self.Page1_text, text=choice, value=command).pack()
        Page1_b1 = Tk.Button(self.frame, text="Next",  command=lambda : self.onClick(), justify=Tk.LEFT)
        Page1_b1.pack(pady=30)

    def listener(self, arg1, arg2=None):
        """pubsub listener - opens main frame when otherFrame closes"""
        self.show()
        if arg1 == "data1":
            self.root.destroy()

    def hide(self):
        self.root.withdraw()

    def onClick(self):
        frameChoice=self.Page1_text.get()
        if frameChoice == "usbsdChoice":
            FrameChoice="FrameOne"
            subframe = FrameOne()
            self.hide()
        if frameChoice == "cddvdChoice":
            FrameChoice="FrameTwo"
            subframe = FrameTwo()
            self.hide()
        if frameChoice == "VideoCommand":
            FrameChoice="FrameThree"
            subframe = FrameThree()
            self.hide()
        if frameChoice == "KdenScr":
            FrameChoice="FrameFour"
            subframe = FrameFour()
            self.hide()
        if frameChoice == "KdenProj":
            FrameChoice="FrameFive"
            subframe = FrameFive()
            self.hide()

    def show(self):
        self.root.update()
        self.root.deiconify()

class FrameOne(Tk.Toplevel):

    def __init__(self):
        """Constructor"""
        Tk.Toplevel.__init__(self)
        self.geometry("600x400+300+300")
        self.title("USB/SD Card")
        self.USBOpts_text=Tk.StringVar()
        self.USBOpts_text.set("None")
        self.USBOptsLIST=Tk.Listbox(self, height=15, width=70)
        for IMAGE in discDIRContents:
                self.USBOptsLIST.insert(0, IMAGE)
        self.USBOptsLIST.pack()
        self.USBOpts_text2=Tk.StringVar()
        self.USBOpts_text2.set("None")
        self.pane = Tk.PanedWindow(self, orient=Tk.VERTICAL)
        self.pane1= Tk.LabelFrame(self.pane, text="Available Drives", width=20, height=20)
        for DRIVE in DRIVES:
                self.USBOptsLIST2=Tk.Radiobutton(self.pane1, variable=self.USBOpts_text2, text=DRIVE, value=DRIVE, justify=Tk.LEFT).pack(anchor=Tk.W, padx=20)
        USBOpts_button1 = Tk.Button(self, text="Next",  command=lambda : self.onClick(), justify=Tk.LEFT)
        self.pane.add(self.pane1)
        self.pane.place(x=10, y=250)
        USBOpts_button1.pack()
        USBOpts_button1.place(x=500, y=250)

    def onClose(self):
        pub.sendMessage("mainListener", arg1="data1")
        self.destroy()

class FrameTwo(Tk.Toplevel):

    def __init__(self):
        """Constructor"""
        Tk.Toplevel.__init__(self)
        self.geometry("600x400+300+300")
        self.title("Burn ISO Image on AlienServer")
        btn = Tk.Button(self, text="Close", command=self.onClose)
        btn.pack()

    def onClose(self):
        pub.sendMessage("mainListener", arg1="data")
        self.destroy()

class FrameThree(Tk.Toplevel):

    def __init__(self):
        """Constructor"""
        Tk.Toplevel.__init__(self)
        self.geometry("400x200+300+300")
        self.title("Folder Choice")
        btn = Tk.Button(self, text="Close", command=self.onClose)
        btn.pack()

    def onClose(self):
        pub.sendMessage("mainListener", arg1="data")
        self.destroy()

class FrameFour(Tk.Toplevel):

    def __init__(self):
        """Constructor"""
        Tk.Toplevel.__init__(self)
        self.geometry("400x200+300+300")
        self.title("Kden Scripts Choice")
        btn = Tk.Button(self, text="Close", command=self.onClose)
        btn.pack()

    def onClose(self):
        pub.sendMessage("mainListener", arg1="data")
        self.destroy()

class FrameFive(Tk.Toplevel):

    def __init__(self):
        """Constructor"""
        Tk.Toplevel.__init__(self)
        self.geometry("400x200+300+300")
        self.title("Project Choice")
        btn = Tk.Button(self, text="Close", command=self.onClose)
        btn.pack()

    def onClose(self):
        pub.sendMessage("mainListener", arg1="data")
        self.destroy()

if __name__ == "__main__":
    ISOmain()
