import json
from pathlib import Path

target = 'global/excel/runes.txt'


def migrate(txt_file):
    with Path(__file__).parent.joinpath('res', 'variable_props.json').open('r', encoding='utf-8') as fp:
        props = json.load(fp)

    for row in txt_file:
        for i in range(7):
            if row[f'T1Code{i + 1}'] not in props:
                continue

            row[f'T1Min{i + 1}'] = row[f'T1Max{i + 1}']
