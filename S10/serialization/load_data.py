# Load
import pickle


with open('data.p', 'rb') as f:
    dct = pickle.load(f)


print(dct, type(dct))

