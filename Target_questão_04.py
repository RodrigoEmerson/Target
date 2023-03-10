sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

total = sp + rj + mg + es + outros

perc_sp = (sp / total) * 100
perc_rj = (rj / total) * 100
perc_mg = (mg / total) * 100
perc_es = (es / total) * 100
perc_outros = (outros / total) * 100

print('SP: {:.2f} %'.format(perc_sp))
print('RJ: {:.2f} %'.format(perc_rj))
print('MG: {:.2f} %'.format(perc_mg))
print('ES: {:.2f} %'.format(perc_es))
print('Outros: {:.2f} %'.format(perc_outros))
