#!/usr/bin/env python

import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'}


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

    while True:
        city = input(
            "\nEnter the City Name to Analyze (New York City, Chicago or Washington): ").lower()
        if city not in ['chicago', 'new york city', 'washington']:
            print("Please Enter Correct City Name. Try again.")
            continue
        else:
            break

    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        month = input(
            "\nEnter Month Name to filter by, or enter 'all' to apply no month filter (January, February, March, April, May, June or type 'all') :  ").lower()
        if month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            print("Please Enter Correct Month Name. Try again.")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input("\nEnter Day Name of week to filter by, or 'all' to apply no day filter (Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday or type 'all') : ").lower()
        if day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            print("Please Enter Correct Day Name. Try again.")
            continue
        else:
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

    # convert the Start Time and End Time column to datetime

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month and day of week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month

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

    common_month = df['month'].mode()[0]
    print('Most Common Month:', common_month)

    # TO DO: display the most common day of week

    common_day = df['day_of_week'].mode()[0]
    print('Most Common day:', common_day)

    # TO DO: display the most common start hour
    df['Start Hour'] = df['Start Time'].dt.hour
    common_start_hour = df['Start Hour'].mode()[0]
    print('Most Common Hour:', common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    common_start_station = df['Start Station'].value_counts().idxmax()
    print('Most Commonly used start station:', common_start_station)

    # TO DO: display most commonly used end station

    common_end_station = df['End Station'].value_counts().idxmax()
    print('Most Commonly used end station:', common_end_station)

    # TO DO: display most frequent combination of start station and end station trip

    common_start_and_end_station = df.groupby(
        ['Start Station', 'End Station']).size().nlargest(1)
    print('\nMost Commonly used combination of start station and end station trip: \n',
          common_start_and_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    total_travel_time = sum(df['Trip Duration'])
    print("Total travel time : ", total_travel_time)

    # TO DO: display mean travel time

    mean_travel_time = df['Trip Duration'].mean()
    print("Mean travel time: ", mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    user_types = df['User Type'].value_counts()
    print("User Types:\n", user_types)

    # TO DO: Display counts of gender

    try:
      gender_types = df['Gender'].value_counts()
      print("\nGender Types:\n", gender_types)
    except KeyError:
      print("\nGender Types:\nNo data available for this month.")

    # TO DO: Display earliest, most recent, and most common year of birth

    try:
        earliest_year_bith = df['Birth Year'].min()
        print("\nEarliest Year: ", int(earliest_year_bith))
    except KeyError:
        print("\nNo data available for this month.")

    try:
        most_recent_year = df['Birth Year'].max()
        print('\nMost Recent Year:', int(most_recent_year))
    except KeyError:
        print("\nNo data available for this month.")

    try:
        most_common_year = df['Birth Year'].value_counts().idxmax()
        print('\nMost Common Year:', int(most_common_year))
    except KeyError:
        print("\nNo data available for this month.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    
    counter = 0
    choice = input("\nDo you want to see the first 5 rows of data? (Enter 'Yes' or 'No') :  ").lower()
    if choice == "yes":
        counter += 5
        # display data
        result = df.head(5)
        print("\nFirst 5 rows of the DataFrame : ")
        print(result)
        while True:
            choice = input("\nDo you want to see the next 5 rows of data? (Enter 'Yes' or 'No') : ").lower()
            if choice == "yes":
                counter += 5                
                result_next = df[counter:counter+5]
                print("\nNext 5 rows of the DataFrame : ")
                print(result_next)                
            elif choice == "no":
                print('-'*40)
                return None
            else:
                print("\nPlease Enter 'Yes' or 'No' Only")
    elif choice == "no":
        print('-'*40)
        return None
    else:
        print("\nPlease Enter 'Yes' or 'No Only")
        display_data(df)
    
    print('-'*40)


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
