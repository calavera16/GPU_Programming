import numpy as np
from time import time
import matplotlib
from matplotlib import pyplot as plt

matplotlib.use("AGG")


def simple_mandelbrot(
    width, height, real_low, real_high, imag_low, imag_high, max_iters
):
    real_vals = np.linspace(real_low, real_high, width, dtype=np.float64)
    imag_vals = np.linspace(imag_low, imag_high, height, dtype=np.float64)

    mandelbrot_graph = np.ones((height, width), dtype=np.float32)

    # 2. Iterate over each pixel/point
    for x in range(width):
        for y in range(height):
            c = np.complex64(real_vals[x] + imag_vals[y] * 1j)
            z = np.complex64(0)
            for i in range(max_iters):
                z = z**2 + c
                if np.abs(z) > 2:
                    mandelbrot_graph[y, x] = 0
                    break
    return mandelbrot_graph


if __name__ == "__main__":
    t1 = time()
    mandel = simple_mandelbrot(512, 512, -2, 2, -2, 2, 256)
    t2 = time()
    mandel_time = t2 - t1
    fig = plt.figure(1)
    plt.imshow(mandel, extent=(-2, 2, -2, 2), cmap="hot")
    t3 = time()
    plt.savefig("mandelbrot.png", dpi=fig.dpi)
    t4 = time()
    dump_time = t4 - t3
    print("It took {} seconds to calculate the Mandelbrot graph".format(mandel_time))
    print("It took {} seconds to dump the image.".format(dump_time))
