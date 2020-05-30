lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

trashed_helmet = 0
trashed_sword = 0
trashed_shield = 0
armor_repair_required = False
trashed_armor = 0

for lost_fight in range(1, lost_fights +1):
    if lost_fight % 2 == 0:
        trashed_helmet += 1
    if lost_fight % 3 == 0:
        trashed_sword += 1
    if lost_fight % 2 == 0 and lost_fight % 3 == 0:
        trashed_shield += 1
        armor_repair_required = True
    if trashed_shield % 2 == 0 and trashed_shield > 0 and armor_repair_required:
        trashed_armor += 1
        armor_repair_required = False

expenses = trashed_helmet * helmet_price + trashed_sword * sword_price + trashed_shield * shield_price + trashed_armor * armor_price
print(f'Gladiator expenses: {expenses:.2f} aureus')