from slugify import slugify

def generate_content(keyword, lang="en"):
    # Dummy functions: Bạn có thể dùng template, hoặc gọi API GPT/OpenAI nếu cần
    title = f"{keyword.title()} - Beautiful Stock Photos"
    meta = f"{keyword.title()} photos. Free download. {keyword} images for blog, website, social, more."[:160]
    description = "\n".join([
        f"Here are {keyword} images you can use for your creative projects.",
        "All images are high quality and free to use.",
        "Perfect for blogs, websites, or social media.",
        f"Download {keyword} pictures now!",
        "Attribution is appreciated."
    ])
    return {
        "title": title,
        "meta": meta,
        "description": description
    }