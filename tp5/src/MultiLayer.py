import numpy as np
from Accuracy import Accuracy
from F1 import F1
from Precision import Precision
from Recall import Recall
from Layer import Layer
from Adam import Adam

metric_functions = {
'F1': F1,
'recall': Recall,
'precision': Precision,
'accuracy': Accuracy
}

class MultiLayer:
    def __init__(self, neurons_per_layer, activation_function, activation_derivative, learning_rate, optimizer, weights = None):
        self.layers = []
        self.activation_function = activation_function
        self.activation_derivative = activation_derivative
        self.loss_function = (lambda x, y: np.mean(np.power(x - y, 2)))
        self.loss_derivative = (lambda x, y: y - x)
        self.learning_rate = learning_rate
        self.optimizer = Adam
        for i in range(0, len(neurons_per_layer) - 1):
            input_qty = neurons_per_layer[i] #+ 1
            output_qty = neurons_per_layer[i + 1]
            optimizer = self.optimizer(learning_rate)
            self.layers.append(Layer(input_qty, output_qty, learning_rate, optimizer, activation_function, activation_derivative, weights))
        
        # for i in range(0, len(neurons_per_layer) - 1):
        #     if i == len(neurons_per_layer) - 2:
        #         rows = neurons_per_layer[i] + 1
        #         cols = neurons_per_layer[i + 1]
        #         if weights is None:
        #             self.layers.append(Output(rows, cols, learning_rate, output_func, output_derivative, np.random.uniform(-1, 1, size=(rows, cols))))
        #         else:
        #             self.layers.append(Output(rows, cols, learning_rate, output_func, output_derivative, weights))
        #     else:
        #         rows = neurons_per_layer[i] + 1
        #         cols = neurons_per_layer[i + 1]
        #         self.layers.append(Intermediate(rows, cols, learning_rate, intermediate_func, intermediate_derivative, np.random.uniform(-1, 1, size=(rows, cols))))

    def forward_propagation(self, input):
        for layer in self.layers:
            # input_copy = []
            # input_copy.append(1) # SACAR BIAS?
            # for i in range(0, len(input)):
            #     input_copy.append(input[i])

            input = layer.activate(input)
        return input
    
    def back_propagation(self, deltas):
        # self.layers[-1].set_deltas(deltas)
        # for i in range(len(self.layers) - 2, -1, -1):
        #     deltas = self.layers[i].set_deltas(self.layers[i + 1].get_deltas(), self.layers[i + 1].get_weights()[1:])
        last_delta = deltas
        deltas_w = []
        last_delta_to_return = None
        for i in range(len(self.layers) - 1, -1, -1):
            input_error, new_deltas, delta_w = self.layers[i].backward_no_store(last_delta)
            last_delta = input_error
            last_delta_to_return = new_deltas
            deltas_w.append(delta_w)

        deltas_w.reverse()
        return deltas_w, last_delta_to_return


    def update_weights(self, epoch, deltas_w):
        for i in range(len(self.layers)):
            self.layers[i].update_weights(deltas_w[i], epoch) # revisar metodos de optimizacion
            # self.layers[i].weights += self.learning_rate * deltas_w[i]
    #     new_weights = []
    #     for layer in self.layers:
    #         layer.update_weights()
    #         new_weights.append(layer.get_weights())
    #     return new_weights

    
    def test_forward_propagation(self, input):
    #     if weights is not None:
    #         for i in range(0, len(self.layers)):
    #             self.layers[i].set_weights(weights[i])
    #     for layer in self.layers:
    #         input_copy = []
    #         input_copy.append(1)
    #         for i in range(0, len(input)):
    #             input_copy.append(input[i])
    #         input = layer.test_activate(input_copy)
    #     return input
        result = input
        for layer in self.layers:
            result = layer.activate(result)
        return result

    
    def calculate_error(self, data, expected):
        # error = 0
        # for i in range(0, len(data)):
        #     output = self.test_forward_propagation(data[i])
        #     for j in range(0, len(output)):
        #         error += ((expected[i][j] - output[j]) ** 2) / 2
        # return error
        error = 0
        result = self.test(data)[0]
        for i in range(0, len(result)):
            count = 0
            result[i] = result[i].round().astype(int)
            for j in range(0, len(result[i])):
                if result[i][j] != expected[i][j]:
                    count += 1
                if count > error:
                    error = count
        return error
    
    def set_delta_w(self):
        new_weights = []
        for layer in self.layers:
            layer.set_delta_w()
            new_weights.append(layer.get_weights())
        return new_weights
    
    def get_weights(self):
        weights = []
        for layer in self.layers:
            weights.append(layer.get_weights())
        return weights
    
    def train(self, training_data, expected_data, max_epochs, testing_data, testing_expected):

        training_set = np.array(training_data)
        expected_set = np.array(expected_data)
        all_errors = []
        pixel_errors = []
        computed_error = None
        epoch = 0
        
        while epoch < max_epochs:
            err = 0
            for i in range(0, len(training_set)):
                output = training_set[i]
                for layer in self.layers:
                    output = layer.activate(output)
                err += self.loss_function(expected_set[i], output)
                error = self.loss_derivative(expected_set[i], output)
                for layer in reversed(self.layers):
                    error = layer.backward(error, epoch)
            err /= len(training_set)
            computed_error = self.calculate_error(testing_data, testing_expected)
            
            if epoch % 10000 == 0:
                print(f'Epoch: {epoch} - Error: {computed_error} ')
            
            if epoch % 1000 == 0:
                all_errors.append(err)
                pixel_errors.append(computed_error)

            if computed_error == 1:
                break  
            
            epoch += 1
        return all_errors , pixel_errors
        
        
    def test(self, test_data):
        test_set = [test_data]
        results = []
        for i in range(0, len(test_set)):
            output = test_set[i]
            for layer in self.layers:
                output = layer.activate(output)
            results.append(output)
        return results