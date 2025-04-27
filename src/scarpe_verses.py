import os
import shutil

import requests
import bs4

verse_count = 40
verse_base_url_template = "https://mek.oszk.hu/05500/05570/html/jozsef_attila"
save_folder = "verses"
# verse_source_encoding = "iso-8859-2"


def setup_directory():
    if os.path.exists(save_folder):
        shutil.rmtree(save_folder)
    os.makedirs(save_folder)


def scrape_verses():
    all_verses = []

    for i in range(1, verse_count + 1):
        verse_padded_number = str(i).zfill(4)
        verse_url = f'{verse_base_url_template}{verse_padded_number}.html'
        print(f'Scraping verse #{i} at "{verse_url}"')
        page_content = get_url_as_utf8(verse_url)
        verse_content = fix_characters(scrape_verse(page_content))
        all_verses.append(verse_content)

        verse_save_path = os.path.join(save_folder, f'verse_{verse_padded_number}.txt')
        with open(verse_save_path, 'w', encoding='utf-8') as verse_file:
            verse_file.write(verse_content)
            print(f'Saved verse #{i} at "{verse_save_path}"')

    all_verses_save_path = os.path.join(save_folder, 'all_verses.txt')
    with open(all_verses_save_path, 'w', encoding='utf-8') as verses_file:
        verses_file.write('\n\n'.join(all_verses))
        print(f'Saved all joined verses at "{all_verses_save_path}"')


def get_url_as_utf8(verse_url) -> str:
    response = requests.get(verse_url, headers={'User-Agent': 'Mozilla/5.0'})
    return response.text


def scrape_verse(page_content):
    soup = bs4.BeautifulSoup(page_content, features="html.parser")
    return soup.body.get_text(' ', strip=True)


def fix_characters(verse_content):
    return (verse_content.replace('õ', 'ő')
                    .replace('Õ', 'Ő')
                    .replace('û', 'ű')
                    .replace('Û', 'Ű'))


if __name__=="__main__":
    setup_directory()
    scrape_verses()