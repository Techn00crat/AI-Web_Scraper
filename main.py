# import streamlit as st
# from scrape import (
#     scrape_website, 
#     extract_body_content, 
#     split_dom_content, 
#     clean_body_content
# )
# from parse import parse_with_ollama

# st.title("AI Web Scraper")
# url = st.text_input("Enter a Website URL: ")

# if st.button("Scrape Site"):
#     st.write("Scraping the Website...")

#     result = scrape_website(url)
#     body_content = extract_body_content(result)
#     cleaned_content = clean_body_content(body_content)

#     st.session_state.dom_content = cleaned_content

#     with st.expander("View DOM Content"):
#         st.text_area("DOM Content", cleaned_content, height=300)
        

# if "dom_content" in st.session_state:
#     parse_description = st.text_area("Describe what you want?")

#     if st.button("Parse Content"):
#         if parse_description:
#             st.write("Parsing the Content...")

#             dom_chunks = split_dom_content(st.session_state.dom_content)
#             result = parse_with_ollama(dom_chunks, parse_description)
#             st.write(result)
















# import streamlit as st
# from scrape import (
#     scrape_website, 
#     extract_body_content, 
#     split_dom_content, 
#     clean_body_content
# )
# from parse import parse_with_ollama

# st.title("AI Web Scraper")
# url = st.text_input("Enter a Website URL:")

# if st.button("Scrape Site"):
#     st.write("Scraping the Website...")

#     result = scrape_website(url)
#     body_content = extract_body_content(result)
#     cleaned_content = clean_body_content(body_content)

#     st.session_state.dom_content = cleaned_content

#     with st.expander("View DOM Content"):
#         st.text_area("DOM Content", cleaned_content, height=300)

# # Initialize session state for the description and feedback
# if "parse_description" not in st.session_state:
#     st.session_state.parse_description = ""

# if "is_satisfied" not in st.session_state:
#     st.session_state.is_satisfied = None  # None means no feedback yet

# # Show description input if no feedback is given yet or if the user clicked "No"
# if st.session_state.is_satisfied is None or not st.session_state.is_satisfied:
#     st.session_state.parse_description = st.text_area(
#         "Describe what you want to extract from the website:", 
#         value=st.session_state.parse_description
#     )

#     if st.button("Parse Content"):
#         if st.session_state.parse_description:
#             st.write("Parsing the Content")
            
#             # Split content into chunks for processing
#             dom_chunks = split_dom_content(st.session_state.dom_content)
#             result = parse_with_ollama(dom_chunks, st.session_state.parse_description)
            
#             # Show results
#             st.write("Parsed Results:")
#             st.write(result)

#             # Ask for user feedback
#             st.session_state.is_satisfied = None  # Reset satisfaction before feedback
#             col1, col2 = st.columns(2)
#             with col1:
#                 if st.button("Yes"):
#                     st.session_state.is_satisfied = True
#                     st.write("Thank you for your feedback!")
#             with col2:
#                 if st.button("No"):
#                     st.session_state.is_satisfied = False
#                     st.write("Please provide a new description below.")
# else:
#     # If satisfied, display a message
#     if st.session_state.is_satisfied:
#         st.write("You are satisfied with the results! Thank you!")
#     # If not satisfied, the prompt input is enabled again
#     elif not st.session_state.is_satisfied:
#         st.session_state.parse_description = st.text_area(
#             "Describe what you want to extract from the website (New Description):", 
#             value=st.session_state.parse_description
#         )

#         if st.button("Parse Content Again"):
#             if st.session_state.parse_description:
#                 st.write("Parsing the Content...")
                
#                 # Split content into chunks for processing
#                 dom_chunks = split_dom_content(st.session_state.dom_content)
#                 result = parse_with_ollama(dom_chunks, st.session_state.parse_description)
                
#                 # Show new results
#                 st.write("Parsed Results:")
#                 st.write(result)

#                 # Ask for user feedback again
#                 col1, col2 = st.columns(2)
#                 with col1:
#                     if st.button("Yes"):
#                         st.session_state.is_satisfied = True
#                         st.write("Thank you for your feedback!")
#                 with col2:
#                     if st.button("No"):
#                         st.session_state.is_satisfied = False
#                         st.write("Please provide a new description below.")




# if "dom_content" in st.session_state:
#     parse_description = st.text_area("Describe what you want?")

#     if st.button("Parse Content"):
#         if parse_description:
#             st.write("Parsing the Content")

#             dom_chunks = split_dom_content(st.session_state.dom_content)
#             result = parse_with_ollama(dom_chunks, parse_description)
#             st.write(result)

# import streamlit as st
# from scrape import (
#     scrape_website, 
#     extract_body_content, 
#     split_dom_content, 
#     clean_body_content
# )
# from parse import parse_with_ollama

# st.title("AI Web Scraper")
# url = st.text_input("Enter a Website URL:")

# if st.button("Scrape Site"):
#     st.write("Scraping the Website...")
#     result = scrape_website(url)
#     body_content = extract_body_content(result)
#     cleaned_content = clean_body_content(body_content)
#     st.session_state.dom_content = cleaned_content

#     with st.expander("View DOM Content"):
#         st.text_area("DOM Content", cleaned_content, height=300)

# # Initialize session state for the description and feedback
# if "parse_description" not in st.session_state:
#     st.session_state.parse_description = ""

# if "is_satisfied" not in st.session_state:
#     st.session_state.is_satisfied = None  # None means no feedback yet

# # Show description input if no feedback is given yet or if the user clicked "No"
# if st.session_state.is_satisfied is None or not st.session_state.is_satisfied:
#     st.session_state.parse_description = st.text_area(
#         "Describe what you want to extract from the website:", 
#         value=st.session_state.parse_description
#     )

#     if st.button("Parse Content"):
#         if st.session_state.parse_description:
#             st.write("Parsing the Content...")
            
#             # Split content into chunks for processing
#             dom_chunks = split_dom_content(st.session_state.dom_content)
#             result = parse_with_ollama(dom_chunks, st.session_state.parse_description)
            
#             # Show results
#             st.write("Parsed Results:")
#             st.write(result)

#             # Feedback box
#             with st.container():
#                 st.markdown(
#                     """
#                     <div style="padding: 5px; border: 1px solid #d6d6d6; border-radius: 10px;">
#                         <h4 style="text-align: center;">Are you satisfied with the results?</h4>
#                     </div>
#                     """,
#                     unsafe_allow_html=True
#                 )
#                 col1, col2 = st.columns(2)
#                 with col1:
#                     if st.button("Yes"):
#                         st.session_state.is_satisfied = True
#                         st.success("Thank you for your feedback!")
#                 with col2:
#                     if st.button("No"):
#                         st.session_state.is_satisfied = False
#                         st.warning("Please provide a new description below.")

# # If satisfied, display a message
# if st.session_state.is_satisfied:
#     st.write("You are satisfied with the results! Thank you!")
# elif st.session_state.is_satisfied is False:
#     # If not satisfied, prompt for a new description
#     st.session_state.parse_description = st.text_area(
#         "Describe what you want to extract from the website (New Description):", 
#         value=st.session_state.parse_description
#     )

#     if st.button("Parse Content Again"):
#         if st.session_state.parse_description:
#             st.write("Parsing the Content...")
#             dom_chunks = split_dom_content(st.session_state.dom_content)
#             result = parse_with_ollama(dom_chunks, st.session_state.parse_description)
#             st.write("Parsed Results:")
#             st.write(result)

#             # Feedback box again
#             with st.container():
#                 st.markdown(
#                     """
#                     <div style="padding: 20px; border: 1px solid #d6d6d6; border-radius: 10px; background-color: #f9f9f9;">
#                         <h4 style="text-align: center;">Are you satisfied with the results?</h4>
#                     </div>
#                     """,
#                     unsafe_allow_html=True
#                 )
#                 col1, col2 = st.columns(2)
#                 with col1:
#                     if st.button("Yes"):
#                         st.session_state.is_satisfied = True
#                         st.success("Thank you for your feedback!")
#                 with col2:
#                     if st.button("No"):
#                         st.session_state.is_satisfied = False
#                         st.warning("Please provide a new description below.")


import streamlit as st
from scrape import (
    scrape_website, 
    extract_body_content, 
    split_dom_content, 
    clean_body_content
)
from parse import parse_with_ollama
import pandas as pd
import json

st.title("AI Web Scraper")
url = st.text_input("Enter a Website URL:")

# Button states need to be managed in session state
if "is_scraped" not in st.session_state:
    st.session_state.is_scraped = False

if "is_parsed" not in st.session_state:
    st.session_state.is_parsed = False

if "is_satisfied" not in st.session_state:
    st.session_state.is_satisfied = None  # None means no feedback yet

if "parsed_result" not in st.session_state:
    st.session_state.parsed_result = ""

if st.button("Scrape Site"):
    st.session_state.is_scraped = True
    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)
    st.session_state.dom_content = cleaned_content

if st.session_state.is_scraped:
    st.expander("View DOM Content").text_area("DOM Content", st.session_state.dom_content, height=300)

    st.session_state.parse_description = st.text_area(
        "Describe what you want to extract from the website:", 
        value=st.session_state.get("parse_description", "")
    )

    if st.button("Parse Content"):
        st.session_state.is_parsed = True
        dom_chunks = split_dom_content(st.session_state.dom_content)
        parsed_result = parse_with_ollama(dom_chunks, st.session_state.parse_description)
        st.session_state.parsed_result = parsed_result

if st.session_state.is_parsed:
    st.write("Parsed Results:")
    st.write(st.session_state.parsed_result)

    with st.container():
        st.markdown(
            """
            <div style="padding: 5px; border: 1px solid #d6d6d6; border-radius: 10px;">
                <h4 style="text-align: center;">Are you satisfied with the results?</h4>
            </div>
            """,
            unsafe_allow_html=True
        )
        col1, col2 = st.columns(2)
        if col1.button("Yes"):
            st.session_state.is_satisfied = True
        if col2.button("No"):
            st.session_state.is_satisfied = False

if st.session_state.is_satisfied is True:
    st.write("Thank you for your feedback! You can now download the results.")

    # File format selection
    file_format = st.radio("Select the file format to download:", options=["JSON", "CSV"])

    def parse_markdown_table(md_table):
        rows = [row.strip("|").split("|") for row in md_table.strip().split("\n") if row.startswith("|")]
        headers = [header.strip() for header in rows[0]]
        data = [{headers[i]: cell.strip() for i, cell in enumerate(row)} for row in rows[1:]]
        return data

    try:
        structured_data = parse_markdown_table(st.session_state.parsed_result)
    except Exception:
        structured_data = [{"Parsed Result": st.session_state.parsed_result}]

    if isinstance(structured_data, list) and all(isinstance(item, dict) for item in structured_data):
        df = pd.DataFrame(structured_data)
    else:
        df = pd.DataFrame([{"Parsed Result": structured_data}])

    if file_format == "JSON":
        file_data = json.dumps(structured_data, indent=4)
        st.download_button(
            label="Download JSON File",
            data=file_data,
            file_name="parsed_result.json",
            mime="application/json",
        )
    elif file_format == "CSV":
        csv_data = df.to_csv(index=False)
        st.download_button(
            label="Download CSV File",
            data=csv_data,
            file_name="parsed_result.csv",
            mime="text/csv",
        )

elif st.session_state.is_satisfied is False:
    st.warning("Please provide a new description to improve the parsing results.")
