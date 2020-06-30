from abc import ABC, abstractmethod


class IModel(ABC):

    def __init__(self):
        self.data_source = 'all'

    @abstractmethod
    def train(self):
        pass


class RegLog(IModel):

    def __init__(self):
        super().__init__()

    def train(self):
        print(self.data_source)


class NeuralNets(IModel):

    def __init__(self):
        pass


class SVM(IModel):

    def __init__(self):
        pass
