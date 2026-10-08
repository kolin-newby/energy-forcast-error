# main.py

from src.clean import cleanEiaData
from src.fetch_eia import fetchEiaData


def main():
    cleanEiaData(fetchEiaData())


if __name__ == "__main__":
    main()
