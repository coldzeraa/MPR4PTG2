from abc import ABC, abstractmethod
from django.db.models import AutoField

class Service(ABC):

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def store(self):
        pass

    @abstractmethod
    def get(self, id:AutoField):
        pass
    
    
    