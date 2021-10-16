import pandas as pd

inp_file = "../data/data.csv"
out_word_file = "../data/words.txt"

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

