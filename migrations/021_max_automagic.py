import json
from pathlib import Path

target = 'global/excel/automagic.txt'


def migrate(txt_file):
    for row in txt_file:
        if row['spawnable'] != '1':
            continue

        for i in range(3):
            row[f'mod{i + 1}min'] = row[f'mod{i + 1}max']
