# IdeaSpark: AI Business Strategist Agent

## The Problem
Entrepreneurs struggle to structure their ideas into viable business plans. The process is complex and time-consuming.

## The Solution
IdeaSpark is an AI Agent built with the Google Agent Development Kit (ADK). It acts as a specialized business consultant.

## Architecture
It uses a root `LlmAgent` powered by Gemini 1.5 Pro. It has access to three specific function tools:
1.  `analyze_idea`: Decomposes ideas using the Business Model Canvas.
2.  `create_strategy`: Generates SWOT analysis and marketing plans.
3.  `generate_forecast`: Calculates financial projections.

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run the agent using the ADK runtime.
