from battles.models import BattleSet
from itertools import islice
import csv

csv_file_name = '/Users/priya/Projects/kaggle_dataset/GOT_dataset/game-of-thrones/battles.csv'
data_reader = csv.reader(open(csv_file_name), delimeter=',', quotechar='"')


def write_to_table(start_index, end_index):
    bulk_data = []
    for col in islice(data_reader, start_index, end_index):
        battle = BattleSet()
        battle.name = col[0]
        battle.year = col[1]
        battle.battle_number = col[2]
        battle.attacker_king = col[3]
        battle.defender_king = col[4]
        battle.attacker_1 = col[5]
        battle.attacker_2 = col[6]
        battle.attacker_3 = col[7]
        battle.attacker_4 = col[8]
        battle.defender_1 = col[9]
        battle.defender_2 = col[10]
        battle.defender_3 = col[11]
        battle.defender_4 = col[12]
        battle.attacker_outcome = col[13]
        battle.battle_type = col[14]
        battle.major_death = col[15]
        battle.major_capture = col[16]
        battle.attacker_size = col[17]
        battle.defender_size = col[18]
        battle.attacker_commander = col[19]
        battle.defender_commander = col[20]
        battle.summer = col[21]
        battle.location = col[22]
        battle.region = col[23]
        battle.note = col[24]
        bulk_data.append(battle)
    BattleSet.objects.bulk_create(bulk_data)

write_to_table(1, 40)