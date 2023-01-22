'''
connect pin 0 of the transmitter board to pin 0 of the reciever board.
upload this main.py to the transmitter board.
if everything works well,
the led on the transmitter board should blink when the led on the reciever board blinks.
for import errors try running in thonny
'''

from Send import transmit

while True:
    transmit()  