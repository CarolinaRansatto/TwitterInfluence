import pickle


def load_network():
    return pickle.load(open('files/network.graph', 'rb'))
