import requests
from bs4 import BeautifulSoup
import random


class PokeWiki:
    def fetch_page(self, pokemon_name):
        POKEMON_WIKI_URL = "https://pokemon.fandom.com/wiki"
        r = requests.get(f"{POKEMON_WIKI_URL}/{pokemon_name}", timeout=10)
        return r.text

    def get_species(self, name):
        html_str = self.fetch_page(name)  # fetch pokemon page
        soup = BeautifulSoup(html_str, "html.parser")
        div_tag = soup.select_one("div[data-source='species'] > div")

        if div_tag is None:
            return None

        species = div_tag.string
        return species

    def get_abilities(self, name):
        html_str = self.fetch_page(name)  # fetch pokemon page
        soup = BeautifulSoup(html_str, "html.parser")
        a_list = soup.select("div[data-source='ability'] > div > a")

        abilities = [a.string for a in a_list]
        return abilities

    def random_pokemon_name(self):
        html_str = self.fetch_page("List_of_Pokémon")  # fetch pokemon list page
        soup = BeautifulSoup(html_str, "html.parser")
        pokemon_list = soup.select("table.wikitable tr td:nth-child(3) a")
        max = len(pokemon_list)
        random_number = random.randrange(max)

        pokemon_name = pokemon_list[random_number].string
        return pokemon_name

