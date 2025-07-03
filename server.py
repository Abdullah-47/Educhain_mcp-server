from mcp.server.fastmcp import FastMCP
from educhain import Educhain, LLMConfig
from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel,Field
from typing import List, Optional
import os
import dotenv
import traitlets  # Explicitly import to resolve dependency error

# Load environment variables
dotenv.load_dotenv()
os.environ["OPENAI_API_KEY"] = "your-key-here"  # Replace with actual key

# Initialize Gemini model
if "GEMINI_API_KEY" not in os.environ:
    raise ValueError("Missing GEMINI_API_KEY")
gemini_flash = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=os.getenv("GEMINI_API_KEY")
)
client = Educhain(LLMConfig(custom_model=gemini_flash))

# Create MCP server
mcp = FastMCP("Educhain Server", dependencies=["educhain"], auto_mount_resources=True)

# Tool: Generate MCQs
@mcp.tool()
def generate_mcqs(topic: str, num: int = 3, difficulty: str = "Easy") -> dict:
    """Generate multiple-choice questions for a given topic"""
    try:
        mcqs = client.qna_engine.generate_questions(
            topic=topic,
            num=num,
            question_type="Multiple Choice",
            difficulty_level=difficulty
        )
        return mcqs.model_dump()
    except Exception as e:
        return {"error": str(e)}

#Flashcard generator tool
@mcp.tool()
def generate_flashcards(topic: str, num: int = 5) -> dict:
    """Generate flashcards for a given topic"""
    try:
        flashcards = client.content_engine.generate_flashcards(
            topic=topic,
            num=num
        )
        return flashcards.model_dump()
    except Exception as e:
        return {"error": str(e)}

# Dynamic Resource: Lesson Plan Generator
class MainTopic(BaseModel):
    title: str
    description: str
    activities: List[str]

class LessonPlan(BaseModel):
    title: str = Field(..., description="The overall title of the lesson plan.")
    subject: str = Field(..., description="The subject area of the lesson.")
    learning_objectives: List[str] = Field(..., description="Learning objectives.")
    lesson_introduction: str = Field(..., description="Introduction to the topic.")
    main_topics: List[MainTopic] = Field(..., description="Topics and activities.")
    learning_adaptations: Optional[str] = None
    real_world_applications: Optional[str] = None
    ethical_considerations: Optional[str] = None


@mcp.resource("lessonplan://{topic}")
def generate_lesson_plan(topic: str) -> LessonPlan:
    """Generate a lesson plan for a specific topic."""
    lesson_topic = topic.replace("-", " ").title()
    try:
        lesson_plan = client.content_engine.generate_lesson_plan(
            topic=lesson_topic,
            response_model=LessonPlan
        )
        return lesson_plan
    except Exception as e:
        return LessonPlan(title="Error", subject=lesson_topic, learning_objectives=[str(e)], lesson_introduction="", main_topics=[])

# Validate resource registration
if __name__ == "__main__":
    print("Registered resources:", mcp.list_resources())
    print("Registered tools:", mcp.list_tools())
