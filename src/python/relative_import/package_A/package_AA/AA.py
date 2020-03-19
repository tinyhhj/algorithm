print('__name__',__name__,'__package__',__package__)

import main
msg = main.setname(__name__)

msg('..A')
msg('..package_B.B')
msg('..package_AA.AA')


msg('D')
msg('main')
msg('package_B.B')
msg('package_AA.AA')