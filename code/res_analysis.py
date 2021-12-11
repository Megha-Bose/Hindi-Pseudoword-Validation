import pandas as pd
import numpy as np


# pseudowords
# pslong = get_list('../data/pslong_words.txtOUTPUT')
pslong = ['upiyat', 'asnmvanngh', 'jarjnnd', 'khalatvki', 'thera', 'lulphnn', 'barijaz', 'shinnshit', 'dakdoon', 'tyoglnn']
# psshort = get_list('../data/psshort_words.txtOUTPUT')
psshort = ['ooksar', 'taldi', 'liyat', 'eemi', 'talhi', 'shabinn', 'khin', 'khudarn', 'phaj', 'naji']

# words
# hflong = get_list('../data/hflong_words.txtOUTPUT')
hflong = ['chikanapks', 'bhikshuon', 'vaivahik', 'karenge', 'nimnastriy', 'dharmaprant', 'sarvotkrisht', 'pichharta', 'golagappe', 'mngakar']
# hfshort = get_list('../data/hfshort_words.txtOUTPUT')
hfshort = ['urta', 'ratri', 'dabi', 'pnja', 'ghusi', 'pray', 'ausat', 'tooti', 'jamin', 'katakar']
# lflong = get_list('../data/lflong_words.txtOUTPUT')
lflong = ['aavedanakarta', 'maurng', 'kooddan', 'nistej', 'lngri', 'doraha', 'yatnaen', 'pathkon', 'moorti', 'mahasngram']
#lfshort = get_list('../data/lfshort_words.txtOUTPUT')
lfshort = ['bari', 'baston', 'majhin', 'barso', 'vrishti', 'chhutte', 'oophan', 'tahal', 'saph', 'tope']


def get_list(file):
    with open(file) as inf:
        lines = inf.readlines()
        lines = [line.rstrip() for line in lines]
    return list(lines)


participant_data_file = ''

data_times_df = pd.read_csv(participant_data_file + "data_times.csv")
data_df = pd.read_csv(participant_data_file + +"data.csv")

participant_ids = list(data_df.index)
print(participant_ids)


def add_participant_ratings(pid, rating_file):
    val = []
    with open(rating_file) as inf:
        lines = inf.readlines()
        # alternate wordiness and familiarity imput taken
        counter = 0
        for line in lines:
            temp = line.split()
            value = temp[0]
            rating = temp[1]
            rt = temp[2]
            bool = temp[3]
            counter+=1
    

for pid in participant_ids:
    rating_file = data_df.loc[pid, 'lchoice:12']
    # validate_participant(pid)
    add_participant_ratings(pid, rating_file)


