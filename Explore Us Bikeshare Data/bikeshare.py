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
    cities=['chicago','new york city','washington']
    months = ['january', 'february', 'march', 'april', 'may', 'june','all']
    days =['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'all']
    while True :
        city = input('/n pls enter the city: ')
        if city not in cities :
            continue 
        else :
            break


    # TO DO: get user input for month (all, january, february, ... , june)
    while True :
            month = input('/n pls enter the month or all:  ')
            if month not in months :
                continue 
            else :
               break


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True :
        day = input('/n pls enter the day or all: ')
        if day not in days :
            continue 
        else :
            break


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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['hour'] = df['Start Time'].dt.hour
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    month = df['month'].value_counts().idxmax()
    print('the most common month ',month)


    # TO DO: display the most common day of week
    day = df['day_of_week'].value_counts().idxmax()
    print('the most common month ',day)


    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start = df['Start Station'].value_counts().idxmax()
    print('Most Popular Start station:', most_start)
    


    # TO DO: display most commonly used end station
    most_end = df['End Station'].value_counts().idxmax()
    print('Most Popular End station:', most_end)


    # TO DO: display most frequent combination of start station and end station trip
    print('most frequent combination of start station and end station trip:', most_start,'&',most_end)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total = df['Trip Duration'].sum()
    print('total travel time',total)


    # TO DO: display mean travel time
    mean = df['Trip Duration'].mean()
    print('mean travel time',mean)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('counts of user types',user_types)


    # TO DO: Display counts of gender
    try :
        gender = df['Gender'].value_counts()
        print(' counts of gender',gender)
    except KeyError:
        print('no such gender given')
    


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        max_year = df['Birth Year'].max()
        print(' most recent year of birth',max_year)
    except KeyError:
        print('no such year given')
    try :
        min_year = df['Birth Year'].min()
        print(' earliest year of birth',min_year)
    except KeyError:
        print('no such year given')    
    try:
        year = df['Birth Year'].value_counts().idxmax()
        print(' most common year of birth',year)
    except KeyError:
        print('no such year given')    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    index=0
    user_input=input('would you like to display 5 rows of raw data? ').lower()
    while user_input in ['yes','y','yep','yea'] and index+5 < df.shape[0]:
        print(df.iloc[index:index+5])
        index += 5
        user_input = input('would you like to display more 5 rows of raw data? ').lower()
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
