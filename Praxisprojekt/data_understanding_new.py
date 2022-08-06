# importing packages
import pandas as pd
import json
from datetime import date
import matplotlib.pyplot as plt

pd.options.mode.chained_assignment = None

# path for saving data
path = "C:/res/python_dhbw/output/clean_data.csv"

# importing first sheet
access_json = open('data_specs.json',)
data = json.load(access_json)
#data['database_path']
vehicle_data = pd.read_excel(
    data['database_path'] + "/" + data['database_name'], 0)

# importing second sheet
vehicle_data_fin = pd.read_excel(
    data['database_path'] + "/" + data['database_name'], 1)


# dropping na's to have a cleaner dataframe
vehicle_data_clean = vehicle_data.dropna()
vehicle_data_fin_clean = vehicle_data_fin.dropna()

# joining the two dataframes together for the FIN numbers
merged_vehicle_data = pd.merge(vehicle_data_clean, vehicle_data_fin_clean,
        how='left', left_on=['h_vehicle_hash'], right_on=['h_vehicle_hash'])

merged_vehicle_data_clean = merged_vehicle_data.drop(['Unnamed: 0_x'], axis=1)

# drop unnecessery columns
merged_vehicle_data_clean = merged_vehicle_data_clean.drop(
                                    ['Unnamed: 0_y'], axis=1)
vehicle_data_final = merged_vehicle_data_clean.drop(
    ['h_vehicle_hash','record_source','load_ts'], axis=1)

# drop rows with invalid fin numbers
vehicle_data_final = vehicle_data_final.query(
            "fin.str.len() == 17", engine="python")

# drop rows with invalid dates
today = date.today()
today_date = today.strftime('%d/%m/%Y %H:%M:%S')
start_date = '01.01.2002'

vehicle_data_final['production_date'] = pd.to_datetime(vehicle_data_final['production_date'], errors='coerce', dayfirst=True)
mask = (vehicle_data_final['production_date'] > start_date) & (vehicle_data_final['production_date'] <= today_date)

vehicle_data_final = vehicle_data_final.loc[mask]

# data first exercise no.2 https://www.geeksforgeeks.org/sort-dataframe-according-to-row-frequency-in-pandas/
first_date = '01.01.2014'
second_date = '31.12.2020'
plot_mask = (vehicle_data_final['production_date'] >= first_date) & (vehicle_data_final['production_date'] <= second_date)
vehicle_data_final_plot = vehicle_data_final.loc[plot_mask]

top_countries = vehicle_data_final_plot.groupby(['country'])['production_date'].count().reset_index(
    name='Count').sort_values(['Count'], ascending=False)
print(top_countries)

# plot
countries = top_countries["country"].head(3)
sales = top_countries["Count"].head(3)
plt.style.use('ggplot')
barplot = plt.bar(x=countries, height=sales)
plt.bar_label(barplot, labels=sales, label_type="edge")
plt.title("Top 3 Selling Countries between 2014 and 2020")
plt.ylabel("Sales").set_color("black")
plt.xlabel("Countries").set_color("black")

# data second exercise no.2
vehicle_data_final_plot['year_production'] = pd.DatetimeIndex(vehicle_data_final_plot['production_date']).year

top_year = vehicle_data_final_plot.groupby(['year_production'])['country'].count().reset_index(
    name='Count').sort_values(['Count'], ascending=False)
print(top_year)

#plot 2
year_of_sales = top_year["year_production"]
amount_of_sales = top_year["Count"]

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
explode = (0.1, 0, 0, 0, 0, 0, 0)  # only "explode" the first slice

def make_autopct(values):
    def my_autopct(pct):
        total = sum(amount_of_sales)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct

textprops = {"fontsize":6.5}
fig1, ax1 = plt.subplots()
ax1.pie(amount_of_sales, explode=explode, labels=year_of_sales, autopct=make_autopct(amount_of_sales), shadow=True, startangle=90, textprops=textprops)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
ax1.set_title("Vehicles sold per year", bbox={'facecolor':'0.8', 'pad':5})


# data third exercise no.1
vehicle_data_final_first_sale = vehicle_data_final.sort_values(["production_date"]).head()

print(vehicle_data_final_first_sale)

#plot 3



# show the plots
plt.show()

# export to csv without index
vehicle_data_final.to_csv(path, index=False)

