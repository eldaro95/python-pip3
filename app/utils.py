def get_population(mob_days):
  population_dict = {
    '2022': int(mob_days['2022 Population']),
    '2020': int(mob_days['2020 Population']),
    '2015': int(mob_days['2015 Population']),
    '2010': int(mob_days['2010 Population']),
    '2000': int(mob_days['2000 Population']),
    '1990': int(mob_days['1990 Population']),
    '1980': int(mob_days['1980 Population']),
    '1970': int(mob_days['1970 Population'])
  }
  labels = population_dict.keys()
  values = population_dict.values()
  return labels, values


def population_by_country(data, country):
  result = list(filter(lambda item: item['Country'] == country, data))
  return result