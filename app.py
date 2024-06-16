import streamlit as st
from crewai import Agent, Task, Crew
from langchain_groq import ChatGroq
from crewai_tools import SerperDevTool, tool
import os
from dotenv import load_dotenv
import pandas as pd
from IPython.display import Markdown

# Load environment variables
load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")

# Initialize LLM and Search Tool
llm = ChatGroq(temperature=0, model_name="llama3-70b-8192", api_key=GROQ_API_KEY)
search_tool = SerperDevTool(api_key=SERPER_API_KEY)


def create_agent(role, goal, backstory):
    return Agent(
        llm=llm,
        role=role,
        goal=goal,
        backstory=backstory,
        allow_delegation=False,
        verbose=True,
    )


planner = create_agent(
    role="Content Planner",
    goal="Plan engaging and factually accurate content on {topic}",
    backstory="You are planning a blog article about {topic}. You collect information that helps the audience learn and make informed decisions. Your work serves as a foundation for the Content Writer.",
)

writer = create_agent(
    role="Content Writer",
    goal="Write an insightful and factually accurate opinion piece on {topic}",
    backstory="You are writing an opinion piece on {topic}, based on the planner's outline. You provide objective insights and acknowledge opinions.",
)

editor = create_agent(
    role="Editor",
    goal="Edit the blog post to align with the organization's writing style.",
    backstory="You review the blog post from the writer, ensuring it follows best practices, provides balanced viewpoints, and avoids major controversial topics.",
)


def create_task(description, expected_output, agent):
    return Task(description=description, expected_output=expected_output, agent=agent)


plan = create_task(
    description=(
        "1. Prioritize the latest trends, key players, and news on {topic}.\n"
        "2. Identify the target audience, their interests, and pain points.\n"
        "3. Develop a detailed content outline with an introduction, key points, and a call to action.\n"
        "4. Include SEO keywords and relevant data or sources."
    ),
    expected_output="A comprehensive content plan with an outline, audience analysis, SEO keywords, and resources.",
    agent=planner,
)

write = create_task(
    description=(
        "1. Use the content plan to craft a compelling blog post on {topic}.\n"
        "2. Incorporate SEO keywords naturally.\n"
        "3. Name sections/subtitles engagingly.\n"
        "4. Structure the post with an engaging introduction, insightful body, and summarizing conclusion.\n"
        "5. Proofread for grammatical errors and brand voice alignment."
    ),
    expected_output="A well-written blog post in markdown format, ready for publication, with each section having 2-3 paragraphs.",
    agent=writer,
)

edit = create_task(
    description="Proofread the given blog post for grammatical errors and brand voice alignment.",
    expected_output="A well-written blog post in markdown format, ready for publication, with each section having 2-3 paragraphs.",
    agent=editor,
)

crew = Crew(agents=[planner, writer, editor], tasks=[plan, write, edit], verbose=2)


def main():
    st.title("AI Content Creation Workflow")

    topic = st.text_input(
        "Enter the topic for content creation", "Artificial Intelligence"
    )

    if st.button("Start Workflow"):
        with st.spinner("Running the content creation workflow..."):
            result = crew.kickoff(inputs={"topic": topic})
        st.write(result)
        st.success("Workflow completed!")


if __name__ == "__main__":
    main()
