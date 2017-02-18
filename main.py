import logging

import config
from controller import Controller
from gui import Gui
from phone import Phone

def main():
    import config
    phone = Phone()
    phone.setSoundDevices(config.SND_SPK, config.SND_MIC, config.SND_RING)
    phone.register(config)

    gui = Gui()

    controller = Controller(phone, gui)

    import time
    while True:
        phone.loop()
        gui.loop()
        time.sleep(0.1)

if __name__ == '__main__':
    #logging.basicConfig(level=logging.INFO)
    main()
