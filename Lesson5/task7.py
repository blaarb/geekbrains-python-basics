# Генератор
# import random
# with open("task7.txt", "w") as task7_txt:
#     for i in range(1, 11):
#         task7_txt.write(f"firm_{i} 00{random.randint(0, 10)} "
#                         f"{random.randint(1000, 10000)} {random.randint(1000, 10000)}\n")

firms_dictionary = {}
revenue_counter = 0
revenue_total = 0
average_revenue = 0
with open("task7.txt") as input_sequence:
    for line in input_sequence:
        line_array = line.split()
        firm_revenue = int(line_array[2]) - int(line_array[3])
        if firm_revenue > 0:
            revenue_total += firm_revenue
            revenue_counter += 1
            firms_dictionary.update({line_array[0]: firm_revenue})

average_revenue = revenue_total / revenue_counter
result_list = [firms_dictionary, {"average_profit": average_revenue}]
print(result_list)
