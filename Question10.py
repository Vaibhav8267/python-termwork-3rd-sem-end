import pickle

my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

with open("dict_data.pkl", "wb") as file: 
    pickle.dump(my_dict, file)

print("Dictionary has been saved to dict_data.pkl.")

with open("dict_data.pkl", "rb") as file: 
    loaded_dict = pickle.load(file)

print("Dictionary has been loaded from dict_data.pkl.")
print("Loaded Dictionary:", loaded_dict)
