import pandas as pd

inp_file = "../data/data.csv"

def get_mean_sd(df, freq_type, label):
  label_df = df.loc[df['label'] == label]
  mu = label_df[[freq_type]].mean()
  sd = label_df[[freq_type]].std()
  return mu, sd

df = pd.read_csv(inp_file)
w_df = df.loc[df['label'] != 'nw']

freq_types = ['freq_sh', 'freq_em', 'freq_WL_news', 'freq_WL_blog']
labels = w_df['label'].unique()


for freq_type in freq_types:
  print(freq_type)
  print('all words')
  mu = w_df[[freq_type]].mean()
  sd = w_df[[freq_type]].std()
  print('mean = %f, standard deviation = %f' % (mu, sd))
  for label in labels:
    print(label)
    mu, sd = get_mean_sd(w_df, freq_type, label)
    print('mean = %f, standard deviation = %f' % (mu, sd))
  print('\n')