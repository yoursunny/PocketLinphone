class Controller:
    def __init__(self, phone, gui):
        self.phone = phone
        self.gui = gui

        self.phone.on('incoming', self._incoming)
        self.phone.on('connected', self._connected)
        self.phone.on('end', self._end)

    def _incoming(self, remoteUri):
        f = self.gui.showIncomingCall(remoteUri)
        f.on('accept', self.phone.accept)
        f.on('decline', self.phone.decline)

    def _connected(self, remoteUri):
        f = self.gui.showInCall(remoteUri)
        f.on('hangup', self.phone.hangup)

    def _end(self, remoteUri):
        self.gui.close()
