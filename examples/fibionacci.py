from agents_for_all import Agent
from agents_for_all.llms.direct import DirectModel
from agents_for_all.tools.python import Python

llm = DirectModel(
  api_endpoint="http://localhost:1234/v1/chat/completions",
  model="deepseek-r1-distill-qwen-14b"
)
agent = Agent(llm=llm, tools=[Python()])
result = agent.do("Generate a Fibonacci sequence of length 10.")
print("OUTPUT")
print(result.output) # Final output
print("HISTORY")
print(result.history) # History of steps taken
