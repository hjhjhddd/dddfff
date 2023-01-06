target = 'global/excel/runes.txt'


def migrate(txt_file):
    for row in filter(lambda r: r['firstLadderSeason'] != '', txt_file):
        row['firstLadderSeason'] = ''
        row['lastLadderSeason'] = ''
