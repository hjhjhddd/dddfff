target = 'global/excel/cubemain.txt'


def migrate(txt_file):
    formulas = (
        {
            'description': '1 Any Armor + Stamina Potion -> Superior Armor', 'enabled': 1, 'version': 100,
            'numinputs': 2, 'input 1': 'armo', 'input 2': 'vps', 'output': '"usetype,hiq"', 'lvl': 99
        },
        {
            'description': '1 Any Weapon + Stamina Potion -> Superior Weapon', 'enabled': 1, 'version': 100,
            'numinputs': 2, 'input 1': 'weap', 'input 2': 'vps', 'output': '"usetype,hiq"', 'lvl': 99
        },
        {
            'description': '1 Superior Armor -> Another Superior Armor', 'enabled': 1, 'version': 100,
            'numinputs': 1, 'input 1': '"armo,hiq"', 'output': '"usetype,hiq"', 'lvl': 99
        },
        {
            'description': '1 Any Armor + Stamina Potion -> Superior Armor', 'enabled': 1, 'version': 100,
            'numinputs': 1, 'input 1': '"weap,hiq"', 'output': '"usetype,hiq"', 'lvl': 99
        },

    )

    txt_file.append({'description': 'Superior Items'})

    for formula in formulas:
        txt_file.append(formula)
