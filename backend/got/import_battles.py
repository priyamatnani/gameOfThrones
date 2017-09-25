from battles.models import BattleSet
from itertools import islice
import csv

csv_file_name = '/Users/kartik/Documents/kaggle_datasets/game_of_thrones/game-of-thrones/battles1.csv'
data_reader = csv.reader(open(csv_file_name), quotechar='"')


def write_to_table(start_index, end_index):
    bulk_data = []
    for col in islice(data_reader, start_index, end_index):
        battle = BattleSet()
        battle.name = str(col[0]).strip().lower() if col[0] else None
        battle.year = int(col[1]) if col[1] else None        
        battle.battle_number = int(col[2]) if col[2] else None
        battle.attacker_king = str(col[3]).strip().lower() if col[3] else None
        battle.defender_king = str(col[4]).strip().lower() if col[4] else None
        battle.attacker_1 = str(col[5]).strip().lower() if col[5] else None
        battle.attacker_2 = str(col[6]).strip().lower() if col[6] else None
        battle.attacker_3 = str(col[7]).strip().lower() if col[7] else None
        battle.attacker_4 = str(col[8]).strip().lower() if col[8] else None
        battle.defender_1 = str(col[9]).strip().lower() if col[9] else None
        battle.defender_2 = str(col[10]).strip().lower() if col[10] else None
        battle.defender_3 = str(col[11]).strip().lower() if col[11] else None
        battle.defender_4 = str(col[12]).strip().lower() if col[12] else None
        battle.attacker_outcome = str(col[13]).strip().lower() if col[13] else None
        battle.battle_type = str(col[14]).strip().lower() if col[14] else None
        battle.major_death = int(col[15]) if col[15] else None
        battle.major_capture = int(col[16]) if col[16] else None
        battle.attacker_size = int(col[17]) if col[17] else None
        battle.defender_size = int(col[18]) if col[18] else None
        battle.attacker_commander = str(col[19]).strip().lower() if col[19] else None
        battle.defender_commander = str(col[20]).strip().lower() if col[20] else None
        battle.summer = int(col[21]) if col[21] else None
        battle.location = str(col[22]).strip().lower() if col[22] else None
        battle.region = str(col[23]).strip().lower() if col[23] else None
        battle.note = str(col[24]).strip().lower() if col[24] else None
        bulk_data.append(battle)
    BattleSet.objects.bulk_create(bulk_data)

write_to_table(1, 40)