from setuptools import setup
import pathlib
import pkg_resources


# with pathlib.Path('requirements.txt').open() as requirements_txt:
#     install_requires = [
#         str(requirement)
#         for requirement
#         in pkg_resources.parse_requirements(requirements_txt)
#     ]

setup(
    name='yolov5_crowdhuman',
    author='vshokorov',
    author_email='some_mail@gmail.com',
    url="",
    version='0.0.1',
    install_requires=[
        'numpy',
    ],
    py_modules=["yolov5_crowdhuman"]
#     install_requires=install_requires,
)
