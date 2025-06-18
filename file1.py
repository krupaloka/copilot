import os
import platform

def get_uptime():
    if platform.system() == "Windows":
        import ctypes
        from ctypes import wintypes

        class Uptime(ctypes.Structure):
            _fields_ = [("IdleTime", wintypes.LARGE_INTEGER),
                        ("KernelTime", wintypes.LARGE_INTEGER),
                        ("UserTime", wintypes.LARGE_INTEGER)]

        lib = ctypes.windll.kernel32
        uptime = lib.GetTickCount64() // 1000
        return uptime
    else:
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            return int(uptime_seconds)

if __name__ == "__main__":
    uptime = get_uptime()
    print(f"System uptime: {uptime} seconds")
