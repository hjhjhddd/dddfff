target = 'global/excel/cubemain.txt'


def migrate(txt_file):
    formulas = (
        {
            'description': '1 Any Armor + Thawing Potion -> Rare Armor', 'enabled': 1, 'version': 100,
            'numinputs': 2, 'input 1': 'armo', 'input 2': 'wms', 'output': '"usetype,rar"', 'lvl': 99
        },
        {
            'description': '1 Any Weapon + Thawing Potion -> Rare Weapon', 'enabled': 1, 'version': 100,
            'numinputs': 2, 'input 1': 'weap', 'input 2': 'wms', 'output': '"usetype,rar"', 'lvl': 99
        },
        {
            'description': '1 Any Amulet + Thawing Potion -> Rare Amulet', 'enabled': 1, 'version': 100,
            'numinputs': 2, 'input 1': 'amu', 'input 2': 'wms', 'output': '"usetype,rar"', 'lvl': 99
        },
        {
            'description': '1 Any Ring + Thawing Potion -> Rare Ring', 'enabled': 1, 'version': 100,
            'numinputs': 2, 'input 1': 'ring', 'input 2': 'wms', 'output': '"usetype,rar"', 'lvl': 99
        },
        {
            'description': '1 Rare Armor -> Another Rare Armor', 'enabled': 1, 'version': 100,
            'numinputs': 1, 'input 1': '"armo,rar"', 'output': '"usetype,rar"', 'lvl': 99
        },
        {
            'description': '1 Rare Weapon -> Another Rare Weapon', 'enabled': 1, 'version': 100,
            'numinputs': 1, 'input 1': '"weap,rar"', 'output': '"usetype,rar"', 'lvl': 99
        },
        {
            'description': '1 Rare Amulet -> Another Rare Amulet', 'enabled': 1, 'version': 100,
            'numinputs': 1, 'input 1': '"amu,rar"', 'output': '"usetype,rar"', 'lvl': 99
        },
        {
            'description': '1 Rare Ring -> Another Rare Ring', 'enabled': 1, 'version': 100,
            'numinputs': 1, 'input 1': '"ring,rar"', 'output': '"usetype,rar"', 'lvl': 99
        },
    )

    txt_file.append({'description': 'Rare Items'})

    for formula in formulas:
        txt_file.append(formula)
