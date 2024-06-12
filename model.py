# Load model directly

# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM
from transformers import logging as hf_logging
from huggingface_hub import HfApi, HfFolder
import torch
import logging
device = "cuda:0" if torch.cuda.is_available() else "cpu"
# Clear cache
torch.cuda.empty_cache()
hf_logging.set_verbosity_info()

tokenizer = AutoTokenizer.from_pretrained("Writer/palmyra-small")
model = AutoModelForCausalLM.from_pretrained("Writer/palmyra-small").to(device)
print(';bruh')
model.save_pretrained("./local_model")
tokenizer.save_pretrained("./local_model")

# Step 4: Load the model and tokenizer from the local storage
local_model_path = "./local_model"
model = AutoModelForCausalLM.from_pretrained(local_model_path).to(device)
tokenizer = AutoTokenizer.from_pretrained(local_model_path)
print(';bruh')
def chat(text):
    print('im here')
    input_ids = tokenizer.encode("What is LLM?", return_tensors="pt").cuda()
    print(input_ids)
    print(input_ids.shape)
    print('here')
    output = model.generate(
        input_ids,
        temperature=0.9,
        max_new_tokens=100
    )
    print('bro')
    # Decode and print generated text
    for i, sample_output in enumerate(output):
        print("{}: {}".format(i + 1, tokenizer.decode(sample_output, skip_special_tokens=True)))

def print_gpu_memory():
    print("GPU memory allocated:", torch.cuda.memory_allocated())
    print("GPU memory cached:", torch.cuda.memory_reserved())

if __name__=='__main__':
    print(chat(''))
