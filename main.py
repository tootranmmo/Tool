import yaml
from modules.keyword_importer import load_keywords
from modules.content_generator import generate_content
from modules.image_scraper import scrape_and_download_images
from modules.internal_linker import insert_internal_links
from modules.exporter import export_articles, export_csv_json
from modules.scheduler import generate_sitemap, schedule_posts
from modules.indexing import ping_google_index
from modules.logger import Logger

def main():
    # Load config
    with open("config.yaml", "r", encoding="utf-8") as f:
        config = yaml.safe_load(f)
    logger = Logger(config.get("log_file", "output/log.txt"))

    # 1. Import keywords
    keywords_by_lang = load_keywords("keywords.txt", config["languages"])
    logger.log("Imported keywords.")

    # 2. For each language & keyword: generate content, images, links
    for lang, keywords in keywords_by_lang.items():
        for keyword in keywords:
            logger.log(f"[{lang}] Processing: {keyword}")
            content = generate_content(keyword, lang)
            images, image_sources = scrape_and_download_images(
                keyword, lang, config
            )
            article_html = export_articles(
                keyword, lang, content, images, image_sources, config
            )
            # Insert internal links
            article_html = insert_internal_links(article_html, keywords, keyword)
            # Export HTML
            # ... (Đã xuất trong export_articles)
    # 3. Export CSV/JSON
    export_csv_json(keywords_by_lang, config)
    # 4. Generate sitemap
    generate_sitemap(config)
    # 5. (Optional) Ping Google Index
    if config.get("google_indexing_api_key"):
        ping_google_index(config)
    logger.log("All done!")

if __name__ == "__main__":
    main()