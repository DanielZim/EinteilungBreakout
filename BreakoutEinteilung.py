def number_to_base(n, b, m):
    digits = []
    for _ in range(m):
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

groups = list()

groups.append(['Anne', 'Martina', 'Sandro',	'Thomas', 'Sofia', 'Yves', 'Heiko', 'Dominik F.', 'Angelika', 'Sophie', 'Hamideh', 'Daniel'])
groups.append(['Larissa', 'Timur', 'Sebastian H.', 'Sandro', 'Frederik', 'Maximilian', 'Dominik F.', 'Yves'	,'Sophie', 'Hamideh', 'Daniel', 'Angelika', 'Sofia', 'Manar'])
groups.append(['Sebastian H.', 'Stephan', 'Maximilian', 'Frederik', 'Roman', 'Emre', 'Robert', 'Christopher'])
groups.append(['Yves','Maximilian','Angelika','Timur','Jan', 'Christopher'])
groups.append(['Thomas'	,'Ralf'	,'Sandro',	'Angelika'	,'Snigdha'	,'Larissa',	'Timur','Sofia'	])
groups.append(['Sebastian H.', 'Ralf',	'Martina', 'Sandro', 'Max', 'Sofia', 'Stephan',	'Anne', 'Manar', 'Emre', 'Robert', 'Sebastian K.'])
groups.append(['Frederik',	'Max', 'Dominik W', 'Stephan', 'Robert', 'Sebastian K.'])
groups.append(['Larissa', 'Ralf', 'Dominik W', 'Anne', 'Daniel', 'Timur', 'Sebastian K.'])
groups.append(['Sebastian H.', 'Frederik', 'Stephan', 'Emre', 'Christopher', 'Snigda'])
groups.append(['Stephan',' Maximilian',	'Max' ,'Martina', 'Jan', 'Dominik W.', 'Larissa', 'Sebastian K.'])
groups.append(['Snighda', 'Hamideh'])
groups.append(['Daniel', 'Jan',	'Hamideh', 'Thomas'])
groups.append(['Yves', 'Snigdha', 'Anne', 'Jan', 'Manar'])
groups.append(['Martina', 'Max', 'Ralf', 'Robert', 'Manar', 'Thomas', 'Christopher'])

number_breakout_slots = 4
minimal_number_collisions = 10

# Iterate through all possible variants
for i in range(number_breakout_slots**len(groups)):

    # Get current variant of breakout slots
    variant = number_to_base(i, number_breakout_slots, len(groups))

    # Fill the slots with the participants
    slots = [[] for _ in range(number_breakout_slots)]
    for j in range(len(groups)):
        slots[variant[j]].extend(groups[j])

    # Get possible collisions of participants
    collisions = set()
    for slot in slots:
        for participant in slot:
            if slot.count(participant) > 1:
                collisions.add(participant)

    # New minimum of collisions found?
    if len(collisions) <= minimal_number_collisions:
        minimal_number_collisions = len(collisions)
        print(variant)
        print(collisions)
        print(len(collisions))
        print('')

print('finished')
print(number_breakout_slots**len(groups))
