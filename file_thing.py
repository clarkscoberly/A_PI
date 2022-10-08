
# file1 = "this.txt"

# file2 = "new.txt"
file2 = open("new.txt", 'w')

with open("this.txt") as f:
    # contents = f.readlines()
    for line in f:
        print(line)
        # input()
        if "(base 16)" in line:
            file2.write(line)


file2.close()

