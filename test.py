import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

excel_file_path = ".\pizza_sales\Data Model - Pizza Sales.xlsx"
# Read Excel file into a Pandas DataFrame
df = pd.read_excel(excel_file_path, engine='openpyxl')

#Détails de la commande :

#a)
pizzas_per_order = df.groupby('order_id')['pizza_name'].count()
print("La répartition du nombre de pizzas par commande :")
print(pizzas_per_order.value_counts().sort_index())

#b)
print()
total_prices_per_order = df.groupby('order_id')['total_price'].sum()
print("Aperçu des prix totaux pour les 5 premières commandes :")
print(total_prices_per_order.head(5))
print()
print("La répartition des prix totaux pour les commandes :")
print(total_prices_per_order.describe())
print()
plt.figure(figsize=(10, 6))
sns.histplot(total_prices_per_order, bins=30, kde=True, color='skyblue')
plt.title('Distribution des prix totaux pour les commandes')
plt.xlabel('Prix total')
plt.ylabel('Fréquence')
#plt.show()

#Analyse du chiffre d’affaires en fonction du temps :

#a)
df['order_date'] = pd.to_datetime(df['order_date'])
chiffre_affaires_quotidien = df.groupby(df['order_date'].dt.date)['total_price'].sum()
print(f"Le chiffre d'affaires quotidien :\n {chiffre_affaires_quotidien}")

#b)
print()
print("Y a-t-il une corrélation entre l'heure de la journée et le total de la commande ?")
df['hour_of_day'] = df['order_time'].apply(lambda x: x.hour if pd.notnull(x) else x)

plt.figure(figsize=(12, 6))
sns.scatterplot(x='hour_of_day', y='total_price', data=df)
plt.title("Corrélation entre l'heure de la journée et le total de la commande")
plt.xlabel("Heure de la journée")
plt.ylabel("Total de la commande")
plt.show()


############################

# Define time periods (you may adjust this based on your specific needs)
bins = [11, 18, 21]
labels = ['Matin/Aprem', 'Nuit']
df['time_period'] = pd.cut(df['hour_of_day'], bins=bins, labels=labels, right=False)

# Visualize the data
plt.figure(figsize=(12, 6))
sns.boxplot(x='time_period', y='total_price', data=df)
plt.title("Distribution of Total Prices across Time Periods")
plt.xlabel("Time Period")
plt.ylabel("Total Price")
plt.show()

# Perform ANOVA test
import scipy
f_statistic, p_value = scipy.stats.f_oneway(*[group['total_price'] for name, group in df.groupby('time_period')])
print("ANOVA Test:")
print("F-statistic:", f_statistic)
print("p-value:", p_value)

# Check for statistical significance (common alpha level is 0.05)
alpha = 0.05
if p_value < alpha:
    print("There is a significant difference in total prices across time periods.")
else:
    print("There is no significant difference in total prices across time periods.")











