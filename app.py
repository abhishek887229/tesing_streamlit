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

# Display the column names for debugging purposes
st.write("Columns in the CSV file:", df.columns)

# Set the title and a catchy tagline
st.title("Unacademy Ludhiana Dugri")
st.write("### Unlock Your Potential with Every Lesson! 🎓")
st.write("Enter your roll number to fetch student details:")

# Input field for the roll number
roll_number = st.text_input("Enter Roll Number")

# Search button to retrieve student data
if st.button("Search"):
    if roll_number:
        # Use the correct column name based on your CSV structure
        student_data = df[df['roll'] == int(roll_number)]  # 'c' is the roll number column

        # If a student is found, display the details
        if not student_data.empty:
            st.write(f"### Student Information for Roll Number {roll_number}")
            st.write(f"**Name**: {student_data['name'].values[0]}")
            st.write(f"**English Marks**: {student_data['english'].values[0]}")
            st.write(f"**Hindi Marks**: {student_data['hindi'].values[0]}")
            st.write(f"**Punjabi Marks**: {student_data['punjabi'].values[0]}")
            st.write(f"**Math Marks**: {student_data['math '].values[0]}")
            st.write(f"**Total Marks**: {student_data['total'].values[0]}")
            st.write(f"**Rank**: {student_data['rank '].values[0]}")
        else:
            st.error("No student found with this roll number.")
    else:
        st.warning("Please enter a roll number.")
