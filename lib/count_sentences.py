#!/usr/bin/env python3
import re
class MyString:
    def __init__(self, value=''):
        self.value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, value):
        if (type(value) not in (str,)):
            print("The value must be a string.")
        else:
            self._value = value
            
    def is_sentence(self):
        return self.value[-1] == '.'
    
    def is_question(self):
        return self.value[-1] == '?'
    
    def is_exclamation(self):
        return self.value[-1] == '!'
    
    def count_sentences(self):
        return len(re.findall('\w\.|\w\?|\w\!', self.value))