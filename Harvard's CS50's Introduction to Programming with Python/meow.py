#for loop for a cat meowing

#meow 1
# for _ in range(10):
#     print("meow")

#meow 2

# print("meow\n" * 5, end="")

#meow 3
# n = 0
# while n < 3:
#     print("meow")
#     n += 1

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        m = int(input("What number of meows do you want? "))
        if m > 0:
            return m

def meow(m):
    for _ in range(m):
        print("meow")

main()