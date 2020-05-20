import abc


class AbsObserver():
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def update(self, value):
        pass
