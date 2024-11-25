
# Optional: You can also add any custom styling or other Streamlit widgets to further enhance the interface.
import streamlit as st
import pandas as pd

# Load student data (update with your file path or URL)
file_path = "https://docs.google.com/spreadsheets/d/e/2PACX-1vSTAZfXiEdMZJXKglli57YzfLBIressqGtBfPsu2b2e0QdUxtPBimCoYn86zBnCMVElGsiS-DyXv2JZ/pub?gid=0&single=true&output=csv"  # Update this with your CSV file path or URL

# Read the CSV into a pandas DataFrame
@st.cache_data
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

# Load the data into a DataFrame
df = load_data(file_path)

# Set the title and a catchy tagline
st.title("Unacademy Ludhiana Dugri")
st.write("### Unlock Your Potential with Every Lesson! 🎓")
st.write("Enter your roll number to fetch student details:")

# Input field for the roll number
roll_number = st.text_input("Enter Roll Number")

# Search button to retrieve student data
if st.button("Search"):
    if roll_number:
        # Filter the data for the entered roll number
        student_data = df[df['roll'] == int(roll_number)]
        st.write(df.head())
        # If a student is found, display the details
        if not student_data.empty:
            st.write(f"### Student Information for Roll Number {roll_number}")
            st.write(f"**Name**: {student_data['Name'].values[0]}")
            st.write(f"**Marks in Subject 1**: {student_data['Subject 1'].values[0]}")
            st.write(f"**Marks in Subject 2**: {student_data['Subject 2'].values[0]}")
            st.write(f"**Marks in Subject 3**: {student_data['Subject 3'].values[0]}")
            st.write(f"**Marks in Subject 4**: {student_data['Subject 4'].values[0]}")
            st.write(f"**Marks in Subject 5**: {student_data['Subject 5'].values[0]}")
            st.write(f"**Rank**: {student_data['Rank'].values[0]}")
        else:
            st.error("No student found with this roll number.")
    else:
        st.warning("Please enter a roll number.")
