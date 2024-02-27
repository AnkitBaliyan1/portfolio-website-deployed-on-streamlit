import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
from pages import *

def page_configuration():
    """
    This function is to confifure tha page static like 
    style, title, etc.
    """
    st.set_page_config(
        page_title="Ankit's Portfolio",
        # page_icon=":smiley:",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)



def configure_sidebar():
    image = Image.open('static/myphoto-wo-bg.png')

    local_css("static/style.css")

    st.sidebar.image(image, use_column_width=True)
    st.sidebar.subheader("Contact:")
    st.sidebar.markdown("Phone: +91-9958631596")
    st.sidebar.markdown("Email: [a.baliyan008@gmail.com](mailto:a.baliyan008@gmail.com)")
    st.sidebar.markdown('[LinkedIn](https://www.linkedin.com/in/ankitbaliyan1/)  \n [GitHub](https://github.com/AnkitBaliyan1)')
    st.sidebar.markdown("""
                        ##### Tools Known: 
                        - Python
                        - SQL
                        - R-Programming
                        - Tableau
                        - PowerBI
                        - Figma
                        - Streamlit
                        - Django
                        - Azure
                        - Virtual Machine

                        """)
    


def main_page():
    selected_page = option_menu(
        menu_title=None,
        options = ["About Me", "Academics", "Work Experiences", "GenAI projects", "Machine Learning",
                   "Dashboard", "SQL Projects", "More", "Contact Me"],
        icons=None,
        default_index=0,
        orientation="horizontal",
    )

    if selected_page == "About Me":
        about()
    elif selected_page == "Academics":
        academics()
    elif selected_page == "Work Experiences":
        workexperience()
    elif selected_page == "GenAI projects":
        genai()
    elif selected_page == "Machine Learning":
        machinelearning()
    elif selected_page == "Dashboard":
        dashboard()
    elif selected_page == "SQL Projects":
        sql()
    elif selected_page == "Contact Me":
        contactme()
    else:
        st.markdown("""
                    ## Work in progress:

                    Thank you for visiting my portfolio! I'm currently in the process of adding more content and sections to provide you with a comprehensive view of my work and achievements. Please bear with me as I continue to update and improve the site. In the meantime, feel free to explore the existing sections and projects. Your patience and understanding are greatly appreciated.

                    If you have any questions or would like to get in touch, don't hesitate to reach out. Thank you for your interest and support!
                    """)

def main():

    # configure page details
    page_configuration()
    

    # configure side bar
    configure_sidebar()


    # configure main page
    main_page()
    # st.write("main_page")



if __name__ == "__main__":
    main()