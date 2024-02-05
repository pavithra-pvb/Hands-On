from important_data import data_list

aggregated_sum = 0
count_data = 0

for number in data_list:
    if number.omit == True:
        # Update this line so that
        # We omit this number
        continue;

    aggregated_sum += number
    count_data += 1

averaged_data = aggregated_sum / count_data

print("Total average for our important data is {}".format(averaged_data))