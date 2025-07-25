from setuptools import setup

package_name = 'multi_drone_ctl'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    author='Your Name',
    maintainer='Your Name',
    maintainer_email='you@example.com',
    description='ROS2 node for multi drone control',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            'drone_ctl = multi_drone_ctl.drone_ctl:main'
        ],
    },
)
