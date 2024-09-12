from crewai import Agent
from tools import tool
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os


## call the gemini models
llm=ChatGoogleGenerativeAI(model="gemini-1.5-flash",
                           verbose=True,
                           temperature=0.5,
                           google_api_key=os.getenv("GOOGLE_API_KEY"))

# Create a researcher agent with memory and verbose mode

researcher=Agent(
    role="SeniorResearcher",
    goal='Deep research on {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that get high reach on linkedin."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True

)

## create a writer agent with custom tools responsible in writing linkedin post

post_writer = Agent(
  role='Writer',
  goal='Create a beautiful and eye catching linkedin post on {topic}',
  verbose=True,
  memory=True,
  backstory=(
    "With a flair for simplifying complex topics, you craft"
    "engaging narratives that captivate and educate, bringing new"
    "discoveries to light in an accessible manner."
  ),
  tools=[tool],
  llm=llm,
  allow_delegation=False
)