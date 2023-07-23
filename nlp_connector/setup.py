from setuptools import setup

package_name = 'nlp_connector'

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
    maintainer='jomsuppakit',
    maintainer_email='6438232221@student.chula.ac.th',
    description='NLP connector for ROS2<',
    license='s',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': ['nlp_connector = nlp_connector.nlp_connector_server:main',
                            'test_send_request = nlp_connector.nlp_connector_client:main'
        ],
    },
)
