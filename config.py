from xremap.dsl import define_keymap, define_modmap

from myxremap.key import Key, Modifier
from myxremap.keymap import KeyMap, KeySwap

key_map = KeyMap()

key_map.extend(
    [
        KeySwap(Key("Q"), Key("Q")),
        KeySwap(Key("E"), Key("Comma")),
        KeySwap(Key("R"), Key("Dot")),
        KeySwap(Key("T"), Key("Semicolon")),
        KeySwap(Key("Y"), Key("M")),
        KeySwap(Key("U"), Key("R")),
        KeySwap(Key("I"), Key("D")),
        KeySwap(Key("O"), Key("Y")),
        KeySwap(Key("P"), Key("P")),
        KeySwap(Key("A"), Key("A")),
        KeySwap(Key("S"), Key("O")),
        KeySwap(Key("D"), Key("E")),
        KeySwap(Key("F"), Key("I")),
        KeySwap(Key("G"), Key("U")),
        KeySwap(Key("H"), Key("G")),
        KeySwap(Key("J"), Key("T")),
        KeySwap(Key("K"), Key("K")),
        KeySwap(Key("L"), Key("S")),
        KeySwap(Key("Semicolon"), Key("N")),
        KeySwap(Key("Z"), Key("Z")),
        KeySwap(Key("X"), Key("X")),
        KeySwap(Key("C"), Key("C")),
        KeySwap(Key("V"), Key("V")),
        KeySwap(Key("B"), Key("F")),
        KeySwap(Key("N"), Key("B")),
        KeySwap(Key("M"), Key("H")),
        KeySwap(Key("Comma"), Key("J")),
        KeySwap(Key("Dot"), Key("L")),
    ]
)

# See Issue#1.
# KeyMap for inputting ~(tilde) with Shift+`
# Using xmodmap, assign KatakanaHiragana to ~(tilde).
# In Xmodmap,
# keycode 101 = asciitilde Romaji Hiragana_Katakana Romaji Hiragana_Katakana Romaji
key_map[Key("Grave", Modifier.SHIFT)] = Key("KatakanaHiragana")

key_map[Key("K", Modifier.ALT)] = Key("Up")
key_map[Key("Comma", Modifier.ALT)] = Key("Down")
key_map[Key("M", Modifier.ALT)] = Key("Left")
key_map[Key("Dot", Modifier.ALT)] = Key("Right")

key_map[Key("J", Modifier.ALT)] = Key("BackSpace")
key_map[Key("L", Modifier.ALT)] = Key("Delete")

key_map[Key("G", Modifier.ALT)] = Key("KPAsterisk")
key_map[Key("H", Modifier.ALT)] = Key("KPPlus")
key_map[Key("B", Modifier.ALT)] = Key("KPSlash")
key_map[Key("N", Modifier.ALT)] = Key("KPMinus")

define_modmap({"CapsLock": "Control_L", "Alt_R": "Super_L"})
define_keymap({}, key_map.dump(), "Global")
