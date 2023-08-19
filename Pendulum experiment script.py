import pandas as pd
import matplotlib.pyplot as plt

def read_data(file_path, sheet_num):
    df = pd.read_excel(file_path, sheet_name=sheet_num)
    return df

def cut_noise(df):
    full_time = df.at[df.index[-1], 'Time (s)']
    df = df[(df['Time (s)'] >= 1.0) & (df['Time (s)'] <= (full_time - 1.0))]
    return df

def drop_time(df):
    return df.drop('Time (s)', axis=1)

def calculate_statistics(df):
    means = df.mean()
    std_devs = df.std()
    return means, std_devs

def plot_data(df, title, ylabel):
    plot = df.plot(x='Time (s)', title=title)
    plot.set_xlabel("Time (s)")
    plot.set_ylabel(ylabel)
    return plot

def save_plots(figure, filename):
    figure.savefig(filename)

def main():
    file_path = "/content/phyphoxdata.xls"

    # Read accelerometer and gyroscope data
    df_acceleration = read_data(file_path, 0)
    df_gyroscope = read_data(file_path, 1)

    # Cut noise from the dataframes
    df_acceleration = cut_noise(df_acceleration)
    df_gyroscope = cut_noise(df_gyroscope)

    # Drop timestamp column from the dataframes
    df_acceleration_no_timestamps = drop_time(df_acceleration)
    df_gyroscope_no_timestamps = drop_time(df_gyroscope)

    # Calculate statistics (mean and standard deviation)
    means_acceleration, std_dev_acceleration = calculate_statistics(df_acceleration_no_timestamps)
    means_gyroscope, std_dev_gyroscope = calculate_statistics(df_gyroscope_no_timestamps)

    # Plot and save acceleration and gyroscope data
    plot_acceleration = plot_data(df_acceleration, "Acceleration", "Acceleration (m/s^2)")
    plot_gyroscope = plot_data(df_gyroscope, "Gyroscope", "Gyroscope (rad/s)")
    save_plots(plot_acceleration.get_figure(), 'plot_acceleration.png')
    save_plots(plot_gyroscope.get_figure(), 'plot_gyroscope.png')

    print("Means of Acceleration:\n", means_acceleration)
    print("Standard Deviations of Acceleration:\n", std_dev_acceleration)
    print("Means of Gyroscope:\n", means_gyroscope)
    print("Standard Deviations of Gyroscope:\n", std_dev_gyroscope)

if __name__ == "__main__":
    main()