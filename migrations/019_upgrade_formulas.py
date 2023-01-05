target = 'global/excel/cubemain.txt'


def migrate(txt_file):
    formulas = (
        {
            'description': '1 Normal Armor + Key -> Exceptional Armor', 'enabled': 1, 'version': 100,
            'numinputs': 2, 'input 1': 'armo,bas', 'input 2': 'key', 'output': '"useitem,mod,exc"'
        },
        {
            'description': '1 Normal Weapon + Key -> Exceptional Weapon', 'enabled': 1, 'version': 100,
            'numinputs': 2, 'input 1': 'weap,bas', 'input 2': 'key', 'output': '"useitem,mod,exc"'
        },
        {
            'description': '1 Exceptional Armor + Key -> Elite Armor', 'enabled': 1, 'version': 100,
            'numinputs': 2, 'input 1': 'armo,exc', 'input 2': 'key', 'output': '"useitem,mod,eli"'
        },
        {
            'description': '1 Exceptional Weapon + Key -> Elite Weapon', 'enabled': 1, 'version': 100,
            'numinputs': 2, 'input 1': 'weap,exc', 'input 2': 'key', 'output': '"useitem,mod,eli"'
        },
    )

    txt_file.append({'description': 'Upgrade Items'})

    for formula in formulas:
        txt_file.append(formula)
