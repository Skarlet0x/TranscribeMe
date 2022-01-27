# --- IMPORTS --- ###

from tkinter import *
from tkinter import ttk
import json

# --- TO DO LIST --- #

# figure out the width on the entry widget
# or
# exchange it for a text widget

# look into the padding problem between buttons

# introduce a pic/logo

# introduce multiple tabs to keep different conversions open at the same time


# --- UI SETUP --- #


root = Tk()
root.call("source", r"C:\Users\Petra Bajac\PycharmProjects\themes\Forest Theme\forest-dark.tcl")
root.minsize(width=600, height=100)
root.config(padx=50, pady=50)
root.title("Converter")

ttk.Style().theme_use('forest-dark')

widgets_frame = ttk.Frame(root, padding=(0, 0, 0, 10))
widgets_frame.grid(row=0, column=1, padx=10, pady=(30, 10), sticky="nsew", rowspan=3)
widgets_frame.columnconfigure(index=0, weight=1)


# --- CANVAS & WIDGETS --- #


text_entry = ttk.Entry(widgets_frame, width=70)
text_entry.insert(0, "")
text_entry.grid(row=0, column=0, padx=5, pady=(0, 10), sticky="ew", columnspan=6)

text_output = ttk.Entry(widgets_frame, width=70)
text_output.insert(0, "")
text_output.grid(row=2, column=0, padx=5, pady=(10, 10), sticky="ew", columnspan=6)


# --- BUTTONS --- #

# --- FUTHARK --- #

def futhark_conversion():
    text_output.delete(0, END)
    my_input = text_entry.get().upper()
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
button_futhark.grid(column=0, row=1, padx=5)

# --- GLAGOLITIC --- #

def glagoljica_conversion():
    text_output.delete(0, END)
    my_input = text_entry.get().upper()
    glagoljica = []
    with open("glagoljica.json", encoding="utf8") as g:
        glagoljica_dic = json.load(g)
        for item in my_input:
            if item == "J":
                if my_input[my_input.index(item) - 1] == "N":
                    glagoljica.pop()
                    glagoljica.append(glagoljica_dic["NJ"])
                elif my_input[my_input.index(item) - 1] == "L":
                    glagoljica.pop()
                    glagoljica.append(glagoljica_dic["LJ"])
                else:
                    glagoljica.append(glagoljica_dic[item])
            elif item == "Ž":
                if my_input[my_input.index(item) - 1] == "D":
                    glagoljica.pop()
                    glagoljica.append(glagoljica_dic["DŽ"])
                else:
                    glagoljica.append(glagoljica_dic[item])
            else:
                glagoljica.append(glagoljica_dic[item])
    my_output = ' '.join([str(letter) for letter in glagoljica])
    text_output.insert(END, my_output)

button_glagolitic = ttk.Button(widgets_frame, text="GLAGOLITIC", command=glagoljica_conversion, style="Accent.TButton")
button_glagolitic.grid(column=1, row=1, padx=5)

# --- CYRILLIC --- #

def cirilica_conversion():
    text_output.delete(0, END)
    my_input = text_entry.get()
    cirilica = []
    with open("cirilica.json", encoding="utf8") as c:
        cirilica_dic = json.load(c)
        for item in my_input:
            if item == "J":
                if my_input[my_input.index(item) - 1] == "N":
                    cirilica.pop()
                    cirilica.append(cirilica_dic["NJ"])
                elif my_input[my_input.index(item) - 1] == "L":
                    cirilica.pop()
                    cirilica.append(cirilica_dic["LJ"])
                else:
                    cirilica.append(cirilica_dic[item])
            elif item == "Ž":
                if my_input[my_input.index(item) - 1] == "D":
                    cirilica.pop()
                    cirilica.append(cirilica_dic["DŽ"])
            elif item == "j":
                if my_input[my_input.index(item) - 1] == "n":
                    cirilica.pop()
                    cirilica.append(cirilica_dic["nj"])
                elif my_input[my_input.index(item) - 1] == "l":
                    cirilica.pop()
                    cirilica.append(cirilica_dic["lj"])
                elif my_input[my_input.index(item) - 1] == "L":
                    cirilica.pop()
                    cirilica.append(cirilica_dic["LJ"])
                elif my_input[my_input.index(item) - 1] == "N":
                    cirilica.pop()
                    cirilica.append(cirilica_dic["NJ"])
                else:
                    cirilica.append(cirilica_dic[item])
            elif item == "ž":
                if my_input[my_input.index(item) - 1] == "d":
                    cirilica.pop()
                    cirilica.append(cirilica_dic["dž"])
                elif my_input[my_input.index(item) - 1] == "D":
                    cirilica.pop()
                    cirilica.append(cirilica_dic["DŽ"])
                else:
                    cirilica.append(cirilica_dic[item])
            else:
                cirilica.append(cirilica_dic[item])
    my_output = ' '.join([str(letter) for letter in cirilica])
    text_output.insert(END, my_output)

button_cyrillic = ttk.Button(widgets_frame, text="CYRILLIC", command=cirilica_conversion, style="Accent.TButton")
button_cyrillic.grid(column=2, row=1, padx=5)

# --- NATO --- #

def nato_conversion():
    text_output.delete(0, END)
    my_input = text_entry.get().upper()
    nato_code = []
    with open("nato.json", encoding="utf8") as n:
        nato_dic = json.load(n)
        for item in my_input:
            nato_code.append(nato_dic[item])
    my_output = ' '.join([str(letter) for letter in nato_code])
    text_output.insert(END, my_output)

button_nato = ttk.Button(widgets_frame, text="NATO", command=nato_conversion, style="Accent.TButton")
button_nato.grid(column=3, row=1)

# --- MORSE --- #

def morse_conversion():
    text_output.delete(0, END)
    my_input = text_entry.get().upper()
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
button_morse.grid(column=4, row=1, padx=5)

# --- BINARY --- #

def binary_conversion():
    text_output.delete(0, END)
    my_input = text_entry.get()
    binary = []
    with open("binary.json", encoding="utf8") as b:
        binary_dic = json.load(b)
        for item in my_input:
            if item == "J":
                if my_input[my_input.index(item) - 1] == "N":
                    binary.pop()
                    binary.append(binary_dic["NJ"])
                elif my_input[my_input.index(item) - 1] == "L":
                    binary.pop()
                    binary.append(binary_dic["LJ"])
                else:
                    binary.append(binary_dic[item])
            elif item == "j":
                if my_input[my_input.index(item) - 1] == "n":
                    binary.pop()
                    binary.append(binary_dic["nj"])
                elif my_input[my_input.index(item) - 1] == "l":
                    binary.pop()
                    binary.append(binary_dic["lj"])
                else:
                    binary.append(binary_dic[item])
            elif item == "Ž":
                if my_input[my_input.index(item) - 1] == "D":
                    binary.pop()
                    binary.append(binary_dic["DŽ"])
            elif item == "ž":
                if my_input[my_input.index(item) - 1] == "d":
                    binary.pop()
                    binary.append(binary_dic["dž"])
                else:
                    binary.append(binary_dic[item])
            else:
                binary.append(binary_dic[item])
    my_output = ' '.join([str(letter) for letter in binary])
    text_output.insert(END, my_output)

button_binary = ttk.Button(widgets_frame, text="BINARY", command=binary_conversion, style="Accent.TButton")
button_binary.grid(column=5, row=1, padx=5)

root.mainloop()
