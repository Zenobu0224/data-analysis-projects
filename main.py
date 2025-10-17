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


def split_val(value, split, axis, side):
    return (
        np.array_split(value, split, axis=axis)[side]
    )


def sales_by_platform(df, sales, platform):
    return (
        df.groupby(platform)[sales]
        .sum()
        .reset_index()
    )

try:

    df = pd.read_csv('data-analysis-projects/videogamesales/vgsales.csv')   # dataframe

    fill_null_val(df, 'Year', 0)                    # fill null value in column(Year) with 0
    fill_null_val(df, 'Publisher', 'Unknown')       # fill null value in column(Publisher) with Unknown

    df['Year'] = pd.to_numeric(df['Year'], errors='coerce').astype(int)

    # drop duplicated value
    drop_duplicated_val(df, subset=['Name', 'Platform', 'Year', 'Genre', 'Publisher', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales'])

    # top 10 best selling games(global sales)
    top10 = top_10(df, 'Global_Sales', 'Name', 10)

    top10_global_sales_2d = split_val(top10.values, 2, 1, 0)
    top10_global_games_2d =    split_val(top10.values, 2, 1, 1)

    reshape_top10_global_sales = top10_global_sales_2d.reshape(-1)
    reshape_top10_global_games = top10_global_games_2d.reshape(-1)

    # Global Sales by Platform
    platform_sale = sales_by_platform(df, 'Global_Sales', 'Platform')

    print(platform_sale)

    # PRINT TERMINAL
    print("\nTop 10 best-selling games globally (via Global_Sales)")
    print(top10)


    # VISUALIZATION
    x = np.arange(10)

    # plt.title("Top 10 Best-selling Games Globally", fontweight='bold', fontsize=20)
    # plt.bar(reshape_top10_global_games, reshape_top10_global_sales, edgecolor='black', color="#509e67")
    # plt.grid(True, alpha=0.3)
    # plt.xlabel('Games', fontfamily='Comic Sans MS', fontweight='bold', fontsize=17)
    # plt.ylabel('Revenues (by Million $)', fontfamily='Comic Sans MS', fontweight='bold', fontsize=17)
    # plt.xticks(rotation=35)
    # plt.tight_layout()
    # plt.show()

    sales_by_platform_ticks = np.arange(31)
    plt.title("Sales by Platform", fontweight='bold', fontsize=20)
    plt.barh(platform_sale['Platform'], platform_sale['Global_Sales'], edgecolor='black', color="#C886F7F6")
    plt.xlabel('Sales in Millions (Global Sales)', fontweight='bold', fontsize=13, fontfamily='Comic Sans MS')
    plt.grid(True, alpha=0.4, linestyle='--')
    plt.ylabel('Platform', fontweight='bold', fontsize=13, fontfamily='Comic Sans MS')
    plt.show()

except Exception as e:

    print(f"Error  :  {e}")