#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.file import File
from extract_utils.fixups_blob import (
    BlobFixupCtx,
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixup_remove,
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)
from extract_utils.tools import (
    llvm_objdump_path,
)
from extract_utils.utils import (
    run_cmd,
)

namespace_imports = [
    'device/samsung/universal9830-common',
    'hardware/samsung',
    'hardware/samsung_slsi-linaro/exynos',
    'hardware/samsung_slsi-linaro/graphics',
    'vendor/samsung/universal9830-common'
]


def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f'{lib}_{partition}' if partition == 'vendor' else None


lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        'libuuid',
    ): lib_fixup_vendor_suffix,
}


blob_fixups: blob_fixups_user_type = {
    'vendor/lib64/libbayergdccore.so': blob_fixup()
        .replace_needed('libOpenCL.so', 'libGLES_mali.so'),
    (
        'vendor/lib64/libkeymaster_helper.so',
        'vendor/lib64/libskeymaster4device.so',
    ): blob_fixup()
        .replace_needed('libcrypto.so', 'libcrypto-v33.so'),
    'vendor/lib64/libnpuc_backend.so': blob_fixup()
        .add_needed('liblog.so')
        .add_needed('libnpuc_cmdq.so'),
    'vendor/lib64/libnpuc_graph.so': blob_fixup()
        .add_needed('libnpuc_common.so'),
    (
        'vendor/lib64/libnpuc_common.so',
        'vendor/lib64/libnpuc_controller.so',
        'vendor/lib64/libnpuc_frontend.so',
        'vendor/lib64/libnpuc_template.so',
    ): blob_fixup()
        .add_needed('liblog.so'),
    'vendor/lib64/libeden_ud_gpu.so': blob_fixup()
        .replace_needed('libOpenCL.so', 'libGLES_mali.so')
        .add_needed('libeden_ud_cpu.so'),
    'vendor/lib64/libsec-ril.so': blob_fixup()
        .sig_replace('80 0E 40 F9 E1 03 16 AA 82 0C 80 52 E3 03 15 AA', '80 0E 40 F9 E1 03 16 AA 82 0C 80 52 03 00 80 D2'),
    'vendor/lib64/libsensorlistener.so': blob_fixup()
        .add_needed('libsensorndkbridge_shim.so'),
    'vendor/lib64/libwvhidl.so': blob_fixup()
        .replace_needed('libprotobuf-cpp-lite-3.9.1.so', 'libprotobuf-cpp-full-3.9.1.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    'universal9830-common',
    'samsung',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
)

if __name__ == '__main__':
    utils = ExtractUtils.device(module)
    utils.run()
