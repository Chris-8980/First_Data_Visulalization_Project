import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Loading Dataset csv File
amz = pd.read_csv('amazon_ecommerce_sample_dataset.csv')
print(amz.head())

# How does total revenue change over time?
plt.figure(figsize = (10,6))
amz['order_date'] = pd.to_datetime(amz['order_date'])

# Daily Revenue
daily_revenue = amz.groupby((amz['order_date'].dt.date))['order_value'].sum()

# Weekly Revenue
weekly_revenue = amz.groupby((amz['order_date'].dt.to_period('W')))['order_value'].sum()
weekly_revenue.index = weekly_revenue.index.to_timestamp()

# Monthly Revenue
monthly_revenue = amz.groupby((amz['order_date'].dt.to_period('M')))['order_value'].sum()
monthly_revenue.index = monthly_revenue.index.to_timestamp()

plt.plot(daily_revenue, label = 'Days',)
plt.plot(weekly_revenue, label = 'Weeks', marker = 'o')
plt.plot(monthly_revenue, label = 'Months', marker = 'o')
plt.xticks(rotation = 45)
plt.xlabel('Date Timeline')
plt.ylabel('Revenue')
plt.title('Revenue as per Timeline')
plt.legend()
plt.grid()
plt.savefig('Line_Plot.png') # Saving plot in current working directory (cwd)
plt.close()

# Which product categories contribute the most to total revenue and profit?

# Category-wise revenue and profit calculation

category_summary = amz.groupby('category').agg(total_revenue = ('order_value', 'sum'),
                     total_profit = ('profit', 'sum')).sort_values(by = 'total_revenue', 
                                                                   ascending = False)
category_revenue = category_summary['total_revenue']
# print(category_summary)

# Visualization 1: Revenue by Category

plt.figure(figsize = (8,5))
sns.barplot(x = category_summary.index, y =category_summary['total_revenue'],
             hue = category_summary.index, palette = 'Set2', legend = False)
plt.xlabel('Category')
plt.ylabel('Total Revenue')
plt.title('Total Revenue by Product Category')
plt.savefig('Bar_Chart_1.png') # Saving plot in current working directory (cwd)
plt.close()

# Visualization 2: Profit by Catgeory

plt.figure(figsize = (8,5))
sns.barplot(x = category_summary.index, y = category_summary['total_profit'],
             hue = category_summary.index, palette = 'Set2',  legend = False)
plt.xlabel('Category')
plt.ylabel('Total Profit')
plt.title('Total Profit by Product Category')
plt.savefig('Bar_Chart_2.png') # Saving plot in current working directory (cwd)
plt.close()


# How is the total revenue distributed across different product categories?

plt.figure(figsize = (7,7))
plt.pie(category_revenue, labels = category_revenue.index, autopct = '%1.1f%%',
         startangle = 140, colors = plt.cm.tab10.colors)
plt.title('Revenue Distribution By Category')
plt.savefig('Pie_Chart.png')
plt.close()

# Displaying all the plots together i.e. subplots for:
# Line Chart, Pie Chart, Bar Plot 1, Bar Plot 2

# Subplot figure and axis
fig, ax = plt.subplots(2,2,figsize = (16,10))

# Creating subplot for Line Chart
ax[0,0].plot(daily_revenue, label = 'Days',)
ax[0,0].plot(weekly_revenue, label = 'Weeks', marker = 'o')
ax[0,0].plot(monthly_revenue, label = 'Months', marker = 'o')
ax[0,0].tick_params(axis = 'x', rotation = 45)
ax[0,0].set_xlabel('Date Timeline', labelpad = 5)
ax[0,0].set_ylabel('Revenue')
ax[0,0].set_title('Revenue as per Timeline')
ax[0,0].grid()
ax[0,0].legend()

# Creating subplot for Pie Chart
ax[0,1].pie(category_revenue, labels = category_revenue.index, autopct = '%1.1f%%',
             startangle = 140, colors = plt.cm.tab10.colors)
ax[0,1].set_title('Revenue Distribution By Category')

# Creating subplot for Bar Plot 1
sns.barplot(x = category_summary.index, y =category_summary['total_revenue'], 
            hue = category_summary.index, ax = ax[1,0], palette = 'Set1',  legend = False)

ax[1,0].set_title('Revenue by Category')
ax[1,0].tick_params(axis = 'x', rotation = 20)

# Creating subplot for Bar Plot 2
sns.barplot(x = category_summary.index, y = category_summary['total_profit'], 
            hue = category_summary.index, ax = ax[1,1], palette = 'Set2', legend = False)
ax[1,1].set_title('Profit by Category')
ax[1,1].tick_params(axis = 'x', rotation = 20)
plt.tight_layout()
plt.subplots_adjust(hspace = 0.4)
plt.savefig('Combined Plots.png')
plt.show()