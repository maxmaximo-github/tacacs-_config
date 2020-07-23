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

from os import name
from os import popen
from subprocess import call
from subprocess import STDOUT
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


def TacacsIPAlive(ip_tacacs):
    """
    Funcion para verificar que si esta vivo el servidor tacacs.

    Esta realiza un testeo de ping a la direccion ingresada por el usuario.
    """
    if name == "nt":
        reply = popen(f"ping ip -n 4").read()

        if "Received = 4" and "Approximate" in reply:
            return True
        else:
            return False

    else:
        reply = call(
            f"ping -c 3 {ip_tacacs}",
            shell=True,
            stdout=open("/dev/null", "w"),
            stderr=STDOUT)

        if reply != 0:
            print("No puede ser comprobada la conectividad con el servidor")
            return False
        else:
            return True


def TacacsIPValidation():
    """
    Funcion para validar IPv4 del servidor tacacs.

    Esta funcion valida que el ingreso de la direccion IPv4 del servidor Tacacs
    sea correcto.
    """
    while True:
        ip_tacacs = input(
            f" \n{red}Ingresa la {blue}direccion {green}IPv4{red}/{green}v6"
            + f" {red}del {green}Servidor Tacacs+ {red}>> {green}")

        if ":" in ip_tacacs:
            try:
                IPv6Address(ip_tacacs)
                ping_validation = TacacsIPAlive(ip_tacacs)

                return ip_tacacs, ping_validation
                break

            except AddressValueError:
                print(
                    f"{green}{ip_tacacs} {red}no es una"
                    + f" {green}IPv6 {red}valida.")
                continue

        elif "." in ip_tacacs:
            try:
                IPv4Address(ip_tacacs)
                ping_validation = TacacsIPAlive(ip_tacacs)

                return ip_tacacs, ping_validation
                break

            except AddressValueError:
                print(
                    f"{green}{ip_tacacs} {red}no es una"
                    + f" {green}IPv4 {red}valida.")
                continue

        else:
            print(f"{ip_tacacs} no es una direccion valida.")


def TacacsPort(ip_tacacs, ping_validation):
    """
    Funcion para definir el puerto tacacs.

    Esta funcion permite determinar si se desea cambiar el numero de puerto
    al servidor tacacs.
    """
    # List of possible input of user
    list_yes = [
        "y", "ye", "yes",
        "Y", "YE", "YES",
        "YEs", "YeS", "Yes",
        ]
    list_no = [
        "n", "no", "non",
        "none", "N", "No",
        "NO", "None", "NONE"
        ]

    try:
        if not ping_validation:
            print(
                f"No pudo comprobarse la conectividad "
                + f"de ping con {ip_tacacs}.")
            confirmation_err = input("Deseas continuar y/n: ")
            # Determinar si concide una condicion de la lista "list_yes"
            if confirmation_err in list_yes:
                ciclo = True
                response = "Ping Fail"
            else:
                ciclo = False

        else:
            ciclo = True
            response = "Ping Success"

        invalid_option = ""
        while ciclo:

            CleanScreen()

            # Verificar si validacion es cierto para determinar si se desea
            # continuar con la ejecucion del programa un que no se tenga
            # conectividad Ping
            """
            if ping_validation:
                response = "Ping Sucess"
                pass

            else:
                if not response:
                    print(response)
                    print(
                        f"No pudo comprobarse la conectividad de "
                        + f"ping con {ip_tacacs}.")
                    confirmation_err = input(
                        "Deseas continuar de todos modos y/n: ")

                    if confirmation_err in list_yes:
                        response = "Ping Fail"
                        pass

                    else:
                        break
                else:
                    response = "Ping Fail"
            """

            # Print Data Input on terminal
            print(f" {blue}{'='*65}{color_reset}")
            print(
                f"{' '*4}{green}{'DATA INPUT':^35} {red}{'==>'} "
                + f" {green}{'TEST':>10}")
            print(f" {blue}{'='*65}{color_reset}")
            print(
                f"{' '*4}{green}{'Tacacs Server IPv4'} {red}==> "
                + f" {green}{ip_tacacs} {red}==> "
                + f"{blue}({green}{response}!!!!{blue})")
            print(f" {blue}{'='*65}{color_reset}")

            # Mensaje de error si es que ingreso un dato incorrecto
            if invalid_option:
                print(
                    f"\n \t {green_blink}{invalid_option}"
                    + f" {red}no es una opcion valida.\n")
            else:
                print("\n")

            # Message for user in screen
            print(
                f" {green}Tacacs+ {blue}opera en el {red}puerto"
                + f" {green}49/tcp {blue}por {green}default.")

            confirmation = input(
                f" {blue}Deseas {red}configurar un {blue}Numero de"
                + f" {green}puerto {red}diferente: {green}y/n {red}>> {green}")

            if confirmation in list_yes:
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

            elif confirmation in list_no:
                tacacsport_inputuser = 49
                break

            else:
                print("Has selecionado una opcion no valida.\n\n\n")
                invalid_option = confirmation
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

    except KeyError:
        CleanScreen()
        print(
            f" No se ha podido establer conexion con el servidor")
