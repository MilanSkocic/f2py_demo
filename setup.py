from setuptools import find_packages
import numpy
from numpy.distutils.core import Extension, setup

fib_c_ext = Extension(name="example.fib_c",
                      sources=["./example/src/_fib.c", "./example/src/fib.c"],
                      include_dirs=[numpy.get_include()],
                      define_macros=[('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')])

fib_fortran_ext = Extension(name="example.fib_f90",
                            sources=["./example/src/fib.f90"],
                            include_dirs=[numpy.get_include()],
                            define_macros=[('NPY_NO_DEPRECATED_API', 'NPY_1_7_API_VERSION')])

setup(
    name="C and Fortran Extension Demo",
    version="1.0",
    packages=find_packages(),
    include_package_data=True,
    ext_modules=[fib_fortran_ext, fib_c_ext]
)
