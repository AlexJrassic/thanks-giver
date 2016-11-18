import random
from papirus import PapirusText
from time import sleep
from subprocess import call
from gpiozero import Button
from signal import pause

text = PapirusText()
button = Button(21)

messages = [
    "puppies.”,
    "pie.”,
    “kittens.”,
    “cake.”,
    “Raspberry Pi.“,
	  “bagels.”,
    “ice cream.“,
    “Harry Potter.“,
    “music.”,
    "LEGO"
]

def thanks():
    out = "I am thankful for " + random.choice(messages)
    call (["sudo", "papirus-write", out])
    sleep(0.5)

button.when_pressed = thanks

pause()
