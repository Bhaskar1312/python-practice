from abc import ABC, abstractmethod
# abstract base class

class InvalidOperationError(Exception):
    pass

class Stream(ABC):
    def __init__(self):
        self.opened = False
    def open(self):
        if self.opened:
            raise InvalidOperationError("Stream already opened")
        self.opened = True
    def close(self):
        if not self.opened:
            raise InvalidOperationError("Stream already closed")
        self.opened = False
    
    @abstractmethod
    def read(self): #Can't instantiate abstract class Stream with abstract method read
        pass

class FileStream(Stream):
    def read(self):
        print("Reading data from a file")

class NetworkStream(Stream):
    # pass
    def read(self):
        print("Reading data from a network") # if we dont implement abstract method, it will give error
    
# st = Stream()
# st.open()
# st.read()

fst = FileStream()
fst.read()

nst = NetworkStream()
nst.read()
