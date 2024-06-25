import random

import numpy as np

from MultiLayer import MultiLayer

class TrainingUtils:

    @staticmethod
    def generate_batches(characters, batch_size):
        batch_size = max(batch_size, 1)

        num_complete_batches, remainder = divmod(len(characters), batch_size)

        random.shuffle(characters)

        batches = [characters[i * batch_size:(i + 1) * batch_size] for i in range(num_complete_batches)]

        if remainder:
            last_batch = characters[num_complete_batches * batch_size:]
            random_fill = random.sample(characters, batch_size - remainder)
            last_batch.extend(random_fill)
            batches.append(last_batch)

        return batches

    @staticmethod
    def add_noise(data, noise_factor):
        for i in range(len(data)):
            if random.random() < noise_factor:
                data[i] = data[i] * -1
        return data
