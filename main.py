# --- IMPORTS --- ###

from tkinter import *
from tkinter import ttk
import json

# --- TO DO LIST --- #

# crop the pic - not centered !
# introduce multiple tabs to keep different conversions open at the same time


# -------- UI SETUP -------- #


root = Tk()
root.call("source", r"C:\Users\Petra Bajac\PycharmProjects\themes\Forest Theme\forest-dark.tcl")
root.minsize(width=600, height=100)
root.config(padx=50, pady=0)
root.title("Converter")

ttk.Style().theme_use('forest-dark')

widgets_frame = ttk.Frame(root, padding=(0, 0, 0, 10))
widgets_frame.grid(row=0, column=1, padx=10, pady=(30, 10), sticky="nsew", rowspan=3)
widgets_frame.columnconfigure(index=0, weight=1)

# -------- CANVAS & WIDGETS -------- #


image = PhotoImage(file='converter.png')
my_logo = Label(widgets_frame, image=image)
my_logo.grid(row=0, column=0, columnspan=6)

text_input = ttk.Entry(widgets_frame, width=70)
text_input.insert(0, "")
text_input.grid(row=1, column=0, padx=5, pady=(0, 10), sticky="ew", columnspan=6, ipady=20)

text_output = ttk.Entry(widgets_frame, width=70)
text_output.insert(0, "")
text_output.grid(row=3, column=0, padx=5, pady=(10, 10), sticky="ew", columnspan=6, ipady=20)


# -------- BUTTONS -------- #


def copy_to_clipboard():
    my_text = text_output.get()
    root.clipboard_clear()
    root.clipboard_append(my_text)


clipboard_button = ttk.Button(widgets_frame, text="COPY TO CLIPBOARD", command=copy_to_clipboard)
clipboard_button.grid(column=4, row=6, columnspan=6, pady=(10, 10))


def clear_all():
    text_output.delete(0, END)
    text_input.delete(0, END)


clear_button = ttk.Button(widgets_frame, text="CLEAR ALL", command=clear_all)
clear_button.grid(column=3, row=6, sticky="ew", pady=(10, 10))


# --- FUTHARK --- #


def futhark_conversion():
    text_output.delete(0, END)
    my_input = text_input.get().upper()
    futhark = []
    with open("futhark.json", encoding="utf8") as f:
        futhark_dic = json.load(f)
        for item in my_input:
            if item == "H":
                if my_input[my_input.index(item) - 1] == "T":
                    futhark.pop()
                    futhark.append(futhark_dic["TH"])
                else:
                    futhark.append(futhark_dic[item])
            elif item == "G":
                if my_input[my_input.index(item) - 1] == "N":
                    futhark.pop()
                    futhark.append(futhark_dic["NG"])
                else:
                    futhark.append(futhark_dic[item])
            else:
                futhark.append(futhark_dic[item])
    my_output = ' '.join([str(letter) for letter in futhark])
    text_output.insert(END, my_output)


button_futhark = ttk.Button(widgets_frame, text="FUTHARK", command=futhark_conversion, style="Accent.TButton")
button_futhark.grid(column=0, row=2, padx=3)


# --- GLAGOLITIC --- #

def glagolitic_conversion():
    text_output.delete(0, END)
    my_input = text_input.get().upper()
    glagolitic = []
    with open("glagoljica.json", encoding="utf8") as g:
        glagolitic_dic = json.load(g)
        for item in my_input:
            if item == "J":
                if my_input[my_input.index(item) - 1] == "N":
                    glagolitic.pop()
                    glagolitic.append(glagolitic_dic["NJ"])
                elif my_input[my_input.index(item) - 1] == "L":
                    glagolitic.pop()
                    glagolitic.append(glagolitic_dic["LJ"])
                else:
                    glagolitic.append(glagolitic_dic[item])
            elif item == "Ž":
                if my_input[my_input.index(item) - 1] == "D":
                    glagolitic.pop()
                    glagolitic.append(glagolitic_dic["DŽ"])
                else:
                    glagolitic.append(glagolitic_dic[item])
            else:
                glagolitic.append(glagolitic_dic[item])
    my_output = ' '.join([str(letter) for letter in glagolitic])
    text_output.insert(END, my_output)


button_glagolitic = ttk.Button(widgets_frame, text="GLAGOLITIC", command=glagolitic_conversion, style="Accent.TButton")
button_glagolitic.grid(column=1, row=2, padx=3)


# --- CYRILLIC --- #

def cyrillic_conversion():
    text_output.delete(0, END)
    my_input = text_input.get()
    cyrillic = []
    with open("cirilica.json", encoding="utf8") as c:
        cyrillic_dic = json.load(c)
        for item in my_input:
            if item == "J":
                if my_input[my_input.index(item) - 1] == "N":
                    cyrillic.pop()
                    cyrillic.append(cyrillic_dic["NJ"])
                elif my_input[my_input.index(item) - 1] == "L":
                    cyrillic.pop()
                    cyrillic.append(cyrillic_dic["LJ"])
                else:
                    cyrillic.append(cyrillic_dic[item])
            elif item == "Ž":
                if my_input[my_input.index(item) - 1] == "D":
                    cyrillic.pop()
                    cyrillic.append(cyrillic_dic["DŽ"])
            elif item == "j":
                if my_input[my_input.index(item) - 1] == "n":
                    cyrillic.pop()
                    cyrillic.append(cyrillic_dic["nj"])
                elif my_input[my_input.index(item) - 1] == "l":
                    cyrillic.pop()
                    cyrillic.append(cyrillic_dic["lj"])
                elif my_input[my_input.index(item) - 1] == "L":
                    cyrillic.pop()
                    cyrillic.append(cyrillic_dic["LJ"])
                elif my_input[my_input.index(item) - 1] == "N":
                    cyrillic.pop()
                    cyrillic.append(cyrillic_dic["NJ"])
                else:
                    cyrillic.append(cyrillic_dic[item])
            elif item == "ž":
                if my_input[my_input.index(item) - 1] == "d":
                    cyrillic.pop()
                    cyrillic.append(cyrillic_dic["dž"])
                elif my_input[my_input.index(item) - 1] == "D":
                    cyrillic.pop()
                    cyrillic.append(cyrillic_dic["DŽ"])
                else:
                    cyrillic.append(cyrillic_dic[item])
            else:
                cyrillic.append(cyrillic_dic[item])
    my_output = ' '.join([str(letter) for letter in cyrillic])
    text_output.insert(END, my_output)


button_cyrillic = ttk.Button(widgets_frame, text="CYRILLIC", command=cyrillic_conversion, style="Accent.TButton")
button_cyrillic.grid(column=2, row=2, padx=3)


# --- NATO --- #

def nato_conversion():
    text_output.delete(0, END)
    my_input = text_input.get().upper()
    nato_code = []
    with open("nato.json", encoding="utf8") as n:
        nato_dic = json.load(n)
        for item in my_input:
            nato_code.append(nato_dic[item])
    my_output = ' '.join([str(letter) for letter in nato_code])
    text_output.insert(END, my_output)


button_nato = ttk.Button(widgets_frame, text="NATO", command=nato_conversion, style="Accent.TButton")
button_nato.grid(column=3, row=2, padx=3)


# --- MORSE --- #

def morse_conversion():
    text_output.delete(0, END)
    my_input = text_input.get().upper()
    morse_code = []
    with open("morse.json", encoding="utf8") as m:
        morse_dic = json.load(m)
        for item in my_input:
            if item == "J":
                if my_input[my_input.index(item) - 1] == "N":
                    morse_code.pop()
                    morse_code.append(morse_dic["NJ"])
                elif my_input[my_input.index(item) - 1] == "L":
                    morse_code.pop()
                    morse_code.append(morse_dic["LJ"])
                else:
                    morse_code.append(morse_dic[item])
            elif item == "Ž":
                if my_input[my_input.index(item) - 1] == "D":
                    morse_code.pop()
                    morse_code.append(morse_dic["DŽ"])
                else:
                    morse_code.append(morse_dic[item])
            else:
                morse_code.append(morse_dic[item])
    my_output = ' '.join([str(letter) for letter in morse_code])
    text_output.insert(END, my_output)


button_morse = ttk.Button(widgets_frame, text="MORSE", command=morse_conversion, style="Accent.TButton")
button_morse.grid(column=4, row=2, padx=3)


# --- BINARY --- #

def binary_conversion():
    text_output.delete(0, END)
    my_input = text_input.get()
    binary_code = []
    with open("binary.json", encoding="utf8") as b:
        binary_dic = json.load(b)
        for item in my_input:
            if item == "J":
                if my_input[my_input.index(item) - 1] == "N":
                    binary_code.pop()
                    binary_code.append(binary_dic["NJ"])
                elif my_input[my_input.index(item) - 1] == "L":
                    binary_code.pop()
                    binary_code.append(binary_dic["LJ"])
                else:
                    binary_code.append(binary_dic[item])
            elif item == "j":
                if my_input[my_input.index(item) - 1] == "n":
                    binary_code.pop()
                    binary_code.append(binary_dic["nj"])
                elif my_input[my_input.index(item) - 1] == "l":
                    binary_code.pop()
                    binary_code.append(binary_dic["lj"])
                else:
                    binary_code.append(binary_dic[item])
            elif item == "Ž":
                if my_input[my_input.index(item) - 1] == "D":
                    binary_code.pop()
                    binary_code.append(binary_dic["DŽ"])
            elif item == "ž":
                if my_input[my_input.index(item) - 1] == "d":
                    binary_code.pop()
                    binary_code.append(binary_dic["dž"])
                else:
                    binary_code.append(binary_dic[item])
            else:
                binary_code.append(binary_dic[item])
    my_output = ' '.join([str(letter) for letter in binary_code])
    text_output.insert(END, my_output)


button_binary = ttk.Button(widgets_frame, text="BINARY", command=binary_conversion, style="Accent.TButton")
button_binary.grid(column=5, row=2, padx=3)

root.mainloop()
