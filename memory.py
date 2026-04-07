mission_history = []

def save_mission(mission_input, mission_output):
    mission_history.append({
        "input": mission_input,
        "output": mission_output
    })

def show_history():
    return mission_history