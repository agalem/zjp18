# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def manage_aged_brie(self, item):
        #I've ignored sell in in this class -> don't sure about that
        if item.name == "Aged Brie":
            #additional behaviour
            if item.sell_in <= 10:
                if item.quality < 50:
                    item.quality = item.quality + 1
            if item.sell_in <= 5:
                if item.quality < 50:   
                    item.quality = item.quality + 1

            #default behaviour when quality < 50    
            if item.quality < 50:
                item.quality = item.quality + 1

   
    def manage_backstage_passes(self, item):
        if item.name == "Backstage passes to a TAFKAL80ETC concert":
            #decrease to 0 after concert
            if item.sell_in < 0:
                item.quality = 0
            #still before concert
            else:
                if item.sell_in <= 10:
                    if item.quality < 50:
                        item.quality = item.quality + 1
                if item.quality <= 5:
                    if item.quality < 50:
                        item.quality = item.quality + 1

                #default behaviour
                if item.quality < 50:
                    item.quality = item.quality + 1


    def manage_sulfuras(self, item):
        if item.name == "Sulfuras, Hand of Ragnaros":
            #never has to be sold -> ignore sell_in
            if item.quality < 50:
                item.quality = item.quality + 1

    def manage_conjured(self, item):
        if item.sell_in < 0:
            if item.quality > 3:
                item.quality = item.quality - 4
            else:
                item.quality = 0
        else:
            if item.quality > 0:
                item.quality = item.quality - 1

    def manage_default_item(self, item):
        if item.sell_in < 0:
            if item.quality > 1:
                item.quality = item.quality - 2
            else:
                item.quality = 0
        else:
            if item.quality > 0:
                item.quality = item.quality - 1

    def update_quality(self):
        for item in self.items:

            #magane sell in value
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            
            #call appropriate functions
            if item.name == "Aged Brie":
                self.manage_aged_brie(item)
            elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                self.manage_backstage_passes(item)
            elif item.name == "Sulfuras, Hand of Ragnaros":
                self.manage_sulfuras(item)
            elif item.name ==  "Conjured Mana Cake":
                self.manage_conjured(item)
            else:
                #default item
                self.manage_default_item(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
