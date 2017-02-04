import Tkinter as tk

class Gui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)

        self.frame = None

    def loop(self):
        self.root.update_idletasks()
        self.root.update()

    def close(self):
        if self.frame is not None:
            self.frame.destroy()
            self.frame = None
        self.root.withdraw()

    def _show(self):
        self.root.withdraw()
        self.frame.grid(sticky=tk.N+tk.E+tk.S+tk.W, row=0, column=0)
        self.root.deiconify()

    def showIncomingCall(self, remoteUri):
        self.frame = IncomingCallFrame(self.root, remoteUri)
        self._show()

    def showInCall(self, remoteUri):
        self.frame = InCallFrame(self.root, remoteUri)
        self._show()

class DialPadFrame(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        self.PLACEHOLDER = tk.Label(self, text='123\n456\n789\n*0#', font=(None, 32))
        self.PLACEHOLDER.grid(sticky=tk.N+tk.E+tk.S+tk.W)

class IncomingCallFrame(tk.Frame):
    def __init__(self, master, remoteUri):
        tk.Frame.__init__(self, master)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=2)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.TITLE = tk.Label(self, text='Incoming call from', font=(None, 16))
        self.TITLE.grid(sticky=tk.N+tk.E+tk.S+tk.W, row=0, columnspan=2)

        self.URI = tk.Label(self, font=(None, 16))
        self.URI['text'] = remoteUri
        self.URI.grid(sticky=tk.N+tk.E+tk.S+tk.W, row=1, columnspan=2)

        self.ACCEPT = tk.Button(self, text='ACCEPT', font=(None, 16), command=self.accept)
        self.ACCEPT.grid(sticky=tk.N+tk.E+tk.S+tk.W, row=2, column=0)

        self.DECLINE = tk.Button(self, text='DECLINE', font=(None, 16), command=self.decline)
        self.DECLINE.grid(sticky=tk.N+tk.E+tk.S+tk.W, row=2, column=1)

    def accept(self):
        print 'ACCEPT'

    def decline(self):
        print 'DECLINE'

class InCallFrame(tk.Frame):
    def __init__(self, master, remoteUri):
        tk.Frame.__init__(self, master)

        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=2)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.TITLE = tk.Label(self, text='Connected with', font=(None, 16))
        self.TITLE.grid(sticky=tk.N+tk.E+tk.S+tk.W, row=0)

        self.URI = tk.Label(self, font=(None, 16))
        self.URI['text'] = remoteUri
        self.URI.grid(sticky=tk.N+tk.E+tk.S+tk.W, row=1)

        self.HANGUP = tk.Button(self, text='HANGUP', font=(None, 16), command=self.hangup)
        self.HANGUP.grid(sticky=tk.N+tk.E+tk.S+tk.W, row=2)

        self.DIALPAD = DialPadFrame(self)
        self.DIALPAD.grid(sticky=tk.N+tk.E+tk.S+tk.W, row=0, column=1, rowspan=3)

    def hangup(self):
        print 'HANGUP'

def demo():
    gui = Gui()

    import time
    def delay(t):
        for i in range(int(t * 10)):
            gui.loop()
            time.sleep(0.1)

    gui.showIncomingCall('555-555-1200')
    delay(3)
    gui.close()
    delay(0.5)

    gui.showInCall('555-555-1200')
    delay(3)
    gui.close()
    delay(0.5)

if __name__ == '__main__':
    demo()
