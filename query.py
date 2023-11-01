import requests


class Query:

    indicator_code: str
    year_start: int
    year_end: int
    world_gdp: list[str, [int, float]]
    all_gdp: list[list[str, float], list[str, float]]

    def __init__(self, year_start, year_end):
        self.indicator_code = "NY.GDP.MKTP.CD"
        self.year_start = year_start
        self.year_end = year_end
        self.world_gdp = ["World"]
        self.all_gdp = []

    def query_api(self):
        self.get_all_gdp()

    def get_all_gdp(self):
        countries_url = "https://api.worldbank.org/v2/country?format=json&per_page=300"
        response = requests.get(countries_url)

        if response.status_code == 200:
            country_data = response.json()

            self.get_world_gdp_data()
            new_year_start = int(self.world_gdp[-1][0])
            new_year_end = int(self.world_gdp[1][0])

            self.year_start = new_year_start
            self.year_end = new_year_end

            for country in country_data[1]:
                country_id = country['id']
                country_gdp_url = f"http://api.worldbank.org/v2/country/{country_id}/indicators/{self.indicator_code}?format=json"
                country_gdp_response = requests.get(country_gdp_url)

                if country_gdp_response.status_code == 200:
                    country_gdp_data = country_gdp_response.json()

                    country_gdp = [country['name']]
                    if country_gdp_data[1] is not None and country['capitalCity'] != "":
                        i = 1
                        for gdp_per_year in country_gdp_data[1]:
                            if new_year_start <= int(gdp_per_year['date']) <= new_year_end:
                                world_gdp_year_value = float(self.world_gdp[i][1])

                                if gdp_per_year['value'] is not None:
                                    percentage_gdp = round(float(gdp_per_year['value']) / world_gdp_year_value, 2)
                                    country_gdp.append(percentage_gdp)
                                else:
                                    country_gdp.append(0.0)
                                i += 1

                            elif new_year_start > int(gdp_per_year['date']):
                                break
                        self.all_gdp.append(country_gdp)

                else:
                    print(f"Failed to fetch GDP data for {country['name']}")
                    exit(1)

            self.all_gdp.sort(reverse=True, key=lambda x: x[1])

        else:
            print("Failed to fetch the list of countries")
            exit(1)

    def get_world_gdp_data(self):
        world_gdp_url = f"http://api.worldbank.org/v2/country/wld/indicators/{self.indicator_code}?format=json"
        world_gdp_response = requests.get(world_gdp_url)

        if world_gdp_response.status_code == 200:
            world_gdp_data = world_gdp_response.json()

            for gdp_per_year in world_gdp_data[1]:
                if self.year_start <= int(gdp_per_year['date']) <= self.year_end:
                    self.world_gdp.append([gdp_per_year['date'], gdp_per_year['value']])

        else:
            print(f"Failed to fetch world's GDP data")
            exit(1)
