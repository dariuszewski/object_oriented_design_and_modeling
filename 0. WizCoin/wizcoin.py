import collections.abc
from multiprocessing.sharedctypes import Value
import operator


class WizCoinException(Exception):
    pass

class WizCoin:
    def __init__(self, galleons, sickles, knuts):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def weight(self, unit='grams'):
        weight_in_grams = (self.galleons * 33.103) + (self.sickles * 11.34) + (self.knuts * 5.0)
        if unit == 'grams':
            return weight_in_grams
        elif unit == 'kilograms':
            return weight_in_grams * 0.0001
        else:
            raise ValueError("unit must be 'grams' or 'kilograms'")

    @property
    def galleons(self):
        return self._galleons
    
    @galleons.setter
    def galleons(self, value):
        if not isinstance(value, int):
            raise WizCoinException('galleons must be int, not ' + value.__class__.__qualname__)
        if value < 0:
            raise WizCoinException('galleons must be positive integer, not ' + value.__class__.__qualname__)
        self._galleons = value

    @property
    def sickles(self):
        return self._sickles
    
    @sickles.setter
    def sickles(self, value):
        if not isinstance(value, int):
            raise WizCoinException('sickles must be int, not ' + value.__class__.__qualname__)
        if value < 0:
            raise WizCoinException('sickles must be positive integer, not ' + value.__class__.__qualname__)
        self._sickles = value
    
    @property
    def knuts(self):
        return self._knuts
    
    @knuts.setter
    def knuts(self, value):
        if not isinstance(value, int):
            raise WizCoinException('knuts must be int, not ' + value.__class__.__qualname__)
        if value < 0:
            raise WizCoinException('knuts must be positive integer, not ' + str(value))
        self._knuts = value

    @property
    def total(self):
        return (self.galleons * 17 * 29) + (self.sickles * 29) + (self.knuts)

    def __repr__(self):
        return f"{self.__class__.__qualname__}({self.galleons}, {self.sickles}, {self.knuts})"

    def __str__(self):
        return f"{self.galleons} galleons, {self.sickles} sicles, {self.knuts} knuts"

    def __add__(self, other):
        if not isinstance(other, WizCoin):
            return NotImplemented
        return WizCoin(other.galleons + self.galleons, other.sickles +
         self.sickles, other.knuts + self.knuts)
    
    def __mul__(self, other):
        if not isinstance(other, int):
            return NotImplemented
        if other < 0:
            raise WizCoinException('cannot multiple by negative integer')
        return WizCoin(self.galleons * other, self.sickles * other, self.knuts * other)
    
    def __rmul__(self, other):
        return self.__mul__(other)

    def __iadd__(self, other):
        if not isinstance(other, WizCoin):
            return NotImplemented
        
        self.galleons += other.galleons
        self.sickles += other.sickles
        self.knuts += other.knuts

        return self

    def __imul__(self, other):
        if not isinstance(other, int):
            return NotImplemented        
        if other < 0:
            raise WizCoinException('cannot multiple by negative integer')

        self.galleons *= other
        self.sickles *= other
        self.knuts *= other
        return self

    def __sub__(self, other):
        if not isinstance(other, WizCoin):
            return NotImplemented
        return WizCoin(self.galleons - other.galleons, self.sickles -
         other.sickles, self.knuts - other.knuts)        

    def __isub__(self, other):
        if not isinstance(other, WizCoin):
            return NotImplemented
        
        self.galleons -= other.galleons
        self.sickles -= other.sickles
        self.knuts -= other.knuts

        return self

    def __pow__(self, other):
        if isinstance(other, int):
            return WizCoin(self.galleons ** other, self.sickles ** other, self.knuts ** other)
        else:
            return NotImplemented


    def __ipow__(self, other):
        if isinstance(other, int):
            self.galleons **= other
            self.sickles **= other
            self.knuts **= other
        else:
            return NotImplemented

    def __int__(self):
        return self.total


    def __float__(self):
        return float(self.total)


    def __bool__(self):
        if self.galleons == 0 and self.sickles == 0 and self.knuts == 0:
            return False
        else:
            return True

    def __getitem__(self, key):
        if not isinstance(key, (int, slice)):
            raise TypeError(f'indices must be integers or slices, not {key.__class__.__qualname__}')

        slicer = [self.galleons, self.sickles, self.knuts]
        if isinstance(key, int):
            return slicer[key]
        elif isinstance(key, slice):
            return slicer[key.start:key.stop:key.step]


    def __setitem__(self, key, value):
        raise TypeError('item assignment not supported')


    def __delitem__(self, key):
        raise TypeError('item deletion not supported')
        
    def _comparisonHelperOperator(self, operatorFunc, other):

        if isinstance(other, WizCoin):
            return operatorFunc(self.total, other.total)
        elif isinstance(other, (int, float)):
            return operatorFunc(self.total, other)
        elif isinstance(other, collections.abc.Sequence):
            other_value = (other[0] * 17 * 29) + (other[1] * 29) + other[2]
            return operatorFunc(self.total, other_value)
        elif operatorFunc == operator.eq:
            return False
        elif operatorFunc == operator.ne:
            return True
        else:
            return NotImplemented

    
    def __eq__(self, other):
        return self._comparisonHelperOperator(operator.eq, other)

    def __ne__(self, other):
        return self._comparisonHelperOperator(operator.ne, other)

    def __lt__(self, other):
        return self._comparisonHelperOperator(operator.lt, other)

    def __le__(self, other):
        return self._comparisonHelperOperator(operator.le, other)

    def __gt__(self, other):
        return self._comparisonHelperOperator(operator.gt, other)

    def __ge__(self, other):
        return self._comparisonHelperOperator(operator.ge, other)
    
    def __len__(self):
        """The length of this object is the number of coins it has."""
        return self.galleons + self.sickles + self.knuts

    def change_to_galleons(self):
        while self.knuts >= 29:
            self.knuts -= 29
            self.sickles += 1
        while self.sickles >= 17:
            self.sickles -= 17
            self.galleons += 1

    def change_to_knuts(self):
        self.knuts += self.galleons * 29 * 17
        self.knuts += self.sickles * 17
        self.galleons = 0
        self.sickles = 0