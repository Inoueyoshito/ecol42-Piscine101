from pokewiki import PokeWiki
from requests.exceptions import RequestException


def main():
    test_pokemon("bulbasaur")
    test_pokemon("ditto")
    test_pokemon("pikachu")
    test_pokemon("snorlax")
    test_pokemon("no such pokemon")
    test_pokemon("")


def test_pokemon(name):
    try:
        p = PokeWiki()

        print(f"name : {name}")
        print(f"species : {p.get_species(name)}")
        print(f"abilities : {p.get_abilities(name)}")
        print()
    except RequestException as e:
        print(e)


if __name__ == "__main__":
    main()
