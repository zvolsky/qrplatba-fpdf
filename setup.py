from distutils.core import setup
setup(
  name = 'qrplatba-fpdf',
  py_modules = ['qrplatba_fpdf'],
  version = '0.9.2',
  description = 'Another approach to print QRPlatba QR code, using fpdf/wfpdf/pyqrcode',
  install_requires = ['wfpdf', 'pyqrcode'],
  author = 'Mirek Zvolsky',
  author_email = 'zvolsky@seznam.cz',
  url = 'https://github.com/zvolsky/qrplatba-fpdf',
  download_url = 'https://github.com/zvolsky/qrplatba-fpdf/tarball/0.9.2',
  keywords = ['qr', 'qrplatba', 'qr code', 'qr platba'],
  classifiers=[
      'Development Status :: 5 - Production/Stable',
      'Topic :: Office/Business :: Financial :: Accounting',
      'Intended Audience :: Developers',
      'Intended Audience :: Financial and Insurance Industry',
      'License :: OSI Approved :: MIT License',
      'Operating System :: OS Independent',
      'Programming Language :: Python',
      'Topic :: Software Development',
      'Programming Language :: Python :: 2',
  ],
)
