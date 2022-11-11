target = 'global/excel/qualityitems.txt'


def migrate(txt_file):
    for row in txt_file:
        row['mod1min'] = row['mod1max']
        row['mod2min'] = row['mod2max']
