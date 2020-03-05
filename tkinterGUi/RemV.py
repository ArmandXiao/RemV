

from myPackage.__main__ import main

if __name__ == '__main__':
    # 需要在 powershell环境下运行
    import os
    os.chdir(os.getcwd())
    main()