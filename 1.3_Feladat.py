szinek = ['kék', 'piros', 'fehér', 'fekete', 'zöld', 'sárga', 'barna', 'piros', 'fehér', 'szürke']

szin = input('Adj meg egy színt!\t')
if szin in szinek:
	print('A megadott szín szerepel a listában.')
if szin not in szinek:    
	print('A megadott szín nem szerepel a listában.')
if szin in szinek:
  print(f"Ez a szín: {szin} enyiszer szerepel a listában:  {szinek.count(szin)}")
szinek.append(szin)
print('A lista színei:')
for szin in szinek:
	print(szin, end=', ')