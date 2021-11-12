import csv
from collections import OrderedDict

vowels = OrderedDict([
('ँ','n'),
('ं','n'),
('ः','a'),
('अ','a'), 
('आ','aa'), 
('इ','i'), 
('ई','ee'), 
('उ','u'), 
('ऊ','oo'), 
('ऋ','ri'), 
('ए','e'), 
('ऐ','ae'), 
('ओ','o'), 
('औ','au'), 
('ा','a'), 
('ि','i'), 
('ी','i'), 
('ु','u'), 
('ू','oo'), 
('ृ','ri'), 
('े','e'), 
('ै','ai'), 
('ो','o'), 
('ौ','au')
])

consonants = OrderedDict([
('क','k'), 
('ख','kh'), 
('ग','g'), 
('घ','gh'), 
('ङ','ng'),

('च','ch'), 
('छ','chh'), 
('ज','j'), 
('ज़','z'),
('ज़','z'), #these two are very different, see them in unicode by 'ज़'.encode('utf-8'). You'll see.
('झ','jh'), 
('ञ','nj'), 

('ट','t'), 
('ठ','th'), 
('ड','d'), 
('ड़','r'),
('ड़','r'), #these two are very different, see them in unicode by 'ड़'.encode('utf-8'). You'll see.
('ढ','dh'), 
('ण','n'), 

('त','t'), 
('थ','th'), 
('द','d'), 
('ध','dh'), 
('न','n'), 

('प','p'), 
('फ','ph'), 
('फ़','f'),
('फ़','f'), #these two फ़ are very different, see them in unicode by 'फ़'.encode('utf-8'). You'll see.
('ब','b'), 
('भ','bh'), 
('म','m'), 

('य','y'), 
('र','r'), 
('ल','l'), 
('व','v'), 
('श','sh'), 

('ष','sh'), 
('स','s'), 
('ह','h'),
('क्ष','ksh'),
('त्र','tr'),
('ज्ञ','gy')
	])

with open('svar.csv', 'w') as f:
	csvwriter = csv.writer(f)
	for k,v in zip(vowels.keys(), vowels.values()):
		csvwriter.writerow([k,v])

with open('vyanjan.csv', 'w') as f:
	csvwriter = csv.writer(f)
	for k,v in zip(consonants.keys(), consonants.values()):
		csvwriter.writerow([k,v])
