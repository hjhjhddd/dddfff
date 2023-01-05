target = 'global/excel/cubemain.txt'


def migrate(txt_file):
    formulas = (
        {
            'description': '1 Any Armor + Scroll of Town Portal -> Set Armor', 'enabled': 1, 'version': 100,
            'numinputs': 2, 'input 1': 'armo', 'input 2': 'tsc', 'output': '"usetype,set"', 'lvl': 99
        },
        {
            'description': '1 Any Weapon + Scroll of Town Portal -> Set Weapon', 'enabled': 1, 'version': 100,
            'numinputs': 2, 'input 1': 'weap', 'input 2': 'tsc', 'output': '"usetype,set"', 'lvl': 99
        },
        {
            'description': '1 Any Amulet + Scroll of Town Portal -> Set Amulet', 'enabled': 1, 'version': 100,
            'numinputs': 2, 'input 1': 'amu', 'input 2': 'tsc', 'output': '"usetype,set"', 'lvl': 99
        },
        {
            'description': '1 Any Ring + Scroll of Town Portal -> Set Ring', 'enabled': 1, 'version': 100,
            'numinputs': 2, 'input 1': 'ring', 'input 2': 'tsc', 'output': '"usetype,set"', 'lvl': 99
        },
    )

    txt_file.append({'description': 'Set Items'})

    for formula in formulas:
        txt_file.append(formula)
