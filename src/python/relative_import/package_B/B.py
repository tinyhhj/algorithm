print('__name__',__name__,'__package__',__package__)

import main
msg = main.setname(__name__)

msg('..main')
msg('..D')
msg('.AA','package_A.package_AA')
