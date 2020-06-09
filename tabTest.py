def count_spaces(filename):
    with open(filename,"r") as f1:
        contents=f1.readlines()

    total_tab=0
    total_space=0
    for line in contents:
        total_tab += line.count("    ")
        total_tab += line.count("\t")
        total_space += line.count(" ")
    print("Space count = ",total_space)
    print("Tab count = ",total_tab)
    print("New line count = ",len(contents))
    return total_space,total_tab,len(contents)

count_spaces('main.yaml')