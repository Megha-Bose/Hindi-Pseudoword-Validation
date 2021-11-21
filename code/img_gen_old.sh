#!/bin/bash
input="../data/sample_pseudo_words.txt"
output="../img/pseudo_words"
while IFS= read -r line
do
  convert -background yellow -fill black -font Lohit-Devanagari -size 200x100 -gravity center 'caption:'"$line" "$line".png
  mv "$line".png "$output"
done < "$input"