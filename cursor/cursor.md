Cursor Process: Replicating the Tableau Dashboard (as a Streamlit App)
======================================================================

This guide outlines using Cursor to build a Streamlit web app that exactly replicates your final Tableau dashboard.

Your Role: Analyst / Developer (guiding the app's structure)

Cursor's Role: AI Pair-Programmer (writing all the code)

### **Step 1: Setup and Load Data**

1.  Open your project folder (containing employment\_data\_final.csv) in Cursor.
    
2.  Create a new file: dashboard.py.
    
3.  **First Prompt:** "In dashboard.py, please write the Python code to import streamlit as st, pandas as pd, and plotly.express as px. Then, write the code to load employment\_data\_final.csv into a pandas DataFrame called df."
    

### **Step 2: Q1 & Q3: The "AI vs. Growth Map" Function**

This function will build your 4-variable bubble chart.

1.  **Prompt:** "Please create a new function called build\_growth\_map(data\_frame). This function should take a DataFrame and return a **Plotly bubble chart** with the following properties:"
    
    *   x='AI Applicability Score'
        
    *   y='Employment Percent Change'
        
    *   size='Employment Change'
        
    *   color='Median Annual Wage'
        
    *   color\_continuous\_scale='OrRd' (for the Orange-Blue/Red effect, OrRd is a good proxy)
        
    *   hover\_name='Title'
        
    *   Add two reference lines (using add\_vline and add\_hline) for the mean of the x and y axes, with a 'dash' line style.
        
    *   Set the title to 'AI vs Growth Map'.
        

### **Step 3: Q2: The "Analytics Roles" Functions**

This requires functions for your two bar charts.

1.  **Filter Logic Prompt:** "First, I need a list of analytics roles. Add code to the _main_ part of the script (outside a function) that creates a list called analytics\_roles\_list. This list should contain all Titles from the DataFrame that contain (case-insensitive) 'Analyst', 'Data', 'Specialist', or 'Operations'.
    
2.  **Chart 1 Prompt (Deep-Dive):** "Now, create a function build\_analytics\_deep\_dive(data\_frame, roles\_list). This function should:
    
    1.  Filter the data\_frame to only include titles in the roles\_list.
        
    2.  Return a Plotly horizontal bar chart of these roles, with x='AI Applicability Score', y='Title', and sorted descending by AI Applicability Score.
        
    3.  Set the title to 'Analytics Role Deep-Dive'."
        
3.  **Chart 2 Prompt (Growth):** "Create a similar function build\_analytics\_growth(data\_frame, roles\_list). It should:
    
    1.  Filter the data\_frame to only include titles in the roles\_list.
        
    2.  Return a Plotly horizontal bar chart with x='Employment Percent Change', y='Title', and sorted descending by Employment Percent Change.
        
    3.  Set the title to 'Analytics Role Growth'."
        

_(Note: You won't create a separate function for "Least Affected" as it's not on the main dashboard, but you could add it as another tab later.)_

### **Step 4: Build the Streamlit Dashboard Layout**

This prompt puts it all together, matching your Tableau layout.

1.  **Prompt:** "Finally, add all the Streamlit 'main' code to the bottom of dashboard.py. This code should:
    
    1.  Set the page config to layout='wide'.
        
    2.  Display the main title: st.title('AI, Jobs, and Salary Analysis')
        
    3.  Create a global filter: Add a st.multiselect widget for the Title column, labeled 'Filter by Job Title:'. Store the selection in selected\_titles.
        
    4.  Create a filtered DataFrame: if selected\_titles: filtered\_df = df\[df\['Title'\].isin(selected\_titles)\] else: filtered\_df = df.copy()
        
    5.  Create a two-column layout: col1, col2 = st.columns(\[2, 1\]) (This makes the left column 2/3 width, right column 1/3)
        
    6.  In col1: Display the main bubble chart by calling col1.plotly\_chart(build\_growth\_map(filtered\_df), use\_container\_width=True)
        
    7.  In col2: Display the two analytics charts stacked vertically:
        
        *   col2.plotly\_chart(build\_analytics\_deep\_dive(filtered\_df, analytics\_roles\_list), use\_container\_width=True)
            
        *   col2.plotly\_chart(build\_analytics\_growth(filtered\_df, analytics\_roles\_list), use\_container\_width=True)"
            
2.  **Run the App:** Open your terminal in Cursor and run streamlit run dashboard.py. This will launch the interactive app that mirrors your Tableau dashboard.
