from abc import ABC, abstractmethod
 
class ConversationStage(ABC):
    @abstractmethod
    def start(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass