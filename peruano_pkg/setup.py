from setuptools import setup
import os
from glob import glob
from setuptools import setup
from setuptools import find_packages

package_name = 'peruano_pkg'

package_files = [
    'launch/Tarea.launch.py',
    'launch/Nodos.launch.py',
]
####
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
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='jackson',
    maintainer_email='jdicano1319@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = peruano_pkg.jack_pub:main',
            'listener = peruano_pkg.jack_sub:main',
            'rpm = peruano_pkg.T_PubRpm:main',
            'suppub = peruano_pkg.T_PubSub:main',
            'linspeed = peruano_pkg.T_LinSpeed:main',
            'penviar = peruano_pkg.P_EnviarFoto:main',
            'precibir = peruano_pkg.P_RecibirFoto:main',
        ],
        
    },
)
