my_list = ["much", "loves", "bananas", "very", "Bob"]

def replays_list_items (my_list):
    my_list[0], my_list[-1] = my_list[-1], my_list[0]
    return my_list

print(replays_list_items(my_list))