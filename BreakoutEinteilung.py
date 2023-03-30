from numba import jit
from numba import types
from numba.typed import Dict
import numpy as np
import time


@jit(nopython=True)
def get_number_collisions(variant, groups):
    number_collisions = 0
    for participant, groups_participant in groups.items():
        for i in range(len(groups_participant)):
            for j in range(len(groups_participant)):
                if i >= j:
                    continue
                if variant[groups_participant[i] - 1] == variant[groups_participant[j] - 1]:
                    number_collisions += 1

    return number_collisions


def get_collisions(variant, groups):
    collisions = list()
    for participant, groups_participant in groups.items():
        for i in range(len(groups_participant)):
            for j in range(len(groups_participant)):
                if i >= j:
                    continue
                if variant[groups_participant[i] - 1] == variant[groups_participant[j] - 1]:
                    collisions.append(
                        [participant, groups_participant[i], groups_participant[j]])

    return collisions


@jit(nopython=True)
def number_to_base(n, b, m):
    digits = []
    for _ in range(m):
        digits.append(int(n % b))
        n //= b

    return np.asarray(digits)


@jit(nopython=True)
def check_variant(variant):
    k = 0
    for j in range(len(variant)):
        if variant[j] > k:
            return False
        if variant[j] == k:
            k += 1

    return True

# Determine the default integer type
default_int_type = np.asarray([0]).dtype

if default_int_type == np.int64:
    value_type = types.int64[:]
elif default_int_type == np.int32:
    value_type = types.int32[:]
else:
    raise Exception("Unknown data type")

groups = Dict.empty(
    key_type=types.unicode_type,
    value_type=value_type,
)


groups['Daniel'] = np.asarray([1, 8, 9, 15])
groups['Anne'] = np.asarray([3, 7, 8, 13])
groups['SebastianH'] = np.asarray([2, 4, 6, 10])
groups['Timur'] = np.asarray([1, 6, 8, 14])  
groups['Yves'] = np.asarray([5, 8, 9, 14])
groups['Jan'] = np.asarray([1,11, 5, 14])
groups['Hamideh']=np.asarray([1,8,3,12])
groups['Freddy']=np.asarray([2,3,4,10])
groups['Larissa']=np.asarray([1,13,14,15])
groups['Dominik']=np.asarray([5,8,11,1])
groups['Phi']=np.asarray([3,4,5,11])
groups['Martin'] = np.asarray([1,3,7,14])
groups['Nicolas'] = np.asarray([2,10,13,14])
groups['Emre'] = np.asarray([1, 3, 4, 10])
groups['Joerg'] = np.asarray([12,13,14])
groups['Kai'] = np.asarray([8,9,11,15])
groups['Lars'] = np.asarray([1,2,7,14])
groups['Maximilian'] = np.asarray([10,14,13,2])
groups['SebastianW'] = np.asarray([1,9,12,14])
groups['Snigdha'] = np.asarray([1, 8, 12, 13])
groups['Ralf'] =  np.asarray([1, 2, 7, 8])
groups['Martina'] = np.asarray([ 1, 14, 15])
groups['Thomas'] = np.asarray([ 1, 7, 11, 14])
groups['Christopher'] = np.asarray([ 2, 3, 10, 13])



number_breakout_slots = 4
minimal_number_collisions = 1000
number_groups = 15

start = time.time()
print("Started")

topics = [[] for _ in range(number_groups)]

for participant, groups_participant in groups.items():
    for i in groups_participant:
        topics[i-1].append(participant)

for i in range(len(topics)):
    print("Topic " + str(i+1) + ": " + str(topics[i]))

print("")

n = 0

# Iterate through all possible variants
for i in range(number_breakout_slots**(number_groups-0)):

    # Get current variant of breakout slots
    variant = number_to_base(i, number_breakout_slots, number_groups)

    if not check_variant(variant):
        continue

    number_collisions = get_number_collisions(variant, groups)

    # New minimum of collisions found?
    if number_collisions <= minimal_number_collisions:
        minimal_number_collisions = number_collisions
        print('Breakout Groups Assignments: ' + str(variant+1))
        print('Collisions: ' + str(get_collisions(variant, groups)))
        print('Number of Collisions: ' + str(number_collisions))
        print('')
        n += 1

end = time.time()
print(end - start)
print('Finished')
print(number_breakout_slots**number_groups)
# 3 slots: 4782969 varianten
# 4 slots: 268435456 varianten
print(n)
