import streamlit as st
import pandas as pd

# Path to your CSV file (update with actual path or URL)
file_path = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSTAZfXiEdMZJXKglli57YzfLBIressqGtBfPsu2b2e0QdUxtPBimCoYn86zBnCMVElGsiS-DyXv2JZ/pub?gid=0&single=true&output=csv"

# Load student data
@st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

# Load the data into a DataFrame
df = load_data(file_path)

# Set the title and a catchy tagline
st.title("Unacademy Ludhiana Dugri")
st.markdown("<h3 style='text-align: center; color: #4CAF50;'>Unlock Your Potential with Every Lesson! 🎓</h3>", unsafe_allow_html=True)
# Add some space
st.markdown("<br>", unsafe_allow_html=True)

# Input field for the roll number
st.markdown("<h4 style='color: #ff6347;'>Enter your roll number to fetch student details:</h4>", unsafe_allow_html=True)
roll_number = st.text_input("Enter Roll Number", "")

# Add a stylish button with balloon emoji
search_button = st.button("Search 🎯", help="Click to fetch student details")

# Define a function to display a balloon animation
def balloon_animation():
    st.markdown("""
    <style>
    @keyframes balloon {
        0% {transform: scale(1);}
        50% {transform: scale(1.2);}
        100% {transform: scale(1);}
    }
    .balloon {
        animation: balloon 1s ease-in-out;
    }
    </style>
    <div class="balloon" style="font-size: 50px; color: #ff6347; text-align: center;">🎈</div>
    """, unsafe_allow_html=True)

# Check if the button is pressed and roll number is provided
if search_button:
    if roll_number:
        # Use the correct column name based on your CSV structure
        student_data = df[df['roll'] == int(roll_number)]  # 'c' is the roll number column

        # Balloon effect upon button click
        balloon_animation()

        # If a student is found, display the details
        if not student_data.empty:
            st.markdown(f"### Student Information for Roll Number {roll_number}", unsafe_allow_html=True)
            st.markdown(f"**Name**: {student_data['name'].values[0]}", unsafe_allow_html=True)
            st.markdown(f"**English Marks**: {student_data['english'].values[0]}", unsafe_allow_html=True)
            st.markdown(f"**Hindi Marks**: {student_data['hindi'].values[0]}", unsafe_allow_html=True)
            st.markdown(f"**Punjabi Marks**: {student_data['punjabi'].values[0]}", unsafe_allow_html=True)
            st.markdown(f"**Math Marks**: {student_data['math '].values[0]}", unsafe_allow_html=True)
            st.markdown(f"**Total Marks**: {student_data['total'].values[0]}", unsafe_allow_html=True)
            st.markdown(f"**Rank**: {student_data['rank '].values[0]}", unsafe_allow_html=True)

            # Add some space
            st.markdown("<br><br>", unsafe_allow_html=True)

            # Display a success message with a background color
            st.success("Student information successfully retrieved! 🎉", icon="✅")
        else:
            st.error("No student found with this roll number. Please check the roll number and try again.", icon="❌")
    else:
        st.warning("Please enter a roll number to search.", icon="⚠️")

# Add some extra spacing at the bottom
st.markdown("<br><br>", unsafe_allow_html=True)

# Footer - You can customize the footer with links or information about your project
st.markdown(
    """
    <div style='text-align: center; font-size: 14px; color: gray;'>
        <p>Made with ❤️ by Unacademy Ludhiana Dugri</p>
        <p>For more information, visit our website or contact us.</p>
    </div>
    """, unsafe_allow_html=True
)
