from langgraph.func import entrypoint, task

@task
def first() -> str:
    print("Step 1...")
    return "First"

@task
def second() -> str:
    print("Step 2...")
    return "Second"

@entrypoint()
def simple_flow(input):
    print(f"DONE... {first().result()} {second().result()}") 


def start():
    simple_flow.invoke(input="check")


