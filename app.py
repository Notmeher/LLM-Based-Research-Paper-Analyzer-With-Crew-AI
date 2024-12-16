import streamlit as st
from crew import crew_workflow
import pandas as pd

st.title("LLM Based Research Paper Analyzer With Crew AI")

# Upload the research paper (PDF)
pdf_file = st.file_uploader("Upload a research paper (PDF):", type=["pdf"])

if st.button("Analyze Research Paper"):
    if pdf_file:
        # Save the uploaded PDF file to a temporary location
        with open("uploaded_research_paper.pdf", "wb") as f:
            f.write(pdf_file.read())
        
        # Call the crew_workflow to process the uploaded PDF
        result = crew_workflow("uploaded_research_paper.pdf")
        
        # Handle errors from the workflow
        if "error" in result:
            st.error(result["error"])
        else:
            # Display Methodology
            st.subheader("Methodology")
            st.write(result["methodology"])

            # Display Results
            st.subheader("Results")
            st.write(result["results"])

            # Display Discussion
            st.subheader("Discussion")
            st.write(result["discussion"])

            # Display Limitations
            st.subheader("Limitations")
            st.write(result["limitations"])

            # Display Novelty Suggestions
            st.subheader("Novelty Suggestions")
            st.write(result["novelty_suggestions"])

            # Display Similar Research Topics
            st.subheader("Similar Research Topics")
            st.write(result["similar_topic_suggestions"])
    else:
        st.error("Please upload a PDF file.")
