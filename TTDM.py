#! python3
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mtgtools.MtgDB import MtgDB
from mtgtools.PCardList import PCardList
from mtgtools.PSetList import PSetList
from PIL import Image
import os
from shutil import copyfile

mtg_db = MtgDB('my_db.fs')
cards = mtg_db.root.scryfall_cards 
sets = mtg_db.root.scryfall_sets 

deckname = input('What is this deck\'s name? ')
IN = open('deck.txt')

rawtext = IN.read()
print(rawtext)
muhdeck = cards.from_str(rawtext)
splits = muhdeck.where(layout = 'split')
for x in range(0,len(splits)):
    splits[x].name = splits[x].name.split('//')[0]
    #print(splits[x].name)
IN.close()

muhdeck.download_images_from_scryfall('normal', ('Decklist\\'+ deckname + '\\'))  #04x card xyz --- makes card 4 times

#Renamer:

for filename in os.listdir(os.path.join('Decklist', deckname)):
    amtofcard = len(muhdeck.where_exactly(name=filename[0:len(filename)-4]))
    if amtofcard==0:
        newname = '01x ' + filename
    else:
        newname = str(amtofcard).zfill(2) + 'x ' + filename
    
    os.rename(os.path.join('Decklist', deckname, filename), os.path.join('Decklist', deckname, newname))
copyfile('00 Back.jpg', os.path.join('Decklist', deckname, '00 Back.jpg'))
