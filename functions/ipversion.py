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


def IPTypeVersion(ip):
    """
    Funcion para determinar que version de protocolo IP es la direccion.

    Esta funcion determina que tipo de version es la IP que se esta
    inyectando
    """
    if ":" in ip:
        version = "6"

    else:
        version = "4"

    return version
