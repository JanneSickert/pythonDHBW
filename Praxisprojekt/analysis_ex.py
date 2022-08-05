import matplotlib.pyplot as plt
import pandas as pd
import datetime
import numpy as np

class Analyser:
    def __init__(self, table, engine_table, figure_save_path):
        self.figure_save_path = figure_save_path
        self.final_table = table
        self.engine_table = engine_table


    def run(self):
        self.visualize_sales_per_countries()
        self.optional()

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

    def optional(self):
        aufgabe1 = """
        Welche Fin hat das
        Zeitlich erste 
        verkaufte Fahrzeug.
        """
        aufgabe2 = """
        Wie viele Fahrzeuge wurden
        zwischen 2017 und 2021
        mit den in der Aufgabenstellung beschribenden
        Motoren verkauft.
        """
        # Aufgabe 1
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
        print(aufgabe1)
        print(str(fin))
        # ------------------------
        # Aufgabe 2
        motoren = ["OM 934", "OM 936", "OM 470", "OM 471"]
        key = ["Sales Code", "Code Description En", "Code Description De"]
        data = pd.DataFrame({
            "Sales Code": self.engine_table[key[0]],
            "Code Description En": self.engine_table[key[1]],
            "Code Description De": self.engine_table[key[2]]
        })
        code = []
        i, k = 0, 0
        while i < len(motoren):
            while k < len(data[key[1]]):
                p1, p2 = data[key[1]][k], data[key[2]][k]
                p1 = motoren[i] == p1
                p2 = motoren[i] == p2
                if p1 or p2:
                    code.append(data[key[0]][i])
                k = k + 1
            k = 0
            i = i + 1
        a = 0
        b = 0
        c = 0
        d = 0
        sca = "sales_code_array"
        counter = 0
        index_list = []
        while a < len(self.final_table[sca]):
            while b < len(self.final_table[sca][a]):
                e = self.final_table[sca][a].split(", ")
                while d < len(e):
                    while c < len(code):
                        if e[d] == code[c]:
                            counter = counter + 1
                            index_list.append(a)
                            c = len(code)
                            d = len(e)
                            b = len(self.final_table[sca][a])
                        c = c + 1
                    c = 0
                    d = d + 1
                d = 0
                b = b + 1
            b = 0
            c = 0
            d = 0
            a = a + 1
            print("complete", a)
        i = 0
        von = datetime.datetime(2017,  1,  1, 0, 0)
        bis = datetime.datetime(2021,  1,  1, 0, 0)
        bisss = counter
        while i < bisss:
            try:
                date = self.final_table["production_date"][index_list[i]]
                if date > von and date < bis:
                    pass
                else:
                    counter = counter - 1
            except Exception:
                counter = counter - 1
            i = i + 1
        print(aufgabe2)
        print(counter)