target = 'global/excel/cubemain.txt'


def migrate(txt_file):
    formulas = (
        {
            'description': '1 Any Item + El Rune', 'enabled': 1, 'version': 100,
            'numinputs': 2, 'input 1': 'any', 'input 2': 'r01', 'output': '"useitem,sock=1"'
        },
        {
            'description': '1 Any Item + Eld Rune', 'enabled': 1, 'version': 100,
            'numinputs': 2, 'input 1': 'any', 'input 2': 'r02', 'output': '"useitem,sock=2"'
        },
        {
            'description': '1 Any Item + Tir Rune', 'enabled': 1, 'version': 100,
            'numinputs': 2, 'input 1': 'any', 'input 2': 'r03', 'output': '"useitem,sock=3"'
        },
        {
            'description': '1 Any Item + Nef Rune', 'enabled': 1, 'version': 100,
            'numinputs': 2, 'input 1': 'any', 'input 2': 'r04', 'output': '"useitem,sock=4"'
        },
        {
            'description': '1 Any Item + Eth Rune', 'enabled': 1, 'version': 100,
            'numinputs': 2, 'input 1': 'any', 'input 2': 'r05', 'output': '"useitem,sock=5"'
        },
        {
            'description': '1 Any Item + Ith Rune', 'enabled': 1, 'version': 100,
            'numinputs': 2, 'input 1': 'any', 'input 2': 'r06', 'output': '"useitem,sock=6"'
        },
    )

    txt_file.append({'description': 'Socket Items'})

    for formula in formulas:
        txt_file.append(formula)
