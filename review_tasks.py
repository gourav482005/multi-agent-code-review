from crewai import Task
from agents.agents import (
    security_agent,
    performance_agent,
    style_agent,
    documentation_agent
)


security_task = Task(
    agent=security_agent,
    description="Review the provided Python code and identify any potential security issues. Focus on risky functions, exposed credentials, or bad input handling.",
    expected_output="A list of security vulnerabilities found in the code, with explanations."
)


performance_task = Task(
    agent=performance_agent,
    description="Analyze the Python code for performance problems like inefficient loops, unnecessary variables, or bad logic.",
    expected_output="Suggestions for improving code speed and efficiency."
)


style_task = Task(
    agent=style_agent,
    description="Check if the code follows Python style guides (like PEP8). Look for bad indentation, naming conventions, and spacing.",
    expected_output="A style review report highlighting issues and how to fix them."
)


documentation_task = Task(
    agent=documentation_agent,
    description="Review if the code has helpful docstrings and inline comments. Point out missing or unclear documentation.",
    expected_output="A report on the quality of documentation and suggestions to improve it."
)


all_tasks = [security_task, performance_task, style_task, documentation_task]
