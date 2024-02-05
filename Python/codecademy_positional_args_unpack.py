from os.path import join

path_segment_1 = "/Home/User"
path_segment_2 = "Codecademy/videos"
path_segment_3 = "cat_videos/surprised_cat.mp4"

# join all three of the paths here!
result = join(path_segment_1, path_segment_2, path_segment_3)
print(result)


def myjoin(*args):
    joined_string = args[0]
    for arg in args[1:]:
        joined_string += '/' + arg
    return joined_string


string1 = "Hi There!,"
string2 = "How are you?"
string3 = "Hope you are doing good."

my_result = myjoin(string1, string2, string3)
print(my_result)
