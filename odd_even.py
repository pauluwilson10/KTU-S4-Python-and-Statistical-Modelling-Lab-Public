# def separate_tuples(tuples_list):
#     odd_tuples = []
#     even_tuples = []
#
#     for tup in tuples_list:
#         if sum(tup) % 2 == 0:
#             even_tuples.append(tup)
#         else:
#             odd_tuples.append(tup)
#
#     return odd_tuples, even_tuples
#
# # Example list of tuples
# tuples_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)]
#
# # Separating odd and even tuples
# odd_tuples, even_tuples = separate_tuples(tuples_list)
#
# # Printing the results
# print("Odd Tuples:")
# for tup in odd_tuples:
#     print(tup)
#
# print("\nEven Tuples:")
# for tup in even_tuples:
#     print(tup)
# Function to take input from the user and create a list of tuples
def create_tuple_list():
    tuple_list = []
    while True:
        user_input = input("Enter elements of the tuple separated by commas (or enter 'exit' to finish): ")
        if user_input.lower() == 'exit':
            break
        elements = user_input.split(',')  # Split the input by commas
        elements = tuple(map(int,elements)) # Convert elements to integers and create a tuple
        tuple_list.append(elements)  # Append the tuple to the list
    return tuple_list


def sep_tuple(tuple_list):
    odd_tuple=[]
    even_tuple=[]

    for tup in tuple_list:
        if sum(tup)%2==0:
            even_tuple.append(tup)
        else:
            odd_tuple.append(tup)

    return odd_tuple,even_tuple

tuple_list = create_tuple_list()
odd_tuples,even_tuples=sep_tuple(tuple_list)
print("List of tuples:", tuple_list)

#
print("Odd tuple")
for odd in odd_tuples:
    print(odd)

print("Even  tuple")
for even in even_tuples:
    print(even)