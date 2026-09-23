import os

def turing_machine(input_word, states, tape_symbols, start_state, final_states, transitions):
    output_file = "vysledek.txt"
    output_path = os.path.join(os.path.dirname(__file__), output_file)

    current_state = start_state
    tape = [None] * 30
    head_position = 5

    for char in input_word:
        tape[head_position] = char
        head_position += 1
    head_position = 5

    log = [
        "=== Nová simulace Turingova stroje ===\n",
        f"Počáteční slovo: {input_word}\n",
        f"Počáteční stav pásky: {tape}\n\n"
    ]

    while current_state not in final_states:
        current_symbol = tape[head_position]
        transition = next(
            (t for t in transitions if t[0] == current_state and t[1] == current_symbol),
            None
        )
        if not transition:
            log.append("Přechodová funkce nenalezena. Stroj se zastavil.\n")
            break
        current_state, write_symbol, move = transition[2]
        tape[head_position] = write_symbol
        head_position += move
        if head_position < 0:
            tape.insert(0, None)
            head_position = 0
        elif head_position >= len(tape):
            tape.append(None)
        log.append(f"Stav: {current_state}, Páska: {tape}, Pozice hlavy: {head_position}\n")

    log.append("\nTuringův stroj dosáhl koncového stavu.\n")
    log.append(f"Konečný stav pásky: {tape}\n\n")

    with open(output_path, "a", encoding="utf-8") as file:
        file.writelines(log)

    print(f"Výsledky simulace byly zapsány do souboru: {output_path}")


turing_machine(
    input_word="1100100110",
    states=["q0", "q1", "q2", "q3", "q4", "q5", "q6", "q7"],
    tape_symbols=["0", "1", None],
    start_state="q0",
    final_states=["q7"],
    transitions=[
        ["q0", "0", ["q1", None, 1]],
        ["q1", "0", ["q1", "0", 1]],
        ["q1", "1", ["q2", "1", 1]],
        ["q2", "1", ["q2", "1", 1]],
        ["q2", None, ["q3", None, -1]],
        ["q3", "1", ["q4", None, -1]],
        ["q4", None, ["q7", None, 1]],
        ["q4", "1", ["q5", "1", -1]],
        ["q5", "1", ["q5", "1", -1]],
        ["q5", "0", ["q6", "0", -1]],
        ["q6", "0", ["q6", "0", -1]],
        ["q6", None, ["q0", None, 1]]
    ]
)

turing_machine(
    input_word="1101",
    states=["q0", "q1", "q2", "q3", "q4", "q5"],
    tape_symbols=["0", "1", None],
    start_state="q0",
    final_states=["q5"],
    transitions=[
        ["q0", "0", ["q1", None, 1]],
        ["q0", "1", ["q1", None, 1]],
        ["q0", None, ["q5", None, 0]],
        ["q1", "0", ["q1", "0", 1]],
        ["q1", "1", ["q1", "1", 1]],
        ["q1", None, ["q2", None, -1]],
        ["q2", "0", ["q3", "0", -1]],
        ["q2", "1", ["q3", "1", -1]],
        ["q3", None, ["q4", None, 1]],
        ["q4", "0", ["q5", "0", 1]],
        ["q4", "1", ["q5", "1", 1]],
    ]
)


turing_machine(
    input_word="101110",
    states=["q0", "q1", "q2"],
    tape_symbols=["0", "1", None],
    start_state="q0",
    final_states=["q2"],
    transitions=[
        ["q0", "0", ["q0", "0", 1]],
        ["q0", "1", ["q0", "0", 1]],
        ["q0", None, ["q2", None, 0]]
    ]
)
