# Lablo

A modding-as-code project using tool [larzuk][1] for character build testings of
game [Diablo II: Resurrected][2].

## Features

- Horadric Cube for new characters.
- Akara sells all gems, charms, runes and jewel.
- Maximize defense of all armors.
- Maximize properties of all superior items.
- Maximize properties of all rune words.
- Maximize properties of all magical prefix/suffix.
- Maximize properties of all craft items.
- Maximize properties of all set items.
- Maximize properties of all unique items.
- Horadric Cube formulas to generate items. (see **Horadric Cube Formulas**)
- Maximize stacks of all tomes to 100.
- Enable ladder rune words.

## Horadric Cube Formulas

### Superior Items

- 1 Any Item + Stamina Potion -> Superior item
- 1 Superior Item -> New superior item with same type

### Socket Items

- 1 Any Item + El Rune = Make 1 socket
- 1 Any Item + Eld Rune = Make 2 sockets
- 1 Any Item + Tir Rune = Make 3 sockets
- 1 Any Item + Nef Rune = Make 4 sockets
- 1 Any Item + Eth Rune = Make 5 sockets
- 1 Any Item + Ith Rune = Make 6 sockets

### Ethereal Items

- 1 Any Item + Antidote Potion -> Make item ethereal

### Magical Items

- 1 Any Item + Mana Potion (Any) -> Magical item
- 1 Magical Item -> New magical item with same type

### Rare Items

- 1 Any Item + Thawing Potion -> Rare Item
- 1 Rare Item -> New rare item with same type

### Set Items

- 1 Any Item + Scroll of Town Portal -> Set Item

### Unique Items

- 1 Any Item + Scroll of Identify -> Unique Item

### Upgrade Items

- 1 Normal Item + Key -> Exceptional Item
- 1 Exceptional Item + Key -> Elite Item

## Usage

see [https://github.com/he-yaowen/larzuk](https://github.com/he-yaowen/larzuk)

## License

Copyright (C) 2022 HE Yaowen <he.yaowen@hotmail.com>

The BSD 3-Clause License, see [LICENSE](./LICENSE).

[1]: https://github.com/he-yaowen/larzuk

[2]: https://diablo2.blizzard.com
