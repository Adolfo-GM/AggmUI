# DEMO

from AggmGPT import *

Aggm_code = open("main.aggm").read()

def Aggm2Python(code):
   prompt = f'''
 
   Translate the following code into python. Do not send aything else and do not reply. Send the translated code as python.
   Translate this code to python: ${code}

   '''
   output = AskAggmGPT(prompt)
   file = open("output.py", "w")
   file.write(output)
   return output

if __name__ == "__main__":
    print(Aggm2Python(Aggm_code))
    print("✅ Translation of 'main.aggm' complete. Output saved to output.py.")