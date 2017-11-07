import pickle

entry = {}
with open('serial.pickle', 'wb') as pickle_file:
    pickle.dump(entry, pickle_file)

with open('serial.pickle', 'rb') as pickle_file:
    entry = pickle.load(pickle_file)