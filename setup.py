from setuptools import setup

setup(name='test_package',
      version='0.1',
      description='A library to investigate the data and provide necessary EDA information.',
      url='https://github.com/lnorouzi-pk/test_package',
      author='Leila Norouzi',
      author_email='lnorouzi@prokarma.com',
      license='MIT',
      packages=['test_package'],
      install_requires=[
            'numpy',
            'pandas',
            'matplotlib',
            'seaborn'

      ],
      classifiers=[
        'Programming Language :: Python :: 3.6',
      ],
      include_package_data=True,
      test_suite='nose.collector',
      tests_require=['nose'],
      zip_safe=False)