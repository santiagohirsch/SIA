from Metric import Metric

class Precision(Metric):
    @classmethod
    def calculate(self, true_positive, true_negative, false_positive, false_negative):
        if true_positive == 0 and false_positive == 0:
            return 0
        return true_positive / (true_positive + false_positive)