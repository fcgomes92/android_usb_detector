from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='android_usb_detector',
      version='0.0.1',
      description='The funniest joke in the world',
      long_description=readme(),
      long_description_content_type="text/markdown",
      url='',
      author='Flying Circus',
      author_email='flyingcircus@example.com',
      license='MIT',
      package_dir={"": "src"},
      packages=setuptools.find_packages(where="src"),
      zip_safe=False,
      scripts=['bin/android_usb_detector'],
      include_package_data=True,
      install_requires=[
          'pyudev',
          'paho-mqtt'
      ])
