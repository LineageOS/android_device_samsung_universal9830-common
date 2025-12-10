#
# Copyright (C) 2025 The LineageOS Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# Inherit from common
$(call inherit-product, device/samsung/universal9830-common/device-common.mk)

# NFC
PRODUCT_COPY_FILES += \
<<<<<<< HEAD   (2ebab9175d5854486dfd84c1e7764015c02a4ce8 universal9830: Move NFC config to Hubble)
    $(LOCAL_PATH)/hubble/configs/nfc/libnfc-sec-vendor.conf:$(TARGET_COPY_OUT_VENDOR)/etc/libnfc-sec-vendor.conf
=======
    $(LOCAL_PATH)/hubble/configs/nfc/libnfc-sec-vendor.conf:$(TARGET_COPY_OUT_VENDOR)/etc/libnfc-sec-vendor.conf

# Overlays
DEVICE_PACKAGE_OVERLAYS += $(LOCAL_PATH)/hubble/overlay
>>>>>>> CHANGE (086d3350ae362e1aa48f81384d223e29dacd0407 universal9830: Move brightness overlays to Hubble)
