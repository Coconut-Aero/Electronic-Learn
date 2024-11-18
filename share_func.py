def nand4(x, y, z, m):
    return int(not (x and y and z and m))

def ls74138(x, y, z, data):
    res = x * 4 + y * 2 + z * 1
    return int(not res==data)