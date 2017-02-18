import linphone
import logging
from pyee import EventEmitter

class Phone(EventEmitter):
    def __init__(self):
        EventEmitter.__init__(self)

        linphone.set_log_handler(self._logHandler)
        callbacks = {'call_state_changed': self._callStateHandler}
        self.core = linphone.Core.new(callbacks, None, None)

        self.core.max_calls = 1
        self.core.ring = '/usr/share/sounds/linphone/rings/oldphone.wav'
        self.core.ring_level = 100
        self.core.echo_cancellation_enabled = False
        self.core.echo_limiter_enabled = False
        self.core.video_capture_enabled = False
        self.core.video_display_enabled = False
        self.core.video_preview_enabled = False

    def getSoundDevices(self):
        return [(d, self.core.sound_device_can_playback(d), self.core.sound_device_can_capture(d)) for d in self.core.sound_devices]

    def setSoundDevices(self, spk, mic, ring):
        self.core.playback_device = spk
        self.core.capture_device = mic
        self.core.ringer_device = ring

    def register(self, config):
        self.proxyCfg = self.core.create_proxy_config()
        self.proxyCfg.identity_address = self.core.create_address('sip:{0}@{1}'.format(config.SIP_USERNAME, config.SIP_DOMAIN))
        self.proxyCfg.server_addr = config.SIP_SERVER
        self.core.add_proxy_config(self.proxyCfg)
        self.authInfo = self.core.create_auth_info(config.SIP_USERNAME, None, config.SIP_PASSWORD, None, None, config.SIP_DOMAIN)
        self.core.add_auth_info(self.authInfo)

    def isRegistered(self):
        return self.proxyCfg.state == linphone.RegistrationState.Ok

    def loop(self):
        self.core.iterate()

    def accept(self):
        call = self.core.current_call
        if call is None or call.state != linphone.CallState.IncomingReceived:
            return False
        self.core.accept_call(call)
        return True

    def decline(self):
        call = self.core.current_call
        if call is None or call.state != linphone.CallState.IncomingReceived:
            return False
        self.core.decline_call(call, linphone.Reason.Declined)
        return True

    def hangup(self):
        self.core.terminate_all_calls()

    def _logHandler(self, level, msg):
        method = getattr(logging, level)
        method(msg)

    def _callStateHandler(self, core, call, state, msg):
        remoteUri = call.remote_address.as_string_uri_only()
        if state == linphone.CallState.IncomingReceived:
            print 'Incoming call from {0}'.format(remoteUri)
            self.emit('incoming', remoteUri)
        elif state == linphone.CallState.Connected:
            print 'Connected with {0}'.format(remoteUri)
            self.emit('connected', remoteUri)
        elif state == linphone.CallState.End:
            print 'Call with {0} ended'.format(remoteUri)
            self.emit('end', remoteUri)
        elif state == linphone.CallState.Released:
            print 'Call with {0} released'.format(remoteUri)
        else:
            print 'Event {0} for call from {0}'.format(state, remoteUri)
