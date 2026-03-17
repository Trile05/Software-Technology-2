move_count = 0

def main():
    global move_count

    n = int(input("Enter number of disks: "))

    print("The moves are:")
    moveDisks(n, 'A', 'B', 'C')

    print("Total number of moves:", move_count)


def moveDisks(n, fromTower, toTower, auxTower):

    global move_count

    if n == 1:
        print("Move disk", n, "from", fromTower, "to", toTower)
        move_count += 1

    else:
        moveDisks(n - 1, fromTower, auxTower, toTower)

        print("Move disk", n, "from", fromTower, "to", toTower)
        move_count += 1

        moveDisks(n - 1, auxTower, toTower, fromTower)


main()