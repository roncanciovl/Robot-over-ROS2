from setuptools import setup

import os
from glob import glob
from setuptools import setup
from setuptools import find_packages

package_name = 'modelo_robot'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        #COLOQUE NUEVO 
        #('share/' + package_name, package_files),
        #('share/' + package_name + '/launch', package_files),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        #######nuevo_robot
        (os.path.join('share', package_name, 'urdf'), glob('urdf/*')),
        (os.path.join('share', package_name, 'meshes'), glob('meshes/*')),
        (os.path.join('share', package_name, 'worlds'), glob('worlds/*')),

    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='z3rn291',
    maintainer_email='u7003510@unimilitar.edu.co',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'F = modelo_robot.Perras:main',
            'L = modelo_robot.P_reci:main',



        ],
    },
)
