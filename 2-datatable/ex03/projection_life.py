def project_life(income, life):
    """
    Create a scatter plot to project life expectancy against gross domestic
    product (GDP) for the year 1990, with custom x-axis ticks

    Parameters
    ----------
    income: DataFrame
        A DataFrame containing income data for different countries
    life: DataFrame
        A DataFrame containing life expectancy data for different countries

    Returns
    -------
    None
    """
    try:
        # Filter income and life expectancy data for the year 1900
        filter_income = income.loc[:, "1900"]
        filter_life = life.loc[:, "1900"]
        if (filter_income.empty or filter_life.empty):
            raise AssertionError("country does not exist on dataset")

        # Combine the filtered data series into a single DataFrame
        df = pd.concat({'Gross Domestic Product': filter_income,
                        'Life Expectancy': filter_life}, axis=1)

        # Create a scatter plot with custom x-axis ticks
        df.plot(
            kind="scatter",
            x="Gross Domestic Product",
            y="Life Expectancy",
            title="1990",
            logx=True,
        )

        # Customize x-axis ticks and labels
        plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])

        # Save the plot as an image
        plt.savefig("projection_life.jpg")
        # plt.show()
    except Exception as e:
        print(f"Error: {e}")


def main():
    income = load(
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    )
    life = load("life_expectancy_years.csv")
    if (income is None or life is None):
        return
    else:
        project_life(income, life)


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import pandas as pd
    from load_csv import load
    main()
