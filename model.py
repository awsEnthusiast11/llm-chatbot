# Load model directly
from dotenv import load_dotenv
import os
load_dotenv()
# Load model directly
from transformers import GPT2Tokenizer, GPT2LMHeadModel
from transformers import logging as hf_logging
from huggingface_hub import HfApi, HfFolder
import torch
import logging
device = "cuda:0" if torch.cuda.is_available() else "cpu"
# Clear cache
torch.cuda.empty_cache()
hf_logging.set_verbosity_error()
token = os.environ['access_token']
HfFolder.save_token(token)

# tokenizer = GPT2Tokenizer.from_pretrained("ComCom/gpt2-small")
# model = GPT2LMHeadModel.from_pretrained("ComCom/gpt2-small").to(device)
# model.save_pretrained("./local_model")
# tokenizer.save_pretrained("./local_model")

# Step 4: Load the model and tokenizer from the local storage
local_model_path = "./local_model"
model = GPT2LMHeadModel.from_pretrained(local_model_path,ignore_mismatched_sizes=True).to(device)
tokenizer = GPT2Tokenizer.from_pretrained(local_model_path)
def chat(text):
    input_ids = tokenizer.encode(text, return_tensors="pt").cuda()
    output = model.generate(
        input_ids,
        temperature=0.9,
        max_new_tokens=100
    )
    # Decode and print generated text
    res = tokenizer.decode(output[0])
    res_split = res.split("\n")
    return res_split[2]
def print_gpu_memory():
    print("GPU memory allocated:", torch.cuda.memory_allocated())
    print("GPU memory cached:", torch.cuda.memory_reserved())

if __name__=='__main__':
    print(chat('hello buddy'))
