# Sdxl_gen

  - Streamlit-based sdxl turbo images generator.


## Installation:

  - This miniapp requires some decent Python, 3.10 and up, CUDA 12.8, PyTorch components and Streamlit installed.
  - Here's short instructions on how to make it work:
    - Use Anaconda / Miniconda
    - conda create -n ai python=3.13
    - conda activate ai
    - pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu128
    - pip3 install diffusers transformers accelerate streamlit
    - launch run.cmd or just `python t2i_st.py`
  - *Warning: it will download around 15Gb of NN weights*


## Example prompts:

  - Full size photo of a two photorealistic plutonium cubes with complex geometric pattern, parts of the old mechanism, ancient weared rusty cyberpunk, hellraiser style, dark anodized scratched bronze, ultra detail
  - Ours en peluche jaune, a restaurant is lit up at night on a rainy day, “gas station photography, cgsociety ), sad cop looking at a, by Nōami, picture of a loft in morning, dark ominous mood, petrol energy, a quaint, photo realistic symmetrical, drive out, pouring, terminal dark
  - A photo of a realistic corroded chrome sphere, ancient cyberpunk, octane render
  - A neon-lit alleyway in a rainy cyberpunk city, slick wet streets reflecting glowing holograms, vintage android detective with a trench coat and glowing eyes, smoke curling from a street vendor’s cart, ultra detailed, moody noir lighting, cinematic composition
  - Close-up of a weathered, high-tech revolver resting on a cracked concrete floor, neon signs flickering in the background, sci-fi noir style, heavy shadows and reflections, detailed textures of worn metal and scratched glass, rendered with octane
  - A futuristic cyberpunk rooftop at night, overlooking a sprawling megacity with towering skyscrapers, holographic ads flickering through the fog, lone figure with cybernetic enhancements standing in silhouette, noir atmosphere, cold blue and purple color palette, ultra realistic

## Demo video:
  - [![Demo video](docs/demo.jpg)](https://youtu.be/thDtiN_u4DY)