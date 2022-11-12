import json
from pathlib import Path

target = 'global/excel/magicprefix.txt'


def migrate(txt_file):
    with Path(__file__).parent.joinpath('res', 'variable_props.json').open('r', encoding='utf-8') as fp:
        props = json.load(fp)

    for row in txt_file:
        if row['spawnable'] != '1':
            continue

        for i in range(3):
            if row[f'mod{i + 1}code'] not in props:
                continue

            row[f'mod{i + 1}min'] = row[f'mod{i + 1}max']
