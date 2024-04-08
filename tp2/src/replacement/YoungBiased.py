from src.replacement.Replacement import Replacement

class YoungBiased(Replacement):
    @staticmethod
    def replace(population, children, selection1, selection2, B):
        n_children = len(children)
        n_population = len(population)
        if n_children > n_population:
            return selection1.select(children, B * n_population) + selection2.select(children, (1 - B) * n_population)
        else:
            return children + selection1.select(population, B * (n_population-n_children)) + selection2.select(population, (1 - B) * (n_population-n_children))