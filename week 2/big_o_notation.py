import time
# 0(1) constant time complexity
def print_first_item(my_list):
    start_time = time.perf_counter()
    first_item = my_list[0]
    print(f"first item : {first_item}")
    end_time = time.perf_counter()
    print(f"time taken for 0(1) complexity: {end_time - start_time}")


# 0(n) linear time complexity
def print_all_items(my_list):
    start_time = time.perf_counter()
    for item in my_list:
        pass
    end_time = time.perf_counter()
    print(f"time taken for 0(n) complexity: {end_time - start_time}")

small_list = list(range(10))
large_list = list(range(1000000))

print_first_item(small_list)
print_first_item(large_list)
print_all_items(small_list)
print_all_items(large_list)
