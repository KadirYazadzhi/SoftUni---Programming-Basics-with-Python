pyramid_number = int(input())

prints = 0

for row in range(pyramid_number):

    for col in range(row + 1):
        prints += 1
        print(prints, end=' ')

        if prints == pyramid_number:
            exit()

    print()