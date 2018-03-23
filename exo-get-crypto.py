#!/usr/bin/env python3.5
#-*- coding: utf-8 -*-

import cryptocompare

while True:
    curr = ['USD']
    inp = input ("\nBonjour veuillez choisir votre fonctionalitée \nEntrez : \n 1: Liste des cryptomonnaies\n 2: Prix de la cryptomonnaie désirée\n 3: Quitter le programme\n> ")

    if inp == '1':
        crypto_list = cryptocompare.get_coin_list(format=True)
        for liste in crypto_list:
            print(liste)
    elif inp == '2':
        mon = input("Entrez le nom de votre cryptomonnaie :\n")
        print(cryptocompare.get_price(mon, curr))
    elif inp == '3':
        exit()
    else:
        print("Une Erreur est survenue veuillez rééssayer\n")
