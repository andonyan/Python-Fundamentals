N = int(input())
highest_snowballValue = 0
highest_snowballSnow = 0
highest_snowballTime = 0
highest_snowballQuality = 0

for counter in range(N):
    snowballSnow = int(input())
    snowballTime = int(input())
    snowballQuality = int(input())
    current_snowballValue = (snowballSnow / snowballTime) ** snowballQuality
    if current_snowballValue >= highest_snowballValue:
        highest_snowballValue = current_snowballValue
        highest_snowballSnow = snowballSnow
        highest_snowballTime = snowballTime
        highest_snowballQuality = snowballQuality

print(f'{highest_snowballSnow} : {highest_snowballTime} = {int(highest_snowballValue)} ({highest_snowballQuality})')