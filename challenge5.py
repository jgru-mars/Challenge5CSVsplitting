import pandas as pd


def main():

    # read DataFrame
    data = pd.read_csv("2015.csv")

    # This makes either the city or institution an Institution ID if they have been assigned already
    data['Institution ID'] = data.groupby(['ï»¿Institution', 'City']).ngroup()

    # create the Institutions.csv by finding columns in 2015.csv, dropping duplicates, and then writing to new csv
    institution = data[['Institution ID', 'ï»¿Institution', 'City', 'State/Province', 'Country']]
    institution = institution.drop_duplicates(['Institution ID'])
    institution.to_csv('Institutions.csv', index=False)

    # create the Teams.csv by finding columns in 2015.csv, dropping duplicates, and then writing to new csv
    team = data[['Team Number', 'Advisor', 'Problem', 'Ranking', 'Institution ID']]
    team = team.drop_duplicates(['Institution ID'])
    team.to_csv('Teams.csv', index=False)


if __name__ == '__main__':
    main()