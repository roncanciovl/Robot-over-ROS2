from setuptools import setup

package_name = 'ivan_pkg'

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
    maintainer='ivan',
    maintainer_email='ivany7709@gmail.com',
    description='TODO: Package description',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
                'talker = ivan_pkg.my_pub:main',
                'listener = ivan_pkg.my_sub:main',
                'RPM = ivan_pkg.rpm_publisher:main',
                'my_node = ivan_pkg.lineal_speed:main',
                'image = ivan_pkg.client:main',
                
        ],
},

)
