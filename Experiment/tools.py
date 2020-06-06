
def readfile(filename):

    file = open(filename)

    x_list = []
    y_list = []
    z_list = []
    ap_list = []

    while 1:
        line = file.readline()
        if line == "":
            break
        content = line.split(",")
        x_list.append(int(content[0]))
        y_list.append(int(content[1]))
        z_list.append(int(content[2]))
        if len(content) == 4:
            ap_list.append(int(content[3]))

    file.close()

    return x_list, y_list, z_list, ap_list




