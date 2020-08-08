locations = ['barcelona', 'machu picchu', 'uyuni', 'guiana shield', 'ulruru']

print("元の順番")
print(locations)

print("\nアルファベット順")
print(sorted(locations))

print("\n元の順番")
print(locations)

print("\nアルファベットの逆順")
print(sorted(locations, reverse=True))

print("\n元の順番")
print(locations)

print("\n逆順")
locations.reverse()
print(locations)

print("\n元の順番")
locations.reverse()
print(locations)

print("\nアルファベット順")
locations.sort()
print(locations)

print("\nアルファベットの逆順")
locations.sort(reverse=True)
print(locations)
