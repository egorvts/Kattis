height, width, kernel_height, kernel_width = map(int, input().split())

image = []
kernel = []


def kernel_to_list(kernel: list) -> list:
    result = []
    for k in kernel:
        result.extend(k)

    return result


def solution(image: list, kernel: list) -> list:

    for i in range(height):
        image.append(list(map(int, input().split())))

    for i in range(kernel_height):
        inp = list(map(int, input().split()))
        inp.reverse()
        kernel.insert(0, inp)

    kernel = kernel_to_list(kernel)

    result = []

    for i in range(height-kernel_height+1):
        row = []
        for j in range(width-kernel_width+1):
            image_part = []

            for k in range(i, i+kernel_height):
                image_part += image[k][j:j+kernel_width]

            for k in range(len(kernel)):
                image_part[k] *= kernel[k]

            row.append(sum(image_part))
        result.append(row)

    return result


for s in solution(image, kernel):
    print(*s)
