import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

def filter_items(condition, dict_list):
    """
    Return a new list containing only the dictionaries that satisfy
    the given condition function.
    """
    return [item for item in dict_list if condition(item)]


def aggregate(aggregation_key, aggregation_function, dict_list):
    """
    Aggregate values associated with aggregation_key using the
    provided aggregation function.
    """
    values = [float(item[aggregation_key]) for item in dict_list]
    return aggregation_function(values)

# 1. Print the average temperature of all the cities
avg_temp_all = aggregate("temperature", lambda vals: sum(vals) / len(vals), cities)
print(f"The average temperature of all the cities: {avg_temp_all:.2f}")
print()

# 2. Print all cities in Germany
germany_list = filter_items(lambda c: c["country"] == "Germany", cities)
germany_cities = [c["city"] for c in germany_list]
print("All cities in Germany:")
print(germany_cities)
print()

# 3. Print all cities in Spain with a temperature above 12°C
spain_warm_list = filter_items(lambda c: c["country"] == "Spain" and float(c["temperature"]) > 12.0, cities)
spain_warm_cities = [c["city"] for c in spain_warm_list]
print("Cities in Spain with temperature > 12°C:")
print(spain_warm_cities)
print()

# 4. Count the number of unique countries
unique_countries = len(set(c["country"] for c in cities))
print(f"Number of unique countries: {unique_countries}")
print()

# 5. Print the average temperature for all the cities in Germany
germany_avg_temp = aggregate("temperature", lambda vals: sum(vals) / len(vals), germany_list)
print(f"Average temperature for all cities in Germany: {germany_avg_temp:.2f}")
print()

# 6. Print the max temperature for all the cities in Italy
italy_list = filter_items(lambda c: c["country"] == "Italy", cities)
italy_max_temp = aggregate("temperature", max, italy_list)
print(f"Max temperature for all cities in Italy: {italy_max_temp:.2f}")
print()