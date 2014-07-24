from distutils.core import setup

import py2app
#init for 
OPTIONS = {
    'argv_emulation':False,
    'includes':[
                "PyQt4.QtCore",
                "PyQt4.QtWidgets",
                "PyQt4.QtGui",
                "sip",
                ]
}

########
# APP = ['appmain/Company.py']
# APP=['crayon/aranduka.py']
#kws...
#init test...
#GITTEST push 3
APP=['company/AppMainComp.py']
setup(
    name='CRPRERP',
    app=APP,
    version='0.1',
    url='',
    license='CrayonSoftware',
    author='kafka',
    author_email='wonsork@gmail.com',
    description='crayon press erp',

    packages=['appmain','company','database'],
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],


)

#
# APP = ['appmain/AppMain.py']
# DATA_FILES = [
#     ('xml',['appmain/xml/examples.xml']),
#     ('images',['appmain/images/demobg.png',
#                'appmain/images/qtlogo_small.png',
#                'appmain/images/trolltech-logo.png'])
# ]
#
#
# setup(
#     app=APP,
#     data_files=DATA_FILES,
#     options={'py2app': OPTIONS},
#     packages=["appmain","company"],
#     # setup_requires=['py2app'],
# )
