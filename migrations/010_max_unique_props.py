import json
from pathlib import Path

target = 'global/excel/uniqueitems.txt'


def migrate(txt_file):
    with Path(__file__).parent.joinpath('res', 'variable_props.json').open('r', encoding='utf-8') as fp:
        props = json.load(fp)

    for row in txt_file:
        if row['enabled'] != '1':
            continue

        for i in range(12):
            if row[f'prop{i + 1}'] not in props:
                continue

            row[f'min{i + 1}'] = row[f'max{i + 1}']
