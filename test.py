import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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
plt.title('Distribution of Total Prices for Orders')
plt.xlabel('Total Price')
plt.ylabel('Frequency')
plt.show()

#Analyse du chiffre d’affaires en fonction du temps :

#a)


#b)