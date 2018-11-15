#  Dump
import pickle
# from cPickle import pickle
# pickle = cPickle.pickle
# pickle.load = cPickle.pickle.load
import json


dct = {
    'firstname': 'John',
    'lastname': 'Smith'
}


# with open('data.p', 'wb') as f:
#     pickle.dump(dct, f)


with open('data.json', 'w') as f:
    json.dump(dct, f)
