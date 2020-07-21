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


from nmap import PortScanner
from functions.cleanscreen import clean_screen


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


def TacacsPort(ip_tacacs):
    """
    """
    try:

        print("Tacas opera en el puerto 49/tcp por default")
        condicion = input("Deseas configurarlo otro No. puerto: y/n")

        while True:
            if condicion == "y":
                while True:
                    port_tacacs = input("Ingresa el numero del puerto: ")

                    if port_tacacs.isnumeric():
                        port_tacacs = int(port_tacacs)
                        break
                    else:
                        print(
                            "La entrada es incorrecta. Escribe un numero "
                            + " entero.")
                        continue

                if 0 < port_tacacs < 65536:
                    break

                else:
                    print("El puerto esta fuera del rango permitido")
                    continue

            elif condicion == "n":
                port_tacacs = 49
                break

            else:
                print("Has selecionado una opcion no valida.")

                continue
    except KeyboardInterrupt:
        print(
            f"\n\n\t{red}Has detenido el {green}programa {red}con el teclado.")

    return port_tacacs
