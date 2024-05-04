from src.exercises.exercise3 import Metric
from src.exercises.exercise3 import Precision
from src.exercises.exercise3 import Recall

class F1(Metric):
    
    def calculate(self, true_positive, true_negative, false_positive, false_negative):
        precision = Precision().calculate(true_positive, true_negative, false_positive, false_negative)
        recall = Recall().calculate(true_positive, true_negative, false_positive, false_negative)
        return 2 * (precision * recall) / (precision + recall)