from Metric import Metric

class Recall(Metric):
    @classmethod
    def calculate(self, true_positive, true_negative, false_positive, false_negative):
        return true_positive / (true_positive + false_negative)