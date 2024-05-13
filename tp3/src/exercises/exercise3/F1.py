from Metric import Metric
from Precision import Precision
from Recall import Recall

class F1(Metric):
    @classmethod
    def calculate(self, true_positive, true_negative, false_positive, false_negative):
        precision = Precision().calculate(true_positive, true_negative, false_positive, false_negative)
        recall = Recall().calculate(true_positive, true_negative, false_positive, false_negative)
        if precision == 0 and recall == 0:
            return 0
        return 2 * (precision * recall) / (precision + recall)