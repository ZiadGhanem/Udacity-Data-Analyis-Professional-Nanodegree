import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = None
    allowed_cities = {"chicago", "new york", "washington"}
    while city not in allowed_cities:
        city = str(input("Would you like to see data for Chicago, New York, or Washington?\n")).lower()


    # TO DO: get user input for month (all, january, february, ... , june)
    month = None
    allowed_months = {"all", "january", "february", "march", "april", "may", "june"}
    while month not in allowed_months:
        month = str(input("Which month? All, January, February, March, April, May, or June? Please type out the full month name.\n")).lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = None
    allowed_days = {"all", "saturday", "sunday", "monday", "tuesday", "wednesday", "thrusday", "friday"}
    while day not in allowed_days:
        day = str(input("Which day? All, Saturday, Sunday, Monday, Tuesday, Wednesday, Thrusday, or Friday? Please type out the full day name.\n")).lower()


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    if city == "chicago":
        df = pd.read_csv("chicago.csv")
    elif city == "new york":
        df = pd.read_csv("new_york_city.csv")
    else:
        df = pd.read_csv("washington.csv")
        
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    if month != "all":
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df.loc[df["month"] == month]

    if day != "all":
        df = df.loc[df["day_of_week"] == day.title()]
        

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    print("The most common month is {}.".format(months[df["month"].mode()[0] - 1].title()))
         

    # TO DO: display the most common day of week
    print("The most common day of the week is {}.".format(df["day_of_week"].mode()[0]))


    # TO DO: display the most common start hour
    print("The most common day of the week is {}.".format(df["hour"].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used start station is {}.".format(df["Start Station"].mode()[0]))

    # TO DO: display most commonly used end station
    print("The most commonly used end station is {}.".format(df["End Station"].mode()[0]))


    # TO DO: display most frequent combination of start station and end station trip
    print("The most frequent combination of start station and end station trip is {} and {}".format(
        df[["Start Station", "End Station"]].mode()["Start Station"][0],
        df[["Start Station", "End Station"]].mode()["End Station"][0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total travel time is {} seconds.".format(df["Trip Duration"].sum()))

    # TO DO: display mean travel time
    print("The total travel time is {} seconds.".format(df["Trip Duration"].mean()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("Counts of user types:")
    for index, value in df["User Type"].value_counts().items():
        print("{}: {}".format(index, value))
    print("\n")

    # TO DO: Display counts of gender
    if "Gender" in df.columns:
        print("Counts of gender:")
        for index, value in df["Gender"].value_counts().items():
            print("{}: {}".format(index, value))
        print("\n")


    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        print("Earliest year of birth is {}.".format(df["Birth Year"].min()))
        print("Most recent year of birth is {}.".format(df["Birth Year"].max()))
        print("Most common year of birth is {}.".format(df["Birth Year"].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

