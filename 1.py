import sys
try:
    import os
    import platform
    detect_os = platform.system().lower()
    if 'linux' == detect_os:
        import lglic
    else:
        import wglic
except Exception as e:
    print(e)
