import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


try:

    df = pd.read_csv('data-analysis-projects/videogamesales/vgsales.csv')

    print(df)

except Exception as e:
    
    print(f"Error  :  {e}")