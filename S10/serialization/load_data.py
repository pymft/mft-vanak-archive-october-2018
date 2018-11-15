# Load
import pickle
import json

# with open('data.p', 'rb') as f:
#     dct = pickle.load(f)


with open('data.json', 'r') as f:
    dct = json.load(f)


print(dct, type(dct))

