from setuptools import setup
#######
from glob import glob
import os
##########


package_name = 'Reyes_Pa'
#############
package_files = [
    'launch/Prueba.launch.py'
    'Union_launch.py'
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
        #('share/' + package_name + '/launch', package_files)
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        #######
    
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
            'talker = Reyes_Pa.Fino:main',
            'RPM = Reyes_Pa.T1_PubRPM:main',
            'SupPub = Reyes_Pa.T1_PubSub:main',
            'LinSpeed = Reyes_Pa.T1_SubLinSpeed:main',
            'hola = Reyes_Pa.Prueba:main',
        ],
        
    },
)



