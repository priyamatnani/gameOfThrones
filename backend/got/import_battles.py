from battles.models import BattleSet
from itertools import islice
import csv

csv_file_name = '/Users/kartik/Documents/kaggle_datasets/game_of_thrones/game-of-thrones/battles1.csv'
data_reader = csv.reader(open(csv_file_name), quotechar='"')


def write_to_table(start_index, end_index):
    bulk_data = []
    for col in islice(data_reader, start_index, end_index):
        battle = BattleSet()
        battle.name = str(col[0])
        battle.year = int(col[1]) if col[1] else None        
        battle.battle_number = int(col[2]) if col[2] else None
        battle.attacker_king = str(col[3])
        battle.defender_king = str(col[4])
        battle.attacker_1 = str(col[5])
        battle.attacker_2 = str(col[6])
        battle.attacker_3 = str(col[7])
        battle.attacker_4 = str(col[8])
        battle.defender_1 = str(col[9])
        battle.defender_2 = str(col[10])
        battle.defender_3 = str(col[11])
        battle.defender_4 = str(col[12])
        battle.attacker_outcome = str(col[13])
        battle.battle_type = str(col[14])
        battle.major_death = int(col[15]) if col[15] else None
        battle.major_capture = int(col[16]) if col[16] else None
        battle.attacker_size = int(col[17]) if col[17] else None
        battle.defender_size = int(col[18]) if col[18] else None
        battle.attacker_commander = str(col[19])
        battle.defender_commander = str(col[20])
        battle.summer = int(col[21]) if col[21] else None
        battle.location = str(col[22])
        battle.region = str(col[23])
        battle.note = str(col[24])
        bulk_data.append(battle)
    BattleSet.objects.bulk_create(bulk_data)

write_to_table(1, 40)