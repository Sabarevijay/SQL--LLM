# from dotenv import load_dotenv
# load_dotenv() ## load all the environemnt variables

# import streamlit as st
# import os
# import sqlite3

# import google.generativeai as genai
# ## Configure Genai Key

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ## Function To Load Google Gemini Model and provide queries as response

# def get_gemini_response(question,prompt):
#     model=genai.GenerativeModel('gemini-pro')
#     response=model.generate_content([prompt[0],question])
#     return response.text

# ## Fucntion To retrieve query from the database

# def read_sql_query(sql,db):
#     conn=sqlite3.connect(db)
#     cur=conn.cursor()
#     cur.execute(sql)
#     rows=cur.fetchall()
#     conn.commit()
#     conn.close()
#     for row in rows:
#         print(row)
#     return rows

# ## Define Your Prompt
# prompt=[
#     """
#     You are an expert in converting English questions to SQL query!
#     The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
#     SECTION and MARKS  \n\nFor example,\nExample 1 - How many entries of records are present?, 
#     the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
#     \nExample 2 - Tell me all the students studying in Data Science class?, 
#     the SQL command will be something like this SELECT * FROM STUDENT 
#     where CLASS="Data Science"; 
#     also the sql code should not have ``` in beginning or end and sql word in output

#     """


# ]

# ## Streamlit App

# st.set_page_config(page_title="I can Retrieve Any SQL query")
# st.header("BIT Chatbot ")

# question=st.text_input("Ask any question ",key="input")

# submit=st.button("Submit")

# # if submit is clicked
# if submit:
#     response=get_gemini_response(question,prompt)
#     print(response)
#     response=read_sql_query(response,"student.db")
#     st.subheader("The Response is")
#     for row in response:
#         print(row)
#         st.header(row)


from dotenv import load_dotenv
load_dotenv()  # Load all environment variables

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

# Configure GenAI Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function To Load Google Gemini Model and provide queries as response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0], question])
    return response.text

# Function To Retrieve Query Results from the Database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    
    # Convert query results into a natural language response
    if rows:
        student_names = set(row[0] for row in rows)  
        formatted_response = "### The students found are:\n" + "\n".join(f"- {name}" for name in student_names)    
    else:
        formatted_response = "No matching records found in the database."
    
    return formatted_response
  

# Define Your Prompt with Correct Column Names
prompt = [
    """
    You are an expert in converting English questions into SQL queries!
    The SQL database has the name `student.db` and contains a table called `my_table`.
    
    The table `my_table` has the following columns:
    - `id` (INTEGER, Primary Key, Auto-increment)
    - `Reg_no` (INTEGER)
    - `Student_name` (TEXT)
    - `Dept` (TEXT)
    - `Course_code` (TEXT)
    - `Course_Title` (TEXT)
    - `Exam_name` (TEXT)
    - `Semester` (TEXT)
    - `Total_Mark` (TEXT)
    - `email_id` (TEXT)

    **Example Queries:**
    - How many students are in the database?
      **SQL Query:** SELECT COUNT(*) FROM my_table;

    - Show me all students from the CSE department.
      **SQL Query:** SELECT Student_name FROM my_table WHERE Dept="CSE";

    - List all students along with their course titles.
      **SQL Query:** SELECT Student_name, Course_Title FROM my_table;

    - Find the email of a student with Reg_no 7376232AD157.
      **SQL Query:** SELECT email_id FROM my_table WHERE Reg_no="7376232AD157";

    **Important:**
    - The SQL query **must not include** "```" at the beginning or end.
    - The SQL query **must not** include the word "SQL" in the output.
    """
]

# Streamlit App
st.set_page_config(page_title="BIT Chatbot - SQL Query Retrieval")
st.header("BIT Chatbot")

question = st.text_input("Ask any question", key="input")

submit = st.button("Submit")

# If submit is clicked
if submit:
    response = get_gemini_response(question, prompt)
    natural_response = read_sql_query(response, "student.db")
    
    st.subheader("The Response is:")
    st.write(natural_response)  # Display a readable output












