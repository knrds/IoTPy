from time import sleep
from IoTPy.boards.LPCExpresso11U14 import LPCexpresso
from IoTPy.interfaces.gpio import GPIO
from IoTPy.transport import SerialTransport, SocketTransport

# This is platform dependent - please configure to your application
LED_PIN_ID = 'P0_7'
io = SerialTransport()
with LPCexpresso(io) as board, board.digital(LED_PIN_ID) as ledPin, board.digital('P0_14') as rpin:
    ledPin.setup(GPIO.OUTPUT)  # set digital pin to be output
    try:
        while True:
            ledPin.write(1)  # Turn led ON
            sleep(1)
            print(rpin.read())
            ledPin.write(0)  # Turn led OFF
            #
            sleep(1)
    except KeyboardInterrupt:
        ledPin.write(0)  # Turn led OFF
        pass