import json
from TestMultiLayer import test_digits, test_parity, test_xor

def main():
    with open('./config.json') as f:
        config = json.load(f)

    if config["type"] == "xor":
        test_xor(config["neurons_per_layer"], config["learning_rate"], config["batch"], config["epochs"], config["epsilon"])

    if config["type"] == "parity":
        test_parity(config["neurons_per_layer"], config["expansion"], config["split_percentage"], config["learning_rate"], config["batch"], config["epochs"], config["epsilon"])


    if config["type"] == "digits":
        print("neurons_per_layer: ", config["neurons_per_layer"])
        test_digits(config["neurons_per_layer"], config["expansion"], config["split_percentage"], config["learning_rate"], config["batch"], config["epochs"], config["epsilon"])

if __name__ == '__main__':
    main()