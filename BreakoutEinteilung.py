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


groups = Dict.empty(
    key_type=types.unicode_type,
    value_type=types.int64[:],
)


groups['Ralf'] = np.asarray([1, 2, 5, 10])
groups['Daniel'] = np.asarray([3, 4, 5, 7])
groups['Timur'] = np.asarray([1, 3, 5, 2])
groups['Maximilian'] = np.asarray([8, 3, 10, 13])
groups['Yves'] = np.asarray([3, 8, 9, 13])
groups['Dominik F.'] = np.asarray([1, 5, 7])
groups["Manar"] = np.asarray([1, 6, 8, 9])
groups['Tobias'] = np.asarray([4, 5, 7])
groups['Sebastian H'] = np.asarray([3, 11])
groups['Joerg'] = np.asarray([11, 12, 13, 3])
groups["Sebastian K."] = np.asarray([8, 11, 12, 13])
groups['Martina'] = np.asarray([3, 6, 8, 13])
groups['Dominik W.'] = np.asarray([5, 11, 12, 13])
groups['Stephan'] = np.asarray([3, 5, 10, 11])
groups["Snigdha"] = np.asarray([6, 8, 13, 9])
groups['Larissa'] = np.asarray([6, 2, 11, 13])
groups['Sofia'] = np.asarray([1, 2, 6, 13])
groups["Roman"] = np.asarray([5, 10])
groups["Frederik"] = np.asarray([3, 10])
groups['Max'] = np.asarray([3, 11, 12, 13])
groups['Hamideh'] = np.asarray([1, 2, 4, 6])
groups['Heiko'] = np.asarray([1, 2, 3, 9])
groups['Robert'] = np.asarray([10, 3, 12, 13])
groups['Emre'] = np.asarray([1, 3, 10, 11])
groups['Christopher'] = np.asarray([3])
groups['Jan'] = np.asarray([1, 4, 5, 7])
groups['Angelika'] = np.asarray([2, 5, 6, 7])
groups['Sophie'] = np.asarray([1, 5])
groups['Sandro'] = np.asarray([1, 3, 11, 12])
groups['Thomas'] = np.asarray([1, 3, 7, 9])
groups['Anne'] = np.asarray([1, 6, 9, 13])


number_breakout_slots = 4
minimal_number_collisions = 1000
number_groups = 13

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
