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
# from functions.cleanscreen import clean_screen


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
    Funcion para definir el puerto tacacs.

    Esta funcion permite determinar si se desea cambiar el numero de puerto
    al servidor tacacs.
    """
    try:
        while True:
            # clean_screen()
            print(
                f"\n{green}Tacacs+ {blue}opera en el {red}puerto {green}49/tcp"
                + f" {blue}por {green}default.\n")

            condicion = input(
                f"{blue}Deseas {red}configurar un {blue}Numero de"
                + f" {green}puerto {red}diferente: {green}y/n {red}>> {green}")

            if condicion == "y":
                while True:
                    tacacsport_inputuser = input(
                        f"Ingresa el numero del puerto: ")

                    if tacacsport_inputuser.isnumeric():
                        tacacsport_inputuser = int(tacacsport_inputuser)
                        break
                    else:
                        print(
                            "La entrada es incorrecta. Escribe un numero "
                            + " entero.")
                        continue

                if 0 < tacacsport_inputuser < 65536:
                    break

                else:
                    print("El puerto esta fuera del rango permitido")
                    continue

            elif condicion == "n":
                tacacsport_inputuser = 49
                break

            else:
                print("Has selecionado una opcion no valida.\n\n\n")
                continue

    except KeyboardInterrupt:
        print(
            f"\n\n\t{red}Has detenido el {green}programa {red}con el teclado.")

    return tacacsport_inputuser


def TacacsTest(ip_tacacs, tacacsport_inputuser):
    """
    Funcion para definir el puerto tacacs.

    Esta funcion permite determinar si se desea cambiar el numero de puerto
    al servidor tacacs.
    """
    try:
        nmap = PortScanner()
        nmap.scan(ip_tacacs, f"22-443, {tacacsport_inputuser}")
        port_up = nmap[ip_tacacs].has_tcp(tacacsport_inputuser)

        if port_up is True:
            print(
                f"El servidor {ip_tacacs} tiene el puerto"
                + f"{tacacsport_inputuser} activo."
                )
            return tacacsport_inputuser

        else:
            print(
                f"El puerto {tacacsport_inputuser} que has elegido para"
                + f" el servidor Tacacs con ip {ip_tacacs}"
                + f" no se encuentra activo."
                )

    except KeyboardInterrupt:
        print(
            f"\n\n\t{red}Has detenido el {green}programa {red}con el teclado.")
