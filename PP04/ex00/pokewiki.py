import requests


class PokeWiki:
    def fetch_page(self, pokemon_name):
        POKEMON_WIKI_URL = "https://pokemon.fandom.com/wiki"
        r = requests.get(f"{POKEMON_WIKI_URL}/{pokemon_name}", timeout=10)
        return r.text

    def get_species(self, name):
        page = self.fetch_page(name)  # fetch page

        sliced = page[page.find('data-source="species"') :]
        splitted_lines = sliced.splitlines()

        for line in splitted_lines:
            stripped = line.strip()
            if stripped.startswith("<div "):

                return stripped[stripped.find(">") + 1 : stripped.find("</div>")]
        return None

    def get_abilities(self, name):
        page = self.fetch_page(name)  # fetch page

        sliced = page[page.find('data-source="ability"') :]
        splitted_lines = sliced.splitlines()

        for line in splitted_lines:
            stripped = line.strip()
            if stripped.startswith("<div "):

                extracted = [
                    text[: text.find("</a>")]
                    for text in stripped.split("<a ")
                    if text.startswith("href=")
                ]
                return [x[x.find(">") + 1 :] for x in extracted]

        return []

