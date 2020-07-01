from abc import ABC, abstractmethod

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

from data import get_eeg_exams


class IModel(ABC):

    def __init__(self, exams_quantity: int):
        self.data_source = '../all.csv'
        samples, targets = get_eeg_exams(self.data_source)
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(
            samples, targets, test_size=0.3, random_state=50
        )

    @abstractmethod
    def train(self):
        pass


class RegLog(IModel):

    def __init__(self):
        super().__init__()

    def train(self):
        """ Trains data from data source throught LogReg classifier
            from Sckilearn
        """
        classifier = LogisticRegression(
            random_state=0, C=1, solver='lbfgs', penalty='l2'
        ).fit(self.x_train, self.y_train)
        y_pred = classifier.predict(self.x_test)
        classifier.score(self.x_test, self.y_test)


class NeuralNets(IModel):

    def __init__(self, exams_quantity: int):
        super().__init__(exams_quantity)


class SVM(IModel):

    def __init__(self):
        pass
