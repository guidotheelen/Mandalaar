from lxml import etree
from io import StringIO, BytesIO
from random import randint
import fire
import math

xml = '<svg version="1.1" id="Layer_1" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" x="0px" y="0px" viewBox="0 0 100 100" enable-background="new 0 0 100 100" xml:space="preserve"><polygon points="50,52.455 47.165,47.545 52.835,47.545"/></svg>'
tree = etree.parse(StringIO(xml))
svg = tree.getroot()
point_list = [[50000, 52455], [47165, 47545], [52835, 47545]]

x_unit = 2835
y_unit = 4910

def random_color():
    color_list = ["black", "white"]
    random_number = randint(0, len(color_list)-1)
    random_color = color_list[random_number]
    return random_color

def group(number):
    s = '%d' % number
    groups = []
    while s and s[-1].isdigit():
        groups.append(s[-3:])
        s = s[:-3]
    return s + '.'.join(reversed(groups))

def main():
    point_1x = group(point_list[0][0])
    point_1y = group(point_list[0][1])
    point_2x = group(point_list[1][0])
    point_2y = group(point_list[1][1])
    point_3x = group(point_list[2][0])
    point_3y = group(point_list[2][1])
    point_string = f"{point_1x},{point_1y} {point_2x},{point_2y} {point_3x},{point_3y}"

    triangle_group = etree.Element("group")

    for x in range(1, 9):
        if x % 2 == 0:
            poligon = etree.Element("polygon", points=f"{point_string}", transform=f"translate(0,{group(-y_unit*x)}) scale(1, 1)")
            triangle_group.append(poligon)
            for y in range(x+1):
                if y % 2 == 0:
                    poligon = etree.Element("polygon", points=f"{point_string}", transform=f"translate({group(x_unit*y)},{group(-y_unit*x)}) scale(1, 1)")
                    triangle_group.append(poligon)
                    poligon = etree.Element("polygon", points=f"{point_string}", transform=f"translate({group(-x_unit*y)},{group(-y_unit*x)}) scale(1, 1)")
                    triangle_group.append(poligon)
                else:
                    poligon = etree.Element("polygon", points=f"{point_string}", transform=f"translate({group(x_unit*y)},{group(100000-y_unit*x)}) scale(1, -1)")
                    triangle_group.append(poligon)
                    poligon = etree.Element("polygon", points=f"{point_string}", transform=f"translate({group(-x_unit*y)},{group(100000-y_unit*x)}) scale(1, -1)")
                    triangle_group.append(poligon)
        else:
            poligon = etree.Element("polygon", points=f"{point_string}", transform=f"translate(0,{group(100000-y_unit*x)}) scale(1,-1)")
            triangle_group.append(poligon)

            for y in range(x+1):
                if y % 2 == 0:
                    poligon = etree.Element("polygon", points=f"{point_string}", transform=f"translate({group(x_unit*y)},{group(100000-y_unit*x)}) scale(1, -1)")
                    triangle_group.append(poligon)
                    poligon = etree.Element("polygon", points=f"{point_string}", transform=f"translate({group(-x_unit*y)},{group(100000-y_unit*x)}) scale(1, -1)")
                    triangle_group.append(poligon)
                else:
                    poligon = etree.Element("polygon", points=f"{point_string}", transform=f"translate({group(x_unit*y)},{group(-y_unit*x)}) scale(1, 1)")
                    triangle_group.append(poligon)
                    poligon = etree.Element("polygon", points=f"{point_string}", transform=f"translate({group(-x_unit*y)},{group(-y_unit*x)}) scale(1, 1)")
                    triangle_group.append(poligon)

    svg.append(triangle_group)

    svg_file = open("Output.svg", "w")
    svg_file.write(etree.tostring(svg).decode("utf-8"))
    svg_file.close()


if __name__ == '__main__':
  fire.Fire()
