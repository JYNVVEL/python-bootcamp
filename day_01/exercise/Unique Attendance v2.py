attendee_names = set()



attendee_count = int(input('Attendee count: '))

for attendee in range(attendee_count):
    attendee_name = input('Attendee name: ')
    attendee_names.add(attendee_name)

name = 'Jimwel'
attendee_names.discard(name)
print(f"Discarded name: {name}")
print(attendee_names)

random_winner = attendee_names.pop()
print(f'Random Winner: {random_winner}')
