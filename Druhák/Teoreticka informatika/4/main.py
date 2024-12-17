def automat(states, alphabet, transition_function, start_state, accepting_states, input_word):
    current_state = start_state

    for symbol in input_word:
        if symbol not in alphabet:
            return False  # Neplatný symbol ve slově

        if (current_state, symbol) not in transition_function:
            return False  # Žádný přechod pro kombinaci stav/symbol

        current_state = transition_function[(current_state, symbol)]

    return current_state in accepting_states


# Automat 1
states1 = {"q0", "q1"}
alphabet1 = {"a", "b"}
transition_function1 = {
    ("q0", "a"): "q1",
    ("q0", "b"): "q0",
    ("q1", "a"): "q0",
    ("q1", "b"): "q1",
}
start_state1 = "q0"
accepting_states1 = {"q0"}

print(automat(states1, alphabet1, transition_function1, start_state1, accepting_states1, ""))  # True
print(automat(states1, alphabet1, transition_function1, start_state1, accepting_states1, "aa"))  # True
print(automat(states1, alphabet1, transition_function1, start_state1, accepting_states1, "aba"))  # False

# Automat 2
states2 = {"q0", "q1", "q2"}
alphabet2 = {"a", "b"}
transition_function2 = {
    ("q0", "a"): "q1",
    ("q0", "b"): "q0",
    ("q1", "a"): "q1",
    ("q1", "b"): "q2",
    ("q2", "a"): "q1",
    ("q2", "b"): "q0",
}
start_state2 = "q0"
accepting_states2 = {"q2"}

print(automat(states2, alphabet2, transition_function2, start_state2, accepting_states2, "ab"))  # True
print(automat(states2, alphabet2, transition_function2, start_state2, accepting_states2, "aab"))  # True
print(automat(states2, alphabet2, transition_function2, start_state2, accepting_states2, "b"))  # False

# Automat 3
states3 = {"q0", "q1", "q2", "q3"}
alphabet3 = {"a", "b"}
transition_function3 = {
    ("q0", "a"): "q1",
    ("q0", "b"): "q2",
    ("q1", "a"): "q0",
    ("q1", "b"): "q3",
    ("q2", "a"): "q3",
    ("q2", "b"): "q0",
    ("q3", "a"): "q2",
    ("q3", "b"): "q1",
}
start_state3 = "q0"
accepting_states3 = {"q1"}

print(automat(states3, alphabet3, transition_function3, start_state3, accepting_states3, "a"))  # True
print(automat(states3, alphabet3, transition_function3, start_state3, accepting_states3, "ab"))  # False
print(automat(states3, alphabet3, transition_function3, start_state3, accepting_states3, "abb"))  # True
