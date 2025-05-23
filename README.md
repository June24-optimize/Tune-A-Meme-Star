# 🎬 Text-to-Meme-Star

**Text-to-Meme-Star** is a lightweight text-to-video generation model that creates short animated gifs (meme or emoji-style) from natural language prompts. It's optimized for low-latency applications like **chat apps**, where users want a fast, expressive animation generated on the fly from a few words.

> ✨ Example: Input — “dancing cat” → Output — 🤯 animated gif of an dancing cat cartoon.

---

## 🧠 Core Features


- 🐥 **Lightweight Model** (based on stable-diffusion-v1-5)
- ⚡ **Fast Inference** ~ 8sec sampling time.
- ~ 30 minutes finetuning time, this model is finetuned using one training (text, video) pair, trained on 8GB GPUs within 200 iterations.
- 🧪 **Trained on one (text, video) pair** for fine-tuned personalization
- 🎭 **Emoji/Meme Style Control** 
- 🔁 **Short GIF Output** (1–2 seconds, 128×128 or 256×256)
- 🧾 **Prompt-based Generation** for expressive messaging UX

---
## 📊 Results 

| **Training Pair** | **Test Prompt 1** | **Test Prompt 2** | **Test Prompt 3** | **Test Prompt 4** |
|-------------------|-------------------|-------------------|-------------------|-------------------|
| ![](results/cat_apple.gif)<br>`"running apple-cat"` | ![](results/running_pineapple_cat.gif)<br>`"running pineapple-cat"` | ![](results/running_banana_cat.gif)<br>`"running banana-cat"` | ![](results/running_green_apple_pig.gif)<br>`"running green apple-pig"` | ![](results/running_blueberry_elephant.gif)<br>`"running blueberry-elephant"` 
| ![](results/a_spinning_oiiai_cat.gif)<br>`"a spinning oiiai-cat"` | ![](results/a_spinning_oiiai_rabbit.gif)<br>`"a spinning oiiai rabbit"` | ![](results/a_spinning_oiiai_squirrel.gif)<br>`"a spinning oiiai squirrel"` | ![](results/a_spinning_oiiai_pig.gif)<br>`"a spinning oiiai pig"` | ![](results/a_spinning_oiiai_dog.gif)<br>`"a spinning oiiai dog"` 
| ![](results/cat_pop.gif)<br>`"popping cat"` | ![](results/popping_cow.gif)<br>`"popping cow"` | ![](results/popping_rabbit.gif)<br>`"popping rabbit"` | ![](results/popping_pig.gif)<br>`"popping pig"` | ![](results/popping_Basenji_dog.gif)<br>`"popping dog"` |
| ![](results/cat_happy.gif)<br>`"happy cat"` | ![](results/happy_birthday_cake_with_HAPPY_BIRTHDAY_text.gif)<br>`"happy birthday cake with HAPPY BIRTHDAY text"` | ![](results/happy_rabbit_with_LOL_text.gif)<br>`"happy rabbit with LOL text"` | ![](results/happy_avocado_with_Yeah~_text.gif)<br>`"happy avocado with Yeah~ text"` | ![](results/happy_fox_with_FRIDAY_MOOD_text.gif)<br>`"happy fox with FRIDAY MOOD text"` |
| ![](results/banana_cat_is_crying.gif)<br>`"banana cat is crying"` | ![](results/cucumber_cat_is_crying_with_I'm_Fine_text.gif)<br>`"cucumber cat is crying with I'm Fine text"` | ![](results/Tomato_penguin_is_crying.gif)<br>`"Tomato penguin is crying"` | ![](results/eggplant_cat_is_crying.gif)<br>`"eggplant cat is crying"` | ![](results/banana_is_crying_with_Oh_Noooo_text.gif)<br>`"banana is crying with Oh Noooo text"` |

> Each row shows a training (text, video) pair, followed by test results from unseen prompts.

---

## 🛠️ Model Architecture

- **Backbone**: [Stable-Diffusion](https://huggingface.co/sd-legacy/stable-diffusion-v1-5)
- **Temporal Layer**: Custom 2D → 3D motion blocks 
- **Training Framework**: Modified [Tune-A-Video](https://github.com/showlab/Tune-A-Video)
- **Input**: Short sentence or phrase (`"running pineapple-cat"`, `"dancing cat with FRIDAY MOOD text"`)
- **Output**: Animated video (gif or mp4, 16–24 frames)

---

## 📦 Installation

```bash
git clone https://github.com/yourusername/text-to-meme-star.git
cd text-to-meme-star
conda create -n meme-star python=3.9
conda activate meme-star
pip install -r requirements.txt
```
---

## Acknowledgements
This project is built upon [Tune-A-Video](https://github.com/showlab/Tune-A-Video).  
Special thanks to the original authors for their excellent work on text-to-video generation.

