# PocketLinphone

SIP softphone for PocketCHIP

## Setup

Install dependencies:

    sudo apt-get install python-pip python-tk linphone-nogtk
    wget https://www.linphone.org/releases/linphone-python-raspberry/linphone4raspberry-3.9.1-cp27-none-any.whl
    sudo pip install linphone4raspberry-3.9.1-cp27-none-any.whl

Verify dependencies:

    python
    >>> import Tkinter
    >>> import linphone
    >>> exit()
