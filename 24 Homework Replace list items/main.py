
def replays_list_items (in_list):
    if len(in_list) >= 2:
        in_list[0], in_list[-1] = in_list[-1], in_list[0]
        print(in_list)

my_list = ["much", "loves", "bananas", "very", "Bob"]
replays_list_items(my_list)
