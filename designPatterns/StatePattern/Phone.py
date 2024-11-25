from abc import abstractmethod, ABC


class Phone:
    def __init__(self):
        self._state = OffState(self)

    @property
    def get_state(self):
        return self._state

    def set_state(self, state):
        self._state = state

    def turnOn(self):
        return "Turning screen on, device still locked"

    def unlock(self):
        return "Unlock phone and go to home screen"

    def lock(self):
        return "Locking phone and turning off screen"

    def home(self):
        return "Go to home screen"


class State(ABC):
    def __init__(self, phone: Phone):
        self.phone = phone

    @abstractmethod
    def home(self):
        pass

    @abstractmethod
    def onOffOn(self):
        pass


class OffState(State):
    def __init__(self, phone: Phone):
        super().__init__(phone)

    def home(self):
        self.phone.set_state(LockedState(self.phone))
        return self.phone.turnOn()

    def onOffOn(self):
        self.phone.set_state(LockedState(self.phone))
        return self.phone.turnOn()


class LockedState(State):
    def __init__(self, phone: Phone):
        super().__init__(phone)

    def home(self):
        self.phone.set_state(ReadyState(self.phone))
        return self.phone.unlock()

    def onOffOn(self):
        self.phone.set_state(OffState(self.phone))
        return self.phone.lock()


class ReadyState(State):
    def __init__(self, phone: Phone):
        super().__init__(phone)

    def home(self):
        return self.phone.home()

    def onOffOn(self):
        self.phone.set_state(OffState(self.phone))
        return self.phone.lock()