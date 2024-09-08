from crewai import Task
from tools import yt_tool
from agents import blog_researcher, blog_writer

research_task = Task(
  description=(
    "Research the topic '{topic}' using the YouTube channel. "
    "If no specific video is found, summarize general information from relevant videos. "
    "Handle any errors gracefully and provide the best information possible."
  ),
  expected_output='A comprehensive 3 paragraphs long report based on the {topic} from video content or general channel information.',
  tools=[yt_tool],
  agent=blog_researcher,
)

write_task = Task(
  description=(
    "Using the research provided, create a blog post about '{topic}'. "
    "If specific video information is not available, write based on general knowledge of the topic."
  ),
  expected_output='A blog post summarizing information on the topic {topic}, sourced from YouTube or general knowledge.',
  tools=[yt_tool],
  agent=blog_writer,
  async_execution=False,
  output_file='new-blog-post.md'  
)