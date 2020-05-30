n = int(input())
capacity = 255
current_volume = 0
for counter in range(n):
    liters = int(input())
    current_volume += liters
    if liters > capacity or current_volume > capacity:
        print('Insufficient capacity!')
        current_volume -= liters
        continue

print(current_volume)

