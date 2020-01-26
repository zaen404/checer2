import sys
try:
    import os
    import platform
    detect_os = platform.system().lower()
    if 'linux' == detect_os:
        import laav
    else:
        import waav
except Exception as e:
    print(e)
