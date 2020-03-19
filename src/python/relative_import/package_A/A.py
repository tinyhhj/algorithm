print('__name__',__name__,'__package__',__package__)

import main
msg = main.setname(__name__)
msg('..D')
msg('..main')
msg('..package_B.B')
msg('.AA','package_A.package_AA')

msg('D')
msg('main')
msg('package_B.B')
msg('package_AA.AA')




