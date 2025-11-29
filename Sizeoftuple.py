tup = (0, 1, 2, 'a', 3)
print(len(tup))

#Using sys.getsizeof()
import sys
tup = (0, 1, 2, 'a', 3)
print(sys.getsizeof(tup))
#Using memoryview()

tup = (0, 1, 2,'a', 3)
res = memoryview(bytearray(str(tup),'utf-8'))
print(res.nbytes)

#Using id()
tup = (0, 1, 2, 'a', 3)
for item in tup:
    print(f"Memory address of {item}: {id(item)}")


#Using __sizeof__()
tup = (0, 1, 2, 'a', 3)
print(tup.__sizeof__())   

#Using pickle
import pickle
tup = (0, 1, 2, 'a', 3)
pickled_tup = pickle.dumps(tup)
print(len(pickled_tup))

#Using Pympler
from pympler import asizeof
tup = (0, 1, 2, 'a', 3)
print(asizeof.asizeof(tup))

#Using dataclasses
from dataclasses import dataclass
@dataclass
class TupleData:
    data: tuple
tup_data = TupleData((0, 1, 2, 'a', 3))
print(sys.getsizeof(tup_data))
