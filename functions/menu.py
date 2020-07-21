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


def menu():
    """
    Funcion para crear la pantalla de logeo.

    Esta funcion crea una ventana para introducir los datos de username,
    password y secret para ser enviados a los dispositivos cisco.
    """
    try:
        print(f"{blue}Selectione una opcion")
        print(f"\t{red}1{green}) {red}Configuracion de {green}Tacacs+")
        print(f"\t{red}2{green}) {red}Salir")

    except KeyboardInterrupt as error:
        print("Terminaste la operacion", error)
