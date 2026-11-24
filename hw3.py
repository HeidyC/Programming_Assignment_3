# Part 1 - Total Population
# Design Recipe:
# 1. The purpose of this function is the give the total amount of a population.
# 2. Inputs: the counties from the demographics file; Outputs: the amount of counties for that set time given
# 3. Counties type parameter is a list and the return value is an integer.

import county_demographics
from data import CountyDemographics

def population_total(counties: list[CountyDemographics]) -> int:
    total = 0

    for county in counties:
        total += county.population["2014 Population"]

    return total

# Part 2 - Filter Counties by State
# Design Recipe:
# 1. The purpose of this function is to filter the counties that is in a given state in a list.
# 2. Inputs: the counties from the demographics file, the state you are trying to receive information from; Outputs: a list containing the names of the counties in that specific state
# 3. Counties type parameter is a list, the state is a string, and the return value is a list.

def filter_by_state(counties: list[CountyDemographics], state: str) -> list[CountyDemographics]:
    matching_counties = []

    for county in counties:
        if county.state == state:
            matching_counties.append(county)

    return matching_counties

# Part 3 - Calculate Sub-Populations
# Design Recipe:
# 1. The purpose of this function is calculate sub-populations of the counties, for the information that is wanting to be found (education).
# 2. Inputs: the counties from the demographics file, a key for education; Outputs: a total of the estimated population for that specific key
# 3. Counties type of parameter is a list, the key is a string, and the return value is a float.

def population_by_education(counties: list[CountyDemographics], key: str) -> float:
    total = 0.0

    for county in counties:
        if key in county.education:
            population = county.population["2014 Population"]
            percentage = county.education[key]

            total += population * percentage / 100

    return total

# Design Recipe:
# 1. The purpose of this function is calculate sub-populations of the counties, for the information that is wanting to be found (education).
# 2. Inputs: the counties from the demographics file, a key for ethnicity; Outputs: a total of the estimated population for that specific key
# 3. Counties type of parameter is a list, the key is a string, and the return value is a float.

def population_by_ethnicity(counties: list[CountyDemographics], key: str) -> float:
    total_population = 0
    ethnicity_population = 0.0

    for county in counties:
        population = county.population["2014 Population"]
        total_population += population

        if key in county.ethnicities:
            percentage = county.ethnicities[key]
            ethnicity_population += population * percentage / 100

    if total_population == 0:
        return 0.0

    return ethnicity_population / total_population * 100

# Design Recipe:
# 1. The purpose of this function is calculate sub-populations of the counties, for the information that is wanting to be found (the percentage of those below the poverty level).
# 2. Inputs: the counties from the demographics file; Outputs: the percentage of those below the poverty level
# 3. Counties type of parameter is a list and the return value is a float.

def percent_below_poverty_level(counties: list[CountyDemographics]) -> float:
    total_population = 0
    poverty_population = 0.0

    for county in counties:
        population = county.population["2014 Population"]
        percentage = county.income["Persons Below Poverty Level"]

        total_population += population
        poverty_population += population * percentage / 100

    if total_population == 0:
        return 0.0

    return poverty_population / total_population * 100

# Part 4 - Calculate Overall Percentages
# Design Recipe:
# 1. The purpose of this function is to calculate the overall percentages of the certain education level based on the county/counties.
# 2. Inputs: the counties from the demographics file, a key for education; Outputs: a total of the estimated population for that specific key
# 3. Counties type of parameter is a list, the key is a string, and the return value is a float.

def percent_by_education(counties: list[CountyDemographics], key: str) -> float:
    total = population_total(counties)

    if total == 0:
        return 0.0

    education_population = population_by_education(counties, key)

    return 100 * education_population / total

# Design Recipe:
# 1. The purpose of this function is to calculate the overall percentages of the ethnicity of the population based on the county/counties.
# 2. Inputs: the counties from the demographics file, a key for ethnicity; Outputs: a total of the estimated population for that specific key
# 3. Counties type of parameter is a list, the key is a string, and the return value is a float.

def percent_by_ethnicity(counties: list[CountyDemographics], key: str) -> float:
    total = population_total(counties)
    ethnicity_population = 0.0

    if total == 0:
        return 0.0

    for county in counties:
        if key in county.ethnicities:
            population = county.population["2014 Population"]
            percentage = county.ethnicities[key]

            ethnicity_population += population * percentage / 100

    return 100 * ethnicity_population / total

# Design Recipe:
# 1. The purpose of this function is to calculate the overall percentages of the populations who are below the poverty level based on the county/counties.
# 2. Inputs: the counties from the demographics file; Outputs: a total of the estimated population
# 3. Counties type of parameter is a list and the return value is a float.

def percent_below_poverty_level(counties: list[CountyDemographics]) -> float:
    total = population_total(counties)
    poverty_population = 0.0

    if total == 0:
        return 0.0

    for county in counties:
        population = county.population["2014 Population"]
        percentage = county.income["Persons Below Poverty Level"]

        poverty_population += population * percentage / 100

    return 100 * poverty_population / total

# Part 5 - Filter Counties by Demographic Thresholds
# Design Recipe:
# 1. The purpose of this function is to filter counties that meet certain thresholds, which in this case would be whether the education is greater than the given threshold.
# 2. Inputs: the counties given from the demographics files, a key for education, and the threshold in order to filter; Output: a list containing what meets the threshold
# 3. Counties type of parameter is a list, the key is a string, the threshold is a float, and the return value is a list

def education_greater_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    result = []

    for county in counties:
        if key in county.education and county.education[key] > threshold:
            result.append(county)

    return result

# Design Recipe:
# 1. The purpose of this function is to filter counties that meet certain thresholds, which in this case would be whether the education is less than the given threshold.
# 2. Inputs: the counties given from the demographics files, a key for education, and the threshold in order to filter; Output: a list containing what meets the threshold
# 3. Counties type of parameter is a list, the key is a string, the threshold is a float, and the return value is a list

def education_less_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    result = []

    for county in counties:
        if key in county.education and county.education[key] < threshold:
            result.append(county)

    return result

# Design Recipe:
# 1. The purpose of this function is to filter counties that meet certain thresholds, which in this case would be whether the ethnicity is greater than the given threshold.
# 2. Inputs: the counties given from the demographics files, a key for ethnicity, and the threshold in order to filter; Output: a list containing what meets the threshold
# 3. Counties type of parameter is a list, the key is a string, the threshold is a float, and the return value is a list

def ethnicity_greater_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    result = []

    for county in counties:
        if key in county.ethnicities and county.ethnicities[key] > threshold:
            result.append(county)

    return result

# Design Recipe:
# 1. The purpose of this function is to filter counties that meet certain thresholds, which in this case would be whether the ethnicity is less than the given threshold.
# 2. Inputs: the counties given from the demographics files, a key for ethnicity, and the threshold in order to filter; Output: a list containing what meets the threshold
# 3. Counties type of parameter is a list, the key is a string, the threshold is a float, and the return value is a list

def ethnicity_less_than(counties: list[CountyDemographics], key: str, threshold: float) -> list[CountyDemographics]:
    result = []

    for county in counties:
        if key in county.ethnicities and county.ethnicities[key] < threshold:
            result.append(county)

    return result

# Design Recipe:
# 1. The purpose of this function is to filter counties that meet certain thresholds, which in this case would be whether the below poverty level is greater than the given threshold.
# 2. Inputs: the counties given from the demographics files and the threshold in order to filter; Output: a list containing what meets the threshold
# 3. Counties type of parameter is a list, the threshold is a float, and the return value is a list

def below_poverty_level_greater_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    result = []

    for county in counties:
        if county.income["Persons Below Poverty Level"] > threshold:
            result.append(county)

    return result

# Design Recipe:
# 1. The purpose of this function is to filter counties that meet certain thresholds, which in this case would be whether the below poverty level is less than the given threshold.
# 2. Inputs: the counties given from the demographics files and the threshold in order to filter; Output: a list containing what meets the threshold
# 3. Counties type of parameter is a list, the threshold is a float, and the return value is a list

def below_poverty_level_less_than(counties: list[CountyDemographics], threshold: float) -> list[CountyDemographics]:
    result = []

    for county in counties:
        if county.income["Persons Below Poverty Level"] < threshold:
            result.append(county)

    return result