def burstTime(processes):
    bt_array = []
    for i in processes:
        if i=="Create Folder":
            bt_array.append(12)
        elif i=="Read File":
            bt_array.append(17)
        elif i=="Delete File":
            bt_array.append(16)
        elif i=="Write File":
            bt_array.append(18)
        elif i=="Plug Device":
            bt_array.append(15)
    return bt_array

'''xx = burstTime(["Create Folder","Read File","Delete File"])
print(xx)'''
