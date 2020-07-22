#!/usr/bin/env python3

import sys
import csv
import textwrap

def long_print(text):
    "This function ensures text wrapping of long print statements"
    text = text.replace(r'\n','\n')
    #turns '\\n' into '\n' for str.split
    text_list = text.split('\n')
    for line in text_list:
        print(textwrap.fill(line,110))
    #paragraphs are split into a list of strings to ensure proper wrapping
    return


def class_decoder(class_str):
    "This function replaces the class abreviations in the CSV with the full names"
    class_list_short = ['A','B','C','D','P','R','S','W','Z']
    class_list_long = ['Artificer','Bard','Cleric','Druid',
                       'Paladin','Ranger','Sorcerer','Warlock',
                       'Wizard']
    for long, short in zip(class_list_long,class_list_short):
        class_str = class_str.replace(short,long)
    return class_str

def print_spell(dict):
    "This function prints a formatted spell"
    print('\n')
    print(dict['Name_Ritual'])
    print(dict['Book_Page'])
    print(dict['Level_School'])
    print('Casting Time: ' + dict['Cast_Time'])
    print('Components: ' + dict['Components'] + ' ' + dict['Materials'])
    print('Range: ' + dict['Range'])
    print('Duration: ' + dict['Duration'])
    print('Classes: ' + class_decoder(dict['Classes'] + '\n'))
    long_print(dict['Description_Higher_Levels'])
    return

def spell_search(spell_list):
    while(1):
        long_print("\n Type the name of the spell you're searching for, or the index if you know it. To go back enter 'q'")
        search = input()
        if(search == 'q'):
            return
        if search.isdigit():
            spell = spell_list[int(search)]
            print_spell(spell)
            #if input a spell index pass the dictionary containing the spell to the spell print func
        else:
            print('\n')
            for spell in spell_list:
                spell_name = spell['Name_Ritual'].lower()
                if(spell_name.find(search.lower()) > -1):
                    print(spell['Name_Ritual'] + ', index '  + spell['Index'])
            #else search the dictionaries for a matching spell

def class_list(spell_list,long):
    while(1):
        print('What class are you searching (A,B,C,D,P,R,S,W,Z)? Input q to quit')
        dnd_class = input()
        if dnd_class == 'q':
            return
        first_lvl = int(input('What is the first spell level you would like to look for?'))
        last_lvl = int(input('What the last spell level you would like to look for?'))
        lvl_range = range(first_lvl,last_lvl+1)
        for lvl in lvl_range:
            print(lvl)
            for spell in filter(lambda spell: int(spell['Level']) == lvl, spell_list):
                #only output the lvls selected by the user
                if(spell['Classes'].find(dnd_class) > -1):
                    #print the full spell if long == True which is determined by the user before calling
                    if(long):
                        print_spell(spell)
                    else:
                        print(spell['Name_Ritual'] + ', index '  + spell['Index'])
    return

def main():
    #generates list of dictionaries from the csv file for searching
    with open('dnd_5e_spells.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        spell_list=[]
        for row in reader:
            spell_list.append(row)
    #search function
    while(1):
        #until quit char breaks the loop will search indefinitely
        long_print("\nIf you're searching for a specic spell input 'search'."
                   + " If you want a list of class's spell enter 'class_list'." 
                   + " To do the same with spell descriptions enter 'class_print'." 
                   + " To exit the program enter 'q'.")
        search = input()
        search = search.lower()
        #putting search term to lower case for comparisons
        if(search == 'q'):
            return
        elif(search == 'search'):
            spell_search(spell_list)
        elif(search == 'class_list'):
            class_list(spell_list,False)
        elif(search == 'class_print'):
            class_list(spell_list,True)
        else:
            print("Sorry I don't know what you mean")

if __name__ == "__main__":
    main()
