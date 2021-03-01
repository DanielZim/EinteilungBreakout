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
                    collisions.append([participant, groups_participant[i], groups_participant[j]])

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


groups = Dict.empty(
    key_type=types.unicode_type,
    value_type=types.int32[:],
)

groups['Angelika'] = np.asarray([1, 2, 4, 5])
groups['Anne'] = np.asarray([1, 6, 8, 12])
groups['Christopher'] = np.asarray([3, 4, 9, 13])
groups['Daniel'] = np.asarray([1, 2, 8, 11])
groups['Dominik F.'] = np.asarray([1, 2])
groups['Dominik W.'] = np.asarray([7, 8, 10])
groups['Emre'] = np.asarray([3, 9])
groups['Frederik'] = np.asarray([3, 6, 7, 9])
groups['Hamideh'] = np.asarray([1, 2, 9, 11])
# groups['Heiko'] = 1
groups['Jan'] = np.asarray([4, 10, 11, 12])
groups['Larissa'] = np.asarray([2, 4, 8, 10])
groups['Manar'] = np.asarray([2, 6, 12, 13])
groups['Martina'] = np.asarray([1, 6, 10, 13])
groups['Max'] = np.asarray([6, 7, 10, 13])
groups['Maximilian'] = np.asarray([2, 3, 4, 10])
groups['Ralf'] = np.asarray([5, 6, 8, 13])
groups['Robert'] = np.asarray([3, 6, 7, 13])
# groups['Roman'] = 3
groups['Sandro'] = np.asarray([1, 2, 5, 6])
groups['Sebastian H.'] = np.asarray([2, 3, 6, 9])
groups['Sebastian K.'] = np.asarray([6, 7, 8, 10])
groups['Snigdha'] = np.asarray([2, 5, 9, 12])
groups['Sofia'] = np.asarray([1, 2, 5, 6])
groups['Sophie'] = np.asarray([1, 2])
groups['Stephan'] = np.asarray([3, 6, 7, 10])
groups['Timur'] = np.asarray([2, 4, 5, 8])
groups['Thomas'] = np.asarray([1, 5, 11, 13])
groups['Yves'] = np.asarray([1, 2, 4, 12])


number_breakout_slots = 4
minimal_number_collisions = 1000
#number_groups = 13
number_groups = 13

start = time.time()
print("Started")

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
