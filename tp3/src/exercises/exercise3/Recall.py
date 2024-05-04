from src.exercises.exercise3 import Metric

class Recall(Metric):

    def calculate(self, true_positive, true_negative, false_positive, false_negative):
        return true_positive / (true_positive + false_negative)