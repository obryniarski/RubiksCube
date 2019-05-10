

def assert_matching_dimensions(s1, s2, s3, s4, s5, s6):
    # size = len(s1)
    # sides = [s1, s2, s3, s4, s5, s6]
    # for side in sides:
    #     assert len(side) == size, "side arrays have differing dimensions"
    #     for i in range(size):
    #         assert len(side[i]) == size, "side arrays have differing dimensions"
    base_dimension = s1.dimension
    sides = [s1, s2, s3, s4, s5, s6]
    for side in sides:
        assert side.dimension == base_dimension, "not all sides have the same dimension"

