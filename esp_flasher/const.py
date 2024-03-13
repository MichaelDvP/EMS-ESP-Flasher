import re

__version__ = "1.0.2"


ESP32_DEFAULT_OTA_DATA = "https://github.com/MichaelDvP/EMS-ESP-Flasher/raw/my_repo/bin/boot_app0.bin"

ESP32_DEFAULT_BOOTLOADER_FORMAT = (
    "https://github.com/MichaelDvP/EMS-ESP-Flasher/raw/my_repo/"
    "bin/$MODEL$/bootloader_$FLASH_MODE$_$FLASH_FREQ$.bin"
)
ESP32_DEFAULT_PARTITIONS =  "https://github.com/MichaelDvP/EMS-ESP-Flasher/raw/my_repo/partitions/partitions_$MODEL$_$FLASH$.bin"


# https://stackoverflow.com/a/3809435/8924614
HTTP_REGEX = re.compile(
    r"https?://(www\.)?[-a-zA-Z0-9@:%._+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_+.~#?&/=]*)"
)
