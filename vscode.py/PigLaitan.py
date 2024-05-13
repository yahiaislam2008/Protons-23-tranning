"""Pig Latin, by Yahia@gmawithpython.com
Translates English messages into Igpay Atinlay.
Tags: short, word"""
try:
    import pyperclip
except ImportError:
    pass

vowels=("a","e","i","u","o")

def main():
    print("""ahiayyay ovelsay rotonsp(yahia loves protons )
by Yahia@gmawithpython.com
enter your message:""")
    yahia=englishToPigLatian(input('> '))
    print(yahia)