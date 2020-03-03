def number_to_base(n, b, m):
    digits = []
    for _ in range(m):
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


groups = list()
groups.append(['Nico Kopp', 'Erik Burger', 'Timur Sağlam', 'Sofia Ananieva'])
groups.append(['Anne Koziolek', 'Snigdha Singh', 'Martina Rapp', 'Daniel Zimmermann', 'Heiko Klare', 'Larissa Schmid', 'Ralf Reussner'])
groups.append(['Frederik Reiche', 'Robert Heinrich', 'Roman Pilipchuk', 'Emre Taşpolatoğlu', 'Maximilian Walter', 'Stephan Seifermann'])
groups.append(['Yves Schneider', 'Manar Mazkatli', 'Jörg Henß', 'Jan Keim', 'Sebastian Hahner', 'Sebastian Krach'])
groups.append(['Maximilian Walter', 'Snigdha Singh', 'Daniel Zimmermann', 'Jan Keim', 'Robert Heinrich', 'Roman Pilipchuk'])
groups.append(['Erik Burger', 'Nico Kopp', 'Sofia Ananieva', 'Timur Sağlam', 'Heiko Klare', 'Ralf Reussner', 'Manar Mazkatli'])
groups.append(['Emre Taşpolatoğlu', 'Frederik Reiche', 'Stephan Seifermann'])
groups.append(['Sebastian Krach', 'Martina Rapp', 'Jörg Henß', 'Yves Schneider', 'Larissa Schmid', 'Sebastian Hahner'])
groups.append(['Jörg Henß', 'Nico Kopp', 'Erik Burger', 'Manar Mazkatli', 'Sofia Ananieva'])
groups.append(['Stephan Seifermann', 'Frederik Reiche', 'Daniel Zimmermann', 'Yves Schneider', 'Jan Keim'])
groups.append(['Ralf Reussner', 'Sebastian Hahner', 'Heiko Klare', 'Emre Taşpolatoğlu', 'Timur Sağlam', 'Maximilian Walter'])
groups.append(['Martina Rapp', 'Anne Koziolek', 'Robert Heinrich', 'Sebastian Krach', 'Larissa Schmid'])

number_breakout_slots = 3
minimal_number_collisions = 5

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

print('finished')
print(number_breakout_slots**len(groups))
