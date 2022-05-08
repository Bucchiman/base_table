import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


'''
    数値オブジェクトのコラムに関して
    facetにより出力する
'''
def distribution_facet(df, columns):
    f = pd.melt(df, value_vars=columns)
    g = sns.FacetGrid(f, col="variable",  col_wrap=2, ax=ax, sharex=False, sharey=False)
    g = g.map(sns.distplot, "value")
    plt.savefig("distribution_facet.pdf")




def main():
    pass


if __name__ == "__main__":
    main()
