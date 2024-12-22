# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import configparser
import os

def print_f():
    #setup
    old_file_array = []
    new_file_arr = []
    old_config = configparser.ConfigParser()
    new_config = configparser.ConfigParser()
    #ole file 1
    old_config.read('old_file.ini')
    for key in old_config.sections():
        for key2 in old_config[key]:
            old_file_array.append(key2)

    #new file to merge
    new_config.read('new_file.ini')
    for key in new_config.sections():
        for key2 in new_config[key]:
            new_file_arr.append(key2)

    #sections
    sections= [];
    for section in new_config.sections():
        sections.append(section)

    old_file_array.sort()
    new_file_arr.sort()
    elements_ajoutes = list(set(new_file_arr) - set(old_file_array))
    elements_supprimes = list(set(old_file_array) - set(new_file_arr))
    #print(old_file_array)
    #print(new_file_arr)
    print('Nouveaux éléments : %s' % (elements_ajoutes))
    print('Éléments supprimés : %s' % (elements_supprimes))

    nouvelles_lignes_arr = []
    print("\n-------------------------------- NOUVELLES LIGNES --------------------------------")
    for section in sections:
        for elem in elements_ajoutes:
            print('%s=%s' % (elem, new_config.get(section, elem)))
            nouvelles_lignes_arr.append(elem + "=" + new_config.get(section, elem))

    try:
        os.remove("output.ini")
    except:
        print("Pas de fichier output existant. \n")
    file = open("output.ini", "x")
    #remise à zéro du fichier
    file.write("")
    for line in nouvelles_lignes_arr:
        file.write("".join(line) + "\n")

    print("\nFichier output.txt créé")
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_f()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
