from langgraph.graph import StateGraph
from typing import TypedDict

# Define the shared state
class AgentState(TypedDict):
    messages: list
    patient_data: dict  # Shared state for patient details and resources

# Agent Nodes
def patient_scheduling_agent(state, config):
    message = "Scheduling appointment for patient: " + state['patient_data']['name']
    return {"messages": state['messages'] + [{"content": message}]}

def diagnosis_assistance_agent(state, config):
    message = "Diagnosing symptoms: " + ", ".join(state['patient_data']['symptoms'])
    return {"messages": state['messages'] + [{"content": message}]}

def resource_allocation_agent(state, config):
    resources = state['patient_data'].get('resources_needed', [])
    message = f"Allocating resources: {', '.join(resources)}"
    return {"messages": state['messages'] + [{"content": message}]}

# Configure Workflow
workflow = StateGraph(AgentState)

# Define nodes
workflow.add_node("patient_scheduling", patient_scheduling_agent)
workflow.add_node("diagnosis_assistance", diagnosis_assistance_agent)
workflow.add_node("resource_allocation", resource_allocation_agent)

# Define edges (workflow starts from patient_scheduling)
workflow.add_edge("patient_scheduling", "diagnosis_assistance")
workflow.add_edge("diagnosis_assistance", "resource_allocation")

# Debug step to check node reachability
for node in workflow.nodes:
    print(f"Node: {node}, Incoming Edges: {workflow.get_incoming_edges(node)}, Outgoing Edges: {workflow.get_outgoing_edges(node)}")

# Compile and Execute
try:
    app = workflow.compile()
    state = {
        "messages": [],
        "patient_data": {
            "name": "John Doe",
            "symptoms": ["fever", "cough"],
            "resources_needed": ["bed", "radiology"]
        }
    }

    response = app.invoke(state)
    for message in response["messages"]:
        print(message["content"])

except ValueError as e:
    print(f"Graph validation error: {e}")
