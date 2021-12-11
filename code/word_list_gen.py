import pandas as pd
import random

inp_file = "../data/SHABD_DATABASE.csv"
out_word_file = "../data/words.txt"
out_hflong_word_file = "../data/hflong_words.txt"
out_lflong_word_file = "../data/lflong_words.txt"
out_hfshort_word_file = "../data/hfshort_words.txt"
out_lfshort_word_file = "../data/lfshort_words.txt"

# def get_devanagari(word):
#     return word.encode('iso-8859-1', 'ignore').decode('utf8', 'ignore')

def get_len_threshold():
    filename = "../data/data.csv"
    df = pd.read_csv(filename)
    long_word_df = df.loc[df['label'] == 'hflong']
    long_len_list = long_word_df['length']
    long_word_df = df.loc[df['label'] == 'lflong']
    long_len_list.append(long_word_df['length'])
    return min(long_len_list)

def get_freq_threshold():
    filename = "../data/data.csv"
    df = pd.read_csv(filename)
    hf_word_df = df.loc[df['label'] == 'hflong']
    hf_list = hf_word_df['freq_sh']
    hf_word_df = df.loc[df['label'] == 'hfshort']
    hf_list.append(hf_word_df['freq_sh'])
    return min(hf_list)

def write_samples(word_list, out_file, num):
    word_list = random.sample(list(word_list), num)
    f = open(out_file, "w")
    for word in word_list:
        f.write(str(word))
        f.write("\n")
    f.close()

len_thresh = get_len_threshold()
freq_thresh = get_freq_threshold()
print('Length Threshold: ',len_thresh)
print('Frequency Threshold: ',freq_thresh)

# df = pd.read_csv(inp_file)

# num = 10

# # hf
# hf_word_df = df.loc[df['frequency'] >= freq_thresh]

# # hflong
# hflong_word_df = hf_word_df.loc[hf_word_df['total_length'] >= len_thresh]
# hflong_word_list = hflong_word_df['word']
# write_samples(hflong_word_list, out_hflong_word_file, num)

# # hfshort
# hfshort_word_df = hf_word_df.loc[hf_word_df['total_length'] < len_thresh]
# hfshort_word_list = hfshort_word_df['word']
# write_samples(hfshort_word_list, out_hfshort_word_file, num)

# # lf
# lf_word_df = df.loc[df['frequency'] < freq_thresh]

# # lflong
# lflong_word_df = lf_word_df.loc[lf_word_df['total_length'] >= len_thresh]
# lflong_word_list = lflong_word_df['word']
# write_samples(lflong_word_list, out_lflong_word_file, num)

# # lfshort
# lfshort_word_df = lf_word_df.loc[lf_word_df['total_length'] < len_thresh]
# lfshort_word_list = lfshort_word_df['word']
# write_samples(lfshort_word_list, out_lfshort_word_file, num)
