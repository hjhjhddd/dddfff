target = 'global/excel/cubemain.txt'


def migrate(txt_file):
    formulas = (
        {
            'description': '1 Any Armor + Antidote Potion -> Ethereal Armor', 'enabled': 1, 'version': 100,
            'numinputs': 2, 'input 1': 'armo', 'input 2': 'yps', 'output': '"useitem"', 'mod 1': 'ethereal', 'mod 1 min': 1, 'mod 1 max': 1
        },
        {
            'description': '1 Any Weapon + Antidote Potion -> Ethereal Weapon', 'enabled': 1, 'version': 100,
            'numinputs': 2, 'input 1': 'weap', 'input 2': 'yps', 'output': '"useitem"', 'mod 1': 'ethereal', 'mod 1 min': 1, 'mod 1 max': 1
        },
    )

    txt_file.append({'description': 'Ethereal Items'})

    for formula in formulas:
        txt_file.append(formula)
