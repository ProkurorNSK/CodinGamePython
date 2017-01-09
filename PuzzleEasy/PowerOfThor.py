light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
while True:
    remaining_turns = int(input())
    path = ""
    if initial_ty < light_y:
        path += "S"
        initial_ty += 1
    if initial_ty > light_y:
        path += "N"
        initial_ty -= 1
    if initial_tx < light_x:
        path += "E"
        initial_tx += 1
    if initial_tx > light_x:
        path += "W"
        initial_tx -= 1
    print(path)
