conference_rooms = ["executive", "hopper", "lovelace", "pod", "snooze booth"]
capacity = [7, 20, 6, 2, 1]
room_dict = {key: value for key, value in zip(conference_rooms, capacity)}

print(room_dict)
