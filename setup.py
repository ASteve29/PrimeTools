from setuptools import setup, Extension
from Cython.Build import cythonize
import sysconfig

# Get standard library path for C++ include directory (optional but robust)
# For example, on some systems, vector might be in a non-standard path.
# This line helps setuptools find the standard C++ library headers.
# std_include_dir = sysconfig.get_path('include') 

extensions = [
    Extension(
        # The name of the resulting Python module (you will `import prime_wrapper` in Python)
        "prime_wrapper",
        # List of source files
        sources=["prime_wrapper.pyx", "prime_utils.cpp"],
        # Specify C++ language
        language="c++",
        # Optional: Compiler arguments, e.g., to use a specific C++ standard
        # extra_compile_args=["-std=c++17"], 
    )
]

setup(
    name="PrimeUtilsCython",
    ext_modules=cythonize(extensions, language_level=3),
    version="1.0",
    author="Your Name"
)
