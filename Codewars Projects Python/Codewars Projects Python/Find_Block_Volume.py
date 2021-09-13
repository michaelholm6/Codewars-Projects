def find_nb(m):
    mass = 0
    level = 1
    while (not mass == m):
        mass += level**3
        level += 1
        if mass > m:
            level = 0
            break
    print (level-1)

find_nb(24723578342962)
