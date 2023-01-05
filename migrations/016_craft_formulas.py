target = 'global/excel/cubemain.txt'


def migrate(txt_file):
    for row in filter(lambda row: row['numinputs'] == '4' and row['input 2'] == 'jew', txt_file):
        row['numinputs'] = 2
        row['input 2'] = row['input 4']
        row['input 3'] = row['input 4'] = ''
        row['lvl'] = 99
