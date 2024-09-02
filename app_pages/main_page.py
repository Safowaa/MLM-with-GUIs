import streamlit as st

def main_page():
    # Set the logo and title
    col1, col2 = st.columns([1, 10])  # Adjust the width ratio to balance logo and title
    with col1:
        st.image("logo/Logo.png", width=100)
        
    with col2:
        st.markdown("<h1 style='font-size: 58px;'>Japan Machine Training Ltd</h1>", unsafe_allow_html=True)


    st.write(""" 
        ### Japan Machine Training Ltd is an IT company that trains all types of machine learning models on different and diverse data for general and specific areas. At Japan Machine Training Ltd, we build and train! There is no impossible insight.
    """)

    st.image("team_pictures/Teampic1.jpg", width=1500)

    st.write("""
        ### We are a team of Data analysts trained in the data world. Each individual on this team has honed their skills to be able to serve you. With diverse backgrounds, we bring you insights from all corners of the world.
    """)

    st.write("### Meet the Team")
    # Create two columns for the Team
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
            ### Asumaning Safowaa Benedicta
            Graduate in Information and Communication Technology, with data analysis from Azubi Africa and Japan team lead. Her zeal, passion, attention to detail, and love for data-driven insights have propelled this company to greater heights.
        """)
        st.image('team_pictures/Safowaa1.png', width=700)
    
    with col2:
        st.markdown(""" 
            ### Josephine Asante 
            Graduate Physician Assistant, with data analysis skills from Azubi Africa. She joined Team Japan earlier this year. Her zeal, passion, attention to detail, and love for data-driven insights have propelled this company to greater heights.
        """)
        st.image('team_pictures/Josephine1.png', width=700)

    st.write("### Connect with us!")

    st.markdown("""
    <div style="display: flex; justify-content: space-evenly;">
        <a href="https://github.com/Safowaa" target="_blank">
            <button style="background-color:#D8C04E; color:black; border:none; padding:10px 90px; text-align:center; font-size:18px; margin:2px; cursor:pointer; border-radius:5px;">
            GitHub
            </button>
        </a>
        <a href="www.linkedin.com/in/benedicta-safowaa-asumaning/" target="_blank">
            <button style="background-color:#D8C04E; color:black; border:none; padding:10px 90px; text-align:center; font-size:18px; margin:2px; cursor:pointer; border-radius:5px;">
            LinkedIn
            </button>
        </a>
        <a href="https://app.powerbi.com/groups/me/reports/a814a603-ddbe-4f36-8c6e-674ecd59f05b/ReportSection?experience=power-bi" target="_blank">
            <button style="background-color:#D8C04E; color:black; border:none; padding:10px 90px; text-align:center; font-size:18px; margin:2px; cursor:pointer; border-radius:5px;">
            PowerBI
            </button>
        </a>
        <a href="https://medium.com/@safowaabenedicta/telco-customer-attrition-analysis-faae3476c6fb" target="_blank">
            <button style="background-color:#D8C04E; color:black; border:none; padding:10px 90px; text-align:center; font-size:18px; margin:2px; cursor:pointer; border-radius:5px;">
            Medium
            </button>
        </a>
    </div>
    """, unsafe_allow_html=True)

    st.write("---")
    # Add copyright notice
    st.write("© 2024 Japan Machine Training Ltd. All Rights Reserved.")

# Run the main page function
if __name__ == "__main__":
    main_page()
