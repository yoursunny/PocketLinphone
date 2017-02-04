import logging

import config
from phone import Phone

def main():
    import config
    phone = Phone()
    phone.setSoundDevices(config.SND_SPK, config.SND_MIC, config.SND_RING)
    phone.register(config)

    import time
    while True:
        phone.loop()
        time.sleep(0.1)

if __name__ == '__main__':
    #logging.basicConfig(level=logging.INFO)
    main()
