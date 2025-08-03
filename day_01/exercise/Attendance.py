from os import remove

attendee_names = []

remove_name = 'Jimwel'.lower()

attendee_count = int(input('Attendance count: '))

for attendee in range(attendee_count):
    attendee_name = input('Attendee name: ').lower()
    attendee_names.append(attendee_name)
    print(attendee_names)

if remove_name in attendee_names:
    attendee_names.remove(remove_name)
    print(attendee_names)

last_remove = attendee_names.pop(-1)
print(attendee_names)
print(last_remove)
