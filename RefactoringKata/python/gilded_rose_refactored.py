# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_brie(self, item):
        if item.quality < 50:
            item.quality = item.quality + 1
        if item.sell_in < 0:
            if item.quality < 50:
                item.quality = item.quality + 1
        item.sell_in = item.sell_in - 1
    
    def update_passes(self, item):
        if item.sell_in >= 0 and item.quality < 50:
            item.quality = item.quality + 1
            if item.sell_in <= 10 and item.quality < 50:
                item.quality = item.quality + 1
                if item.sell_in <= 5 and item.quality < 50:
                    item.quality = item.quality + 1
        elif item.sell_in < 0:
            item.quality = 0
        item.sell_in = item.sell_in - 1

    def update_sulfuras(self, item):
        pass

    def update_cake(self, item):
        if item.quality > 1:
            item.quality = item.quality - 2
        elif item.quality == 1:
            item.quality = 0
        if item.sell_in < 0:
            if item.quality > 1:
                item.quality = item.quality - 2
            elif item.quality == 1:
                item.quality = 0
        item.sell_in = item.sell_in - 1

    def update_default(self, item):
        if item.quality > 0:
            item.quality = item.quality - 1
        if item.sell_in < 0:
            if item.quality > 0:
                item.quality = item.quality - 1
        item.sell_in = item.sell_in - 1


    def update_quality(self):
        for item in self.items:
            if item.name == 'Aged Brie':
                self.update_brie(item)
            elif item.name == 'Backstage passes to a TAFKAL80ETC concert':
                self.update_passes(item)
            elif item.name == 'Sulfuras, Hand of Ragnaros':
                self.update_sulfuras(item)
            elif item.name == 'Conjured Mana Cake':
                self.update_cake(item)
            else:
                self.update_default(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
