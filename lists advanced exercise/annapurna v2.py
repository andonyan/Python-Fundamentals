command = input()
store_items_dict = {}

while command != "END":
    current_command = [each_word for each_word in command.split("->")]
    action = current_command[0]
    store_name = current_command[1]
    if action == "Add":
        store_items = [item for item in current_command[2].split(",")]
        if store_name not in store_items_dict:
            store_items_dict[store_name] = store_items
        else:
            store_items_dict[store_name] += store_items
    elif action == "Remove":
        if store_name in store_items_dict:
            store_items_dict.pop(store_name)

    command = input()
print("Stores list:")

for keys, values in sorted(store_items_dict.items(), key=lambda x: (len(x[1]), x[0]), reverse=True):
    print(keys)
    for each_item in values:
        print(f"<<{each_item}>>")