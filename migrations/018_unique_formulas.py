target = 'global/excel/cubemain.txt'


def migrate(txt_file):
    formulas = (
        {
            'description': '1 Any Armor + Scroll of Identify -> Unique Armor', 'enabled': 1, 'version': 100,
            'numinputs': 2, 'input 1': 'armo', 'input 2': 'isc', 'output': '"usetype,uni"', 'lvl': 99
        },
        {
            'description': '1 Any Weapon + Scroll of Identify -> Unique Weapon', 'enabled': 1, 'version': 100,
            'numinputs': 2, 'input 1': 'weap', 'input 2': 'isc', 'output': '"usetype,uni"', 'lvl': 99
        },
        {
            'description': '1 Any Amulet + Scroll of Identify -> Unique Amulet', 'enabled': 1, 'version': 100,
            'numinputs': 2, 'input 1': 'amu', 'input 2': 'isc', 'output': '"usetype,uni"', 'lvl': 99
        },
        {
            'description': '1 Any Ring + Scroll of Identify -> Unique Ring', 'enabled': 1, 'version': 100,
            'numinputs': 2, 'input 1': 'ring', 'input 2': 'isc', 'output': '"usetype,uni"', 'lvl': 99
        },
        {
            'description': '1 Any Grand Charm + Scroll of Identify -> Unique Grand Charm', 'enabled': 1, 'version': 100,
            'numinputs': 2, 'input 1': 'cm3', 'input 2': 'isc', 'output': '"usetype,uni"', 'lvl': 99
        },
    )

    txt_file.append({'description': 'Unique Items'})

    for formula in formulas:
        txt_file.append(formula)
