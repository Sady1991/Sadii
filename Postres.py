#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time

def limpiar():
    os.system("clear")

def pausa():
    input("\nPresiona ENTER para continuar...")

def mostrar_ascii():
    print(r"""
   _____           _       
  / ____|         | |      
 | (___   __ _  __| |_   _ 
  \___ \ / _` |/ _` | | | |
  ____) | (_| | (_| | |_| |
 |_____/ \__,_|\__,_|\__, |
                      __/ |
                     |___/ 
    """)

def abrir_archivo(ruta):
    limpiar()
    print(f"Abriendo archivo:\n{ruta}\n")

    if os.path.exists(ruta):
        os.system(f'cat "{ruta}"')
    else:
        print("El archivo no existe.")

    pausa()

while True:
    limpiar()
    mostrar_ascii()

    print("===== MENU PRINCIPAL =====")
    print("1. Tiramizu")
    print("2. Chocotorta")
    print("3. Chocoflan")
    print("4. Salir")

    opcion = input("\nSelecciona una opcion: ")

    if opcion == "1":
        abrir_archivo("/storage/emulated/0/Postres/Tiramizu.txt")

    elif opcion == "2":
        abrir_archivo("/storage/emulated/0/Postres/Chocotorta.txt")

    elif opcion == "3":
        abrir_archivo("/storage/emulated/0/Postres/Chocoflan.txt")

    elif opcion == "4":
        print("\nSaliendo de Termux...")
        time.sleep(1)
        break

    else:
        print("\nOpcion Errada!!!!")
        pausa()