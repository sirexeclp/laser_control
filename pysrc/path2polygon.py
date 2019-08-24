from svg.path import parse_path
import numpy as np
from numpy.linalg import norm


def find_angle(p0, p1, c):
    p0c = norm(c - p0)  # p0->c (b)
    p1c = norm(c - p1)  # p1->c (a)
    p0p1 = norm(p1 - p0)  # p0->p1 (c)
    return np.arccos((p1c * p1c + p0c * p0c - p0p1 * p0p1) / (2 * p1c * p0c))


def is_corner(last_point, middle_point, first_point):
    return (np.pi - find_angle(last_point, first_point, middle_point)) > 0.5


def c2t(c: complex):
    return c.real, c.imag


def c2a(c: complex):
    return np.array(c2t(c))


def path2polygonPoints(path, step):
    path = parse_path(path)
    corner_count = 0
    points = []
    path_length = path.length()
    last_point = None
    last_last_point = None
    count = 0
    last_was_corner = False

    # step through path in small steps
    for i in np.arange(0, path_length, 0.5):
        relative_position = i / path_length
        point = c2a(path.point(relative_position))  # convert complex number to tuple
        # at corners, always push multiple points
        if count > 2 and not last_was_corner and is_corner(point, last_point, last_last_point):
            corner_count += 1
            points.append(last_last_point)
            points.append(last_point)
            points.append(point)
            last_was_corner = True
        else:
            last_was_corner = False
            # at non-corners push only on sample step
            if count % step == 0:
                points.append(point)
        count += 1
        last_last_point = last_point
        last_point = point

    # always push last point
    points.append(c2a(path.point(1)))
    return points


def print_samples(points, name="test"):
    left_most_x = np.min(points, axis=0)[0]
    right_most_x = np.max(points, axis=0)[0]

    output = f"int {name}[] = {{"
    output += ", ".join([f"Point({(point[0] * 25):.0f}, {(point[1] * 25):.0f})" for point in points])
    output += f"}};\n"
    output += f"addToPointLibrary(\"{name}\", {name}, (sizeof({name})/sizeof(*{name})), "
    output += f"{(left_most_x * 100):.0f}, {(right_most_x * 100):.0f} ); //{len(points)} points"
    return output


if __name__ == "__main__":
    points = path2polygonPoints(
        """M 34.617417,71.75 34.5,4.8522527 C 52.261339,3.5455972 67.416136,2.6942001 65.808439,23.35372 64.952019,34.359041 57.615914,40.960017 42.78125,40.8125"""
        , 13)
    print(points)
    result = print_samples(points, "charP")
    print(result)
    expected = """int charP[] = 
	{Point(865, 1794), Point(865, 1631), Point(865, 1469), Point(865, 1306), 
	Point(864, 1144), Point(864, 981), Point(864, 819), Point(863, 656), 
	Point(863, 494), Point(863, 331), Point(863, 169), Point(863, 131), 
	Point(865, 121), Point(878, 120), Point(977, 113), Point(1140, 107), 
	Point(1302, 115), Point(1458, 156), Point(1583, 257), Point(1640, 408), 
	Point(1646, 570), Point(1615, 729), Point(1531, 867), Point(1400, 961), 
	Point(1245, 1007), Point(1083, 1020), Point(1070, 1020)};
	addToPointLibrary("charP", charP, (sizeof(charP)/sizeof(*charP)), 3450, 6585); //27 points"""
    #assert result.strip() == expected.strip(), "result does not match expected output"

