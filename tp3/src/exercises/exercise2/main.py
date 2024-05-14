import json
from test_non_linear import test_non_linear

def main():
    with open('./config.json') as f:
        config = json.load(f)

    test_non_linear(config["learning_rate"], config["batch"], config["epochs"], config["epsilon"], config["activation_function"])

if __name__ == '__main__':
    main()