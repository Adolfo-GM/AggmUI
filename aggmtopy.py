import sys
import os
from AggmGPT import * 

def Aggm2Python(code):
    prompt = f"""
    Translate the following code into Python. Do not send anything else — no explanations, no comments, just the raw translated Python code.
    Translate this code to Python:
    {code}
    """
    output = AskAggmGPT(prompt)
    with open("output.py", "w", encoding="utf-8") as file:
        file.write(output)
    return output

def main():
    if len(sys.argv) != 2:
        print("Usage: python aggmtopy.py <filename>.aggm")
        sys.exit(1)

    filename = sys.argv[1]

    if not filename.endswith(".aggm"):
        print("Error: Input file must have a .aggm extension.")
        sys.exit(1)

    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

    with open(filename, "r", encoding="utf-8") as file:
        Aggm_code = file.read()

    translated_code = Aggm2Python(Aggm_code)
    print("✅ Translation complete. Output saved to output.py.")
    print("🔗 Translated code preview:")
    print(translated_code)

if __name__ == "__main__":
    main()
