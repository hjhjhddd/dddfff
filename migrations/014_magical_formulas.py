target = 'global/excel/cubemain.txt'


def migrate(txt_file):
    formulas = (
        {
            'description': '1 Any Armor + Mana Potion (Any) -> Magical Armor', 'enabled': 1, 'version': 100,
            'numinputs': 2, 'input 1': 'armo', 'input 2': 'mpot', 'output': '"usetype,mag"', 'lvl': 99
        },
        {
            'description': '1 Any Weapon + Mana Potion (Any) -> Magical Weapon', 'enabled': 1, 'version': 100,
            'numinputs': 2, 'input 1': 'weap', 'input 2': 'mpot', 'output': '"usetype,mag"', 'lvl': 99
        },
        {
            'description': '1 Any Amulet + Mana Potion (Any) -> Magical Amulet', 'enabled': 1, 'version': 100,
            'numinputs': 2, 'input 1': 'amu', 'input 2': 'mpot', 'output': '"usetype,mag"', 'lvl': 99
        },
        {
            'description': '1 Any Ring + Mana Potion (Any) -> Magical Ring', 'enabled': 1, 'version': 100,
            'numinputs': 2, 'input 1': 'ring', 'input 2': 'mpot', 'output': '"usetype,mag"', 'lvl': 99
        },
        {
            'description': '1 Magical Armor -> Another Magical Armor', 'enabled': 1, 'version': 100,
            'numinputs': 1, 'input 1': '"armo,mag"', 'output': '"usetype,mag"', 'lvl': 99
        },
        {
            'description': '1 Magical Weapon -> Another Magical Weapon', 'enabled': 1, 'version': 100,
            'numinputs': 1, 'input 1': '"weap,mag"', 'output': '"usetype,mag"', 'lvl': 99
        },
        {
            'description': '1 Magical Amulet -> Another Magical Amulet', 'enabled': 1, 'version': 100,
            'numinputs': 1, 'input 1': '"amu,mag"', 'output': '"usetype,mag"', 'lvl': 99
        },
        {
            'description': '1 Magical Ring -> Another Magical Ring', 'enabled': 1, 'version': 100,
            'numinputs': 1, 'input 1': '"ring,mag"', 'output': '"usetype,mag"', 'lvl': 99
        },
    )

    txt_file.append({'description': 'Magical Items'})

    for formula in formulas:
        txt_file.append(formula)
