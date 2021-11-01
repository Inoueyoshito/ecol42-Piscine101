from pokewiki import PokeWiki
from requests.exceptions import RequestException


def main():
    print("---pokemon * 2---")
    test_pokemon("bulbasaur")
    test_pokemon("ditto")
    print("---no such pokemon---")
    test_pokemon("no such pokemon")
    test_pokemon("")
    print("---random * 3---")
    for _ in range(3):
        test_pokemon()


def test_pokemon(name="random"):
    try:
        p = PokeWiki()
        if name == "random":
            name = p.random_pokemon_name()

        print(f"name : {name}")
        print(f"species : {p.get_species(name)}")
        print(f"abilities : {p.get_abilities(name)}")
        print()
    except RequestException as e:
        print(e)


if __name__ == "__main__":
    main()
