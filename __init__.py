import ctypes
import os
import platform

# 定义全局变量
quicklz_lib = None

# 定义常量
QLZ_SCRATCH_COMPRESS = 4096  # 修改为实际值
QLZ_SCRATCH_DECOMPRESS = 4096  # 修改为实际值

# Python 封装函数
def compress(data: bytes) -> bytes:
    source = ctypes.create_string_buffer(data)
    dest = ctypes.create_string_buffer(len(data) * 2)  # 预留足够的空间
    scratch = ctypes.create_string_buffer(QLZ_SCRATCH_COMPRESS)  # 根据 QLZ_SCRATCH_COMPRESS 定义
    size = quicklz_lib.qlz_compress(source, dest, len(data), scratch)
    return dest.raw[:size]

def decompress(data: bytes) -> bytes:
    source = ctypes.create_string_buffer(data)
    dest = ctypes.create_string_buffer(len(data) * 10)  # 预留足够的空间
    scratch = ctypes.create_string_buffer(QLZ_SCRATCH_DECOMPRESS)  # 根据 QLZ_SCRATCH_DECOMPRESS 定义
    size = quicklz_lib.qlz_decompress(source, dest, scratch)
    return dest.raw[:size]

def main():
    global quicklz_lib  # 声明 quicklz_lib 为全局变量

    # 获取脚本文件所在的目录
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # 获取当前 Platform，iphoneos / iphonesimulator
    if "simulator" in platform.machine().lower():
        platform_env = "iphonesimulator"
    else:
        platform_env = "iphoneos"

    # 构建动态库的绝对路径
    lib_path = os.path.abspath(os.path.join(script_dir, f"./{platform_env}-arm64/quicklz-1.0/libquicklz.dylib"))
    print("Library path:", lib_path)

    # 构建动态库
    quicklz_lib = ctypes.CDLL(lib_path)

    # 定义 QuickLZ 函数签名
    quicklz_lib.qlz_compress.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_size_t, ctypes.c_char_p]
    quicklz_lib.qlz_compress.restype = ctypes.c_size_t

    quicklz_lib.qlz_decompress.argtypes = [ctypes.c_char_p, ctypes.c_void_p, ctypes.c_char_p]
    quicklz_lib.qlz_decompress.restype = ctypes.c_size_t

main()
