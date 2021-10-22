from get_fruits import GetFruits
from fruit_names import fruits

fruits_available = []

for f in fruits:
    fruits_available.append(GetFruits(f['fruits'],f['cost']))


print(fruits_available[0].fruit_name)
