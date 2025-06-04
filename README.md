# 🚀 Cluster Cryptocurrencies by Volatility and Market Cap

This project applies unsupervised machine learning to group cryptocurrencies based on two key financial indicators: **volatility** and **market capitalization**. The main goal is to identify clusters of similar crypto assets using **K-Means clustering**.

## 🧠 What You’ll Learn

* How to preprocess crypto financial data
* How to compute volatility from price changes
* How to apply K-Means clustering to identify patterns
* How to visualize results with meaningful plots

## 🛠️ Technologies Used

* Python
* pandas
* scikit-learn
* matplotlib
* (Optionally) NumPy

## 📁 Project Structure

```
Cluster_Cryptocurrencies_by_Volatility_and_Market_Cap/
├── main.py                             # Main script for clustering
├── crypto_data.csv                     # CSV file with cryptocurrency data
├── Problema4 - Cluster Cryptocurrencies by Volatility and Market Cap.jpg  # Output plot
└── README.md                           # Project documentation
```

## 📊 Sample Output

![Clustering Output](https://github.com/OrasanuAna/Cluster_Cryptocurrencies_by_Volatility_and_Market_Cap/blob/master/Problema4%20-%20Cluster%20Cryptocurrencies%20by%20Volatility%20and%20Market%20Cap.jpg)

*Figure: Clustered cryptocurrencies based on volatility and market capitalization.*

## 📈 How to Use

1. **Clone the Repository**

   ```bash
   git clone https://github.com/OrasanuAna/Cluster_Cryptocurrencies_by_Volatility_and_Market_Cap.git
   cd Cluster_Cryptocurrencies_by_Volatility_and_Market_Cap
   ```

2. **Install Dependencies**

   ```bash
   pip install pandas scikit-learn matplotlib
   ```

3. **Run the Script**
   Ensure `crypto_data.csv` exists and includes the necessary columns such as:

   * Name/Symbol
   * Market Cap
   * Historical Prices

   Then run:

   ```bash
   python main.py
   ```

4. **View the Results**
   The script will:

   * Calculate volatility and market cap
   * Apply K-Means clustering
   * Display a 2D scatter plot of clusters
