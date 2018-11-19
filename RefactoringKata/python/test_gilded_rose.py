# -*- coding: utf-8 -*-
import unittest

#from gilded_rose import Item, GildedRose
from refactored import Item, GildedRose

class GildedRoseTest(unittest.TestCase):

    def  test_sulfras_if_increase_quality(self):
        items = [
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=20)
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(21, items[0].quality)

    def test_sulfras_if_same_quality_over_50(self):
        items = [
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=10, quality=50)
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(50, items[0].quality)

    def test_sulfras_if_same_sellIn(self):
        items = [
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=20)
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEquals(-1, items[0].sell_in)

    

if __name__ == '__main__':
    unittest.main()
