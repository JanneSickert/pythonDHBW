import matplotlib.pyplot as plt
import pandas as pd
import datetime
import numpy as np

class Analyser:
    def __init__(self, table, figure_save_path):
        self.figure_save_path = figure_save_path
        self.final_table = table
        self.filter_for_years()


    def run(self):
        self.visualize_sales_per_countries()
        self.visualize_sales_per_year()
        self.optional()


    def optional(self):
        print("fin des ertverkauften farzeugs")
        first_date = datetime.datetime(3000, 12, 31, 0, 0)
        index = 0
        for i in range(len(self.final_table["production_date"])):
            d = self.final_table["production_date"][i]
            try:
                if d < first_date:
                    first_date = d
                    index = i
            except Exception:
                pass
        fin = self.final_table["fin"][index]
        print(str(fin))

    def filter_for_years(self):
        df = self.final_table
        df["counter"] = 1
        # your code here #

    def visualize_sales_per_countries(self):
        aufgabe = """
        In welchen top 3 Laendern wurden
        die meisten Farzeuge in diesen
        Zeitraeumen verkauft.
        """
        aufgabe2 = """
        In welchen Jahren 
        wurden die meisten Autos 
        verkauft
        """
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
                    "value: ", str(self.final_table[key[1]][i])
                )
        score = {
            "name": [], 
            "sells": []
        }
        score_date = {
            "datum": [], 
            "times": []
        }
        for index_of_land_in_time_range in index_list:
            if self.final_table[key[1]][index_of_land_in_time_range].year in score_date["datum"]:
                ind = score_date["datum"].index(self.final_table[key[1]][index_of_land_in_time_range].year)
                score_date["times"][ind] = score_date["times"][ind] + 1
            else:
                score_date["datum"].append(self.final_table[key[1]][index_of_land_in_time_range].year)
                score_date["times"].append(1)
            country_name = self.final_table[key[0]][index_of_land_in_time_range]
            if country_name in score["name"]:
                ind = score["name"].index(country_name)
                score["sells"][ind] = score["sells"][ind] + 1
            else:
                score["name"].append(country_name)
                score["sells"].append(1)
        height_score = {
            "name": [], 
            "sells": []
        }
        height_score_date = {
            "datum": [], 
            "times": []
        }
        # for i in range(len(score["name"])):
        #    print(score["name"][i], score["sells"][i])
        # Auto Exportweldmeister
        for i in range(3):
            ind = score["sells"].index(max(score["sells"]))
            height_score["name"].append(score["name"][ind])
            height_score["sells"].append(score["sells"][ind])
            score["sells"][ind] = 0
        print(aufgabe)
        for i in range(len(height_score["name"])):
            print(height_score["name"][i], height_score["sells"][i])
        # Beste Zeiten zum verkaufen
        for i in range(3):
            ind = score_date["times"].index(max(score_date["times"]))
            height_score_date["datum"].append(score_date["datum"][ind])
            height_score_date["times"].append(score_date["times"][ind])
            score_date["times"][ind] = 0
        print(aufgabe2)
        for i in range(len(height_score["name"])):
            print(height_score_date["datum"][i], height_score_date["times"][i])

    def visualize_sales_per_year(self):
        # your code here #
        pass