from Metric import Metric
from Precision import Precision
from Recall import Recall

class F1(Metric):
    @classmethod
    def calculate(self, true_positive, true_negative, false_positive, false_negative):
        precision = Precision().calculate(true_positive, true_negative, false_positive, false_negative)
        recall = Recall().calculate(true_positive, true_negative, false_positive, false_negative)
        return 2 * (precision * recall) / (precision + recall)