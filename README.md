# qrplatba-fpdf
Another approach to print QRPlatba QR code, using fpdf/wfpdf/pyqrcode

This is alternative to the qrplatba module.

```
install_requires = ['wfpdf', 'pyqrcode']   # wfpdf requires fpdf
```

- 0.9.1 PyPI published

## Usage:
```
from wfpdf import PDF
from qrplatba_fpdf import qrplatba

with PDF('test_qrplatba.pdf') as pdf:
    pdf.set_font('', style='B')
    qrplatba(pdf, IBAN, castka=2499)
```

See qrplatba() method doc for more parameters.
For the example see script call in qrplatba_fpdf.py (if __name__ == '__main__':).
