import numpy as np
import h5py

''' Use this to take all the individual month data files(.npz),
    merge and convert them into a large year data h5 file
'''


fns = ['2015-01-data.npz',
       '2015-02-data.npz',
       '2015-03-data.npz',
       '2015-04-data.npz',
       '2015-05-data.npz',
       '2015-06-data.npz',
       '2015-07-data.npz',
       '2015-08-data.npz',
       '2015-09-data.npz',
       '2015-10-data.npz',
       '2015-11-data.npz',
       '2015-12-data.npz']

print("loading from: ", fns[0])
taxi = np.load(fns[0])

data = taxi['data']
date = taxi['date']

for fn in fns[1:]:
    print("Loading from: ", fn)
    taxi = np.load(fn)
    data = np.concatenate((data, taxi['data']), axis=0)
    date = np.concatenate((date, taxi['date']), axis=0)

print(data.shape)
print(date.shape)

print("Saving to STResnet h5py...")


with h5py.File('NYC15_M10x20_T30_InOut.h5', 'w') as f:
    f.create_dataset("data", data=data)
    f.create_dataset("date", data=date.astype(np.bytes_), dtype='S10')
