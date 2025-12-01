# agent.py - STABLE VERSION USING STANDARD ADK PATTERNS

import os
import vertexai

# Use the imports exactly as shown in the Day 2 notebook
from google.adk.agents import LlmAgent
from google.adk.models.google_llm import Gemini
from google.adk.tools.function_tool import FunctionTool

# --- Vertex AI Initialization ---
vertexai.init(
    project=os.environ.get("GOOGLE_CLOUD_PROJECT", ""),
    location=os.environ.get("GOOGLE_CLOUD_LOCATION", ""),
)

# --- Define the Tools as Standard Python Functions ---

def analyze_idea(idea: str) -> dict:
    """
    Analyzes a business idea using the Business Model Canvas.
    Returns a dictionary with the 9 canvas components.
    """
    print(f" -> [Tool] Analyzing idea: {idea}")
    # In a real scenario, this might call another API. 
    # Here we return a structured prompt for the LLM to process.
    return {
        "action": "analyze_business_model_canvas",
        "context": f"Perform a detailed Business Model Canvas analysis for: {idea}"
    }

def create_strategy(idea: str) -> dict:
    """
    Creates a SWOT analysis and marketing strategy.
    """
    print(f" -> [Tool] Creating strategy for: {idea}")
    return {
        "action": "create_swot_and_marketing",
        "context": f"Create a SWOT analysis and marketing strategy for: {idea}"
    }

def generate_forecast(idea: str) -> dict:
    """
    Generates a preliminary financial forecast.
    """
    print(f" -> [Tool] Generating forecast for: {idea}")
    return {
        "action": "generate_financial_forecast",
        "context": f"Create a 3-year financial forecast (startup costs, revenue, break-even) for: {idea}"
    }

# --- Create the Agent ---

# We use the standard LlmAgent class.
# We configure it with the model and the list of tools.
root_agent = LlmAgent(
    name="ideaspark_agent",
    # We use the Gemini class from ADK to wrap the model
    model=Gemini(model="gemini-1.5-pro-preview-0409"), 
    # Instructions for the agent on how to use the tools
    instruction="""
    You are IdeaSpark, an expert AI Business Strategist.
    
    Your goal is to take a user's business idea and generate a comprehensive business plan.
    
    You have access to three specific tools:
    1. analyze_idea: Use this to break down the idea into a Business Model Canvas.
    2. create_strategy: Use this to perform SWOT analysis and marketing planning.
    3. generate_forecast: Use this to create financial projections.
    
    When a user provides an idea:
    1. Call ALL three tools to gather the necessary analysis.
    2. Once you have the results from the tools, synthesize them into a single, beautifully formatted Markdown report.
    3. The report should have clear headings for "Business Model", "Strategy", and "Financials".
    """,
    # Wrap our functions in FunctionTool
    tools=[
        FunctionTool(analyze_idea),
        FunctionTool(create_strategy),
        FunctionTool(generate_forecast)
    ]
)