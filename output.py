import csv


class Output:

    year_start: int
    year_end: int
    all_gdp: list[list[str, float], list[str, float]]

    def __init__(self, year_start, year_end, all_gdp):
        self. year_start = year_start
        self.year_end = year_end
        self.all_gdp = all_gdp

    def output_gdp(self):
        self.print_and_save_gdp()

    def print_and_save_gdp(self):
        with open('output.csv', 'w', newline='') as f:
            csv_file_writer = csv.writer(f)

            years_list = ["Country"]
            i = self.year_start
            while i <= self.year_end:
                years_list.append(str(i))
                i += 1
            print(",".join(years_list))
            csv_file_writer.writerow(years_list)

            for country_with_gdp in self.all_gdp:
                gdps_list = country_with_gdp[1:]
                gdps_list.reverse()
                print(country_with_gdp[0] + "," + ",".join(str(x) for x in gdps_list))
                csv_file_writer.writerow([country_with_gdp[0]] + gdps_list)
