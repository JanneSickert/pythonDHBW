import matplotlib.pyplot as plt
import pandas as pd
import datetime

class Analyser:
    def __init__(self, table, figure_save_path):
        self.figure_save_path = figure_save_path
        self.final_table = table
        self.filter_for_years()

    def run(self):
        self.visualize_sales_per_countries()
        self.visualize_sales_per_year()

    def filter_for_years(self):
        df = self.final_table
        df["counter"] = 1
        # your code here #

    def visualize_sales_per_countries(self):
        # In welchen top 3 Laendern wurden
        # die meisten Farzeuge in diesen
        # Zeitraeumen verkauft.
        von = datetime.datetime(2014,  1,  1, 0, 0)
        bis = datetime.datetime(2020, 12, 31, 0, 0)
        key = ["country", "production_date", "verkaufte_autos_in_zeitspanne"]
        index_list = []
        for i in self.final_table.index:
            try:
                if (self.final_table[key[1]][i] > von) and (self.final_table[key[1]][i] < bis):
                    index_list.append(i)
            except Exception:
                print(
                    "fail at: ", i, 
                    "type: ", type(self.final_table[key[1]][i]), 
                    "value: ", str(self.final_table[key[1]][i]))
        for index_of_land_in_time_range in index_list:
            self.final_table[key[2]][index_of_land_in_time_range] = self.final_table[key[2]][index_of_land_in_time_range] + 1
        print(self.final_table)
            

    def visualize_sales_per_year(self):
        # your code here #
        pass