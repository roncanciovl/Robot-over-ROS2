from setuptools import setup

package_name = 'raul_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='raul',
    maintainer_email='alvaroraulurdanetag@gmail.com',
    description='TODO: Package description',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'talker = raul_pkg.pub_raul:main',
                'listener = raul_pkg.sub_raul:main',
                'rpm2ls = raul_pkg.rpm2ls:main',
                'rpmpub = raul_pkg.pub_rpm:main'
        ],
    },
)
