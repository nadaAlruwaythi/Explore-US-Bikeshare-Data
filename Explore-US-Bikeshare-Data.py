#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd
import time
import numpy as np


# ## Bike Share Data

# In[ ]:





# In[2]:


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
    cities = ('chicago', 'new york city', 'washington')
    months = ('all', 'january', 'february', 'march', 'april', 'may', 'june')
    days = ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Enter the name of the city to analyze (chicago, new york city, washington) : ").lower()
    while city not in cities:
        print("Enter a Valid Name!!")
        city = input("Enter the name of the city to analyze (chicago, new york city, washington) : ").lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input(
        "Enter the name of the month to filter by, or all to apply no month filter (all, january, february, ... , june) : ").lower()
    while month not in months:
        print("Enter a Valid Name!!")
        month = input(
            "Enter the name of the month to filter by, or all to apply no month filter (all, january, february, ... , june) : ").lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input(
        "Enter the name of the day of week to filter by, or all to apply no day filter (all, monday, tuesday, ... sunday) : ").lower()
    while day not in days:
        print("Enter a Valid Name!!")
        day = input(
            "Enter the name of the day of week to filter by, or all to apply no day filter (all, monday, tuesday, ... sunday) : ").lower()

    print('-' * 40)
    return city, month, day

city,month,day = get_filters()


# In[3]:


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
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


# In[5]:


df = load_data(city, month, day)
df.head()


# In[10]:


def time_stats(df):
    

    print('\nCalculating The Most Frequent Times of Travel')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month : ", df['month'].mode()[0])

    # TO DO: display the most common day of week
    print("The most common day of week : ", df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print("The most common start hour : ", df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


# In[11]:


time_stats(df)


# In[12]:


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most commonly used start station : ", df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print("The most commonly used end station : ", df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print("The most most frequent combination of start station and end station trip : \nStart Station : ", df[["Start Station","End Station"]].mode()['Start Station'][0],"\nEnd Station : ",df[["Start Station","End Station"]].mode()['End Station'][0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


# In[13]:


station_stats(df)


# In[18]:


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total travel time : ", df["Trip Duration"].sum())
    df['Trip Duration'].sum()
    # TO DO: display mean travel time
    print("The mean travel time : ", df["Trip Duration"].mean())
    df['Trip Duration'].mean()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


# In[19]:


trip_duration_stats(df)


# In[22]:


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("The counts of user types :")
    userTypes = df['User Type'].value_counts()
    for userType in userTypes.index:
        print(userType, ":", userTypes[userType])

    # TO DO: Display counts of gender
    try:
        print("The counts of gender :")
        genderTypes = df['Gender'].value_counts()
        for genderType in genderTypes.index:
            print(genderType, ":", genderTypes[genderType])
    except:
        print("No Gender Data!!!")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print("The earliest year of birth :",df["Birth Year"].min())
        print("The most recent year of birth :", df["Birth Year"].max())
        print("The most common year of birth :", df["Birth Year"].mode()[0])
    except:
        print("No Birth Year Data!!!")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


# In[23]:


user_stats(df)


# In[24]:


df.info()


# In[27]:


df.Gender.value_counts()


# In[ ]:




