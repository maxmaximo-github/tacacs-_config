#!/usr/bin/env  python3
"""
This script is create for ping IPv4.

It seems that it has to have THIS docstring with a summary line, a blank line
and sume more text like here. Wow.
"""
__author__ = "Cesar Rodriguez"
__copyright__ = "Copyright 2020"
__credits__ = ["Cesar Rodriguez"]
__license__ = "GPL"
__version__ = "1.5.2"
__maintainer__ = "Cesar Rodriguez"
__email__ = "cesarrodriguezpadilla@gmail.com"
__status__ = "Development"


from os import getcwd
from tkinter import Button
from tkinter import Entry
from tkinter import Label
from tkinter import PhotoImage
from tkinter import Tk
from tkinter import TkVersion


def data_user(event=None):
    """
    Funcion para testear IPv4.

    Esta funcion realiza el testeo de Ping.

    Si el resultado es exitoso se guarda en un archivo de texto, de no ser asi
    sino solo se anuncia que no tiene conectividad.
    """
    directory = getcwd()

    username = username_entry.get()
    password = password_entry.get()
    secret = secret_entry.get()

    file = open(file=f"{directory}/tmp/dtusp.txt", mode="w")
    file.write(f"{username},{password},{secret}")
    file.close()

    logging.destroy()


def motion(event):
    logging.destroy()
    return


def login_screen():
    """
    Funcion para testear IPv4.

    Esta funcion realiza el testeo de Ping.

    Si el resultado es exitoso se guarda en un archivo de texto, de no ser asi
    sino solo se anuncia que no tiene conectividad.
    """
    global logging, password_entry, secret_entry, username_entry

    directory = getcwd()

    logging = Tk()
    logging.geometry("275x350")
    logging.title(f"LOGIN ACCESS   v.{TkVersion}")
    logging.configure(background="white")

    image_file = PhotoImage(file=f"{directory}/images/lapiz.png")
    imagen_label = Label(logging, image=image_file, bg="white")
    imagen_label.place(x=65, y=190)

    # Label(
    #     logging, text="Please enter login details", bg="white",
    #     font=("Helvtica", 15)).grid(row=0, column=0)

    Label(
        logging, text="Username:", bg="white",
        font=("Helvtica", 15), fg="red").grid(row=1, column=0)

    username_entry = Entry(
            logging, bg="white",
            font=("Helvtica", 15))
    username_entry.grid(row=2, column=0)

    Label(
        logging, text="Password:", bg="white",
        font=("Helvtica", 15), fg="red").grid(row=3, column=0)

    password_entry = Entry(
            logging, bg="white",
            font=("Helvtica", 15), show='●')
    password_entry.grid(row=4, column=0)

    Label(
        logging, text="Secret:", bg="white",
        font=("Helvtica", 15), fg="red").grid(row=5, column=0)

    secret_entry = Entry(
            logging, bg="white",
            font=("Helvtica", 15), show='●')
    secret_entry.grid(row=6, column=0)

    login_button = Button(
            logging, command=data_user,
            text="Login", font=("Helvtica", 15))

    login_button.config()
    login_button.bind("<Return>", data_user)
    login_button.grid(row=7, column=0)

    logging.mainloop()
