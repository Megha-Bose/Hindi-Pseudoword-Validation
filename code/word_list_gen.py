import pandas as pd
import random

inp_file = "../data/data.csv"
out_word_file = "../data/words.txt"
out_long_word_file = "../data/long_words.txt"
out_short_word_file = "../data/short_words.txt"

def get_devanagari(word):
    return word.encode('iso-8859-1', 'ignore').decode('utf8', 'ignore')

df = pd.read_csv(inp_file)

# get words
word_df = df.loc[df['label'] != 'nw']
word_list = word_df['word']

f = open(out_word_file, "w")

for word in word_list:
    word_in_devanagari = get_devanagari(word)
    f.write(str(word_in_devanagari))
    f.write("\n")

f.close()


num = 15

word_df = df.loc[df['label'] == 'hfshort']
word_list = word_df['word']
word_df = df.loc[df['label'] == 'lfshort']
word_list.append(word_df['word'])

short_word_list = random.sample(list(word_list), num)

f = open(out_short_word_file, "w")

for word in short_word_list:
    word_in_devanagari = get_devanagari(word)
    f.write(str(word_in_devanagari))
    f.write("\n")

f.close()


word_df = df.loc[df['label'] == 'hflong']
word_list = word_df['word']
word_df = df.loc[df['label'] == 'lflong']
word_list.append(word_df['word'])

long_word_list = random.sample(list(word_list), num)

f = open(out_long_word_file, "w")

for word in long_word_list:
    word_in_devanagari = get_devanagari(word)
    f.write(str(word_in_devanagari))
    f.write("\n")

f.close()

