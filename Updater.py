#! python3
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mtgtools.MtgDB import MtgDB

mtg_db = MtgDB('my_db.fs')
cards = mtg_db.root.scryfall_cards 
sets = mtg_db.root.scryfall_sets

mtg_db.full_update_from_scryfall()

