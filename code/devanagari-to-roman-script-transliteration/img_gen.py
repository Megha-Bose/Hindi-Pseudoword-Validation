from subprocess import *

def img_gen_roman(inputf, outputf):
  with open(inputf) as inf:
    lines = inf.readlines()
    lines = [line.rstrip() for line in lines]

  call("python3 runTransliteration.py {}".format(inputf), shell=True)
  transf=inputf+"OUTPUT"

  with open(transf) as trf:
    trlines = trf.readlines()
    trlines = [trline.rstrip() for trline in trlines]

  for i in range(len(lines)):
    j = 0
    while j < len(lines[i]):
      if lines[i][j] == 'ि':
        new_line = ""
        if j > 0:
          new_line = new_line + lines[i][:j-1]
        new_line = new_line + lines[i][j]
        if j > 0:
          new_line = new_line + lines[i][j-1]   
        if j + 1 < len(lines[i]):
          new_line = new_line + lines[i][j+1:]
        lines[i] = new_line
      j+=1
    
    call('''convert -background yellow -fill black -font Lohit-Devanagari -size 300x100 -gravity center 'caption:'"{}" "{}".png'''.format(lines[i], trlines[i]), shell=True)
    call("mv *.png {}".format(outputf), shell=True)


img_gen_roman('../../data/hflong_words.txt', '../../img/words/hflong/')
img_gen_roman('../../data/hfshort_words.txt', '../../img/words/hfshort/')
img_gen_roman('../../data/lflong_words.txt', '../../img/words/lflong/')
img_gen_roman('../../data/lfshort_words.txt', '../../img/words/lfshort/')

img_gen_roman('../../data/pslong_words.txt', '../../img/pseudo_words/long/')
img_gen_roman('../../data/psshort_words.txt', '../../img/pseudo_words/short/')