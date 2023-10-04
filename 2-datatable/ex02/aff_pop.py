def aff_pop(data):
    """
    Plot and display population projections for two countries from a dataset

    Parameters
    ----------
    data: DataFrame
        The dataset containing population data for various countries

    Returns
    -------
    None
    """
    try:
        country_one = "Malaysia"
        country_two = "Thailand"
        # iloc is integer position-based; loc is label-based
        filtered = data.loc[[country_one, country_two], "1800":"2050"]
        if filtered.empty or not len(filtered) == 2:
            raise AssertionError("country does not exist on dataset")
        # expand the 'k' and 'M' suffix to zeros for all columns
        # regular expression (regex) is a pattern/filter that describes a set
        # of strings that matches the pattern
        filtered = filtered.replace(
            {'k': '*1e3', 'M': '*1e6', 'B': '*1e9'}, regex=True
        )
        # pd.eval supports arithmetic operations
        filtered = filtered.apply(pd.eval)
        print(filtered)
        for i, s in filtered.iterrows():
            plt.plot(s.index.astype(int), s.values.astype(int), label=i)
        plt.legend()
        plt.xlabel('Year')
        plt.ylabel('Population')
        plt.title("Population Projections")
        plt.savefig("aff_pop.jpg")
        # plt.show()
    except Exception as e:
        print(f"Error: {e}")


def main():
    data = load("population_total.csv")
    if (data is None):
        return
    else:
        aff_pop(data)


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import pandas as pd
    from load_csv import load
    main()
