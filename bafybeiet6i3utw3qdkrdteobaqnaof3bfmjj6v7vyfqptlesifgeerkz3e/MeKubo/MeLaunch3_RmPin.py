#-----------------------------------------------------------------------
# Name:    MeLaunch3_RmPin
# Purpose:    MeLaunch3_RmPin
#
# Author:    me
#
# Created:    2024052018300101
# Copyright:    (c) me 2024052018300101
# Licence:    copyright & all rights reserved
#-----------------------------------------------------------------------
#_____________________________________________________________________
#
import os
#
import subprocess
#
#_____________________________________________________________________
try \
:
    MePopenProcess00env0 \
        = \
        dict \
        (
        )
    MePopenProcess00env0 \
    .update \
    (
        os \
        .environ \
    )
    MePopenProcess00env0 \
    .update \
    (
        {
            'IPFS_PATH' \
            : \
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                    'zoo' \
                        ,
                    'kubo' \
                        ,
                    '.unixfs' \
                        ,
                )
                    ,
        }
    )
    MePopenProcess00args0 \
        = \
        ' ' \
        .join \
        (
            [
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                    'MeKuboWidgets' \
                        ,
                    'MeKuboRmPin' \
                        ,
                    'MeKuboRmPin.exe' \
                        ,
                ) \
            ] \
                ,
        )
    MePopenProcess00 \
        = \
        subprocess \
        .Popen \
        (
            MePopenProcess00args0 \
                ,
            cwd \
                = \
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                    'MeKuboWidgets' \
                        ,
                    'MeKuboRmPin' \
                        ,
                )
                ,
            env \
                = \
                MePopenProcess00env0 \
                ,
            creationflags \
                = \
                subprocess \
                .CREATE_NEW_CONSOLE \
                ,
            start_new_session \
                = \
                True \
                ,
        )
except \
:
    pass
#_____________________________________________________________________
