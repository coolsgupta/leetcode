from typing import List

class Inventory:
    items: List[Item] = []   # in our current game design, each item is either a quest item or a normal item
    quest_items: List[Item] = []   # for convenience, a subset of items, containing only quest items
    normal_items: List[Item] = []   # for convenience, a subset of items, containing only normal items

    # the user interface will display the last item we picked up
    lastItemCollected: Item = None

    def Last_Item_Collected(self) -> Item:
        return self.lastItemCollected

    def get_item(self, i: Item, quantity: int):
        for x in range(quantity):
            self.items.append(i)
            if i.Is_Quest_Item():
                self.quest_items.append(i)
            else:
                self.normal_items.append(i)
        AchievementSystem.instance.Did_Modify_Item("gain", i.identifier, quantity)
        self.lastItemCollected = i

    def lose_item(self, i: Item, quantity: int):
        for x in range(quantity):
            self.items.remove(i)
            if i.Is_Quest_Item():
                self.quest_items.remove(i)
            else:
                self.normal_items.remove(i)
        AchievementSystem.instance.Did_Modify_Item("lose", i.identifier, quantity)

    def didpickupitem(self, i: Item):
        self.lastItemCollected = i