import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
import matplotlib.dates as mdates

# Load and clean the CSV file
file_path = r"C:\Programming Projects\VS Code\Python\stock price analysis\BHEL Historical Data.csv"

# Read the CSV file
df_raw = pd.read_csv(file_path)

# Clean and preprocess the data
df_clean = df_raw[['Date', 'Price']].copy()

# Convert 'Date' to datetime format
df_clean['Date'] = pd.to_datetime(df_clean['Date'], format='%d-%m-%Y')

# Remove any non-numeric characters from 'Price' and convert to float
df_clean['Price'] = df_clean['Price'].replace({'M': '', 'B': '', ',': ''}, regex=True).astype(float)

# Set 'Date' as the index
df_clean.set_index('Date', inplace=True)

# Check if data is loaded successfully
if df_clean.empty:
    print("Error: No valid data to process.")
else:
    print(df_clean.head())

    # Resample data to yearly frequency (using the last available price of each year)
    df_yearly = df_clean['Price'].resample('YE').last()

    # Plot the cleaned yearly price data
    plt.figure(figsize=(10,6))
    plt.plot(df_yearly, label='Stock Price')

    # Set x-axis major locator to show every year
    plt.gca().xaxis.set_major_locator(mdates.YearLocator(1))  # 1-year intervals
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

    plt.title('Yearly Stock Prices')
    plt.xlabel('Year')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)  # Rotate year labels for better readability

    # Train the ARIMA model on the yearly data
    model = ARIMA(df_yearly, order=(5, 1, 0))  # order (p,d,q)
    model_fit = model.fit()

    # Forecast for the next 10 years
    forecast_steps = 10  # 10 years into the future
    forecast = model_fit.forecast(steps=forecast_steps)

    # Create future dates for the forecast (1-year intervals)
    last_date = df_yearly.index[-1]
    future_dates = pd.date_range(start=last_date + pd.DateOffset(years=1), periods=forecast_steps, freq='Y')

    # Plot the historical data along with the future predictions
    plt.plot(df_yearly.index, df_yearly, label='Historical Data')
    plt.plot(future_dates, forecast, label='10-Year Forecast', linestyle='--')

    # Plot forecasts for 2023, 2024, and 2025
    years_to_predict = [2023, 2024, 2025]
    forecast_df = pd.DataFrame({
        'Year': future_dates.year,
        'Forecast': forecast
    })
    forecast_filtered = forecast_df[forecast_df['Year'].isin(years_to_predict)]
    plt.scatter(forecast_filtered['Year'], forecast_filtered['Forecast'], color='red', zorder=5, label='Forecast 2023-2025')

    # Set x-axis major locator to show every year for future predictions
    plt.gca().xaxis.set_major_locator(mdates.YearLocator(1))  # 1-year intervals
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))

    plt.title('10-Year Stock Price Forecast (1-Year Intervals)')
    plt.xlabel('Year')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)  # Rotate year labels for better readability
    plt.show()

    print("Forecast for the next 10 years (Yearly Intervals):")
    print(forecast)

    # Print the forecast for the years 2023, 2024, and 2025
    print("\nForecast for the years 2023, 2024, and 2025:")
    print(forecast_filtered.set_index('Year'))
