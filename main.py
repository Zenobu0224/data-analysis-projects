import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# fill null with the argument(value)
def fill_null_val(df, column, value):
    return (
        df.fillna({column: value}, inplace=True)
    )


# check how many duplicates
def check_duplicated_val(df, **kwargs):
    return df.duplicated(**kwargs).sum()


# drop duplicated value with columns
def drop_duplicated_val(df, **kwargs):
    df.drop_duplicates(**kwargs, inplace=True)


# find top 10 games according to sales (eg. global sales, japan sales, ..,)
def top_10(df, sales, name, limited):
    return (
        df[[sales, name]]
        .sort_values(by=sales, ascending=False)
        .head(limited)
    )

def top_publishers(df, publishers, sales, limited, ascen):
    return  (
        df.groupby(publishers)[sales]
        .sum()
        .sort_values(ascending=ascen)
        .head(limited)
    )

# Sales by platform
def sales_by_platform(df, sales, platform):
    return (
        df.groupby(platform)[sales]
        .sum()
        .reset_index()
    )

def sum_of_all_sales(df, n_america_sales, europe_sales, japan_sales, other_sales):
    return  (
        df[[n_america_sales, europe_sales, japan_sales, other_sales]].sum()
    )

try:

    df = pd.read_csv('data-analysis-projects/videogamesales/vgsales.csv')   # dataframe

    fill_null_val(df, 'Year', 0)                    # fill null value in column(Year) with 0
    fill_null_val(df, 'Publisher', 'Unknown')       # fill null value in column(Publisher) with Unknown

    df['Year'] = pd.to_numeric(df['Year'], errors='coerce').astype(int)

    # drop duplicated value
    drop_duplicated_val(df, subset=['Name', 'Platform', 'Year', 'Genre', 'Publisher', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales'])

    # top 10 best selling games(global sales)
    top10_games = top_10(df, 'Global_Sales', 'Name', 10)

    # Global Sales by Platform
    platform_sale = sales_by_platform(df, 'Global_Sales', 'Platform')

    # Sales over the years
    sales_per_year = sales_by_platform(df, 'Global_Sales', 'Year')

    overall_regional_sales = sum_of_all_sales(df, 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales')

    sales_by_genre = sales_by_platform(df, 'Global_Sales', 'Genre')

    top10_publishers = top_publishers(df, 'Publisher', 'Global_Sales', 10, False)

    print(top10_publishers)

    # print(sales_per_year)

    # print(platform_sale)

    # # PRINT TERMINAL
    # print("\nTop 10 best-selling games globally (via Global_Sales)")
    # print(top10_games)

    # VISUALIZATION
    x = np.arange(10)

    plt.title("Top 10 Best-selling Games Globally", fontweight='bold', fontsize=20)
    plt.bar(top10_games['Name'], top10_games['Global_Sales'], edgecolor='black', color="#509e67")
    plt.grid(True, alpha=0.3)
    plt.xlabel('Games', fontfamily='Comic Sans MS', fontweight='bold', fontsize=17)
    plt.ylabel('Revenues (by Million $)', fontfamily='Comic Sans MS', fontweight='bold', fontsize=17)
    plt.xticks(rotation=35)
    plt.tight_layout()
    plt.show()

    sales_by_platform_ticks = np.arange(31)
    plt.title("Sales by Platform", fontweight='bold', fontsize=20)
    plt.barh(platform_sale['Platform'], platform_sale['Global_Sales'], edgecolor='black', color="#C886F7F6")
    plt.xlabel('Sales in Millions (Global Sales)', fontweight='bold', fontsize=13, fontfamily='Comic Sans MS')
    plt.grid(True, alpha=0.4, linestyle='--')
    plt.ylabel('Platform', fontweight='bold', fontsize=13, fontfamily='Comic Sans MS')
    plt.show()

    sale_per_year_index = np.arange(40)
    plt.title('Sales Over the Years', fontweight='bold', fontsize=20)
    plt.plot(sale_per_year_index, sales_per_year['Global_Sales'], marker='o', color='#000000')
    plt.xticks(ticks=sale_per_year_index, labels=sales_per_year['Year'], rotation=45)
    plt.grid(True, alpha=0.3)
    plt.xlabel('Year', fontweight='bold', fontsize=13, fontfamily='Comic Sans MS')
    plt.ylabel('Global Sales (by Million $)', fontweight='bold', fontsize=13, fontfamily='Comic Sans MS')
    plt.tight_layout()
    plt.show()

    labels = ['North America Sales', 'Europe  Sales', 'Japan Sales', 'Other Sales']
    pos = np.arange(len(labels))
    plt.title("Regional Sale Comparison", fontweight='bold', fontsize=20)
    plt.bar(pos, overall_regional_sales.values, label=overall_regional_sales.index, color=["#A96FE7", "#84E7C1", "#4085EE", "#D261C5"], edgecolor='black')
    plt.xticks(ticks=pos, labels=labels)
    plt.grid(True, alpha=0.2)
    plt.xlabel('Region', fontweight='bold', fontsize=13, fontfamily="Comic Sans MS")
    plt.ylabel('Sales (by Million $)', fontweight='bold', fontsize=13, fontfamily="Comic Sans MS")
    plt.legend()
    plt.show()

    colors = [
    '#FF6B6B', '#FFA45B', '#FFD93D', '#6BCB77', '#4D96FF', '#89CFF0',
    '#B983FF', '#F25287', '#008891', '#FFD3B6', '#E5989B', '#A8A4CE'
    ]   
    plt.title("Sales by Genre", fontweight='bold', fontsize=20)
    plt.pie(sales_by_genre['Global_Sales'], labels=sales_by_genre['Genre'], startangle=90, colors=colors, autopct='%1.1f%%')
    plt.legend(loc='upper left', bbox_to_anchor=(-0.4, 1.1))
    plt.show()

    plt.title("Top Publishers", fontweight='bold', fontsize=20)
    plt.bar(top10_publishers.index, top10_publishers.values, edgecolor='black', color="#485ED6")
    plt.xlabel("Publisher", fontsize=13, fontweight='bold', fontfamily='Comic Sans MS')
    plt.ylabel("Global Sales (by Million $)", fontsize=13, fontweight='bold', fontfamily='Comic Sans MS')
    plt.grid(True, alpha=0.3)
    plt.xticks(rotation=35)
    plt.tight_layout()
    plt.show()

except Exception as e:

    print(f"Error  :  {e}")