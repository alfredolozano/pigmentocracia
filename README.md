# pigmentocracia
Comparison of skin color of different social sectors by analyzing photos to understand racial privilege in Mexico

Deepgaze Prerequisites
------------

The current version of Deepgaze is based on **Python 2.7**, a porting for Python 3.0 has been scheduled for the next year.

To use the libray you have to install:

- Numpy [[link]](http://www.numpy.org/)

```shell
sudo pip install numpy
```

- OpenCV 2.x (not compatible with OpenCV >= 3.x) [[link]](https://opencv.org/releases.html)

```shell
sudo apt-get install libopencv-dev python-opencv
```

- Tensorflow [[link]](https://www.tensorflow.org/)

```shell
sudo pip install tensorflow
```

Some examples may require additional libraries:

- dlib [[link]](http://dlib.net/)

To avoid conflicts, setup a virtual environment:

* Run the following command to setup virtual environment

```sh
virtualenv env
```

* Activate the virtual environment

```sh
source env/bin/activate
```

* Install the project dependencies
