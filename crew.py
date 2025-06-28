from crewai import Crew
from agents.agents import (
    security_agent,
    performance_agent,
    style_agent,
    documentation_agent
)
from tasks.review_tasks import all_tasks  # List of 4 tasks

# Create a crew with your agents and their tasks
crew = Crew(
    agents=[
        security_agent,
        performance_agent,
        style_agent,
        documentation_agent
    ],
    tasks=all_tasks,
    verbose=True  # Set to False to hide agent logs
)

# Kick off the crew to perform the code review
result = crew.kickoff()

# Print the result in the terminal
print("\n===== 📝 CODE REVIEW REPORT =====\n")
print(result)

# Save the result to a file
with open("reports/review_report.txt", "w", encoding="utf-8") as file:
    file.write(result)
