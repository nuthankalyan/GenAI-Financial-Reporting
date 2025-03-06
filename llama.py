from google import genai
client = genai.Client(api_key="AIzaSyAb2VVM52Xh7s4k1MbhEK6RbqSZ62nwwAo")
import pandas as pd
import matplotlib.pyplot as plt

def generate_insights(prompt):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )

    return response.text  # Access the text attribute instead of subscripting

def generate_visual_code(insights):
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"""
Generate Python code to create **high-quality, visually appealing** financial charts based on the following insights:  
{insights}  

### **Instructions:**  

*Note: only generate graph plotting code based on the provided insights.*

Don't plot multiple graphs in a single frame . I need separate graphs for each insight.
1. Use **Matplotlib, Seaborn, and Plotly** for modern, professional-looking financial visualizations.  
2. Generate appropriate chart types saperately for the given insights, such as:  
   - **Bar charts** for revenue and expense comparisons  
   - **Line charts** for trend analysis over time  
   - **Pie charts** for financial distribution  
   - **Heatmaps** for correlation analysis  
   - **Scatter plots** for profitability vs. revenue  
   - **Candlestick charts** for stock/financial data  

3. Ensure proper layout and avoid **overlapping or cluttered plots**:   
   - Use **plt.figure(figsize=(width, height))** to set an appropriate figure size  
   - Utilize **plt.tight_layout()** to automatically adjust spacing  
   - Arrange multiple plots using **plt.subplots()** instead of individual plt.show() calls  
   - Set **adjustable font sizes and labels** to ensure readability  

4. Apply **modern design aesthetics**:  
   - Use **dark mode** or professional Seaborn themes (e.g., `sns.set_theme()`)  
   - Apply **adaptive font sizes** for different screen sizes  
   - Include **gridlines, annotations, and legends** for clarity  
   - Use **aesthetic color palettes** for better visual appeal  

5. Ensure the code is **fully executable without modifications** and automatically handles errors:  
   - **Handles missing data gracefully**  
   - **Scales dynamically** to fit different screen sizes  
   - **Automatically detects and rectifies layout issues**  

6. **Return only pure Python code** with no comments or docstrings.  

""",
    )

    return response.text

def process_csv(file_path):
    """Read CSV, generate AI insights, and plot graphs"""
    df = pd.read_csv(file_path)
    # Convert DataFrame to text for LLM processing
    text_data = df.to_string(index=False)
    prompt = f"""
Analyze the following financial statements and generate a structured summary, key financial insights, and recommended actions.  

### Input Data:
{text_data}  

### Instructions:

Only generate insights based on the provided financial data.

1. **Financial Summary:**
   - Summarize the overall financial health of the company.
   - Highlight revenue, profit/loss trends, and key financial ratios (e.g., gross margin, net profit margin, return on assets).  
   - Mention any significant changes compared to previous periods.  

2. **Key Insights:**
   - Identify strengths, weaknesses, opportunities, and risks based on financial trends.  
   - Detect any anomalies, irregularities, or financial red flags.  
   - Assess the company’s liquidity, solvency, and profitability.  

3. **Recommended Actions:**
   - Provide strategic recommendations to improve financial performance.  
   - Suggest cost-cutting or revenue-boosting measures if necessary.  
   - Advise on investment, debt management, or operational efficiency.  

Ensure the insights are concise, actionable, and backed by data trends. Present the findings in a structured format for easy readability.  
"""

    insights = generate_insights(prompt)
    num_prompt = f"""
Analyze the following financial data and compute key numerical insights.  

### **Input Data:**  
{text_data}  

### **Instructions:**  
only generate numerical insights based on the provided financial data.
Extract and compute the following numerical insights:  

1. **Profitability Metrics:**  
   - Gross Profit = Revenue - Cost of Goods Sold (COGS)  
   - Gross Profit Margin (%) = (Gross Profit / Revenue) * 100  
   - Net Profit = Revenue - Total Expenses  
   - Net Profit Margin (%) = (Net Profit / Revenue) * 100  

2. **Liquidity Ratios:**  
   - Current Ratio = Current Assets / Current Liabilities  
   - Quick Ratio = (Current Assets - Inventory) / Current Liabilities  

3. **Solvency Ratios:**  
   - Debt-to-Equity Ratio = Total Debt / Shareholder’s Equity  
   - Interest Coverage Ratio = EBIT / Interest Expense  

4. **Efficiency Ratios:**  
   - Accounts Receivable Turnover = Revenue / Accounts Receivable  
   - Inventory Turnover = Cost of Goods Sold / Average Inventory  

5. **Growth Metrics (if multiple periods available):**  
   - Revenue Growth Rate (%) = ((Current Period Revenue - Previous Period Revenue) / Previous Period Revenue) * 100  
   - Net Income Growth Rate (%) = ((Current Period Net Income - Previous Period Net Income) / Previous Period Net Income) * 100  

### **Expected Output Format:**  
Provide a structured text-based output with computed values. For example:  

**Profitability Metrics:**  
- Gross Profit: VALUE  
- Gross Profit Margin: VALUE%  
- Net Profit: VALUE  
- Net Profit Margin: VALUE%  

**Liquidity Ratios:**  
- Current Ratio: VALUE  
- Quick Ratio: VALUE  

**Solvency Ratios:**  
- Debt-to-Equity Ratio: VALUE  
- Interest Coverage Ratio: VALUE  

**Efficiency Ratios:**  
- Accounts Receivable Turnover: VALUE  
- Inventory Turnover: VALUE  

**Growth Metrics:**  
- Revenue Growth Rate: VALUE%  
- Net Income Growth Rate: VALUE%  

If any metric cannot be computed due to missing data, mention "Data not available." Ensure all values are numeric and formatted appropriately for financial analysis.  
"""    
    print("\nAI Insights:")
    print(insights)
    num_insights = generate_insights(num_prompt)
    # Generate Python code for visual charts
    visual_code = generate_visual_code(num_insights)
    
    
    
    
    # Write the generated code to visual.py, excluding the first and last lines
    visual_code_lines = visual_code.split('\n')
    visual_code_to_write = '\n'.join(visual_code_lines[1:-1])
    
    with open("visual.py", "w") as file:
        file.write(visual_code_to_write)
    
    # Execute the generated Python code from visual.py
    try:
        exec(open("visual.py").read())
    except Exception as e:
        print(f"Error executing generated code: {e}")

file = "incomeStatement-CSV-annual.csv"
process_csv(file)