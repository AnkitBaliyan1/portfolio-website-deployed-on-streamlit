import streamlit as st
from PIL import Image
import os
from pathlib import Path

# ********************************************************************************************************************************************************************************************************************************************************************************************************************
# ********************************************************************************************************************************************************************************************************************************************************************************************************************
# ********************************************************************************************************************************************************************************************************************************************************************************************************************
# ********************************************************************************************************************************************************************************************************************************************************************************************************************
# ********************************************************************************************************************************************************************************************************************************************************************************************************************

def resume_hr():
    st.subheader("Resume Screening Assistance with AI")
    st.markdown("Check out the Application here: 👉🏻  [App Link](https://resumeanalysiswithai-byankit.streamlit.app)  👈🏻")
    image = Image.open('static/project-images/resume_hr_app.png')
    st.image(image, use_column_width=True)
    st.markdown('''
                ##### Features:
                - **Job Description Analysis**: Users can input the job description text, which the system uses to identify relevant resumes.
                - **Resume Upload**: Users can upload multiple resumes in PDF format.
                - **Document Analysis**: The system processes the uploaded resumes, extracting text and metadata for analysis.
                - **Vector Embeddings**: Utilizes OpenAI's embedding model to create vector representations of resume documents.
                - **Pinecone Integration**: Integrates with Pinecone, a vector database service, to store and retrieve document embeddings efficiently.
                - **Similar Document Retrieval**: Finds resumes similar to the provided job description using vector similarity search.
                - **Summary Generation**: Generates summaries for relevant resumes to provide quick insights.
                - **Streamlit Interface**: Offers a user-friendly interface built with Streamlit, making it easy to interact with the system.
                ''')
    
def doc_bot():
    st.subheader("Talk to your Documents")
    st.markdown("Check out the Application here: 👉🏻  [App Link](https://customchatbot-byankit.streamlit.app)  👈🏻")
    image = Image.open('static/project-images/doc_bot.png')
    st.image(image, use_column_width=True)
    st.markdown("""
                ##### Features
                - **Upload PDF Documents**: Users can upload PDF documents to be indexed and utilized by the chatbot for answering queries.
                - **Document Indexing**: Uploaded documents are indexed and stored using Pinecone, enabling efficient retrieval based on user queries.
                - **Chatbot Interface**: Users can input queries through a text area and receive answers from the chatbot.
                - **Similar Document Retrieval**: The chatbot retrieves relevant documents based on the user query and presents answers from those documents.
                - **Responsive UI**: The Streamlit interface provides an interactive and user-friendly experience.
                """)
    image = Image.open('static/project-images/doc_bot_rag_flow.png')
    st.image(image, use_column_width=True)

def csv_bot():
    st.subheader("Analyse your CSV document with AI")
    st.markdown("Check out the Application here: 👉🏻  [App Link](https://chatbot-for-csv-analysis-byankit.streamlit.app)  👈🏻")
    image = Image.open('static/project-images/csv_bot_2.png')
    st.image(image, use_column_width=True)
    st.markdown("""
                ##### Features:
                - User-friendly interface deployed on Streamlit for seamless interaction. 💻
                - Natural language processing capabilities for interpreting user queries. 🗣️
                - Backend analysis engine for processing CSV files based on user queries. 🛠️
                - Supports various analytical tasks such as filtering, sorting, aggregating, and visualizing data. 📈
                - Provides flexibility in query formulation to accommodate diverse analysis needs. 🔄
                - Easily extensible for integrating additional analysis functionalities. ➕
                """)
    
def bot_youtube():
    st.subheader("Generate Script for YouTube Video with AI")
    st.markdown("Check out the Application here: 👉🏻  [App Link](https://youtubescriptgenerator-byankit.streamlit.app)  👈🏻")
    image = Image.open('static/project-images/bot_youtube.png')
    st.image(image, use_column_width=True)
    st.markdown("""
                ###### Features 🔥 :
                - **Customizable Script Generation:** Users can specify the topic and duration of the video, as well as adjust the creativity level to control the tone and style of the generated script.
                - **Integration with OpenAI:** Utilizes OpenAI's language model to generate natural and engaging scripts.
                - **DuckDuckGo Search Integration:** Provides relevant search data from DuckDuckGo to enrich the script.
                - **Secure API Key Input:** Allows users to securely input their OpenAI API key via a password text input.
                """)
    
def basic_chatbot():
    st.subheader("Generate Script for YouTube Video with AI")
    st.markdown("Check out the Application here: 👉🏻  [App Link](https://basicchatbot-openai-palm.streamlit.app)  👈🏻")
    image = Image.open('static/project-images/basic_chatbot.png')
    st.image(image, use_column_width=True)
    st.markdown("""
                The Multi-Mode Chatbot is a versatile conversational AI tool that can generate responses using multiple APIs. Built using Streamlit, this multi-page application offers a minimal and straightforward user interface. It leverages the OpenAI and Google GenerativeAI APIs to provide intelligent and context-aware responses. Whether you need a chatbot for customer support, knowledge base, or just casual conversation, this project has you covered.
                ###### Features 🔥 :
                - **Custom Mode:** Users can specify the backend API Modes.
                - **Integration with OpenAI and Google API:** Utilizes OpenAI's and Google's language model to generate natural and engaging response.
                - **Multiple ChatBot Personalities:** User can select multiple personalities of the chatbot for specific usecase.
                - **Short and Crisp Response:** The resposne is crisp and accrate in multiple personalities. Also, there is limit on the length of response generated.
                """)
    
# ********************************************************************************************************************************************************************************************************************************************************************************************************************
# ********************************************************************************************************************************************************************************************************************************************************************************************************************
# ********************************************************************************************************************************************************************************************************************************************************************************************************************
# ********************************************************************************************************************************************************************************************************************************************************************************************************************
# ********************************************************************************************************************************************************************************************************************************************************************************************************************

dashboard_images = ("static/project-images/dashboard/")

def dashboard_real_estate():
    st.subheader("Real Estate Property Management Dashboard")
    image_path = os.path.join(dashboard_images, "Real_Estate_Dashboard.png")
    image = Image.open(image_path)
    
    st.markdown("""
                ###### About Dashboard : 
                The dashboard was created for ease in tracking the multiple real-estate parameters and to help in business decision making.
                """)
    st.image(image, use_column_width=True)
    st.markdown("""
                **KPI Metrics:**
                1. **Total Monthly Revenue:** Track the total revenue generated from properties each month to assess financial performance.
                2. **Occupancy Rate:** Measure the percentage of occupied properties compared to the total available properties.
                3. **Average Rental Length:** Calculate the average duration of property rentals.
                4. **Total Maintenance Costs:** Monitor the cumulative costs associated with property maintenance.

                **Charts:**
                1. **Monthly Revenue & Maintenance by Property Type:** Visualize the monthly revenue and maintenance costs breakdown by property types (e.g., apartments, houses, commercial properties).
                2. **Average of Revenue & Maintenance by Month:** Display the average monthly revenue and maintenance costs to identify trends and seasonality.
                3. **Occupancy by Property Type:** Categorize occupancy rates by property types to identify which types are in higher demand.
                4. **Average Rental Length by Property Type:** Show the average rental duration for different property types.
                5. **Average of Maintenance Cost by Occupier Property:** Calculate the average maintenance cost per occupier property to identify areas where maintenance is more intensive.
                
                """)
    
def dashboard_finance():
    st.subheader("Dashboard for Managing Financial Assets")
    image_path = os.path.join(dashboard_images, "Finance_Dashboard.png")
    image = Image.open(image_path)
    
    st.markdown("""
                
                ###### About Dashboard : 
                The dashboard was developed for a Financial Assets management company to keep a track of its performance over time. It also showcase the portfolio and total assets manager under each category.
                """)
    st.image(image, use_column_width=True)
    st.markdown("""

                **KPI Metrics:**
                1. **Total Assets Under Management (AUM):** Track the total value of assets managed by the organization to assess growth and performance.
                2. **Net Profit Margin:** Measure profitability by calculating the ratio of net profit to total revenue.
                3. **Average Cost Per Acquisition (CPA):** Determine the average cost incurred to acquire new customers.
                4. **Churn Percentage:** Analyze customer retention by calculating the percentage of customers lost over a specific period.

                **Charts:**
                1. **Asset Under Management by Investment Types:** Visualize AUM distribution across various investment types (e.g., stocks, bonds, real estate).
                2. **Monthly Inflow vs. Outflow by Month:** Display the monthly trend of funds inflow and outflow to identify cash flow patterns.
                3. **Asset Under Management by Customer Age Group:** Categorize AUM by age groups to target demographic-specific strategies.
                4. **Sum of Inflow and Outflow by Investment Type:** Show the sum of funds inflow and outflow for each investment type to assess popularity and trends.
                
                """)

def dashboard_healthcare():
    st.subheader("Dashboard for Healthcare Metric")
    image_path = os.path.join(dashboard_images, "Healthcare_dashboard.png")
    image = Image.open(image_path)
    st.markdown("""
                
                ###### About Dashboard :
                This dashboard contains the information about performance of a healthcare institution over time across multiple factors like age group, admission rate, satisfication rate, telehealth calls, etc.
            
                
                """)
    st.image(image, use_column_width=True)
    
    
def dashboard_e_commerce():
    st.subheader("E-commerce")
    image_path = os.path.join(dashboard_images, "ecommerce_dashboard.png")
    image = Image.open(image_path)
    st.markdown("""
                
                ###### About Dashboard :
                The dashboard tries to capture performance of a e-commerce brand across regions, time and channels. 
                
                """)
    st.image(image, use_column_width=True)
    
    
def dashboard_retail():
    st.subheader("Retail Dashboard")
    image_path = os.path.join(dashboard_images, "Retail_dashboard.png")
    image = Image.open(image_path)
    st.markdown("""
                
                ###### About Dashboard :
                This dashboard belongs to a retail store, and simplifies the performance across time. The analysis is done for sales, customer acquired, customer retention and order value.
                
                """)
    st.image(image, use_column_width=True)


# ********************************************************************************************************************************************************************************************************************************************************************************************************************
# ********************************************************************************************************************************************************************************************************************************************************************************************************************
# ********************************************************************************************************************************************************************************************************************************************************************************************************************
# ********************************************************************************************************************************************************************************************************************************************************************************************************************
# ********************************************************************************************************************************************************************************************************************************************************************************************************************
    

def california_house_price():
    st.markdown("""
                # California Hourse Price Prediction

                ## Overview

                This project is a completed regression analysis task that predicts a target variable, `MedHouseVal`, using a given dataset. The code and steps outlined here involve data preprocessing, exploratory data analysis (EDA), and the creation of linear regression models for prediction.

                In addition to the primary objectives of this regression analysis project, I also attempted to investigate the potential relationship between the distance from a water body (e.g., rivers, lakes, or oceans) and property prices. This analysis aimed to explore whether proximity to water bodies had any significant impact on property values.

                ## Project Structure

                The project's structure and key components include:

                - **Data Cleaning**: The code handles missing data by reading the data from CSV files (`train.csv` and `test.csv`) and specifying `na.strings = ""` to manage missing values.

                - **Outlier Handling**: Outliers are addressed using the Interquartile Range (IQR) method. A custom function `handle_outlier()` is defined to handle outliers in specific numeric columns.

                - **Exploratory Data Analysis (EDA)**: Boxplots are created to visualize the distribution of numerical variables and identify outliers. Additionally, a correlation matrix is computed and presented as a heatmap for understanding variable relationships.

                - **Linear Regression Modeling**: Two linear regression models (`mod`) are built:
                1. Predicting `MedHouseVal` based on `MedInc` and `AveRooms`.
                2. Predicting `MedHouseVal` using all available numeric features except `id` and `Population`.

                - **Model Evaluation**: The code calculates the root mean squared error (RMSE) between the actual `MedHouseVal` and the predicted values (`pred_train`) from the linear regression model.

                - **Test Data Processing**: Similar data preprocessing steps, including outlier handling, are applied to the test data. Predictions (`pred_test`) are generated using the trained model (`mod`) for the test dataset.

                ## Challenges

                Unfortunately, I encountered challenges and limitations during this analysis:

                1. Hardware Limitations: Analyzing the relationship between property prices and distance from water bodies often requires large datasets with precise geographic information. Due to hardware limitations, I faced difficulties in handling and processing such extensive data.

                2. Resource Constraints: Gathering and processing geographical data, including distance calculations from water bodies, can be resource-intensive. Lack of access to sufficient computing resources hindered my ability to conduct this analysis efficiently.

                3. Data Availability: Availability of precise geographic data, including accurate distance measurements from water bodies for a large dataset of properties, was also a challenge. Obtaining and integrating such data proved to be a complex task.

                
                """)
    st.markdown("""
                ## Tools:
                - R - Programming
                - R-Studio

                ## Libraries:
                - library("dplyr")
                - library('summarytools')
                - library("ggplot2")
                - library("psych")
                - library("reshape2")
                - library("Metrics")

                
                """)
    st.markdown("Link to GitHub Repository: [Link](https://github.com/AnkitBaliyan1/IPBA-14-Regression)")


# ********************************************************************************************************************************************************************************************************************************************************************************************************************
def company_attrition():
    st.markdown("""
                # Employee Attrition Prediction using Machine Learning

                ## Overview

                This project was completed as part of a Kaggle competition assignment during a program at IIM-Indore. The objective of this classification problem is to predict employee attrition based on comprehensive data, including demographic information, job-related details, and satisfaction scores.

                The dataset consists of 1,677 observations used for training the model and predicting attrition for 1,119 observations. There are over 30 independent variables in the dataset, making it a challenging task. However, this project provided valuable insights into feature selection and data preprocessing techniques.

                ## Data Cleaning and Preprocessing

                Handling a diverse set of independent variables required extensive data cleaning and preprocessing. Several steps were taken to prepare the data for modeling:

                - **Feature Selection**: Variables like 'Over18,' which capture whether the employee is over 18 years of age, were removed since they were homogenous and didn't provide meaningful information.

                - **Outlier Handling**: Outliers in both continuous and categorical variables were addressed to ensure the model's robustness.

                - **Data Entry Errors**: Data entry errors, such as an education level of 15 with only one observation while all others were between 1 and 5, were identified and corrected.

                - **Data Scaling**: LabelEncoder, StandardScaler, and MinMaxScaler from the sklearn.preprocessing library were used for data preprocessing. LabelEncoding and One-Hot Encoding were used for categorical variables, and MinMaxScaler was used for scaling continuous variables.

                ## Model Training and Testing

                Multiple machine learning models were trained and tested on the preprocessed data. The Logistic Regression model achieved the highest accuracy score of over 80%. Other models were also evaluated, including Random Forest Classifier and Decision Tree Classifier.

                ## Results

                The model achieved a correct prediction rate of around 75% on the validation data. However, it performed even better on the total test cases, with an accuracy of over 80%. This accuracy rate ranked as the second-highest among all participants in the competition for predicting attrition.


                This project demonstrates the effectiveness of machine learning in predicting employee attrition and highlights the importance of data preprocessing and feature selection in achieving accurate results.


                """)
    st.markdown("""
                ## Tools:
                - Python
                - Jupyter Notebook


                ## Libraries:
                - Pandas
                - Numpy
                - Matplotlib
                - Seaborn
                - Sklearn
                
                ## Models employed:
                - Logistic Regression
                - Decision Tree Classifier
                - Random Forest Classifier

                
                """)
    st.markdown("Link to GitHub Repository: [Link](https://github.com/AnkitBaliyan1/attrition_prediction)")


# ********************************************************************************************************************************************************************************************************************************************************************************************************************


def twitter_disaster():
    st.markdown("""
                # Twitter Disaster Prediction Model
                ### About this Project
                This project focuses on the development of a classification model that predicts the occurrence of a disaster based on Twitter data. The dataset has undergone extensive data cleaning and preprocessing to ensure the model's effectiveness. The goal is to accurately classify tweets as either related to a disaster or not.
                """)
    
    st.markdown("""
                ## Tools:
                - Python
                - Jupyter Notebook

                ## Libraries:
                - nltk
                - re
                - Pandas
                - Numpy
                - Matplotlib
                - Seaborn
                - Sklearn


                ## Models employed:
                - PassiveAggressiveClassifier,
                - LogisticRegression
                - naive_bayes
                """)
    st.markdown("Link to GitHub Repository: [Link](https://github.com/AnkitBaliyan1/Twitter-Disaster-Detection)")


# ********************************************************************************************************************************************************************************************************************************************************************************************************************
    
def movie_sentiment():
    st.markdown("""
                # IMDb Sentiment Analysis Project
                ### About this Project
                This project focuses on performing sentiment analysis on a dataset of 50,000 movie reviews from IMDb. The objective is to classify each review as either "positive" or "negative" based on its content. Various classification algorithms and deep learning models were employed to achieve this task, and their performance was evaluated using precision and recall metrics.
                
                """)
    
    st.markdown("""
                ## Tools:
                - Python
                - Jupyter Notebook
                - Kaggle

                ## Libraries:
                - nltk
                - re
                - Pandas
                - Numpy
                - Matplotlib
                - Seaborn
                - Sklearn


                ## Models employed:
                - Logistic Regression
                - Decision Tree Classifier
                - Random Forest Classifier
                - Multinomial Classifier
                - KNeighbors Classifier
                - MultinomialNB Classifier
                """)
    st.markdown("Link to GitHub Repository: [Link](https://github.com/AnkitBaliyan1/sentiment_analysis_ML-DL)")
# ********************************************************************************************************************************************************************************************************************************************************************************************************************
 
def bpcl_inventory():
    st.markdown("""
                # Twitter Disaster Prediction Model
                ### About this Project
                This project aims to forecast inventory required based on the sales occured in the past. The time series forecasting was conducted for top 10 performing SKUs, out of over 700 SKUs for 3 different territories.
                The Data was highly impacted by COVID and it was easily depicted in the dataset. 
                
                """)
    st.markdown("""
                ## Tools:
                - Python
                - Jupyter Notebook
                - Tablueu

                # Libraries:
                - pandas
                - Numpy
                - Matplotlib
                - Seaborn
                - Sklearn

                # Models employed:
                - ARIMA
                - SARIMA
                """)
    
    
# ******************************************************************************************************************************************************************************************************************************************************************************************************************** 
    
def dont_get_kicked():
    st.markdown("""
                # Model to predict if the CarBuy at Auction IsBadBuy!
                ### About this Project
                This project involves the development of a classification model to predict whether a buy at an auction is a bad buy or not. The dataset used for this task is highly imbalanced, making it a challenging problem to address. Various machine learning algorithms, including logistic regression, decision tree, random forest, support vector machine (SVM), etc., have been employed to build the classification model. Additionally, techniques such as grid search and randomized grid search have been used to fine-tune the hyperparameters of these models. Both oversampling and undersampling methods have been experimented with to achieve an optimum model.
                

                """)
    
    st.markdown("""
                ## Tools:
                - Python
                - Jupyter Notebook
                - Kaggle
                

                ## Libraries:
                - pandas
                - Numpy
                - Matplotlib
                - Seaborn
                - Sklearn


                ## Models employed:
                - Logistic Regression
                - KNeighbours Classifier
                - Decision Tree Classifier
                - Random Forest Classifier
                - SVC Classifier
                - SVM Classifier
                - XGBoost Classifier
                """)
    st.markdown("Link to GitHub Repository: [Link](https://github.com/AnkitBaliyan1/classification-don-t-get-kicked)")



# ********************************************************************************************************************************************************************************************************************************************************************************************************************
    
def lead_prediction():
    st.markdown("""
                # Lead Prediction Model
                ### About this Project
                The Lead Predictions Web App is designed to predict lead conversions based on user-provided data. This interactive web application allows users to make predictions either one by one or in bulk. The predictions are generated using a machine learning model, and the app provides an easy-to-use interface for lead conversion forecasting.
                

                """)
    st.markdown("""
                ## Tools:
                - Python
                - Streamlit
                - Jupyter Notebook

                ## Libraries:
                - pandas
                - Numpy
                - Matplotlib
                - Seaborn
                - Sklearn
                - Pickle

                ## Models employed:
                - Logistic Regression
                - Decision Tree Classifier
                - Random Forest Classifier
                - SVM Classifier
                """)
    st.markdown("Link to GitHub Repository: [Link](https://github.com/AnkitBaliyan1/Lead_Prediction_Streamlit_Application)")


    
# ********************************************************************************************************************************************************************************************************************************************************************************************************************
# ********************************************************************************************************************************************************************************************************************************************************************************************************************
# ********************************************************************************************************************************************************************************************************************************************************************************************************************
# ********************************************************************************************************************************************************************************************************************************************************************************************************************
# ********************************************************************************************************************************************************************************************************************************************************************************************************************

sql_image_path = ("static/project-images/sql/")

def customer_analysis():
    st.subheader("Customer Analysis")

    st.markdown("""
                ## Project Overview

                This project entails a comprehensive analysis of customer data to derive valuable insights for the business. The SQL queries utilized in this project focus on various aspects of customer behavior, market performance, and employee contributions. The following sections detail the key analyses conducted and the insights obtained from the data.
                """)
    
    image_path = os.path.join(sql_image_path, "customer_analysis_schema.png")
    image = Image.open(image_path)
    st.image(image, use_column_width=True)

    st.markdown(
                """
                ## Project Details

                **1. Average Order Value per Customer**
                Calculate the average order value for each customer to understand their purchasing behavior.

                **2. Customer Lifetime Value**
                Determine the Customer Lifetime Value (CLV) to assess the long-term value of customers to the business.

                **3. Classification of Customers**
                Classify customers as either new or existing within a certain month to track customer retention and acquisition.

                **4. Retention Rate Analysis**
                Analyze the retention rate for each month to understand the customer retention trends over time.

                **5. Customer Orders by Country**
                Count the number of orders from each country to identify the market reach and performance in different regions.

                **6. Employee Performance**
                Evaluate the number of customers served by each employee to understand their individual contributions.

                **7. Top Performing Employees by Country**
                Identify the top-performing employees in each country to acknowledge outstanding sales performances.

                **8. Top Performing Employees by Product Line**
                Determine the top-performing employees for each product line to recognize their contributions to specific product sales.

                **9. Top Performing Countries by Product Line**
                Analyze the top-performing countries for each product line to identify successful markets.

                **10. Top and Worst Product Lines by Country**
                Identify the top 2 and worst performing product lines for each country to focus on improving underperforming areas.

                **11. Product Line Performance Analysis**
                Determine the number of countries where a product line is the top seller or the worst seller to understand market penetration.

                **12. Country Ranking Analysis**
                Rank countries based on the number of offices, order count, and sales to prioritize target regions.

                **13. Active and Inactive Customers**
                Identify active and inactive customers in the last N months to tailor retention strategies.

                **14. Top-Selling Products by Country**
                Determine the top-selling product in each country to understand customer preferences in different regions.

                **15. Average Time Between Orders**
                Calculate the average time between orders for each customer to assess purchasing frequency and behavior.
                """)
    
    col1, col2 = st.columns(2)

    with col1:
        image_path = os.path.join(sql_image_path, "view_1.jpeg")
        image = Image.open(image_path)
        st.image(image, use_column_width=True)
    with col2:
        image_path = os.path.join(sql_image_path, "view_2.jpeg")
        image=Image.open(image_path)
        st.image(image, use_column_width=True)


    st.markdown(
        """
        
        ## Observations and Outcomes

        Here are the key observations made from the analysis of the Power BI dashboard:

        

        1. **Dominance of the USA:** The United States accounts for approximately half of the total orders and contributes to over 50% of the overall revenue, indicating its significant role in the company's sales.

        2. **Significance of Classic Cars:** Classic cars play a vital role in the company's revenue, contributing to around 40% of the total revenue, with 20% of this revenue coming solely from the USA.

        3. **Key Revenue-Generating Countries:** The majority, around 80%, of the total revenue is driven by just three countries: the USA, Spain, and France, emphasizing the importance of these markets for the company's profitability.

        4. **Contribution of Specific Products:** Two product categories, classic cars (40%) and vintage cars (20%), collectively account for 60% of the total revenue, highlighting their crucial role in the company's sales.

        5. **Best Performing Quarter and Month:** The fourth quarter emerges as the best performing quarter, generating 49% of the total revenue, with November alone contributing to 30% of the overall revenue, indicating a strong end-of-year performance.

        6. **Underperforming Product Categories:** Trains and ships are the least performing product categories, contributing to only 2% of the total revenue. Among them, the USA, Spain, and Australia are the primary contributors, signaling potential areas for improvement or strategic adjustments.

        7. **New Zealand's Low Revenue Impact:** Despite being among the top-performing countries, New Zealand generates relatively low-value orders, not contributing significantly to the company's overall revenue, suggesting a need for focused strategies to enhance its revenue contribution.

        These observations provide valuable insights into the key drivers and challenges within the business, offering actionable points for strategic decision-making and operational improvements.


        """
    )


    st.markdown("Link to GitHub Repository: [Link](https://github.com/AnkitBaliyan1/SQL_projects/tree/main/customer_analysis)")



# ********************************************************************************************************************************************************************************************************************************************************************************************************************

def advertisement():
    st.subheader("Advertisement Analysis")

    image_path = os.path.join(sql_image_path, "advertisement_schema.jpeg")
    image=Image.open(image_path)
    st.image(image, use_column_width=True)

    st.markdown("""
            **Problem Statement:**
                An advertising agency is running a digital advertising campaign for a client. The campaign involves displaying ads on various online platforms. To evaluate the campaign's effectiveness and make data-driven decisions, the agency needs to analyze a dataset containing information about the campaign's performance, ad placements, and user interactions.

                **Dataset Details:**

                The dataset required for this project should include the following tables:

                1. **Campaign Data:**
                - `campaign_id` (unique identifier for each campaign)
                - `campaign_name` (name of the advertising campaign)
                - `start_date` (start date of the campaign)
                - `end_date` (end date of the campaign)
                - `budget` (total budget allocated for the campaign)

                2. **Ad Placement Data:**
                - `ad_id` (unique identifier for each ad placement)
                - `campaign_id` (foreign key linking to the campaign it belongs to)
                - `platform` (the online platform where the ad was displayed, e.g., Facebook, Google Ads)
                - `placement_cost` (the cost incurred for placing the ad on the platform)

                3. **User Interaction Data:**
                - `interaction_id` (unique identifier for each user interaction with an ad)
                - `ad_id` (foreign key linking to the ad placement)
                - `user_id` (unique identifier for each user)
                - `interaction_type` (e.g., click, view, conversion)
                - `interaction_date` (date and time when the interaction occurred)
                                """)
    image_path = os.path.join(sql_image_path, "advertisement_schema.jpeg")
    image=Image.open(image_path)
    st.image(image, use_column_width=True)
    st.markdown("""
                Creating a Business Intelligence (BI) dashboard with the dataset and SQL problems provided can offer valuable insights into your advertising campaign's performance. Here are some key performance indicators (KPIs) and charts you can create for your BI dashboard:

                **Key Performance Indicators (KPIs):**

                1. **Total Ad Campaigns:** Display the total number of ad campaigns currently in the dataset. This KPI gives an overview of the campaign volume.

                2. **Total Ads Running:** Show the total number of ads currently active or running across all campaigns. This KPI provides insights into the scale of ad placements.

                3. **User Interactions:** Present the total number of user interactions (clicks, views, and conversions) recorded across all campaigns. This KPI helps assess user engagement.

                4. **Overall % of Budget Spent:** Calculate the percentage of the total budget spent compared to the allocated budget across all campaigns. This KPI offers insights into budget utilization.

                5. **Average Campaign Duration:** Represent the average duration, in days, for all active advertising campaigns. It provides insights into the typical length of campaigns.


                **Charts:**

                1. **Time Series Chart for Total User Interactions:** Plot the total number of user interactions (clicks, views, and conversions) over time (e.g., daily, weekly, or monthly).

                2. **Budget Allocation by Campaign Pie Chart:** Show a pie chart illustrating the allocation of the total budget across different campaigns.

                3. **Placement Cost by Campaign Bar Chart:** Compare CTR for each campaign using a bar chart.

                4. **Conversion Rate by campaign Bar Chart:** Compare the conversion rate for each campaign using bar chart.

                5. **Interaction Type by Campaign Bar Chart:** Compare interaction type count for each campaign using a stacked bar chart.


                """)
    
    st.markdown("Link to GitHub Repository: [Link](https://github.com/AnkitBaliyan1/SQL_projects/tree/main/Advertisement_campaign_Analysis)")



# ********************************************************************************************************************************************************************************************************************************************************************************************************************


def pizza_sales():
    st.subheader("Pizza Sales Analysis")

    st.markdown("""
                #### Project Overview
                The Pizza Sales SQL Project is a comprehensive analytical tool designed to provide in-depth insights into pizza sales performance. By integrating an interactive dashboard with a series of SQL queries, this project aims to deliver real-time data and visualizations to aid in business decision-making.
                """)

    image_path = os.path.join(sql_image_path, "pizza_sales_dashboard.jpeg")
    image=Image.open(image_path)
    st.image(image, use_column_width=True)


    st.markdown("""                
                #### Features
                The project encompasses several key features and metrics:

                **Key Performance Indicators:**
                1. **Total Revenue**: Measures the cumulative earnings from pizza sales.
                2. **Average Order Value**: Calculates the mean value of each sales order.
                3. **Total Pizzas Sold**: The count of all pizzas sold over a given period.
                4. **Total Orders**: The total number of orders received.

                **Charts and Analytics:**
                1. **Average Number of Pizzas per Order**: Analyzes the typical order size.
                2. **Daily Trend of Total Orders**: Observes the daily fluctuations in order numbers.
                3. **Monthly Trend of Orders**: Evaluates long-term ordering trends on a monthly basis.
                4. **Sales by Pizza Category**: Breaks down revenue according to pizza types.
                5. **Sales by Pizza Size**: Assesses sales distribution by the size of the pizzas.
                6. **Total Pizzas Sold by Category**: Counts the number of pizzas sold, categorized by type.
                7. **Top 5 Pizzas by Revenue**: Identifies the most profitable pizza varieties.
                """)
    
    st.markdown("Link to GitHub Repository: [Link](https://github.com/AnkitBaliyan1/SQL_projects/tree/main/Pizza_Sales_Project)")



# ********************************************************************************************************************************************************************************************************************************************************************************************************************


