from ...resource import AsureWebsocket
from abc import abstractmethod

class AsureBaseWebsocket:
    
    @abstractmethod
    async def handler(self, websocket :AsureWebsocket):
        pass 