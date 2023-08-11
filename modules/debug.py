# -*- coding: utf-8 -*-

# --------------------------------------------
# Módulo de depuração do programa
# -------------------------------------------

# importando as bibliotecas necessárias
import folium
import json
import sys


def debug():
    while True:
        user_input = input("Enter command: ")
        if user_input == "stop":
            sys.exit("Stop here!")
        elif user_input == "pause":
            print("Paused. Press enter to continue.")
            input()
            return
        else:
            print("Write <stop> or <pause>")

    return


def pause():
    """
    FORTRANIC logical debugging.
    Just for fortranic beings.
    """
    programPause = input("Press the <ENTER> key to continue...")
    return


def stop():
    """
    FORTRANIC logical debugging.
    Just for fortranic beings.
    """
    sys.exit("Stop here!")
    return
