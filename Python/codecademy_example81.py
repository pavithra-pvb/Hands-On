dirty_harry = "Go ahead, make my day."
split_hairs = dirty_harry.split("a")

print(split_hairs)

user_name = "::::::::Eloise :::::::::::"
user_name_fixed = user_name.strip(":").strip()
print(user_name_fixed)

when_you_are_old = \
    """When you are old and grey and full of sleep,
    And nodding by the fire, take down this book,
    And slowly read, and dream of the soft look
    Your eyes had once, and of their shadows deep;
    
    How many loved your moments of glad grace,
    And loved your beauty with love false or true,
    But one man loved the pilgrim soul in you,
    And loved the sorrows of your changing face;
    
    And bending down beside the glowing bars,
    Murmur, a little sadly, how Love fled
    And paced upon the mountains overhead
    And hid his face amid a crowd of stars."""

list_of_lines = when_you_are_old.split("\n")

print(list_of_lines)
