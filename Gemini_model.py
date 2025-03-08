from google import genai
from google.genai import types
import pathlib
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys
import numpy as np
import seaborn as sns
from matplotlib.ticker import FuncFormatter

# Initialize the client
client = genai.Client(api_key="AIzaSyAb2VVM52Xh7s4k1MbhEK6RbqSZ62nwwAo")

def generate_financial_insights(file_path):
    """
    Generate detailed financial insights and recommendations from a CSV file
    by directly passing the file to the Gemini API.
    
    Args:
        file_path (str): Path to the CSV file containing financial data
        
    Returns:
        str: Financial insights and recommendations
    """
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found")
        return "File not found"
    
    try:
        # Create a Path object for the file
        filepath = pathlib.Path(file_path)
        
        # Read the file content
        file_content = filepath.read_bytes()
        print(f"Successfully read {len(file_content)} bytes from file")
        
        # Create the file part
        file_part = types.Part.from_bytes(
            data=file_content,
            mime_type='text/csv',
        )
        
        # Create the prompt part
        prompt_text = """
Analyze the provided financial statements CSV file and generate a structured summary, key financial insights, and recommended actions.  

### Instructions:

Only generate insights based on the provided financial data.

1. **Financial Summary:**
   - Summarize the overall financial health of the company.
   - Highlight revenue, profit/loss trends, and key financial ratios (e.g., gross margin, net profit margin, return on assets).  
   - Mention any significant changes compared to previous periods.  

2. **Key Insights:**
   - Identify strengths, weaknesses, opportunities, and risks based on financial trends.  
   - Detect any anomalies, irregularities, or financial red flags.  
   - Assess the company's liquidity, solvency, and profitability.  

3. **Recommended Actions:**
   - Provide strategic recommendations to improve financial performance.  
   - Suggest cost-cutting or revenue-boosting measures if necessary.  
   - Advise on investment, debt management, or operational efficiency.  

Ensure the insights are concise, actionable, and backed by data trends. Present the findings in a structured format for easy readability.  
"""
        
        # If direct file input fails, fall back to text-based approach
        try:
            # Try direct file input first
            print("Attempting direct file input to Gemini API...")
            prompt_part = types.Part(text=prompt_text)
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=[file_part, prompt_part]
            )
            return response.text
        except Exception as e:
            print(f"Direct file input failed: {str(e)}")
            print("Falling back to text-based approach...")
            
            # Fall back to text-based approach
            df = pd.read_csv(file_path)
            text_data = df.to_string(index=False)
            
            full_prompt = f"""
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
   - Assess the company's liquidity, solvency, and profitability.  

3. **Recommended Actions:**
   - Provide strategic recommendations to improve financial performance.  
   - Suggest cost-cutting or revenue-boosting measures if necessary.  
   - Advise on investment, debt management, or operational efficiency.  

Ensure the insights are concise, actionable, and backed by data trends. Present the findings in a structured format for easy readability.  
"""
            response = client.models.generate_content(
                model="gemini-2.0-flash",
                contents=full_prompt
            )
            return response.text
            
    except Exception as e:
        print(f"Error generating financial insights: {str(e)}")
        import traceback
        traceback.print_exc()
        return f"Error: {str(e)}"

def generate_visualization_code(file_path, insights=None):
    """
    Generate Python code for visualizing financial data from a CSV file.
    
    Args:
        file_path (str): Path to the CSV file containing financial data
        insights (str, optional): Financial insights to base visualizations on.
                                 If None, insights will be generated first.
        
    Returns:
        str: Python code for visualizing the financial data
    """
    # If insights not provided, generate them first
    if insights is None:
        print("No insights provided. Generating insights first...")
        insights = generate_financial_insights(file_path)
    
    try:
        # Generate visualization code based on the insights
        print("Generating visualization code...")
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=f"""
            Note: the code should generate code only based on provided insights. donot read any csv file
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

6. **IMPORTANT: Include all necessary functions in your code, especially for loading and preprocessing data.**
   - Make sure all functions used in the code are properly defined
   - Do not reference any external functions that aren't defined in your code
   - Do not read any csv file
   - Execute the code only after the code is generated
7. **Return only pure Python code** with no comments or docstrings.  


Make sure the code is completely self-contained and doesn't rely on any external functions or variables.
Include a main() function that calls all the necessary functions and a if __name__ == "__main__": block to execute it.
"""
        )
        
        # Extract the code from the response
        visual_code = response.text
        
        # Clean up the code (remove markdown code blocks if present)
        if "```python" in visual_code:
            visual_code = visual_code.split("```python")[1].split("```")[0].strip()
        elif "```" in visual_code:
            visual_code = visual_code.split("```")[1].split("```")[0].strip()
        
        # Add imports at the beginning if they're not already there
        required_imports = """
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from matplotlib.ticker import FuncFormatter

# Set the style for the plots
sns.set_theme(style="darkgrid")
plt.rcParams['figure.figsize'] = (12, 8)
plt.rcParams['font.size'] = 12
"""
        
        if "import pandas" not in visual_code.lower():
            visual_code = required_imports + "\n" + visual_code
        
        # Write the code to visual.py
        with open("visual.py", "w") as file:
            file.write(visual_code)
        
        print("Visualization code written to visual.py")
        return visual_code
        
    except Exception as e:
        print(f"Error generating visualization code: {str(e)}")
        import traceback
        traceback.print_exc()
        return f"Error: {str(e)}"

def execute_visualization_code():
    """
    Execute the visualization code in visual.py.
    This function can be called independently after generating the visualization code.
    """
    print("\n=== Executing Visualization Code ===")
    
    # Check if visual.py exists
    if not os.path.exists("visual.py"):
        print("Error: visual.py file not found. Generate visualization code first.")
        return False
    
    try:
        print("Running visualization code...")
        
        # Execute the code in a separate process for better isolation
        import subprocess
        result = subprocess.run([sys.executable, "visual.py"], 
                               capture_output=True, 
                               text=True)
        
        if result.returncode == 0:
            print("Visualizations created successfully!")
            if result.stdout:
                print("\nOutput from visualization code:")
                print(result.stdout)
            return True
        else:
            print(f"Error executing visualization code. Return code: {result.returncode}")
            if result.stderr:
                print("\nError details:")
                print(result.stderr)
            
            # Fall back to exec if subprocess fails
            print("\nAttempting to execute code directly...")
            exec(open("visual.py").read())
            print("Visualizations created successfully using direct execution!")
            return True
            
    except Exception as e:
        print(f"Error executing visualization code: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

def analyze_financial_data(file_path):
    """
    Complete financial analysis workflow: generate insights and visualizations.
    
    Args:
        file_path (str): Path to the CSV file containing financial data
    """
    print(f"Analyzing financial data from: {file_path}")
    
    # Step 1: Generate financial insights
    print("\n=== Generating Financial Insights ===")
    insights = generate_financial_insights(file_path)
    print("\nFinancial Insights:")
    print(insights)
    
    # Step 2: Generate visualization code
    print("\n=== Generating Visualization Code ===")
    visual_code = generate_visualization_code(file_path, insights)
    
    # Step 3: Execute the visualization code
    execute_visualization_code()

# Example usage - uncomment and modify the file path as needed
if __name__ == "__main__":
    # Get the file path from command line argument or use default
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
    else:
        # Default file path - update this to your actual file path
        file_path = "financial_data.csv"
    
    # Run the complete analysis
    analyze_financial_data(file_path)
    
    # Alternatively, you can run just the visualization part if you've already generated the code
    # execute_visualization_code() 