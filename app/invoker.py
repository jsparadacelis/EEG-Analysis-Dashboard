import models


class Invoker:

    @classmethod
    def get_model(cls, exams_quantity: int, model_type: str) -> models.IModel:
        if model_type == 'RL':
            return models.RegLog()
        elif model_type == 'NN':
            return models.NeuralNets(exams_quantity)
        elif model_type == 'SVM':
            return models.SVM()
        else:
            return models.RegLog()
