# print("#")
# print("#")
# print("#")


# for _ in range(3):
#     print("#")


# def main():
#     print_column(3)

# def print_column(height):
#     for _ in range(height):
#         print("#")


# main()


# def main():
#     print_square(3)

# def print_square(size):
#     for i in range(size):
#         for j in range(size):
#             print("#", end="")
#         print()

# main()

#==============================================================================
# def main():
#     print_square(3)

# def print_square(size):
#     for i in range(size):
#         print("#" * size)

# main()
#==============================================================================

def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print_row()

def print_row():
    print("#" * 3)
main()

