from crewai import Agent
from tools import yt_tool
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = "gpt-4-0125-preview"
llm = ChatOpenAI(model=os.environ["OPENAI_MODEL_NAME"])

blog_researcher = Agent(
    role='Blog Researcher from Youtube Videos',
    goal='Get the relevant video transcription for the topic {topic} from the provided YouTube channel',
    verbose=True, 
    memory=True,
    backstory=(
       "Expert in understanding videos in AI, Data Science, Machine Learning, and Generative AI, and providing suggestions."
    ),
    llm=llm,
    tools=[yt_tool],
    allow_delegation=True
)

blog_writer = Agent(
    role='Blog Writer',
    goal='Narrate compelling tech stories about the video {topic} from YT video',
    verbose=True,  
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft "
        "engaging narratives that captivate and educate, bringing new "
        "discoveries to light in an accessible manner."
    ),
    llm=llm,
    tools=[yt_tool],
    allow_delegation=False
)