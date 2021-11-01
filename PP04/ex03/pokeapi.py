import requests
import random


class PokeWiki:
    def __init__(self):
        self.POKEMON_API_URL: str = "https://pokeapi.co/api/v2"

    def fetch_pokemon_info(self, pokemon_name_or_num) -> dict:
        r = requests.get(f"{self.POKEMON_API_URL}/pokemon/{pokemon_name_or_num}")
        r.raise_for_status()
        return r.json()

    def _fetch_pokemon_species(self, pokemon_no) -> dict:
        r = requests.get(f"{self.POKEMON_API_URL}/pokemon-species/{pokemon_no}")
        r.raise_for_status()
        return r.json()

    def get_species(self, name: str) -> str:
        try:
            name_stripped = name.strip()
            if name_stripped == "":
                return None

            poke_info = self.fetch_pokemon_info(name_stripped)
            pokemon_no = poke_info["id"]
            poke_species_info = self._fetch_pokemon_species(pokemon_no)
            genera = poke_species_info["genera"]
            species = [
                genus["genus"] for genus in genera if genus["language"]["name"] == "en"
            ][0]
            return species
        except requests.RequestException as e:
            print(e)
            return None

    def get_abilities(self, name: str) -> str:
        try:
            name_stripped = name.strip()
            if name_stripped == "":
                return []

            poke_info = self.fetch_pokemon_info(name_stripped)
            abilities_dicts = poke_info["abilities"]
            return [
                abilities_dict["ability"]["name"] for abilities_dict in abilities_dicts
            ]
        except requests.RequestException as e:
            print(e)
            return []

    def random_pokemon_name(self: str) -> str:
        try:
            poke_info = self.fetch_pokemon_info(random.randrange(1, 899))
            return poke_info["name"]
        except requests.RequestException as e:
            print(e)

