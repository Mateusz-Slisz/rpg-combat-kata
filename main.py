from character.entity import Character
from character.type import CharacterType
from fighting.action import deal_damage
from vegetation.entity import Vegetation
from vegetation.type import VegetationType

if __name__ == "__main__":
    c = Character(character_type=CharacterType.MELEE)
    c2 = Character(character_type=CharacterType.MELEE)
    tree = Vegetation(vegetation_type=VegetationType.TREE, max_health=1000)

    print(f"Fight! {c.__class__.__name__} vs {tree._vegetation_type.value}")
    print(f"{tree.health=}")
    print("Fighting...")
    deal_damage(c, tree, power=100)
    print(f"{tree.health=}")

    print(f"Fight! {c.__class__.__name__} vs {c2.__class__.__name__}")
    print(f"{c2.health=}")
    print("Fighting...")
    deal_damage(c, c2, power=100)
    print(f"{c2.health=}")
