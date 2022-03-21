import pandas

census_data = pandas.read_csv('census.csv')

median = census_data.median()

def main():
    print(median)

if __name__ == "__main__":
    main()