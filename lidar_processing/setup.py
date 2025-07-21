from setuptools import setup

package_name = 'lidar_processing'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your_email@example.com',
    description='LiDAR cropping node',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            'lidar_cropper = lidar_processing.lidar_cropper:main',
        ],
    },
)
