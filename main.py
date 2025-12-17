from src.data_loader import load_data
from src.analyzer import Analyzer
from src.visualizer import plot_trend_by_category

# Load CSV
df = load_data("data/ircc_analyzer_data.csv")

# Analyzer
analyzer = Analyzer(df)

print("Yearly Summary:")
print(analyzer.yearly_summary())

print("\nCategory Summary:")
print(analyzer.category_summary())

# Plot trend for each category
plot_trend_by_category(df)
