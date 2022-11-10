target = 'global/excel/charstats.txt'


def migrate(txt_file):
    start_index = {
        'Amazon': 6,
        'Sorceress': 5,
        'Necromancer': 5,
        'Paladin': 6,
        'Barbarian': 6,
        'Druid': 6,
        'Assassin': 6,
    }

    for key, i in start_index.items():
        row = next(s for s in txt_file if s['class'] == key)
        row[f'item{i}'] = 'box'
        row[f'item{i}count'] = 1
