print('__name__',__name__,'__package__',__package__)

import main

msg = main.setname(__name__)
msg('.main')
msg('.package_A.A')

msg('package_B.B')
msg('package_A.package_AA.AA')