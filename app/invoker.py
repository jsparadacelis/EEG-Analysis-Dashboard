import models


class Invoker:

    @classmethod
    def get_model(cls, model_type: str) -> models.IModel:
        if model_type == 'RL':
            return models.RegLog()
        elif model_type == 'NN':
            return models.NeuralNets()
        elif model_type == 'SVM':
            return models.SVM()
        else:
            return models.RegLog()
