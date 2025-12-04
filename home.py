import streamlit as st

st.markdown("""
    ### ℹ️ About House & Browse
    House & Browse visualizes housing prices across 30 major U.S. metropolitan areas from 2012 to 2023. Using metrics such as median sale price and price-to-income ratio, the dashboard explores how affordability has changed across regions and time.

    ### 🧮 How Price-to-Income Ratio Works
    - Price-to-Income Ratio = **Housing Sale Price ÷ Annual Household Income**
    - Annual Household Income = 2.51 * Annual Income (Median U.S. houshold size = 2.51)
    - Price-to-Income Ratio is divided into 5 levels of affordability:
        - **0.0-3.0:** Affordable
        - **3.1-4.0:** Moderately Unaffordable
        - **4.1-5.0:** Seriously Unaffordable
        - **5.1-8.9:** Severely Unaffordable
        - **9.0+:** Impossibly Unaffordable
            
    *Affordability levels were provided by the Center for Demographics and Policy (See References section)*

            
    ### 📚 References
    #### Dataset
    shengkunwang. (2025). *HouseTS Dataset*. Kaggle. https://www.kaggle.com/datasets/shengkunwang/housets-dataset/data
    
    #### Price-to-Income Ratio Levels
    Cox, Wendell (2025). *Demographia International Housing Affordability, 2025 Edition*. Center for Demographics and Policy. https://www.chapman.edu/communication/_files/Demographia-International-Housing-Affordability-2025-Edition.pdf

    """)