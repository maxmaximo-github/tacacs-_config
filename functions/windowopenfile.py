#!/usr/bin/env  python3
# -*- coding: utf-8 -*-
"""
This script is for configuration Tacacs+ service on Cisco Devices.

It seems that it has to have THIS docstring with a summary line, a blank line
and sume more text like here. Wow.
"""
__author__ = "Cesar Rodriguez"
__copyright__ = "Copyright 2020"
__credits__ = ["Cesar Rodriguez"]
__license__ = "GPL"
__version__ = "0.1.5"
__maintainer__ = "Cesar Rodriguez"
__email__ = "cesarrodriguezpadilla@gmail.com"
__status__ = "Development"


from os import getcwd
from tkinter import Tk
from tkinter import filedialog


def window_openfile():
    """
    Funcion para abrir archivo.

    Esta funcion crea una ventana para abrir un archivo de texto
    """
    openfile = Tk()
    openfile.title("Open Device IP file.")
    openfile.withdraw()

    directory = getcwd()

    filename = filedialog.askopenfilename(
                        initialdir=f"{directory}/devices",
                        title="Select a File",
                        filetypes=(
                            ("txt files", "*.txt"), ("all files", "*.*"))
                        )

    openfile.destroy()

    device_list = []
    for line in open(file=filename, mode="r"):
        line = line.strip("\n")
        device_list.append(line)

    return device_list
