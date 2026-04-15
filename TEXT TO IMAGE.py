
Copy of Text to image4.ipynb
Copy of Text to image4.ipynb_

[3]
20s
# Install
!pip install -q diffusers transformers accelerate gradio

import torch
import gradio as gr
from diffusers import StableDiffusionPipeline

# --- DEVICE ---
device = "cuda" if torch.cuda.is_available() else "cpu"
dtype = torch.float16 if device == "cuda" else torch.float32
…    clear_btn.click(
        fn=lambda: ("", "", None, None),
        inputs=[],
        outputs=[prompt, negative_prompt, output, download]
    )

demo.launch(share=True)

Next steps:
Colab paid products - Cancel contracts here
