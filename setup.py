

from setuptools import setup, find_packages

setup(
  name = "v1pysdk",
  version = "0.5",  
  description = "VersionOne API client for Python 3",  
  author = "Joe Koberg (VersionOne, Inc.)",
  author_email = "Joe.Koberg@versionone.com",
  license = "MIT/BSD",
  keywords = "versionone v1 api sdk",
  url = "http://github.com/VersionOne/v1pysdk",
  
  packages = [
    'v1pysdk',
    ],
  
  install_requires = [
    'testtools',
    'iso8601',
    'python-ntlm3',
    ],

  python_requires='>=3',

  test_suite = "v1pysdk.tests",
  
  )







