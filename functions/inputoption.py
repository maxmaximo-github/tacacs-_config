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


def input_option():
    """
    Funcion es para crear la ventana de logeo.

    Crea una ventana que permite poner las credenciales de los dispositivos
    de capa 2 y 3.
    """
    try:
        while True:
            input_user = input(f"{green}Inserta un valor {red}>> {green}")

            if input_user.isnumeric():
                input_user = int(input_user)

                if input_user == 1:
                    break

                elif input_user == 2:
                    break

                else:
                    print(
                        f"{red}{input_user}{green}) {red}Opcion "
                        + f"{green}No {red}valida.{color_reset}\n")
                    # pass
                    continue

            else:
                print(f"Has ingresado {input_user}")
                print(f"Esta no es una opcion valida.")
                print(f"Intentalo nuevamente.")

    except KeyboardInterrupt:
        print(
            f"\n\n\t{red}Has detenido el {green}programa {red}con el teclado.")

    return input_user
