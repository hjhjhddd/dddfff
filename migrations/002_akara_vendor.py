target = 'global/excel/misc.txt'


def migrate(txt_file):
    gems = (
        # Amethyst
        'gcv', 'gfv', 'gsv', 'gzv', 'gpv',
        # Topaz
        'gcy', 'gfy', 'gsy', 'gly', 'gpy',
        # Sapphire
        'gcb', 'gfb', 'gsb', 'glb', 'gpb',
        # Emerald
        'gcg', 'gfg', 'gsg', 'glg', 'gpg',
        # Ruby
        'gcr', 'gfr', 'gsr', 'glr', 'gpr',
        # Diamond
        'gcw', 'gfw', 'gsw', 'glw', 'gpw',
        # Skull
        'skc', 'skf', 'sku', 'skl', 'skz',
    )

    charms = ('cm1', 'cm2', 'cm3',)

    runes = (
        'r01', 'r02', 'r03', 'r04', 'r05', 'r06', 'r07', 'r08', 'r09', 'r10', 'r11',
        'r12', 'r13', 'r14', 'r15', 'r16', 'r17', 'r18', 'r19', 'r20', 'r21', 'r22',
        'r23', 'r24', 'r25', 'r26', 'r27', 'r28', 'r29', 'r30', 'r31', 'r32', 'r33',
    )

    misc = ('jew',)

    for code in gems + charms + runes + misc:
        row = next(s for s in txt_file if s['code'] == code)
        row['cost'] = 1
        row['AkaraMin'] = 1
        row['AkaraMax'] = 1
        row['AkaraMagicMin'] = 1
        row['AkaraMagicMax'] = 1
        row['PermStoreItem'] = 1
        row['multibuy'] = 1
