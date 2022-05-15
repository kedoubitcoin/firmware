from storage import device
from trezor import utils

import lvgl as lv  # type: ignore[Import "lvgl" could not be resolved]

if utils.EMULATOR:
    font_PJSBOLD36 = lv.font_load("A:/res/PlusJakartaSans-Bold-36.bin")
    font_PJSBOLD32 = lv.font_load("A:/res/PlusJakartaSans-Bold-32.bin")
    font_PJSBOLD24 = lv.font_load("A:/res/PlusJakartaSans-Bold-24.bin")
    font_PJSBOLD20 = lv.font_load("A:/res/PlusJakartaSans-Bold-20.bin")
    font_PJSMID28 = lv.font_load("A:/res/PlusJakartaSans-Medium-28.bin")
    font_PJSMID24 = lv.font_load("A:/res/PlusJakartaSans-Medium-24.bin")
    font_PJSMID20 = lv.font_load("A:/res/PlusJakartaSans-Medium-20.bin")
    font_PJSREG24 = lv.font_load("A:/res/PlusJakartaSans-Regular-24.bin")
    font_MONO32 = lv.font_load("A:/res/JetBrainsMono-Bold-32.bin")
    font_MONO28 = lv.font_load("A:/res/JetBrainsMono-Medium-28.bin")
    font_MONO24 = lv.font_load("A:/res/JetBrainsMono-Medium-24.bin")
    font_LANG_MIX = lv.font_load("A:/res/LANG-MIX.bin")
    font_LANG_MIX_TITLE = lv.font_load("A:/res/LANG-MIX-TITLE.bin")

else:
    if device.get_language() in ["zh_cn", "zh_hk"]:
        font_PJSBOLD36 = lv.font_scs_bold_36
        font_PJSBOLD32 = lv.font_scs_bold_32
        font_PJSBOLD24 = lv.font_scs_bold_24
        font_PJSBOLD20 = lv.font_scs_bold_20
        font_PJSMID28 = lv.font_scs_reg_28
        font_PJSMID24 = lv.font_scs_reg_24
        font_PJSMID20 = lv.font_scs_reg_20
        font_PJSREG24 = lv.font_scs_reg_24
        font_MONO28 = lv.font_scs_reg_28
        font_MONO24 = lv.font_scs_reg_24
    else:
        font_PJSBOLD36 = lv.font_pljs_bold_36
        font_PJSBOLD32 = lv.font_pljs_bold_32
        font_PJSBOLD24 = lv.font_pljs_bold_24
        font_PJSBOLD20 = lv.font_pljs_bold_20
        font_PJSMID28 = lv.font_pljs_medium_28
        font_PJSMID24 = lv.font_pljs_medium_24
        font_PJSMID20 = lv.font_pljs_medium_20
        font_PJSREG24 = lv.font_pljs_regular_24
        font_MONO28 = lv.font_jbm_medium_28
        font_MONO24 = lv.font_jbm_medium_24
    font_LANG_MIX = lv.font_mix_bold_24
    font_LANG_MIX_TITLE = lv.font_mix_title_bold_36
