import openai
from dotenv import load_dotenv
import os
from tools import extract_text_from_pdf

# Load environment variables and set OpenAI API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Task to extract text from PDF
def pdf_extraction_task(inputs):
    pdf_file_path = inputs.get("pdf_file_path")
    if not pdf_file_path:
        return {"error": "No PDF file path provided."}
    
    try:
        # Extract text from the provided PDF file
        text = extract_text_from_pdf(pdf_file_path)
        if not text:
            return {"error": "Failed to extract text from the PDF."}
        return {"text": text}
    except Exception as e:
        return {"error": f"An error occurred during PDF extraction: {str(e)}"}

# Task to analyze the sections (Methodology, Results, Discussion, Limitations)
def research_analysis_task(inputs):
    body_text = inputs.get("body_text")
    if not body_text:
        return {"error": "No body text provided for analysis."}
    
    try:
        # Extract Methodology
        methodology_prompt = (
            f"Identify and summarize the methodology section in the following text:\n\n{body_text}"
        )
        methodology_response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": methodology_prompt}],
            temperature=0.7
        )
        methodology = methodology_response["choices"][0]["message"]["content"].strip()

        # Extract Results
        results_prompt = (
            f"Identify and summarize the results section in the following text:\n\n{body_text}"
        )
        results_response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": results_prompt}],
            temperature=0.7
        )
        results = results_response["choices"][0]["message"]["content"].strip()

        # Extract Discussion
        discussion_prompt = (
            f"Identify and summarize the discussion section in the following text:\n\n{body_text}"
        )
        discussion_response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": discussion_prompt}],
            temperature=0.7
        )
        discussion = discussion_response["choices"][0]["message"]["content"].strip()

        # Extract Limitations
        limitations_prompt = (
            f"Identify and summarize the limitations section in the following text:\n\n{body_text}"
        )
        limitations_response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": limitations_prompt}],
            temperature=0.7
        )
        limitations = limitations_response["choices"][0]["message"]["content"].strip()

        return {
            "methodology": methodology,
            "results": results,
            "discussion": discussion,
            "limitations": limitations
        }
    except Exception as e:
        return {"error": f"An error occurred during research paper analysis: {str(e)}"}

# Task to suggest novelty or improvements
def novelty_idea_task(inputs):
    body_text = inputs.get("body_text")
    if not body_text:
        return {"error": "No body text provided for novelty suggestions."}
    
    try:
        novelty_prompt = (
            f"Based on the following research paper text, suggest novel research ideas or improvements for the methodology or outcomes:\n\n{body_text}"
        )
        novelty_response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": novelty_prompt}],
            temperature=0.7
        )
        suggestions = novelty_response["choices"][0]["message"]["content"].strip()

        return {"suggestions": suggestions}
    except Exception as e:
        return {"error": f"An error occurred during novelty suggestion: {str(e)}"}

# Task to suggest similar research topics
def similar_topic_suggestion_task(inputs):
    body_text = inputs.get("body_text")
    if not body_text:
        return {"error": "No body text provided for topic suggestions."}
    
    try:
        topics_prompt = (
            f"Based on the following research paper text, suggest 5 similar research topics that I could explore, along with a brief description of each topic:\n\n{body_text}"
        )
        topics_response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": topics_prompt}],
            temperature=0.7
        )
        topics = topics_response["choices"][0]["message"]["content"].strip()

        return {"topics": topics}
    except Exception as e:
        return {"error": f"An error occurred during topic suggestion: {str(e)}"}
