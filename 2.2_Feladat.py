t_betus_szavak = []
szavak = ['ajtó','tojás','Ottó','Tamás', 'tép','Tesla','alma','python']
for t_betu in szavak:
    if t_betu[0] == 't' or t_betu[0] == 'T':
        t_betus_szavak.append(t_betu)
        szavak.remove(t_betu)
print(t_betus_szavak)
print(szavak)