from abc import abstractmethod,ABC

# modelo 

class LLMPort(ABC):

    @abstractmethod
    async def strutured(self,propmt,schema):
        pass

    @abstractmethod    
    async def vision(self,prompt,image,schema):
        pass
