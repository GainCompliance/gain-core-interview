class Meta:
    specific = {
        "P2020": ("QWERTY", 2, 5),
        "P2021": ("DVORAK", 4, 3),
        "L2020": ("QWERTZ", 2, 2),
        "L2020": ("COLEMAK", 5, 1),
    }

    sections = [("AZERTY", 1, 5), ("MALTRON", 3, 2), ("JCUKEN", 3, 5)]

    @classmethod
    def get_def_codes(cls):
        return ["P2020", "P2021", "L2020", "L2021"]

    @classmethod
    def get_structure(cls, def_code):
        ret = {}
        for section in cls.sections:
            ret[section[0]] = {"x": section[1], "y": section[2]}
        ret[cls.specific[def_code][0]] = {"x": cls.specific[def_code][1], "y": cls.specific[def_code][2]}
        return ret


if __name__ == "__main__":
    import pdb

    pdb.set_trace()
