# Getting started with AGGM

1 - Download this repository by running the following command in your terminal:

```
git clone https://github.com/Adolfo-GM/AGGM
cd AGGM
```

then choose what LLM you want to use.

### Using AGGM with your own LLM or an API


1 - Create a file called ```AggmGPT.py``` inside the AGGM folder, write a function called ```AskAggmGPT(prompt)``` that takes text as a parameter and outputs the response from the LLM, you can use anything in the function, from a local model to an API.

### Using AGGM with AggmGPT-2

1 - In the same AGGM folder, download the AggmGPT-2 model by running the following command in your terminal:

```
git lfs install
git clone https://huggingface.co/Adolfo-GM/AggmGPT-2 temp-folder
mv temp-folder/* .
mv temp-folder/.* .  
rmdir temp-folder

```

2- You can run ``` aggm.py ``` to see the demo.

3 - To run your own AGGM code, you can run:

 ``` 
 python aggmtopy.py main.aggm

 ``` 
 with main.aggm replaced by your file name.

 Note that AggmGPT may require some setup, so you can also use your own LLM model.