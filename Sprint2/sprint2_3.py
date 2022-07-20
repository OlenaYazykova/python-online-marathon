import re


def figure_perimetr(coord):
    coord_point=[['LB'], ['RB'], ['LT'], ['RT']]
    perim=0
    for i in range(len(coord_point)):
        x=r'#{}([0-9]+):'.format(coord_point[i][0])
        y=r'#{}[0-9]+:([0-9]+)'.format(coord_point[i][0])
        coord_point[i].append([float(re.search(x,coord).group(1)), float(re.search(y,coord).group(1))])
    for i in range(len(coord_point)):
        for j in coord_point[i][0]:
            for k in range(i+1, len(coord_point)):
                if j in coord_point[k][0]:
                    perim+=((coord_point[k][1][0]-coord_point[i][1][0])**2+(coord_point[k][1][1]-coord_point[i][1][1])**2)**(1/2)
    return perim


coord="#LB0:1#RB5:1#LT4:5#RT8:3"
print(figure_perimetr(coord))
