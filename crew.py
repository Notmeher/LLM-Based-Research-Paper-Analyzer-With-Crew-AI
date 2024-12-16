import openai
from dotenv import load_dotenv
import os
from tasks import pdf_extraction_task, research_analysis_task, novelty_idea_task, similar_topic_suggestion_task
import pandas as pd

# Load environment variables and set OpenAI API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def crew_workflow(pdf_file_path):
    # Step 1: Extract text from the PDF
    extraction_result = pdf_extraction_task({"pdf_file_path": pdf_file_path})
    if "error" in extraction_result:
        return {"error": extraction_result["error"]}
    body_text = extraction_result["text"]

    # Step 2: Analyze research paper content (Methodology, Results, Discussion, Limitations)
    analysis_result = research_analysis_task({"body_text": body_text})
    if "error" in analysis_result:
        return {"error": analysis_result["error"]}

    methodology = analysis_result["methodology"]
    results = analysis_result["results"]
    discussion = analysis_result["discussion"]
    limitations = analysis_result["limitations"]

    # Step 3: Suggest Novel Ideas for Future Research
    novelty_suggestions = novelty_idea_task({"body_text": body_text})
    if "error" in novelty_suggestions:
        return {"error": novelty_suggestions["error"]}

    # Step 4: Suggest Similar Topics for Research
    topic_suggestions = similar_topic_suggestion_task({"body_text": body_text})
    if "error" in topic_suggestions:
        return {"error": topic_suggestions["error"]}

    return {
        "methodology": methodology,
        "results": results,
        "discussion": discussion,
        "limitations": limitations,
        "novelty_suggestions": novelty_suggestions["suggestions"],
        "similar_topic_suggestions": topic_suggestions["topics"]
    }
