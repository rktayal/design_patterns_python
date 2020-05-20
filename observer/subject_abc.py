import abc

from observer_abc import AbsObserver


class AbsSubject():
    __metaclass__ = abc.ABCMeta
    _observers = set()

    @abc.abstractmethod
    def attach(self, observer):
        if not isinstance(observer, AbsObserver):
            raise TypeError('Observer not derieved from AbsObserver')
        self._observers |= {observer}

    @abc.abstractmethod
    def detach(self, observer):
        self._observers -= {observer}

    @abc.abstractmethod
    def notify(self, value=None):
        for observer in self._observers:
            if value is None:
                observer.update()
            else:
                observer.update(value)
