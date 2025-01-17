def detect_sequence_and_type(transitions):
    # Step 1: Parse input into a dictionary of state transitions
    state_transitions = {}
    initial_state = transitions[0][0]  # the first present state as initial state
    
    for present_state, next_state, input_signal, output_signal in transitions:
        state_transitions[(present_state, input_signal)] = (next_state, output_signal)
    
    # Step 2: Traverse the state machine to detect the sequence
    current_state = initial_state
    sequence = ""
    visited_transitions = set()  # Track visited transitions to avoid looping
    sequence_detected = False
    final_state = None

    while not sequence_detected:
        found_transition = False
        # Iterate over transitions to find the next state
        for (state, input_signal), (next_state, output_signal) in state_transitions.items():
            if state == current_state and (state, input_signal) not in visited_transitions:
                visited_transitions.add((state, input_signal))
                found_transition = True
                # Append input to sequence if output is 1
                sequence += input_signal
                current_state = next_state

                # Check if we reached a sequence-completing transition
                if output_signal == '1':
                    sequence_detected = True
                    final_state = current_state
                break

        # Stop if no new transition is found to avoid infinite loops
        if not found_transition:
            break

    # Step 3: Determine if it's an overlapping or non-overlapping detector
    # Check if the final state transitions back to the initial state with output '1'
    detector_type = "Overlapping Sequence Detector"  # default assumption
    if final_state and (final_state, '1') in state_transitions:
        next_state, output_signal = state_transitions[(final_state, '1')]
        if next_state == initial_state and output_signal == '1':
            detector_type = "Non Overlapping Sequence Detector"

    # Step 4: Return the detected sequence and detector type
    return sequence, detector_type

transitions = []
#print("Enter transitions (press Enter on an empty line to stop):")
while True:
    line = input().strip()
    if not line:  # Stop input on an empty line
        break
    present_state, next_state, input_signal, output_signal = line.split()
    transitions.append((present_state, next_state, input_signal, output_signal))
print(transitions)
# Step 2: Call the function with the parsed transitions
sequence, detector_type = detect_sequence_and_type(transitions)

# Step 3: Print the results
print(sequence)
print(detector_type)