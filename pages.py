import streamlit as st
from projects import *
from database import *

def about():
    st.title("About Me")
    st.markdown(""" 
    Hey, Welcome to my portfolio website.
    I'm Ankit, an Engineer, Civil Services aspirant and an enthusiast about technology.
    
    "In the pursuit of our professional goals, let us not forget to find joy in the journey, for it is within the process that we discover the true essence of our career and life's work." Let me take you through my journey !!

    🎓 My professional journey commenced with a `B.Tech` degree in Electronics from `Delhi University`, providing me with a strong foundation in data management and analysis. However, my path took an intriguing turn as I ventured into the world of `Civil Services`, cultivating a profound resilience and a holistic perspective that shaped my approach to solving-problems. Also, I have been through an intensive Business Analytics Certification from `IIM-Indore`, sharpening my skills in Statistical Modeling, Storytelling, and Machine Learning Techniques. This immersive experience fortified my understanding of the intricate interplay between data and business strategy.

    💼 I'm working with `Amazon` and has been part of multiple teams where I developed not only the data analysis and business understanding, but also got strong hold on `storeytelling` and `stakeholder management`. Working with Advertising team, my role is to generate more revenue for Amazon through advertising. I handled clients and their all advertisements running on Amazon. Yes, the job was not easy, specially, making them understand their campaign about performance.

    🚀 I am deeply passionate about translating complex data into actionable insights that fuel impactful business decisions. With a focus on GenerativeAI, machine learning, business analytics, and data visualization, I believe that every data point holds the key to unlocking crucial business narratives.

    🧠 My endavour into `Generative AI`, `Large Language Models` has been amazing. I not only developed but also deployed chatbot powered by strong language models, on `Streamlit` and `Azure` (using `Django` framework). I have multiple applications including `RAG (Reterival Augmented Generation)` for different use cases and is a display of my skills into GenAI.

    🔍 Working with `Data Science Masterminds`, I delved into the intricacies of complex survey data, honing my ability to construct robust data pipelines and extract valuable insights from intricate datasets. Each project became an engaging story, teaching me the art of unraveling hidden patterns and trends within the data fabric. My experience at Amazon has further sharpened my business acumen, allowing me to collaborate closely with business experts and communicate insights in a clear and comprehensible manner.

    🌟 I thrive on challenges and am eager to channel my analytical prowess into real-world problem-solving, contributing to the success of your organization. Beyond technical proficiency, I bring a deep sense of empathy and understanding, recognizing that every data point represents a unique human experience.

    🤝 If you are seeking a dedicated, adaptable, and empathetic data science professional, I invite you to connect with me. Together, let's embark on a journey of exploration and innovation, where data transforms into actionable insights that drive transformative change.
    """)



def workexperience():
    st.title("Work experience")
    # st.write("Here, you can find information about my projects, skills, and more.")
    col1, col2, col3 = st.columns(3)  # Create three columns


    st.markdown("<style> .separator { margin-top: 15px; border-left: 3px solid #ddd; height: 200px; } </style>", unsafe_allow_html=True)
    
    # Content for the first box
    with col1:
        st.subheader('Amazon')
        st.markdown('''
                    Position: Sr. Data Associate''')
        st.markdown('Duration: 2.5 years (Sept 2021 - Present)')
        st.markdown("""
                    Description:
                    - Sharing insight drawn from advertisement data to business stakeholders.
                    - Stakeholder Management
                    - Working on building Virtul Assistant""")
        
    

    # Content for the second box
    with col2:
        st.subheader('Data Science Masterminds')
        st.write('Position: Freelancing')
        st.write('Duration: Oct. 2023-Present')
        st.markdown("""
                    Description:
                    - End-to-End Machine Learning projects
                    - Building GenAI based Application for Resume Analysis
                    - Building Dashboard across multiple domains
                    """)

    

    # Content for the third box
    with col3:
        st.subheader('Aangan Trust')
        st.write('Position: Freelancing')
        st.write('Duration: Nov. 2023 - Jan 2024')
        st.markdown("""
                    Description:
                    - Contributed towards making "Child Protection Everybody's Business"
                    - Converted complex survey data into actionable insights 
                    - Build Dashboard on Excel
                    - Developed WebApp to convert survey checkpoints into structured and actionable views.
                    - Developed WebApp to translate Vernacular comments in survey into English
                    """)
    
def academics():
    st.markdown("---")
    col1, col2, col3= st.columns(3)
    
    with col1:
        st.markdown("""
                    ### Indian Institute of Management, Indore  \n
                    **Program:** Integrated Program in Business Analytics   \n
                    **Duration:** 2022-23\n
                    **Score:** 3.958/4.33
                    """)
    
    with col2:
        st.markdown("""
                    ### University of Delhi \n
                    **College:** Acharya Narendra Dev College \n
                    **Program:** B-Tech (Electronics) \n
                    **Duration:** 2013-17 \n
                    **Score:** 72.14%
                    """)
    with col3:
        st.markdown("""
                    ### Holy Child Academy \n
                    **Program:** Intermediate \n
                    **Duration:** 2012-13 \n
                    **Score:** 89.8%\n
                    **Subjects:** PCM
                    """)
        

def _get_buttons(projects_list):
    num_projects = len(projects_list)
    num_columns = min(num_projects, 5)  # Ensure maximum of 5 columns

    # Define custom CSS for button width
    button_style = (
        "width: 200px;"
        "height: 50px;"
        "display: flex;"
        "justify-content: center;"
        "align-items: center;"
        "background-color: #F0F0F0;"
        "border-radius: 5px;"
    )

    rows = (num_projects - 1) // 5 + 1  # Calculate the number of rows needed

    for row in range(rows):
        columns = st.columns(num_columns)  # Create columns for each row
        start_index = row * 5
        end_index = min((row + 1) * 5, num_projects)
        
        for i, col in enumerate(columns):
            if start_index + i < end_index:
                col.markdown(
                    f'<button style="{button_style}">{projects_list[start_index + i]}</button>',
                    unsafe_allow_html=True
                )
    
    st.markdown("---")


def genai():
    st.title("GenAI")
    options = ['Talk To your Document', 'Resume Screening Assistance with AI','CSV Analysis with AI','YouTube Video Script Generator',
               'Basic ChatBot powered by OpenAI and Google API']
    
    _get_buttons(options)

    # Create the dropdown list
    selected_option = st.selectbox('Select the project below 👇🏻:', options)
    
    st.markdown("---")
    if selected_option == 'Talk To your Document':
        doc_bot()
    elif selected_option == 'Resume Screening Assistance with AI':
        resume_hr()
    elif selected_option == 'CSV Analysis with AI':
        csv_bot()
    elif selected_option == 'YouTube Video Script Generator':
        bot_youtube()
    elif selected_option == 'Basic ChatBot powered by OpenAI and Google API':
        basic_chatbot()
    else:
        st.write("Not Found")
    



def machinelearning():
    st.title("Machine learning")
    options = ["California House Pricing","Company Attrition prediction","Twitter Disaster detection","Movie Sentiment Analysis",
               "BPCL Inventory Forecast","Don’t get kicked","Lead Prediciton"]
    _get_buttons(options)

    # Create the dropdown list
    selected_option = st.selectbox('Select the project below 👇🏻:', options)
    
    st.markdown("---")
    if selected_option == "California House Pricing":
        california_house_price()
    elif selected_option == "Company Attrition prediction":
        company_attrition()
    elif selected_option == "Twitter Disaster detection":
        twitter_disaster()
    elif selected_option == "Movie Sentiment Analysis":
        movie_sentiment()
    elif selected_option == "BPCL Inventory Forecast":
        bpcl_inventory()
    elif selected_option == "Don’t get kicked":
        dont_get_kicked()
    elif selected_option == "Lead Prediciton":
        lead_prediction()
    else:
        st.write("Page Not Found - Machine Learning")
    


def sql():
    st.title("SQL Projects")   
    options = ["Customer Analysis","Advertisement Analysis","Pizza Sales Analysis"]

    _get_buttons(options)
    
    selected_option = st.selectbox('Select the project below 👇🏻:', options)
    st.markdown("---")

    if selected_option == "Customer Analysis":
        customer_analysis()
    elif selected_option == "Advertisement Analysis":
        advertisement()
    elif selected_option == "Pizza Sales Analysis":
        pizza_sales()
    else:
        st.write("Page Not Found - SQL ")



def dashboard():
    st.title("Dashboard with BI-tools")

    options = ["Real Estate Property Management",
               "Managing Financial Assets",
               "Healthcare",
               "E-commerce",
               "Retail Dashboard Project"
               ]
    
    _get_buttons(options)

    selected_option = st.selectbox('Select the project below 👇🏻:', options)

    st.markdown("---")
    if selected_option == "Real Estate Property Management":
        dashboard_real_estate()
    elif selected_option == "Managing Financial Assets":
        dashboard_finance()
        # st.subheader("Managing Financial Assets")
    elif selected_option == "Healthcare":
        dashboard_healthcare()
        # st.subheader("Healthcare")
    elif selected_option == "E-commerce":
        dashboard_e_commerce()
    elif selected_option == "Retail Dashboard Project":
        dashboard_retail()
    else:
        st.write("Page Not Found - Dashboard")

def contactme():
    st.title("Contact Me")

    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Name:*")
        phone = st.text_input("Mobile Number:*")
        email = st.text_input("Email:")
        query = st.text_area("Reason for Contact:*")

        # Submit button
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            if not name:
                st.error("Name is required field")
            elif not phone:
                st.error("Mobile number is required field")
            elif not query:
                st.error("You must enter the reason for contact.")
            elif not phone.isdigit() or len(phone) != 10:
                st.error("Please provide a valid Mobile Number.")
                st.error("Hint: It should be all numeric and atleast 10 numbers")
            else:
                st.success("Thanks for reaching out! I'll get back to you as soon as possible.")
                udpate_database(name, phone, email, query)
                
                
