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


from ipaddress import IPv4Address
from ipaddress import IPv6Address
from ipaddress import AddressValueError
from nmap import PortScanner
from functions.cleanscreen import CleanScreen


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


def TacacsIPValidation():
    """
    Funcion para validar IPv4 del servidor tacacs.

    Esta funcion valida que el ingreso de la direccion IPv4 del servidor Tacacs
    sea correcto.
    """
    while True:
        ip_tacacs = input(
            f" \n{red}Ingresa la {blue}direccion {green}IPv4 {red}del"
            + f" {green}Servidor Tacacs+ {red}>> {green}")

        if ":" in ip_tacacs:
            try:
                IPv6Address(ip_tacacs)
                return ip_tacacs
                break

            except AddressValueError:
                print("No es una IPv6 valida.")
                continue

        elif "." in ip_tacacs:
            try:
                IPv4Address(ip_tacacs)
                return ip_tacacs
                break

            except AddressValueError:
                print("No es una IPv4 valida.")
                continue

        else:
            print(f"{ip_tacacs} no es una direccion valida.")


def TacacsPort(ip_tacacs):
    """
    Funcion para definir el puerto tacacs.

    Esta funcion permite determinar si se desea cambiar el numero de puerto
    al servidor tacacs.
    """
    try:
        while True:
            CleanScreen()

            # Print Data Input on terminal
            print(f" {blue}{'='*45}{color_reset}")
            print(
                f"{' '*4}{green}{'DATA INPUT':^35} ")
            print(f" {blue}{'='*45}{color_reset}")
            print(
                f"{' '*4}{green}{'Tacacs Server IPv4'} {red}==> "
                + f" {green}{ip_tacacs}")
            print(f" {blue}{'='*45}{color_reset}")

            print(
                f"\n\n {green}Tacacs+ {blue}opera en el {red}puerto"
                + f" {green}49/tcp {blue}por {green}default.")

            condicion = input(
                f" {blue}Deseas {red}configurar un {blue}Numero de"
                + f" {green}puerto {red}diferente: {green}y/n {red}>> {green}")

            if condicion == "y":
                while True:
                    tacacsport_inputuser = input(
                        f"\nIngresa el numero del puerto: ")

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
    if ":" in ip_tacacs:
        version = "-6"

    else:
        version = "-4"

    try:
        nmap = PortScanner()
        nmap.scan(
            hosts=ip_tacacs, arguments=f"{version} -p {tacacsport_inputuser}")
        port_up = nmap[ip_tacacs].has_tcp(tacacsport_inputuser)

        print(port_up)

        if port_up is True:
            print(
                f"El servidor {ip_tacacs} tiene el puerto"
                + f"{tacacsport_inputuser} activo."
                )
            return tacacsport_inputuser

        else:
            print(
                f" El puerto {tacacsport_inputuser} que has elegido para el")
            print(f" servidor Tacacs con ip {ip_tacacs}")
            print(f" no se encuentra activo.")

    except KeyboardInterrupt:
        print(
            f"\n\n\t{red}Has detenido el {green}programa {red}con el teclado.")
