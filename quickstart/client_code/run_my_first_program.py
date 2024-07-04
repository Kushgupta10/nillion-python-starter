from nada_dsl import *

def nada_main():
    # Define parties
    party1 = Party(name="Party1")
    party2 = Party(name="Party2")
    party3 = Party(name="Party3")
    
    # Define inputs (secret integers)
    a = SecretInteger(Input(name="A", party=party1))
    b = SecretInteger(Input(name="B", party=party2))
    
    # Perform computation (addition of secret integers)
    result = a + b
    
    # Define output (result of computation)
    output = Output(result, "my_output", party3)
    
    # Return the output as a list (as required by the original example)
    return [output]

# Example usage:
if __name__ == "__main__":
    program_output = nada_main()
    print(program_output)
