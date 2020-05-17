# This is the Strategy Interface which will deal with the context
from abc import ABCMeta, abstractmethod


class AbsStrategy():
    __metaclass__ = ABCMeta

    @abstractmethod
    def calculate(self, order):
        """Calculate shipping cost"""
