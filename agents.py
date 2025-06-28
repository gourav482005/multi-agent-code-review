from crewai import Agent

security_agent = Agent(
    role="Security Analyst",
    goal="Identify security issues in the given Python code.",
    backstory="Expert in spotting vulnerabilities like eval(), input misuse, or secrets in code."
)

performance_agent = Agent(
    role="Performance Optimizer",
    goal="Suggest improvements to make the code faster.",
    backstory="Knows how to spot slow loops, redundant logic, and optimize code."
)

style_agent = Agent(
    role="Style Checker",
    goal="Ensure code follows Python style guides (like PEP8).",
    backstory="Fan of readable, clean, well-indented Python code."
)

documentation_agent = Agent(
    role="Documentation Reviewer",
    goal="Check if the code has clear comments and docstrings.",
    backstory="Makes sure code is self-explaining and well-documented."
)
