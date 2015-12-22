# -*- coding: utf-8 -*-

"""Python lib to print QR Platba (czech payment QR code) for fpdf users.
This is alternative to the qrplatba module.
install_requires = ['wfpdf', 'pyqrcode']   # wfpdf requires fpdf

Usage:
See qrplatba() method doc.
For the example see script call bellow (if __name__ == '__main__':).
"""

from datetime import date
import os
import tempfile

import pyqrcode   # pip install pyqrcode
from wfpdf import PDF


def qrplatba(pdf,
             IBAN, castka=None, mena='CZK', splatnost=None, msg=None, KS='0558', VS='', SS=None, IBAN2=None,
             w=36, x=None, y=None, **payment_more):
    """This is the main method which generates the QR platba code.
    pdf - object from: with PDF(<outputfilename>) as pdf:
        (we use wfpdf (which is really minor wrapper),
        we haven't not tested the calling with fpdf directly, but maybe it is easy)
    IBAN..IBAN2 - ACC, AM, CC, DT, MSG, X-KS, X-VS, X-SS, ALT-ACC attributes of payment
    w - width [mm] of the generated image (real width is a little bigger thanks to lines and 'QR platba' label)
    code is printed at current position (if not defined using x,y)
        current position moves to the end of 'QR platba' label
    **payment_more - any other payment attributes (key=value will generate *key:value , '_' in key changes to '-')
    """
    if x is None:
        x = pdf.get_x()
    if y is None:
        y = pdf.get_y()

    qr = 'SPD*1.0*ACC:' + IBAN
    if IBAN2:
        qr += '*ALT-ACC:' + IBAN2
    if castka:
        qr += '*AM:'
        try:
            qr += '%.2f' % castka
        except TypeError:
            qr += castka
    if mena:
        qr += '*CC:' + mena
    if splatnost:
        qr += '*DT:'
        try:
            qr += splatnost
        except TypeError:
            qr += date.strftime(splatnost, '%Y%m%d')
    if msg:
        qr += '*MSG:' + msg
    if KS:
        qr += '*X-KS:' + KS
    if VS:
        qr += '*X-VS:' + VS
    if SS:
        qr += '*X-SS:' + SS
    for key in payment_more:
        qr += '*%s:' % key.replace('_', '-') + payment_more[key]

    png, pixels = getQRCode(qr)
    # as long as we generate qr code with scale=1 w/pixels is module size in [mm]:
    module_size = 1.0 * w / pixels
    # for the line around we add 1* module_size to sure have good quiet zone
    pdf.image(png, x=x + module_size, y=y + module_size, w=w, type='png')
    os.unlink(png)

    pdf.set_font_size(6)
    # pdf.set_font('', style='B')  # we don't set this here
    pllbl = 'QR platba'
    pllbl_w = pdf.get_string_width(pllbl)
    # some positions in next code were corrected (+-module_size) to obtain good result
    pllbl_right = x + pllbl_w + 7 * module_size
    square_size = w + 2 * module_size
    pdf.line(x, y, x + square_size, y)                                        # top
    pdf.line(x, y, x, y + square_size)                                        # left
    pdf.line(x + square_size, y, x + square_size, y + square_size)            # right
    pdf.line(x, y + square_size, x + 2 * module_size, y + square_size)        # bottom before
    pdf.line(pllbl_right, y + square_size, x + square_size, y + square_size)  # bottom after
    pdf.set_xy(x + 3 * module_size, y + square_size)
    pdf.cell(pllbl_w, h=2, txt=pllbl)

def getQRCode(txt):
    qrc = pyqrcode.create(txt)
    fullname = getTemppngName()
    qrc.png(fullname)    # requires pypng installed
    return fullname, qrc.get_png_size()

def getTemppngName():
    with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as f:
        return f.name


if __name__ == '__main__':
    IBAN = 'CZ6255000000000001234567'
    castka = 2499

    with PDF('test_qrplatba.pdf') as pdf:
        pdf.set_font('', style='B')
        qrplatba(pdf, IBAN, castka=2499)
        qrplatba(pdf, IBAN, castka='249.00', mena='USD', VS='2015111', msg='Smith J.', w=30, x=20, y=60,
                 X_URL='HTTP://WWW.SOMEURL.COM/')
