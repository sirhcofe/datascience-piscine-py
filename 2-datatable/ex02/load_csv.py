import pandas as pd


def load(path: str):
    """
    Load a CSV file into a pandas DataFrame, print its dimensions, and return
    the dataset.

    Parameters
    ----------
    path: str
        The path to the CSV file to be loaded.

    Returns
    -------
    pd.DataFrame or None
        A pandas DataFrame containing the loaded data if successful, otherwise
        returns None if an error occurred when loading the dataset
    """
    try:
        dataset = pd.read_csv(path, index_col=0)
        dimensions = dataset.shape
        print(f"Loading dataset of dimensions {dimensions}")
        return (dataset)
    except Exception as e:
        print(f"Error: {e}")
        return None
