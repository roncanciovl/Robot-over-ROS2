from setuptools import setup
import os
from glob import glob

package_name = 'willy_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        (os.path.join('share', package_name), glob('launch/*launch.[pxy][yma]*')),
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='willy',
    maintainer_email='wrojaszabala@gmail.com',
    description='TODO: Package description',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'talker = willy_pkg.publisher_member_function:main',
                'listener = willy_pkg.subscriber_member_function:main',
                'lineal_speed = willy_pkg.lineal_speed:main',
                'client = willy_pkg.Client_photo:main',
                'server = willy_pkg.Server_photo:main'
        ],
},
)