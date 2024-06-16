# Groq-Llama Content Studio Workflow

Welcome to the AI Content Creation Workflow repository, where multiple intelligent agents collaborate to revolutionize content creation. Leveraging the cutting-edge capabilities of Meta's Llama 3 model and Groq's lightning-fast inference engine, this tutorial is designed for developers, bloggers, marketers, and AI enthusiasts who want to integrate advanced AI into their content production workflows.

I am Sanchay Thalnerkar, a data scientist, writer, and content creator. My experience spans various aspects of AI and content creation, and I am excited to share this comprehensive workflow with you. For a more in-depth understanding, you can read my detailed tutorial on lablab: [Mastering AI Content Creation: Leveraging Llama 3 and Groq API](https://lablab.ai/t/mastering-ai-content-creation-leveraging-llama-3-and-groq-api).

## About the Project

This project demonstrates a streamlined workflow for generating high-quality content using the Llama 3 language model and Groq's AI inference technology. It includes a step-by-step guide to setting up the project, initializing AI models, and creating a complete content creation workflow using Python and Streamlit. The workflow is driven by a network of specialized agents, each designed to handle a specific aspect of the content creation process.

### Features

- **Advanced AI Integration**: Utilize Meta's Llama 3 for sophisticated language understanding and content generation.
- **High-Speed AI Processing**: Experience rapid content processing with Groq's state-of-the-art AI inference engine.
- **Agent-Based Workflow**: The workflow is divided into planning, writing, and editing phases, each handled by dedicated AI agents.
- **Interactive Web App**: A Streamlit-based interface that allows users to input topics and receive well-structured content in real-time.

### Agent Roles

The project uses a modular design where each phase of the content creation process is managed by a specialized agent. Below is a description of each agent and its role within the workflow:

```python
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
```

## Getting Started

Follow these instructions to get your project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.7 or higher
- pip and virtualenv

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/<your-username>/AI-Content-Creation-Workflow.git
   cd AI-Content-Creation-Workflow
   ```

2. **Set up a virtual environment**

   ```bash
   virtualenv env
   source env/bin/activate  # On macOS and Linux
   .\env\Scripts\activate   # On Windows
   ```

3. **Install the dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   Create a `.env` file in the project root directory and add the following:

   ```
   GROQ_API_KEY=<your_groq_api_key>
   SERPER_API_KEY=<your_serper_api_key>
   ```

### Running the application



Execute the following command to run the Streamlit application:

```bash
streamlit run app.py
```

Visit `http://localhost:8501` in your web browser to see the application in action.

## Usage

The application allows you to input a topic and automatically generates a comprehensive content plan, a detailed blog post, and a final edited version. The workflow is managed by three specialized agents: a Content Planner, a Content Writer, and an Editor, each working in unison to deliver high-quality content.

## Contributing

We welcome contributions from the community. If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

## Acknowledgments

- Meta for the Llama 3 model
- Groq for their high-performance AI inference engine
- Streamlit for enabling rapid application development

## Check out this demo video to see the workflow in action:


https://github.com/Sanchay-T/Groq-Llama-Content-Studio/assets/64085789/0b258faa-7acb-46fc-9108-dfb34f44aede

---
