from sys import stdin

def image_to_points(img: str) -> list:
    img = img.split('\n')
    rows = list(range(len(img)-1))
    columns = list(range(len(img[0])-1))
    points = []

    for r in rows:
        for c in columns:
            if img[r][c] != ".":
                points.append((img[r][c], r, c))

    points.sort(key=lambda x: x[0])

    return points

def solution(image: str) -> str: 
    points = image_to_points(image)

    for i in range(len(points)-1):
        p1 = points[i]
        p2 = points[i+1]
        if p1[1] == p2[1]:
            for j in range(p1[2]+1, p2[2]):
                if image[p1[1]][j] != ".":
                    image[p1[1]][j] = "+"
                else:
                    image[p1[1]][j] = "-"
        else:
            for j in range(p1[1]+1, p2[1]):
                if image[j][p1[2]] != ".":
                    image[j][p1[2]] = "+"
                else:
                    image[j][p1[2]] = "|"

    print(points)
    return image

images = [] 
image = ""
for line in stdin:  
    if line != "\n":
        line.rstrip()
        image += line
    else:
        images.append(image)
        image = ""
images.append(image)

for image in images:
    print("\n".join(image)) 

def tests():
    print(solution(images[0]))

tests()