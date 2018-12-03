# -*- coding: utf-8 -*-
import unittest

from gilded_rose_refactored import Item, GildedRose

class GildedRoseTest(unittest.TestCase):

    def test_lower_sellIn_value_items(self):
         items = [
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
            Item(name="Conjured Mana Cake", sell_in=1, quality=15),
        ]
         gilded_rose = GildedRose(items)
         gilded_rose.update_quality()
         gilded_rose.update_quality()
         newItemsValuesSellIn = [items[x].sell_in for x in range(9)]
         self.assertSequenceEqual([8, 0, 3, 0, -1, 13, 8, 3, -1], newItemsValuesSellIn)

    def test_quality_value_change(self):
        items = [
            Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
            Item(name="Aged Brie", sell_in=2, quality=0),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
            Item(name="Conjured Mana Cake", sell_in=1, quality=15),
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        newItemsValuesQuality = [items[x].quality for x in range(9)]
        self.assertSequenceEqual([19, 1, 6, 80, 80, 21, 50, 50, 13], newItemsValuesQuality)

    def test_quality_never_over_50_and_under_0(self):
        items = [
            Item(name="+5 Dexterity Vest", sell_in=10, quality=0),
            Item(name="Aged Brie", sell_in=2, quality=50),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=0),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=50),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=50),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=50),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=50),
            Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=-5, quality=0),
            Item(name="Conjured Mana Cake", sell_in=1, quality=0),
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        newItemsValuesQuality = [items[x].quality for x in range(9)]
        self.assertSequenceEqual([0, 50, 0, 50, 50, 50, 50, 0, 0], newItemsValuesQuality)

    def test_sulfuras_not_changes(self):
        items = [
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=10, quality=30),
            Item(name="Sulfuras, Hand of Ragnaros", sell_in=-3, quality=20),
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertSequenceEqual([10, 30, -3, 20], [items[0].sell_in, items[0].quality, items[1].sell_in, items[1].quality])


    def test_passes_quality_raise_stronger(self):
        items = [Item(name='Backstage passes to a TAFKAL80ETC concert', sell_in = 6, quality = 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual(15, items[0].quality)

    def test_once_the_sellIn_passed_quality_degrades_twice(self):
        items = [Item(name="Elixir of the Mongoose", sell_in=-1, quality=7)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        gilded_rose.update_quality()
        self.assertEqual(3, items[0].quality)

    def test_both_values_lower_next_day(self):
        items = [
            Item(name="+5 Dexterity Vest", sell_in=10, quality=10),
            Item(name="Elixir of the Mongoose", sell_in=5, quality=5),
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(9, items[0].sell_in)
        self.assertEquals(9, items[0].quality)
        self.assertEquals(4, items[1].sell_in)
        self.assertEquals(4, items[1].quality)

    def test_aged_brie_increases_in_quality(self):
        items = [
            Item(name="Aged Brie", sell_in=2, quality=30)
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(31, items[0].quality)

    def test_aged_brie_decreases_sellIn(self):
        items = [
            Item(name="Aged Brie", sell_in=2, quality=30)
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(1, items[0].sell_in)

    def test_mana_cake_quality_decreases_twice_before_sellIn(self):
        items = [
            Item(name="Conjured Mana Cake", sell_in=4, quality=15)
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(13, items[0].quality)

    def test_mana_cake_quality_decreases_four_times_after_sellIn(self):
        items = [
            Item(name="Conjured Mana Cake", sell_in=-1, quality=15)
        ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals(11, items[0].quality)

if __name__ == '__main__':
    unittest.main()
