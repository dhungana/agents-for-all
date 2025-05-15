from agents_for_all import Agent
from agents_for_all.llms.direct import DirectModel
from agents_for_all.tools.file import File
from agents_for_all.tools.shell import Shell

llm = DirectModel(
    api_endpoint="http://localhost:1234/v1/chat/completions",
    model="deepseek-r1-distill-qwen-14b",
)
agent = Agent(llm=llm, tools=[File(), Shell()])
result = agent.do(
    "Figure out the system date through Shell tool. Then create a file using File tool"
)
print("OUTPUT")
print(result.output)  # Final output
print("HISTORY")
print(result.history)  # History of steps taken
