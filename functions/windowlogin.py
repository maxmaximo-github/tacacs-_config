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
__version__ = "0.1.5"
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
    Funcion es para crear la ventana de logeo.

    Crea una ventana que permite poner las credenciales de los dispositivos
    de capa 2 y 3.
    """
    directory = getcwd()

    username = username_entry.get()
    password = password_entry.get()
    secret = secret_entry.get()

    file = open(file=f"{directory}/tmp/dtusp.txt", mode="w")
    file.write(f"{username},{password},{secret}")
    file.close()

    logging.destroy()


def window_login():
    """
    Funcion para crear la pantalla de logeo.

    Esta funcion crea una ventana para introducir los datos de username,
    password y secret para ser enviados a los dispositivos cisco.
    """
    global logging, password_entry, secret_entry, username_entry

    directory = getcwd()

    logging = Tk()
    logging.geometry("275x500")
    logging.title(f"LOGIN ACCESS   v.{TkVersion}")
    logging.configure(background="white")

    image_file = PhotoImage(file=f"{directory}/images/lapiz.png")
    imagen_label = Label(logging, image=image_file, bg="white")
    imagen_label.pack()
    # imagen_label.place(x=65, y=190)

    Label(
         logging, text="Please enter login details", bg="white",
         font=("Helvtica", 15)).pack()

    Label(
         logging, text="for L2 and L3 devices.", bg="white",
         font=("Helvtica", 15)).pack()
    # grid(row=0, column=0)

    Label(
        logging, text="Username:", bg="white",
        font=("Helvtica", 15), fg="black").pack()
    # grid(row=1, column=0)

    username_entry = Entry(
            logging, bg="white",
            font=("Helvtica", 15))
    username_entry.pack()
    # username_entry.grid(row=2, column=0)

    Label(
        logging, text="Password:", bg="white",
        font=("Helvtica", 15), fg="black").pack()
    # grid(row=3, column=0)

    password_entry = Entry(
            logging, bg="white",
            font=("Helvtica", 15), show='●')
    password_entry.pack()
    # password_entry.grid(row=4, column=0)

    Label(
        logging, text="Secret:", bg="white",
        font=("Helvtica", 15), fg="black").pack()
    # grid(row=5, column=0)

    secret_entry = Entry(
            logging, bg="white",
            font=("Helvtica", 15), show='●')
    secret_entry.pack()
    # secret_entry.grid(row=6, column=0)

    login_button = Button(
            logging, command=data_user,
            text="Login", font=("Helvtica", 15))

    login_button.config()
    login_button.bind("<Return>", data_user)
    login_button.pack()
    # login_button.grid(row=7, column=0)

    logging.mainloop()
