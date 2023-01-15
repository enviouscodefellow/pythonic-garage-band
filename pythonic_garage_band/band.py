import pytest

class Musician:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return f"My name is {self.name} and I play {self.get_instrument()}"
    
    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}"
    
    def get_instrument(self):
        pass
    
    def play_solo(self):
        pass

class Guitarist(Musician):
    def get_instrument(self):
        return "guitar"
    
    def play_solo(self):
        return "face melting guitar solo"

class Bassist(Musician):
    def get_instrument(self):
        return "bass"
    
    def play_solo(self):
        return "bom bom buh bom"

class Drummer(Musician):
    def get_instrument(self):
        return "drums"
    
    def play_solo(self):
        return "rattle boom crash"

class Band:
    band_list = []
    
    def __init__(self, name, members):
        self.name = name
        self.members = members
        self.band_list.append(self)
    
    def __str__(self):
        return f"{self.name} is a band made up of {[member.name for member in self.members]}"
    
    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}, Members = {[member.name for member in self.members]}"
    
    def play_solos(self):
        solos = []
        for member in self.members:
            solos.append(member.play_solo())
        return solos
            
    @classmethod
    def to_list(cls):
        return cls.band_list
