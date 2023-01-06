target = 'global/excel/misc.txt'


def migrate(txt_file):
    tomes = ('Tome of Town Portal', 'Tome of Identify',)

    for row in filter(lambda r: r['name'] in tomes, txt_file):
        row['maxstack'] = 100
