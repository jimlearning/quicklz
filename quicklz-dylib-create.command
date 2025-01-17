#!/bin/bash

# 使用此脚本前，必须先授权
# 首先 Terminal cd 切换到当前文件夹，然后执行以下脚本
# chmod +x quicklz-dylib-create.command

cd "$(dirname "$0")"
build="../../../../../../../build"

xcrun -sdk iphoneos clang -shared -o libquicklz.dylib -fPIC -arch arm64 -arch arm64e quicklz.c
codesign -s "Apple Development: Mingquan Jin (AABMM84XRG)" --force --deep --timestamp libquicklz.dylib
mkdir -p "iphoneos-arm64/quicklz-1.0/"
mv libquicklz.dylib iphoneos-arm64/quicklz-1.0/libquicklz.dylib
mkdir -p "${build}/quicklz/iphoneos-arm64/quicklz-1.0/"
cp iphoneos-arm64/quicklz-1.0/libquicklz.dylib ${build}/quicklz/iphoneos-arm64/quicklz-1.0/libquicklz.dylib

xcrun -sdk iphonesimulator clang -shared -o libquicklz.dylib -fPIC -arch x86_64 -arch arm64 quicklz.c
codesign -s "Apple Development: Mingquan Jin (AABMM84XRG)" --force --deep --timestamp libquicklz.dylib
mkdir -p "iphonesimulator-arm64/quicklz-1.0/"
mv libquicklz.dylib iphonesimulator-arm64/quicklz-1.0/libquicklz.dylib
mkdir -p "${build}/quicklz/iphonesimulator-arm64/quicklz-1.0/"
cp iphonesimulator-arm64/quicklz-1.0/libquicklz.dylib ${build}/quicklz/iphonesimulator-arm64/quicklz-1.0/libquicklz.dylib