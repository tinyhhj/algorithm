print('__name__',__name__,'__package__',__package__)

# https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time/14132912#14132912
# script vs module

# 파이썬은 파일을 로드할때 두가지 방법으로 로드할 수 있다. "스크립트 혹은 모듈"
# 스크립트는 cli에서 "python script.py"라고 실행시킬 때 첫 진입점이 되는 파일이자 top-level script로 단 하나만 존재한다.
# 모듈의 경우 다른 모듈에 의해 import 되거나, python -m 옵션으로 로딩이 가능하다.
# 네이밍
# 모듈을 로딩할때 모듈의 이름과 패키지 정보를 각각 __name__과 __package__에 담는다.
# top-level script의 경우 name은 __main__, package는 None
# 모듈의 경우 name은 모듈명은 파일명, package는 해당 모듈의 패키지명이 된다. (A 의경우 package_A 단, cli에서 직접 A를
# 호출한다면 top-level-script가 되므로 name은 __main__, package는 None이 된다.)
# 즉 프로그램 진입점이 되는 top-level-script가 top-level-package가 되는것이고, 모듈명에 .(dot)이 없다면 패키지의 일부인것이다.

# relative import
# relative package는 모듈의 __name__과 __package__의 정보를 기반으로 상대경로를 찾는다
# 즉, top-level-script이거나 top-level-script와 같은 패키지를 공유하는 모듈인 경우 상대경로 임포팅이 되지 않는것이다.
# (사실 생각해보면 top-level-package를 임포팅하기 위해서는 절대경로 임포팅을 사용하면 된다
import importlib
def setname(name):
    import warnings
    def pprint(module,package=None):
        try:
            importlib.import_module(module,package)
        except:
            warnings.warn(f'{f"from {package}" if package is not None else ""} import module {module} can`t import from {name}')
    return pprint


msg =setname(__name__)
msg('D')
msg('.D')
msg('package_A.A')
msg('package_B.B')
msg('package_A.package_AA.AA')

