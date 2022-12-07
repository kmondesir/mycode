from mtgsdk import Card
from mtgsdk import Set
from mtgsdk import Type
from mtgsdk import Supertype
from mtgsdk import Subtype
from mtgsdk import Changelog

card = Card.find(386616)

def main():
    print(card.name)
    

if __name__ == '__main__':
    main()