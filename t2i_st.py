"""Streamlit app for text-to-image generation using the Stable Diffusion model."""

import logging
import time


def get_log(name):
	if not logging.getLogger().hasHandlers():
		logging.basicConfig(level=logging.INFO, format='%(asctime)s - "%(name)s" (%(filename)s:%(lineno)d), %(levelname)s\t:"%(message)s"')
	return logging.getLogger(name or __name__)


LOG = logging.getLogger(__name__)
LOG.info("Starting Streamlit app")
import streamlit as st
import torch
from diffusers import AutoPipelineForText2Image
from PIL import Image


class Gen:
	"""Wrapper for the text-to-image model. It is a class to allow for caching of the model."""

	def __init__(self):
		LOG.info("Initializing NN model")
		self.pipe = AutoPipelineForText2Image.from_pretrained("stabilityai/sdxl-turbo", torch_dtype=torch.float16, variant="fp16")
		self.pipe.to("cuda")
		LOG.info("NN model initialized")

	def gen(self, prompt="default prompt"):
		LOG.info(f"Generating image for: {prompt}")
		# measure image generation time
		start = time.time()
		image = self.pipe(prompt=prompt, num_inference_steps=1, guidance_scale=0.0).images[0]
		LOG.info(f"Generated in: {time.time() - start}")
		return image


@st.cache_resource
def get_gen():
	return Gen()


if "generate_trigger" not in st.session_state:
	st.session_state.generate_trigger = True
st.title("SDXL Turbo Image Generator")
gen = get_gen()
prompt = st.text_input("Prompt:", "a photo of a photorealistic chrome sphere, ancient cyberpunk, Octane render")
# image_container = st.empty()
# i = gen.gen(prompt) if prompt else Image.new("RGB", (512, 512), (20, 20, 20))
# image_container.image(i, caption="Generated Image", use_column_width=True)
# st.button('Generate Image', on_click=lambda: setattr(st.session_state, 'generate_trigger', not st.session_state.generate_trigger))
st.button("Generate Image", on_click=lambda: setattr(st.session_state, "generate_trigger", True))
if st.session_state.generate_trigger:
	image_container = st.empty()
	i = gen.gen(prompt) if prompt else Image.new("RGB", (512, 512), (20, 20, 20))
	image_container.image(i, caption="Generated Image", use_container_width=True)
