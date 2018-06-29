import dbus
import subprocess

from galicaster.core import context

dispatcher = context.get_dispatcher()
logger = context.get_logger()

def init():
    SussexKeyboard()

class SussexKeyboard(object):
    def __init__(self):
        self.onboard_process = None
        self.session_bus = dbus.SessionBus()

        if not dispatcher.is_signal('sussexkeyboard-started'):
            logger.info('Adding sussexkeyboard-started signal')
            dispatcher.add_new_signal('sussexkeyboard-started')
        dispatcher.connect('gc-shown', self.configure_keyboard)
        dispatcher.connect('quit', self.unconfigure_keyboard)

    def configure_keyboard(self, dispatcher=None):
        logger.debug('Starting onboard...')
        self.onboard_process = subprocess.Popen(['onboard'])
        logger.info('Started onboard, pid: {}'.format(self.onboard_process.pid))

        logger.debug('Listening for onboard dbus registration')
        self.session_bus.add_signal_receiver(self.keyboard_started, path='/org/onboard/Onboard/Keyboard', dbus_interface='org.freedesktop.DBus.Properties')

    def keyboard_started(self, *args, **kwargs):
        logger.debug('Onboard is ready, removing dbus listener')
        self.session_bus.remove_signal_receiver(self.keyboard_started, path='/org/onboard/Onboard/Keyboard', dbus_interface='org.freedesktop.DBus.Properties')

        logger.debug('Dispatching sussexkeyboard-started signal')
        dispatcher.emit('sussexkeyboard-started')

    def unconfigure_keyboard(self, dispatcher=None):
        logger.debug('Killing onboard')
        if self.onboard_process:
            self.onboard_process.kill()
            logger.info('Killed onboard')
