def capital_str(name):
    if len(name) > 3:
        print(name[:3].capitalize() + name[3:].capitalize())
    else:
        print("nama terlalu pendek")
capital_str("belajar")
