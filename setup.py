from setuptools import setup

package_name = 'dynamic_parameters'

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
    maintainer='Lukas Miller',
    maintainer_email='lukas.miller.95@5outlook.de',
    description='This is a simple example package with a node, which have dynamic parameters, publisher and subscriber',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'dynamic_publisher = dynamic_parameters.dynamic_publisher:main',
            'dynamic_subscriber = dynamic_parameters.dynamic_subscriber:main'
        ],
    },
)
