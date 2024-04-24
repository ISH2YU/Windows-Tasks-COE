def sub_1400019E0(prompt, *args):
    print(prompt % args)

def sub_140001A50(a, value):
    value = int(input(a))
    return value

def sub_1400013E0(x):
    print(x)

v12 = 0
sub_1400019E0("Enter a number between 0 and 4444: ")
v12 = sub_140001A50("", v12)
sub_1400019E0("You entered: %d\n" % v12)

v10 = (6 * v12 * v12) + (47 * v12) + 52

sub_1400019E0("  %d\n" % v10)



