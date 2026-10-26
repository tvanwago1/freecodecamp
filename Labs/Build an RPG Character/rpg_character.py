full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intell, charisma):
    if not isinstance(name, str):
        return 'The character name should be a string'
    elif name == '':
        return 'The character should have a name'
    elif len(name) > 10:
        return 'The character name is too long'
    elif name.count(' ') > 0:
        return 'The character name should not contain spaces'
    else:
        pass

    if not isinstance(strength, int) or not isinstance(intell, int) or not isinstance(charisma, int):
        return 'All stats should be integers'
    elif strength < 1 or intell < 1 or charisma < 1:
        return 'All stats should be no less than 1'
    elif strength > 4 or intell > 4 or charisma > 4:
        return 'All stats should be no more than 4'
    elif strength + intell + charisma != 7:
        return 'The character should start with 7 points'
    else:
        pass
    # stats out of 10
    stre_dot = (full_dot * strength) + (empty_dot * (10 - strength))
    intell_dot = (full_dot * intell) + (empty_dot * (10 - intell))
    charisma_dot = (full_dot * charisma) + (empty_dot * (10 - charisma))

    return f"{name}\nSTR {stre_dot}\nINT {intell_dot}\nCHA {charisma_dot}"

create_character('ren', 4, 2, 1)
print(create_character('ren', 4, 2, 1))