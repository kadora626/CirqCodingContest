import cirq
import numpy as np

def generate_plus_or_minus(sign):
    circuit = cirq.Circuit()
    res_qubit = cirq.LineQubit(0)
    if (sign == -1):
        circuit.append([
            cirq.X(res_qubit),
        ])
    circuit.append([
        cirq.H(res_qubit),
    ])

    return circuit

def generate_bell_state(index):
    circuit = cirq.Circuit()
    res_qubit = [cirq.LineQubit(0), cirq.LineQubit(1)]
    if index % 2 == 1:
        circuit.append([
            cirq.X(res_qubit[0]),
        ])

    circuit.append([
        cirq.H(res_qubit[0]),
        cirq.CNOT(res_qubit[0], res_qubit[1]),
    ])

    if index > 1:
        circuit.append([
            cirq.X(res_qubit[1]),
        ])

    return circuit

def generate_ghz_state(length):
    circuit = cirq.Circuit()
    res_qubit = [cirq.LineQubit(i) for i in range(length)]
    circuit.append([
        cirq.H(res_qubit[0]),
    ])

    for i in range(length - 1):
        circuit.append([
            cirq.CNOT(res_qubit[0], res_qubit[i + 1]),
        ])

    return circuit

def print_result(simulator, circuit):
    result = simulator.simulate(circuit=circuit)
    print(np.around(result.final_state, 5))

def main():
    # prepare simulator
    simulator = cirq.google.XmonSimulator()

    # Results of Generate plus of minus state
    print("Generate plus or minus state")
    print("Plus Circuit:")
    plus_circuit = generate_plus_or_minus(1)
    print(plus_circuit)
    print("Print Plus Circuit Result")
    print_result(simulator, plus_circuit)
    
    print("Minus Circuit:")
    minus_circuit = generate_plus_or_minus(-1)
    print(minus_circuit)
    print("Print Minus Circuit Result")
    print_result(simulator, minus_circuit)

    # Results of Generate Bell states
    print("------------------------")
    print("Generate Bell state")
    for i in range(4):
        print("index: %d" % i)
        bell_circuit = generate_bell_state(i)
        print("Circuit:")
        print(bell_circuit)
        print("Print index %d Results" % i)
        print_result(simulator, bell_circuit)

    # Results of Generate GHZ states
    print("------------------------")
    print("Generate GHZ state")
    for i in range(3):
        print("length: %s" % str(i + 1))
        ghz_circuit = generate_ghz_state(i+1)
        print("Circuit:")
        print(ghz_circuit)
        print("Print lenght %s Results" % str(i + 1))
        print_result(simulator, ghz_circuit)

if __name__ == '__main__':
    main()
