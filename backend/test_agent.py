from agent.agent import run_agent


response = run_agent(
    "My flight was cancelled. I want a full refund.",
    "SK4821X"
)

print("\nAGENT RESPONSE:\n")
print(response)