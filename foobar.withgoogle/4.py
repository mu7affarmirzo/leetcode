"""
Bomb, Baby!
===========

You're so close to destroying the LAMBCHOP doomsday device you can taste it!
But in order to do so, you need to deploy special self-replicating bombs designed
for you by the brightest scientists on Bunny Planet. There are two types:
Mach bombs (M) and Facula bombs (F). The bombs, once released into the LAMBCHOP's inner workings,
will automatically deploy to all the strategic points you've identified and destroy them at the same time.

But there's a few catches. First, the bombs self-replicate via one of two distinct processes:
Every Mach bomb retrieves a sync unit from a Facula bomb; for every Mach bomb, a Facula bomb is created;
Every Facula bomb spontaneously creates a Mach bomb.

For example, if you had 3 Mach bombs and 2 Facula bombs,
they could either produce 3 Mach bombs and 5 Facula bombs, or 5 Mach bombs and 2 Facula bombs.
The replication process can be changed each cycle.

Second, you need to ensure that you have exactly the right number of
Mach and Facula bombs to destroy the LAMBCHOP device.
Too few, and the device might survive. Too many, and you might overload the mass capacitors
and create a singularity at the heart of the space station - not good!

And finally, you were only able to smuggle one of each type of bomb - one Mach,
one Facula - aboard the ship when you arrived, so that's all you have to start with.
(Thus it may be impossible to deploy the bombs to destroy the LAMBCHOP,
but that's not going to stop you from trying!)

You need to know how many replication cycles (generations)
it will take to generate the correct amount of bombs to destroy the LAMBCHOP.
Write a function solution(M, F) where M and F are the number of Mach and Facula bombs needed.
Return the fewest number of generations (as a string) that need to pass before you'll have the exact number
 of bombs necessary to destroy the LAMBCHOP, or the string "impossible" if this can't be done!
 M and F will be string representations of positive integers no larger than 10^50.
 For example, if M = "2" and F = "1", one generation would need to pass,
 so the solution would be "1". However, if M = "2" and F = "4", it would not be possible.
"""


def populate(m, f):
    m = int(m)
    f = int(f)
    option_1 = [str(m), str(m+f)]
    option_2 = [str(m+f), str(f)]

    return [option_1, option_2]


def generate_data(target, populated_data):
    # if index < 3:
    temp = []
    print(f"TARGET: {target}")
    for j in populated_data:

        a = populate(
            j[0], j[1]
        )
        if target in a:
            print(f" FOUND")
            return a, True
        print(f"------ berefor remove: {a}")
        remove_temp = a
        for k in remove_temp:
            print(f'')
            checker_num = int(k[0]) + int(k[1])
            if checker_num > int(target[0]) or checker_num > int(target[1]):
                print(f"-----to pop: {k}")
                a.remove(k)
            if len(a) == 0:
                return 'impossible', False
        print(f"RESULT OF REMOVE: {a}")

        temp += a

        # print(f"POPULATED: {temp}\n")

    return temp, False


def checker(target, data_set):
    pass


def solution(m, f):
    target = [m, f]
    m_start = 1
    f_start = 1
    populated_data = list(populate(m_start, f_start))
    print(f"1: {populated_data}")

    if target in populated_data:
        return 1

    index = 1

    while True:
        index += 1
        print(f"GEN :{index}")
        populated_data, status = generate_data(target, populated_data)
        if status:
            print(f"WE GOT IT: {populated_data}\n")
            return index
        if populated_data == 'impossible':
            return populated_data
        print(f"POPULATED: {populated_data}\n")
        if index == 5:
            break

        # if [{str(m)}, {str(f)}] in populated_data:
        #     break

s = solution('2', '4')

print(f"\n\n\n {s}")
