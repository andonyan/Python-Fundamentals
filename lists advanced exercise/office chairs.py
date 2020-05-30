number_of_rooms = int(input())
free_chairs = 0
all_rooms_have_free_chairs = True
for i in range(1, number_of_rooms + 1):
    tokens = input().split()
    chairs_in_room = tokens[0]
    chairs_occupied = int(tokens[1])
    if chairs_occupied > len(chairs_in_room):
        print(f'{chairs_occupied - len(chairs_in_room)} more chairs needed in room {i}')
        all_rooms_have_free_chairs = False
    else:
        free_chairs += len(chairs_in_room) - chairs_occupied

if all_rooms_have_free_chairs:
    print(f'Game On, {free_chairs} free chairs left')
