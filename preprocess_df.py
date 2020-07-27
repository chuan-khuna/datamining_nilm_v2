import pandas as pd
import numpy as np


def col_to_datetime(df, col):
    df[col] = pd.to_datetime(df[col])


def add_weekday_col(df, col):
    df['weekday'] = df[col].dt.weekday


def add_month_col(df, col):
    df['month'] = df[col].dt.month


def add_day_minute(df, col):
    df['day_minute'] = (df[col].dt.hour * 60) + (df[col].dt.minute)


def add_week_minute(df, col):
    one_day_minute = 24 * 60
    day_minute = (df[col].dt.hour * 60) + (df[col].dt.minute)
    week_day = df[col].dt.weekday
    df['week_minute'] = (week_day * one_day_minute) + day_minute


def get_sampling_period(timestamp):
    sampling_period = timestamp[1] - timestamp[0]
    print(f"sampling period: {sampling_period}")
    sampling_period = sampling_period.total_seconds()
    print(f"sampling period: {sampling_period} sec")
    return sampling_period


def get_appliance_by_type(df, appliance_type, appliance_type_col):
    appliance_df = df[df[appliance_type_col] == appliance_type]
    return appliance_df


def get_appliance_by_name(df, appliance_name, appliance_name_col):
    appliance_df = df[df[appliance_name_col] == appliance_name]
    return appliance_df