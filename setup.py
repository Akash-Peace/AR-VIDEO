import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="arvideo",
    version="0.0.1",
    author="Akash.A",
    author_email="akashcse2000@gmail.com",
    description="Hologram a video in a real-world entity surrounded with ArUco markers.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    url='https://github.com/Akash-Peace',
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    py_modules=["arvideo"],
    package_dir={'':'arvideo'},
    install_requires=['opencv-contrib-python==4.1.0.25', 'numpy']
)