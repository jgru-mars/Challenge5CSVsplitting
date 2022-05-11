import pandas as pd


def main():

    # read DataFrame
    data = pd.read_csv("2015.csv")

    # This makes either the city or institution an Institution ID if they have been assigned already
    data['Institution ID'] = data.groupby(['ï»¿Institution', 'City']).ngroup()

    # outstanding csv creation
    outstanding = data[data['Ranking'] == "Outstanding Winner"].sort_values('ï»¿Institution')
    outstanding = outstanding[['ï»¿Institution', 'Institution ID', 'Ranking']]
    outstanding = outstanding.drop_duplicates("Institution ID")
    outstanding.to_csv('Outstanding.csv', index=False)

    # MeritoriousUSA csv creation
    meritoriousUSA = data[data['Ranking'] == 'Meritorious'] & data[data['Country'] == 'USA']
    meritoriousUSA = meritoriousUSA[['Team Number', 'Country', 'Ranking']]
    meritoriousUSA.to_csv('MeritoriousUSA.csv', index=False)


if __name__ == '__main__':
    main()