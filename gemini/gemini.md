Gemini + Colab Process: Replicating the Tableau Dashboard
=========================================================

This guide outlines the streamlined process for using Google Colab and Gemini to replicate your final Tableau dashboard. The workflow is centered on you (the analyst) prompting Gemini to write Python code, which you then run in your Colab notebook.

### **Step 1: Create Notebook & Load Data**

1.  Create a new Google Colab notebook.
    
2.  Upload your employment\_data\_final.csv file to the Colab environment.
    
3.  Use the first prompt below to have Gemini generate the code to load and inspect your data. Run this code in your Colab notebook.
    

### **Step 2: Visualization Prompts (for Gemini)**

Your role is to provide these prompts to Gemini. Gemini's role is to generate the Python code (using Plotly for interactivity) for you to copy, paste, and run in your Colab notebook.

Prompt 1: Load and Inspect Data

"You are my senior data scientist co-pilot. Please provide the Python code to:

1.  Import pandas.
    
2.  Load the file employment\_data\_final.csv into a pandas DataFrame called df.
    
3.  Display the .info() and .describe() statistics so I can confirm all columns (Title, AI Applicability Score, Employment Percent Change, Median Annual Wage, Employment Change) are loaded correctly."
    

Prompt 2: Create the "AI vs. Growth Map" (Answers Q1 & Q3)

"Please provide the Python code to create a single, interactive bubble chart using Plotly Express to replicate my 'AI vs Growth Map'. This chart must visualize four variables at once:

*   **X-axis:** AI Applicability Score
    
*   **Y-axis:** Employment Percent Change
    
*   **Bubble Size:** Employment Change (the absolute number)
    
*   **Bubble Color:** Median Annual Wage
    
*   **Tooltip:** Should show the Title and all four metrics.
    
*   "
    

Prompt 3: Refine the "AI vs. Growth Map"

"That's great. Now, please update the code for that Plotly chart to:

1.  Change the color scale to 'OrRd' (Orange-Red) to match my Tableau 'Orange-Blue Diverging' where high is orange/red.
    
2.  Add a dashed vertical reference line for the mean AI Applicability Score.
    
3.  Add a dashed horizontal reference line for the mean Employment Percent Change."
    

Prompt 4: Create the Analytics Roles DataFrame (for Q2)

"I need to filter for specific analytics-related roles. Please provide the Python code to:

1.  Define a list of keywords: \['Analyst', 'Data', 'Specialist', 'Operations'\].
    
2.  Create a new DataFrame called analytics\_df that filters the main df to only include rows where the Title column contains _any_ of those keywords (must be case-insensitive).
    
3.  Print the head of this new analytics\_df so I can verify it."
    

Prompt 5: Create the "Analytics Role Deep-Dive" Chart (Answers Q2)

"Using the analytics\_df from the previous step, please provide the code for a Plotly horizontal bar chart titled 'Analytics Role Deep-Dive'.

*   **X-axis:** AI Applicability Score
    
*   **Y-axis:** Title
    
*   **Sorting:** The chart should be sorted descending by AI Applicability Score."
    

Prompt 6: Create the "Analytics Role Growth" Chart (Answers Q2)

"Using the same analytics\_df, please provide the code for a second Plotly horizontal bar chart titled 'Analytics Role Growth'.

*   **X-axis:** Employment Percent Change
    
*   **Y-axis:** Title
    
*   **Sorting:** The chart should be sorted descending by Employment Percent Change."
    

Prompt 7: Find "Least AI-Affected Jobs" (Answers Q2)

"To replicate my 'Least AI-Affected Jobs' worksheet, please provide the Python code to create a list (or DataFrame) of 20 jobs that meet two conditions:

1.  Their AI Applicability Score is _below_ the average AI Applicability Score of the entire dataset.
    
2.  From that filtered group, they are the top 20 based on the highest Employment Percent Change."
    

### **Step 3: Present Your Findings**

Once you have run the code and generated the interactive Plotly visuals in your Colab notebook, you can:

1.  **For Static Presentations (Google Slides):**
    
    *   Take screenshots of your visuals (including tooltips on key data points).
        
    *   Copy the visuals and paste them into your Google Slides deck.
        
    *   Add your analysis and insights to each slide.
        
2.  **For Interactive Dashboards:**
    
    *   **Prompt Gemini:** "Please provide the Python code to combine all the Plotly charts we've made (AI vs Growth Map, Analytics Role Deep-Dive, Analytics Role Growth) into a single-page interactive dashboard using **Streamlit**.
        
    *   **Layout:** The layout should match my Tableau dashboard: The main 'AI vs Growth Map' on the left, and the two 'Analytics' bar charts stacked vertically on the right."
        
    *   You can then run this new script locally (e.g., streamlit run dashboard.py) to present a fully interactive web-based dashboard.
