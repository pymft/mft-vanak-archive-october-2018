#  Dump
import pickle

dct = {
    'firstname': 'John',
    'lastname': 'Smith'
}


with open('data.p', 'wb') as f:
    pickle.dump(dct, f)
