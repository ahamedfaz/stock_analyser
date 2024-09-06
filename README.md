# 📈 Stock Market Analysis Dashboard

This project is a **Stock Market Analysis Dashboard** built using **Streamlit** and **yfinance**. It allows users to visualize stock data, calculate technical indicators (SMA, EMA, and RSI), and gain insights into stock trends. 

## Features
- **Stock Data Visualization:** Users can input a stock ticker and date range to visualize the stock's closing price.
- **Moving Averages (SMA & EMA):** Calculate and display short-term and long-term moving averages.
- **Relative Strength Index (RSI):** Analyze stock momentum and identify overbought/oversold conditions.
- Interactive user input for custom analysis.

## 🔧 Technologies Used
- **Python 3.11.5**
- **Streamlit**
- **yfinance**
- **pandas**
- **matplotlib**
- **TA-Lib (Technical Analysis Library)**

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ahamedfaz/stock_analyse.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd StockMarketAnalysis
   ```
3. **Install the required dependencies:**
   You can install the dependencies using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

## Required Libraries

The project requires the following Python libraries:
- `streamlit`
- `yfinance`
- `pandas`
- `matplotlib`
- `ta`

Install them using:
```bash
pip install streamlit yfinance pandas matplotlib ta
```

## Usage

1. **Run the application:**
   To run the Streamlit app, use the following command:
   ```bash
   streamlit run stock_analysis.py
   ```

2. **Access the Dashboard:**
   Open the link provided in the terminal (typically `http://localhost:8501/`) to access the stock market analysis dashboard.

3. **User Input:**
   - Input the stock ticker (e.g., AAPL, MSFT).
   - Select the start and end date for fetching stock data.
   - Customize the moving average windows and RSI period.

4. **Analyze the Stock:**
   - View the stock’s closing price.
   - Plot and analyze short-term/long-term moving averages (SMA & EMA).
   - Interpret the RSI for stock momentum.

## Project Structure

```bash
.
├── stock_analysis.py        # Main application file
├── README.md                # Project documentation
├── requirements.txt         # Python dependencies
└── .gitignore               # Git ignore file
```


## Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
