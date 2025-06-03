from tuneavideo.pipelines.pipeline_tuneavideo import TuneAVideoPipeline
from tuneavideo.models.unet import UNet3DConditionModel
from tuneavideo.util import save_videos_grid
from diffusers import AutoencoderKL
from transformers import CLIPTextModel, CLIPTokenizer
import torch

pretrained_model_path = "./checkpoints/stable-diffusion-v1-5"
my_model_path = "./outputs/cat-pop"
text_encoder = CLIPTextModel.from_pretrained(pretrained_model_path, subfolder="text_encoder")
vae = AutoencoderKL.from_pretrained(pretrained_model_path, subfolder="vae")
unet = UNet3DConditionModel.from_pretrained(my_model_path, subfolder='unet', torch_dtype=torch.float16).to('cuda')
pipe = TuneAVideoPipeline.from_pretrained(pretrained_model_path, unet=unet, torch_dtype=torch.float16).to("cuda")
# pipe.enable_xformers_memory_efficient_attention()
# pipe.enable_vae_slicing()

prompt = "a egg is popping"
ddim_inv_latent = torch.load(f"{my_model_path}/inv_latents/ddim_latent-350.pt").to(torch.float16)
video = pipe(prompt, latents=ddim_inv_latent, video_length=12, height=256, width=256, num_inference_steps=100, guidance_scale=15).videos

save_videos_grid(video, f"./{prompt}.gif", loop=0)