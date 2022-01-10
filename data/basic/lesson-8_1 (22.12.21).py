# def name(name):
#     print(name.title())
#     return name.title()

# def name(*name):
#     print(name)
#     return list(map(lambda x: x.title(), name))

def name(**name):
    # for k, v in name.items():
    #     for c in v:
    #         name.update(c.title())
    return name

# changed_name = name('adilet', 'azim', 'tilek')
changed_name = name(first='adilet', second='azim', third='tilek')
# name('azat')
print(changed_name)





