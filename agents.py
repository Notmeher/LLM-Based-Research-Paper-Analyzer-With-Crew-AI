from crewai import Agent

# Agent for extracting text from the PDF
pdf_extractor_agent = Agent(
    role='PDF Extractor',
    goal='Extract text from the provided PDF file.',
    verbose=True,
    memory=True,
    tools=['pdf_extractor'],  # Tool to extract text from the PDF
    allow_delegation=False
)

# Agent for analyzing research paper sections (Methodology, Results, Discussion, Limitations)
research_paper_analyzer_agent = Agent(
    role='Research Paper Analyzer',
    goal='Analyze the provided research paper and extract methodology, results, discussion, and limitations.',
    verbose=True,
    memory=True,
    tools=[],  # Use OpenAI for analysis
    allow_delegation=False
)

# Agent for suggesting novelty or improvements
novelty_suggestion_agent = Agent(
    role='Novelty Suggestion Agent',
    goal='Based on the research paper, suggest novel ideas or improvements for future research.',
    verbose=True,
    memory=True,
    tools=[],  # Use OpenAI for suggestions
    allow_delegation=False
)

# Agent for suggesting similar research topics
topic_suggestion_agent = Agent(
    role='Topic Suggestion Agent',
    goal='Based on the research paper, suggest similar research topics and provide brief descriptions.',
    verbose=True,
    memory=True,
    tools=[],  # Use OpenAI for topic suggestions
    allow_delegation=False
)
