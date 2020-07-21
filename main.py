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


# Call functions
from functions.createtmpfolder import create_tmpfolder
from functions.cleanscreen import clean_screen
from functions.inputoption import input_option
from functions.menu import menu
from functions.tacacsport import TacacsPort
from functions.windowlogin import window_login
from functions.windowopenfile import window_openfile


# Colores para impresion en pantalla.
color_reset = "\x1b[0m"
red = "\x1b[00;00;1;031m"
red_blink = "\x1b[00;00;05;031m"
magent = "\x1b[00;00;02;033m"
magent_blink = "\x1b[00;00;05;033m"
blue = "\x1b[00;00;1;034m"
blue_blink = "\x1b[00;00;5;034m"
green = "\x1b[00;00;01;092m"
green_blink = "\x1b[00;00;5;092m"


def main():
    """
    Funcion Principal.

    Esta funcion llama a las demas funciones de la carpeta 'functions'.
    """
    # Verificar si existe carpeta tmp dentro del proyecto
    create_tmpfolder()

    # Limpiar pantalla
    clean_screen()

    # Llamada a la funcion menu
    menu()

    try:

        input_user = input_option()

        if input_user == 1:

            ip_tacacs = input(
                f"ingresa la direccion IP del Servidor Tacacs: ")

            port_tacacs = TacacsPort(ip_tacacs)
            print(port_tacacs)

            device_list = window_openfile()
            print(device_list)

            window_login()

        else:
            print("\n")

    except KeyboardInterrupt:
        print(
            f"\n\n\t{red}Has detenido el {green}programa {red}con el teclado.")

    except UnboundLocalError:
        print()

    finally:
        print(f"{green}{'Fin del programa':^60}{color_reset}\n")
        print(f" {red}{'*'*66}")
        print(
            f"      {blue}Desarrollado y mantenido"
            + f" por: {green}Ing. {__author__}")
        print(f"\t    {blue}Contacto: {green}{__email__}")
        print(f"\t\t        {blue}Version: {green}{__version__}")
        print(f" {red}{'*'*66}{color_reset}\n\n")


if __name__ == '__main__':
    main()
