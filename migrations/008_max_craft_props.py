import json
from pathlib import Path

target = 'global/excel/cubemain.txt'


def migrate(txt_file):
    with Path(__file__).parent.joinpath('res', 'variable_props.json').open('r', encoding='utf-8') as fp:
        props = json.load(fp)

    for row in filter(lambda r: r['numinputs'] == '4' and r['input 2'] == 'jew', txt_file):
        for i in range(4):
            if row[f'mod {i + 1}'] not in props:
                continue

            row[f'mod {i + 1} min'] = row[f'mod {i + 1} max']
