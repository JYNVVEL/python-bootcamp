invited = {'Ana', 'Ben', 'Carlo', 'Dani'}
attended = {'Ben', 'Carlo', 'Ely'}

involved = invited.union(attended)
print(f"Involved Members: {involved}")

absent = invited.difference(attended)
print(f"Absent: {absent}")

gatecrashed = attended.difference(invited)
print(f"Gatecrashed: {gatecrashed}")

invited_and_attended = invited.intersection(attended)
print(f"Attended properly: {invited_and_attended}")