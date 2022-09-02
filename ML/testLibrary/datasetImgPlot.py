from scipy.io import loadmat
import matplotlib.pyplot as plt

mnist_rawFile = loadmat("C:\PythonProject\ML\dataset\mnist-original.mat")

mnist = {
    "data": mnist_rawFile["data"].T,
    "target": mnist_rawFile["label"][0]
}
x, y = mnist["data"], mnist["target"]

for i in range(100):
    number = x[i]
    number_image = number.reshape(28, 28)
    print(y[i])
    plt.imshow(
        number_image,
        cmap=plt.cm.binary,
        interpolation="nearest"
    )
    plt.show()

    print(mnist["data"])
