import os
from slugify import slugify
import requests
from PIL import Image
from io import BytesIO

def scrape_and_download_images(keyword, lang, config):
    # TODO: Thêm chức năng search API Google hoặc Pinterest.
    # Demo: lấy các URL mẫu (cần thay bằng code thật)
    image_urls = [f"https://dummyimage.com/600x400/000/fff&text={slugify(keyword)}+{i}" for i in range(1, config["num_images"]+1)]
    image_dir = os.path.join(config["output_dir"], lang, slugify(keyword))
    os.makedirs(image_dir, exist_ok=True)
    image_paths, image_sources = [], []
    for idx, url in enumerate(image_urls):
        img_name = f"{slugify(keyword)}-{idx+1}.jpg"
        img_path = os.path.join(image_dir, img_name)
        try:
            response = requests.get(url)
            img = Image.open(BytesIO(response.content))
            # Resize nếu cần
            if config.get("resize", False):
                img = img.resize(tuple(config.get("image_size", [800,600])))
            img.save(img_path, optimize=config.get("optimize_image", True))
            image_paths.append(img_path)
            image_sources.append(url)
        except Exception as e:
            print(f"Error downloading {url}: {e}")
    return image_paths, image_sources