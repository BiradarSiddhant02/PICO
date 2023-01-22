'''
connect the pin 0 of the reciever board to the pin 0 of the transmitter board.
upload this main.py to the reciever board.

if everything works well, 
the led on the reciever board should blink when the led on the transmitter board blinks.

for import errors try running in thonny
'''


from Recieve import recieve

while True:
    recieve()