import random
import decimal
import math
from decimal import Decimal
class Qualean():
    '''
    Qualean class is inspired by Quantum+Boolean concepts. We can assign it only 3 possible real states. True, False, and
    Maybe (1, 0, -1) but it internally picks an imaginary state. The moment you assign it a real number, it immediately
    finds an imaginary number random.uniform(-1, 1) and multiplies with it and stores that number internally after using
    Bankers rounding to 10th decimal place.
    '''

    def __init__(self, number):
        '''Constructor function to build the Qualean object'''
        self.number = number

        if not number in [-1, 0, 1]:
            raise ValueError("Please provide only from these options [-1,0,1]")

        decimal.getcontext().prec = 10
        self.number = Decimal(number) * (Decimal(random.uniform(-1, 1)))

    def __str__(self):
        '''This method returns the str object of value of the Qualean object mentioned.'''
        return 'Qualean Number: {0}'.format(self.number)

    def __repr__(self):
        '''This method returns the representation of the Qualean object and the value it contains in a nicely
        formatted string.'''
        return 'Qualean Number({0})'.format(self.number)

    def __lt__(self, other):
        '''This method overrides the lesser than checking < for the user defined Qualean objects.'''
        if isinstance(other, Qualean):
            return (self.number < other.number)
        else:
            raise NotImplementedError

    def __gt__(self, other):
        '''This method overrides the greater than checking > for the user defined Qualean objects.'''
        if isinstance(other, Qualean):
            return (self.number > other.number)
        else:
            raise NotImplementedError

    def __eq__(self, other):
        '''This method overrides the equality checking == for the user defined Qualean objects.'''
        if isinstance(other, Qualean):
            return (self.number == other.number)
        else:
            raise NotImplementedError

    def __le__(self, other):
        '''This method overrides the lesser than or equal to checking <= for the user defined Qualean objects.'''
        if isinstance(other, Qualean):
            return (self.number <= other.number)
        else:
            raise NotImplementedError

    def __ge__(self, other):
        '''This method overrides the greater than or equal to checking >= for the user defined Qualean objects.'''
        if isinstance(other, Qualean):
            return (self.number >= other.number)
        else:
            raise NotImplementedError

    def __float__(self):
        '''This method returns the float conversion of the Qualean object.'''
        return float(self.number)

    def __invertsign__(self):
        '''This method returns the opposite sign of value of the calling Qualean object.'''
        if self.number != 0:
            return (-1) * (self.number)
        else:
            return (self.number)

    def __add__(self, other):
        '''This method overrides the basic implementation of addition + operator for the Qualean class.'''
        decimal.getcontext().prec = 10
        if isinstance(other, Qualean):
            return (self.number + other.number)
        else:
            raise NotImplementedError

    def __mul__(self, other):
        '''This method overrides the basic implementation of multiplication * operator for the Qualean class.'''
        decimal.getcontext().prec = 10
        if isinstance(other, Qualean):
            return (self.number * other.number)
        else:
            raise NotImplementedError

    def __bool__(self):
        '''This dunder method returns the bool value for the Qualean object.'''
        if self.number:
            return True
        else:
            return False

    def __and__(self, other):
        '''This method implements the logical and gate for the user defined Qualean objects'''
        if isinstance(other, Qualean):
            if self.number:
                return other.__bool__()
            else:
                return False
        else:
            raise NotImplementedError

    def __or__(self, other):
        '''This method implements the logical and gate for the user defined Qualean objects'''
        if isinstance(other, Qualean):
            if self.number:
                return True
            else:
                return other.__bool__()
        else:
            raise NotImplementedError

    def __sqrt__(self):
        '''This method implements the mathematical Square root operation on the Qualean object.'''
        if self.number >= 0:
            return (self.number).sqrt()
        else:
            return complex(0, (abs(self.number)).sqrt())
