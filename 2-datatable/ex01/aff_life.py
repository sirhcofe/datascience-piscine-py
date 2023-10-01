def aff_life(data):
    country = "Malaysia"
    mask = data.iloc[:, 0] == country
    filtered = data[mask]
    if filtered.empty:
        raise AssertionError("country does not exist on dataset")
    print(filtered)
    plt.plot(filtered.columns[1:].values.astype(int), filtered.iloc[0, 1:])
    plt.xlabel('Year')
    plt.ylabel('Life expectancy')
    plt.title(f"{country} Life Expectancy Projections")
    plt.savefig(f"{country}_aff.jpg")
    # plt.show()


def main():
    data = load("life_expectancy_years.csv")
    if (data is None):
        return
    else:
        aff_life(data)


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from load_csv import load
    main()
