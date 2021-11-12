from subprocess import *

inputf="../../data/sample_pseudo_words.txt"
outputf="../../img/pseudo_words"
transf=inputf+"OUTPUT"

with open(inputf) as inf:
  lines = inf.readlines()
  lines = [line.rstrip() for line in lines]

call("python3 runTransliteration.py {}".format(inputf), shell=True)

with open(transf) as trf:
  trlines = trf.readlines()
  trlines = [trline.rstrip() for trline in trlines]

for i in range(len(lines)):
  call('''convert -background yellow -fill black -font Lohit-Devanagari -size 200x100 -gravity center 'caption:'"{}" "{}".png'''.format(lines[i], trlines[i]), shell=True)
  call("mv *.png {}".format(outputf), shell=True)