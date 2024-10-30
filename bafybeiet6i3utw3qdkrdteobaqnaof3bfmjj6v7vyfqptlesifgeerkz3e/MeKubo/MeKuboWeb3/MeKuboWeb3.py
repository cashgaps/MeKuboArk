#-----------------------------------------------------------------------
# Name:    MeKuboWeb3
# Purpose:    MeKuboWeb3
#
# Author:    me
#
# Created:    2024052018300101
# Copyright:    (c) me 2024052018300101
# Licence:    copyright & all rights reserved
#-----------------------------------------------------------------------
#_____________________________________________________________________
#
import atexit
#
import json
#
import math
#
import os
#
import pathlib
#
import random
#
import shutil
import signal
import socket
import stat
import subprocess
import sys
#
import threading
import time
import traceback
#
#
import colorama
#
import pyperclip
#
import readchar
#
import segno
#
#_____________________________________________________________
try \
:
    colorama \
    .just_fix_windows_console \
    (
    )
except \
:
    pass
#_____________________________________________________________
try \
:
    if \
        pyperclip \
        .paste \
        (
        ) \
            != \
            '' \
    :
        pyperclip \
        .copy \
        (
            pyperclip \
            .paste \
            (
            ) \
        )
except \
:
    pyperclip \
    .copy \
    (
        '' \
    )
#_____________________________________________________________
MeCounter0 \
    = \
    10000
MeStuffNeedToBreak \
    = \
    False
MeLog \
    = \
    list \
    (
    )
#_____________________________________________________________________
def \
    MeExceptor \
    (
    ) \
:
    print \
    (
        '\n' \
        + \
        '\n' \
        + \
        ':' \
        + \
        '\n' \
            ,
    )
    traceback \
    .print_exc \
    (
        file \
            = \
            sys \
            .stdout \
    )
    print \
    (
        '\n' \
        + \
        ':' \
        + \
        '\n' \
        + \
        '\n' \
            ,
    )
#_____________________________________________________________________
def \
    MeDaemon \
    (
    ) \
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
                    'zoo' \
                        ,
                    'kubo' \
                        ,
                    'kubo.exe' \
                        ,
                ) \
                    ,
                'daemon' \
                    ,
                '--init' \
                    ,
            ] \
                ,
        )
    global \
        MePopenProcess00
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
                )
                ,
            env \
                = \
                MePopenProcess00env0 \
                ,
            universal_newlines \
                = \
                False \
                ,
            stdout \
                = \
                subprocess \
                .DEVNULL \
                ,
            stderr \
                = \
                subprocess \
                .DEVNULL \
                ,
        )
def \
    MeStartDaemonThread \
    (
    ) \
:
    MeThread0 \
        = \
        threading \
        .Thread \
        (
            target \
                = \
                MeDaemon \
                ,
        )
    MeThread0 \
    .start \
    (
    )
def \
    MeStopDaemonThread \
    (
    ) \
:
    try \
    :
        global \
            MePopenProcess00
        MePopenProcess00 \
        .terminate \
        (
        )
    except \
    :
        pass
    try \
    :
        pathlib \
        .Path \
        (
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
                'datastore' \
                    ,
                'LOG' \
                    ,
            ) \
                ,
        ) \
        .unlink \
        (
            missing_ok \
                = \
                True \
                ,
        )
    except \
    :
        pass
    try \
    :
        shutil \
        .rmtree \
        (
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
                'datastore' \
                    ,
            ) \
                ,
            ignore_errors \
                = \
                True \
        )
    except \
    :
        pass
    print \
    (
        colorama \
        .Fore \
        .RESET \
            ,
        end \
            = \
            ''
    )
#_____________________________________________________________________
#_____________________________________________________________________
def \
    MeModem \
    (
    ) \
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
    MePopenProcess01args0 \
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
                    'zoo' \
                        ,
                    'kubo' \
                        ,
                    'modem' \
                        ,
                    'soundmodem.exe' \
                        ,
                ) \
                    ,
            ] \
                ,
        )
    global \
        MePopenProcess01
    MePopenProcess01 \
        = \
        subprocess \
        .Popen \
        (
            MePopenProcess01args0 \
                ,
            cwd \
                = \
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                )
                ,
            env \
                = \
                MePopenProcess00env0 \
                ,
            universal_newlines \
                = \
                False \
                ,
            stdout \
                = \
                subprocess \
                .DEVNULL \
                ,
            stderr \
                = \
                subprocess \
                .DEVNULL \
                ,
        )
def \
    MeStartModemThread \
    (
    ) \
:
    try \
    :
        global \
            MePopenProcess01
        if \
            MePopenProcess01 \
            .poll \
            (
            ) \
                == \
                0 \
        :
            MeThread0 \
                = \
                threading \
                .Thread \
                (
                    target \
                        = \
                        MeModem \
                        ,
                )
            MeThread0 \
            .start \
            (
            )
    except \
    :
        MeThread0 \
            = \
            threading \
            .Thread \
            (
                target \
                    = \
                    MeModem \
                    ,
            )
        MeThread0 \
        .start \
        (
        )
def \
    MeStopModemThread \
    (
    ) \
:
    try \
    :
        global \
            MePopenProcess01
        MePopenProcess01 \
        .terminate \
        (
        )
        del \
            MePopenProcess01
    except \
    :
        pass
    try \
    :
        MeFileNames1 \
            = \
            [
                [
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
                        'modem' \
                            ,
                        'zMeModem.ini' \
                            ,
                    ) \
                        ,
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
                        'modem' \
                            ,
                        'soundmodem.ini' \
                            ,
                    ) \
                        ,
                ] \
                    ,
            ]
        for \
            x \
        in \
            MeFileNames1 \
        :
            with \
                open \
                (
                    x \
                    [
                        0 \
                    ] \
                        ,
                    mode \
                        = \
                        'rb' \
                        ,
                ) \
            as \
                FileObject1 \
            :
                try \
                :
                    with \
                        open \
                        (
                            x \
                            [
                                1 \
                            ] \
                                ,
                            'wb' \
                                ,
                        ) \
                    as \
                        FileOpened1 \
                    :
                        FileOpened1 \
                        .write \
                        (
                            next \
                            (
                                FileReader \
                                (
                                    FileObject1 \
                                        ,
                                    1048576 \
                                        ,
                                )
                            )
                        )
                except:
                    pass
    except \
    :
        pass
    print \
    (
        colorama \
        .Fore \
        .RESET \
            ,
        end \
            = \
            ''
    )
#_____________________________________________________________________
#_____________________________________________________________________
def \
    MeStopThreads \
    (
    ) \
:
    MeStopDaemonThread \
    (
    )
    MeStopModemThread \
    (
    )
#_____________________________________________________________________
#_____________________________________________________________________
def \
    MeSocketeer \
    (
    ) \
:
    global \
        MeToggle0
    MeToggle0 \
        = \
        0
    global \
        MeSocket0
    global \
        Thing0
    try \
    :
        Thing0 \
            = \
            MeSocket0 \
            .recv \
            (
                1024 \
            ) \
            .split \
            (
                b'\r' \
            ) \
            [
                1 \
            ] \
            .decode \
            (
                'ascii' \
            )
        MeToggle0 \
            = \
            1
    except \
    :
        pass
#_____________________________________________________________________
#_____________________________________________________________________
def \
    MeSocketeerThread \
    (
    ) \
:
    global \
        MeThread0
    MeThread0 \
        = \
        threading \
        .Thread \
        (
            target \
                = \
                MeSocketeer \
                ,
        )
    MeThread0 \
    .start \
    (
    )
#_____________________________________________________________________
#_____________________________________________________________________
def \
    MeInputter \
    (
    ) \
:
    readchar \
    .readchar \
    (
    )
    global \
        MeToggle0
    MeToggle0 \
        = \
        1
#_____________________________________________________________________
#_____________________________________________________________________
def \
    MeInputterThread \
    (
    ) \
:
    global \
        MeThread1
    MeThread1 \
        = \
        threading \
        .Thread \
        (
            target \
                = \
                MeInputter \
                ,
        )
    MeThread1 \
    .start \
    (
    )
#_____________________________________________________________________
def \
    MeDisplayMenu \
    (
    ) \
:
    global \
        MeLog
    MeLog \
    .append \
    (
        '''
_______________________________________________________________________

7:key,      8:gc,       9:quit,
4:pin,      5:ls,       6:rm,
1:share,    2:get,      3:more,
0:publish,
                                    :MeKuboWeb3:''' \
    )
    print \
    (
        '''
_______________________________________________________________________

7:key,      8:gc,       9:quit,
4:pin,      5:ls,       6:rm,
1:share,    2:get,      3:more,
0:publish,
                                    :MeKuboWeb3:''' \
            ,
    )
#_____________________________________________________________________
def \
    MeAskForInput \
    (
    ) \
:
    global \
        MeLog
    global \
        MeInput0
    print \
    (
        ':' \
            ,
        '\n:' \
            ,
        end \
            = \
            '' \
            ,
    )
    MeInput0 \
        = \
        readchar \
        .readchar \
        (
        )
    MeLog \
    .append \
    (
        ':' \
        + \
        ' ' \
        + \
        '\n:' \
        + \
        MeInput0 \
    )
    print \
    (
        MeInput0 \
            ,
    )
    MeLog \
    .append \
    (
        ':' \
        + \
        ' ' \
        + \
        '\n\n' \
    )
    print \
    (
        ':' \
            ,
        '\n\n' \
            ,
    )
def \
    MeSaveInput \
    (
    ) \
:
    global \
        MeInput0
def \
    MeCheckInputForStuff \
    (
    ) \
:
    global \
        MeInput0
    global \
        MeStuffNeedToBreak
    MeInputStuffDef0 \
    (
    )
    MeInputStuffDef1 \
    (
    )
def \
    MeDoInputThing \
    (
    ) \
:
    global \
        MeInput0
    if \
        (
            MeInput0 \
                == \
                '0' \
        ) \
    :
        MeInputThingDef0 \
        (
        )
    elif \
        (
            MeInput0 \
                == \
                '1' \
        ) \
    :
        MeInputThingDef1 \
        (
        )
    elif \
        (
            MeInput0 \
                == \
                '2' \
        ) \
    :
        MeInputThingDef2 \
        (
        )
    elif \
        (
            MeInput0 \
                == \
                '3' \
        ) \
    :
        MeInputThingDef3 \
        (
        )
    elif \
        (
            MeInput0 \
                == \
                '4' \
        ) \
    :
        MeInputThingDef4 \
        (
        )
    elif \
        (
            MeInput0 \
                == \
                '5' \
        ) \
    :
        MeInputThingDef5 \
        (
        )
    elif \
        (
            MeInput0 \
                == \
                '6' \
        ) \
    :
        MeInputThingDef6 \
        (
        )
    elif \
        (
            MeInput0 \
                == \
                '7' \
        ) \
    :
        MeInputThingDef7 \
        (
        )
    elif \
        (
            MeInput0 \
                == \
                '8' \
        ) \
    :
        MeInputThingDef8 \
        (
        )
    elif \
        (
            MeInput0 \
                == \
                '9' \
        ) \
    :
        MeAskForInput \
        (
        )
        if \
            (
                MeInput0 \
                    == \
                    '9' \
            ) \
        :
            MeAskForInput \
            (
            )
            if \
                (
                    MeInput0 \
                        == \
                        '9' \
                ) \
            :
                MeInputThingDef9 \
                (
                )
#_____________________________________________________________________
def \
    MeInputStuffDef0 \
    (
    ) \
:
    pass
def \
    MeInputStuffDef1 \
    (
    ) \
:
    pass
#_____________________________________________________________________
def \
    MeInputThingDef0 \
    (
    ) \
:
    global \
        MeLog
    MeLog \
    .append \
    (
        ':publish: ' \
    )
    print \
    (
        ':publish: ' \
            ,
    )
    print \
    (
        ':' \
            ,
        '\n' \
            ,
        end \
            = \
            '' \
            ,
    )
    print \
    (
        colorama \
        .Fore \
        .MAGENTA \
            ,
        end \
            = \
            ''
    )
    #pyperclip0
    print \
    (
        colorama \
        .Fore \
        .RESET \
            ,
        end \
            = \
            ''
    )
    print \
    (
        '?'
            ,
        colorama \
        .Fore \
        .YELLOW \
            ,
        pyperclip \
        .paste \
        (
        ) \
            ,
        colorama \
        .Fore \
        .RESET \
            ,
        '\n'
            ,
        sep \
            = \
            '' \
            ,
        end \
            = \
            '' \
            ,
    )
    print \
    (
        ':' \
            ,
        end \
            = \
            '' \
            ,
    )
    print \
    (
        colorama \
        .Fore \
        .MAGENTA \
            ,
        end \
            = \
            ''
    )
    Thing \
        = \
        input \
        (
        )
    if \
        Thing \
            == \
            '' \
    :
        Thing \
            = \
            pyperclip \
            .paste \
            (
            )
    MeLog \
    .append \
    (
        ':' \
        + \
        ' ' \
        + \
        '\n:' \
        + \
        Thing \
    )
    print \
    (
        colorama \
        .Fore \
        .RESET \
            ,
        end \
            = \
            ''
    )
    #pyperclip1
    MeLog \
    .append \
    (
        ':' \
        + \
        ' ' \
        + \
        '\n\n' \
    )
    print \
    (
        ':' \
            ,
        '\n\n' \
            ,
    )
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
    MeCheckOutputProcess00args0 \
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
                    'zoo' \
                        ,
                    'kubo' \
                        ,
                    'kubo.exe' \
                        ,
                ) \
                    ,
                'name' \
                    ,
                'publish' \
                    ,
                '--resolve=false' \
                    ,
                '--allow-offline=true' \
                    ,
                '--ipns-base=base36' \
                    ,
                '--' \
                    ,
                Thing \
                    ,
            ] \
                ,
        )
    MeCheckOutputProcess00 \
        = \
        subprocess \
        .check_output \
        (
            MeCheckOutputProcess00args0 \
                ,
            cwd \
                = \
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                )
                ,
            env \
                = \
                MePopenProcess00env0 \
                ,
            universal_newlines \
                = \
                False \
                ,
            shell \
                = \
                True \
                ,
        )
    MeCheckOutputProcess01args0 \
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
                    'zoo' \
                        ,
                    'kubo' \
                        ,
                    'kubo.exe' \
                        ,
                ) \
                    ,
                'id' \
                    ,
                '--peerid-base=base32' \
                    ,
            ] \
                ,
        )
    MeCheckOutputProcess01 \
        = \
        subprocess \
        .check_output \
        (
            MeCheckOutputProcess01args0 \
                ,
            cwd \
                = \
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                )
                ,
            env \
                = \
                MePopenProcess00env0 \
                ,
            universal_newlines \
                = \
                False \
                ,
            shell \
                = \
                True \
                ,
        )
    Me0 \
        = \
        [
            x \
            .split \
            (
                ' ' \
            ) \
                for \
                    x \
                in \
                    MeCheckOutputProcess00 \
                    .decode \
                    (
                        'ascii' \
                            ,
                    ) \
                    .split \
                    (
                        '\n' \
                            ,
                    )
                    if \
                        x \
                            != \
                            '' \
        ]
    [
        MeLog \
        .append \
        (
            ':published: \n' \
            + \
            '/' \
            + \
            x \
            [
                3 \
            ] \
            .split \
            (
                '/' \
                    ,
            ) \
            [
                1 \
            ] \
            + \
            '/' \
            + \
            x \
            [
                3 \
            ] \
            .split \
            (
                '/' \
                    ,
            ) \
            [
                2 \
            ] \
            + \
            ' ' \
            + \
            '\n' \
            + \
            ':published to: \n' \
            + \
            '/ipns/' \
            + \
            json \
            .loads \
            (
                MeCheckOutputProcess01 \
                .decode \
                (
                    'ascii' \
                )
            ) \
            [
                'ID' \
            ]
            + \
            ' ' \
        ) \
            for \
                x \
            in \
                Me0 \
                if \
                    x \
                    [
                        0 \
                    ] \
                        != \
                        '' \
    ]
    [
        print \
        (
            ':published: \n' \
            + \
            '/' \
            + \
            x \
            [
                3 \
            ] \
            .split \
            (
                '/' \
                    ,
            ) \
            [
                1 \
            ] \
            + \
            '/' \
            + \
            colorama \
            .Fore \
            .MAGENTA \
            + \
            x \
            [
                3 \
            ] \
            .split \
            (
                '/' \
                    ,
            ) \
            [
                2 \
            ] \
            + \
            colorama \
            .Fore \
            .RESET \
            + \
            ' ' \
                ,
            ':published to: \n' \
            + \
            '/ipns/' \
            + \
            colorama \
            .Fore \
            .MAGENTA \
            + \
            json \
            .loads \
            (
                MeCheckOutputProcess01 \
                .decode \
                (
                    'ascii' \
                )
            ) \
            [
                'ID' \
            ]
            + \
            colorama \
            .Fore \
            .RESET \
            + \
            ' ' \
                ,
            sep \
                = \
                '\n' \
                ,
        ) \
            for \
                x \
            in \
                Me0 \
                if \
                    x \
                    [
                        0 \
                    ] \
                        != \
                        '' \
    ]
    pyperclip \
    .copy \
    (
        str \
        (
            json \
            .loads \
            (
                MeCheckOutputProcess01 \
                .decode \
                (
                    'ascii' \
                )
            ) \
            [
                'ID' \
            ]
        )
    )
def \
    MeInputThingDef1 \
    (
    ) \
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
    MeCheckOutputProcess00args0 \
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
                    'zoo' \
                        ,
                    'kubo' \
                        ,
                    'kubo.exe' \
                        ,
                ) \
                    ,
                'add' \
                    ,
                '-trH' \
                    ,
                '-p=false' \
                    ,
                '-s=buzhash' \
                    ,
                '--cid-version=1' \
                    ,
                '--hash=sha2-256' \
                    ,
                '--' \
                    ,
                (
                    os \
                    .path \
                    .join \
                    (
                        '.' \
                            ,
                        'zoo' \
                            ,
                        'things' \
                            ,
                        'shares' \
                            ,
                    )
                ) \
                    ,
            ] \
                ,
        )
    MeCheckOutputProcess00 \
        = \
        subprocess \
        .check_output \
        (
            MeCheckOutputProcess00args0 \
                ,
            cwd \
                = \
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                )
                ,
            env \
                = \
                MePopenProcess00env0 \
                ,
            universal_newlines \
                = \
                False \
                ,
            shell \
                = \
                True \
                ,
        )
    Me0 \
        = \
        [
            x \
            .split \
            (
                ' ' \
            ) \
                for \
                    x \
                in \
                    MeCheckOutputProcess00 \
                    .decode \
                    (
                        'ascii' \
                            ,
                    ) \
                    .split \
                    (
                        '\n' \
                            ,
                    )
                    if \
                        x \
                            != \
                            '' \
        ]
    global \
        MeLog
    MeLog \
    .append \
    (
        ':shares: ' \
    )
    print \
    (
        ':shares: ' \
            ,
    )
    [
        MeLog \
        .append \
        (
            x \
            [
                1 \
            ] \
            + \
            ' : ' \
            + \
            '".' \
            + \
            x \
            [
                2 \
            ] \
            [
                6 \
                : \
                # \
            ] \
            + \
            '"' \
        ) \
            for \
                x \
            in \
                Me0 \
                if \
                    x \
                    [
                        0 \
                    ] \
                        != \
                        '' \
    ]
    [
        print \
        (
            colorama \
            .Fore \
            .MAGENTA \
            + \
            x \
            [
                1 \
            ] \
            + \
            colorama \
            .Fore \
            .RESET \
                ,
            '".' \
            + \
            x \
            [
                2 \
            ] \
            [
                6 \
                : \
                # \
            ] \
            + \
            '"' \
                ,
            sep \
                = \
                ' : ' \
                ,
        ) \
            for \
                x \
            in \
                Me0 \
                if \
                    x \
                    [
                        0 \
                    ] \
                        != \
                        '' \
    ]
    [
        pyperclip \
        .copy \
        (
            str \
            (
                x \
                [
                    1 \
                ] \
            )
        )
            for \
                x \
            in \
                Me0 \
                if \
                    x \
                    [
                        0 \
                    ] \
                        != \
                        '' \
    ]
def \
    MeInputThingDef2 \
    (
    ) \
:
    global \
        MeLog
    MeLog \
    .append \
    (
        ':get: ' \
    )
    print \
    (
        ':get: ' \
            ,
    )
    print \
    (
        ':' \
            ,
        '\n' \
            ,
        end \
            = \
            '' \
            ,
    )
    print \
    (
        colorama \
        .Fore \
        .MAGENTA \
            ,
        end \
            = \
            ''
    )
    #pyperclip0
    print \
    (
        colorama \
        .Fore \
        .RESET \
            ,
        end \
            = \
            ''
    )
    print \
    (
        '?'
            ,
        colorama \
        .Fore \
        .YELLOW \
            ,
        pyperclip \
        .paste \
        (
        ) \
            ,
        colorama \
        .Fore \
        .RESET \
            ,
        '\n'
            ,
        sep \
            = \
            '' \
            ,
        end \
            = \
            '' \
            ,
    )
    print \
    (
        ':' \
            ,
        end \
            = \
            '' \
            ,
    )
    print \
    (
        colorama \
        .Fore \
        .MAGENTA \
            ,
        end \
            = \
            ''
    )
    Thing \
        = \
        input \
        (
        )
    if \
        Thing \
            == \
            '' \
    :
        Thing \
            = \
            pyperclip \
            .paste \
            (
            )
    MeLog \
    .append \
    (
        ':' \
        + \
        ' ' \
        + \
        '\n:' \
        + \
        Thing \
    )
    print \
    (
        colorama \
        .Fore \
        .RESET \
            ,
        end \
            = \
            ''
    )
    #pyperclip1
    MeLog \
    .append \
    (
        ':' \
        + \
        ' ' \
        + \
        '\n\n' \
    )
    print \
    (
        ':' \
            ,
        '\n\n' \
            ,
    )
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
    MeCheckOutputProcess00args0 \
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
                    'zoo' \
                        ,
                    'kubo' \
                        ,
                    'kubo.exe' \
                        ,
                ) \
                    ,
                'get' \
                    ,
                '-o=' \
                + \
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                    'zoo' \
                        ,
                    'things' \
                        ,
                    'gets' \
                        ,
                    Thing \
                    .split \
                    (
                        '/' \
                    ) \
                    [
                        -1 \
                    ] \
                        ,
                ) \
                    ,
                '-p=false' \
                    ,
                '--' \
                    ,
                Thing \
                    ,
            ] \
                ,
        )
    MeCheckOutputProcess00 \
        = \
        subprocess \
        .check_output \
        (
            MeCheckOutputProcess00args0 \
                ,
            cwd \
                = \
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                )
                ,
            env \
                = \
                MePopenProcess00env0 \
                ,
            universal_newlines \
                = \
                False \
                ,
            shell \
                = \
                True \
                ,
        )
    Me0 \
        = \
        [
            x \
            .split \
            (
                ' ' \
            ) \
                for \
                    x \
                in \
                    MeCheckOutputProcess00 \
                    .decode \
                    (
                        'ascii' \
                            ,
                    ) \
                    .split \
                    (
                        '\n' \
                            ,
                    )
                    if \
                        x \
                            != \
                            '' \
        ]
    MeLog \
    .append \
    (
        ':gets: ' \
    )
    print \
    (
        ':gets: ' \
            ,
    )
    [
        MeLog \
        .append \
        (
            x \
            [
                3 \
            ] \
        ) \
            for \
                x \
            in \
                Me0 \
                if \
                    x \
                    [
                        0 \
                    ] \
                        != \
                        '' \
    ]
    [
        print \
        (
            x \
            [
                3 \
            ] \
                ,
            sep \
                = \
                ' : ' \
                ,
        ) \
            for \
                x \
            in \
                Me0 \
                if \
                    x \
                    [
                        0 \
                    ] \
                        != \
                        '' \
    ]
def \
    MeInputThingDef3 \
    (
    ) \
:
    Thing \
        = \
        ''
    while \
        Thing \
            != \
            '9' \
    :
        global \
            MeLog
        MeLog \
        .append \
        (
            '''
_______________________________________________________________________

7:log,      8:rndm,     9:return,
4:car,      5:par,      6:crypt,
1:verify,   2:qr,       3:more,
0:sign,
                                    :mores:one:''' \
        )
        print \
        (
            '''
_______________________________________________________________________

7:log,      8:rndm,     9:return,
4:car,      5:par,      6:crypt,
1:verify,   2:qr,       3:more,
0:sign,
                                    :mores:one:''' \
                ,
        )
        print \
        (
            ':' \
                ,
            '\n:' \
                ,
            end \
                = \
                '' \
                ,
        )
        Thing \
            = \
            readchar \
            .readchar \
            (
            )
        MeLog \
        .append \
        (
            ':' \
            + \
            ' ' \
            + \
            '\n:' \
            + \
            Thing \
        )
        print \
        (
            Thing \
                ,
        )
        MeLog \
        .append \
        (
            ':' \
            + \
            ' ' \
            + \
            '\n\n' \
        )
        print \
        (
            ':' \
                ,
            '\n\n' \
                ,
        )
        if \
            (
                Thing \
                    == \
                    '0' \
            ) \
        :
            MeInputThingDef3Def0 \
            (
            )
        elif \
            (
                Thing \
                    == \
                    '1' \
            ) \
        :
            MeInputThingDef3Def1 \
            (
            )
        elif \
            (
                Thing \
                    == \
                    '2' \
            ) \
        :
            MeInputThingDef3Def2 \
            (
            )
        elif \
            (
                Thing \
                    == \
                    '3' \
            ) \
        :
            MeInputThingDef3Def3 \
            (
            )
        elif \
            (
                Thing \
                    == \
                    '4' \
            ) \
        :
            MeInputThingDef3Def4 \
            (
            )
        elif \
            (
                Thing \
                    == \
                    '5' \
            ) \
        :
            MeInputThingDef3Def5 \
            (
            )
        elif \
            (
                Thing \
                    == \
                    '6' \
            ) \
        :
            MeInputThingDef3Def6 \
            (
            )
        elif \
            (
                Thing \
                    == \
                    '7' \
            ) \
        :
            MeInputThingDef3Def7 \
            (
            )
        elif \
            (
                Thing \
                    == \
                    '8' \
            ) \
        :
            MeInputThingDef3Def8 \
            (
            )
def \
    MeInputThingDef3Def0 \
    (
    ) \
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
    MeCheckOutputProcess01args0 \
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
                    'zoo' \
                        ,
                    'kubo' \
                        ,
                    'kubo.exe' \
                        ,
                ) \
                    ,
                'id' \
                    ,
                '--peerid-base=base32' \
                    ,
            ] \
                ,
        )
    MeCheckOutputProcess01 \
        = \
        subprocess \
        .check_output \
        (
            MeCheckOutputProcess01args0 \
                ,
            cwd \
                = \
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                )
                ,
            env \
                = \
                MePopenProcess00env0 \
                ,
            universal_newlines \
                = \
                False \
                ,
            shell \
                = \
                True \
                ,
        )
    #timestamper0
    global \
        MeCounter0
    MeCounter0 \
        += \
        1
    if \
        (
            MeCounter0 \
                >= \
                10000 \
        ) \
    :
        MeCounter0 \
            = \
            0
    TimeStamper \
        = \
        lambda \
        : \
        (
            (
                int \
                (
                    time \
                    .time \
                    (
                    )
                ) \
                * \
                (
                    10 \
                    ** \
                    4
                )
            ) \
            + \
            (
                MeCounter0 \
            ) \
        )
    #timestamper1
    MeSigk0 \
        = \
        json \
        .loads \
        (
            MeCheckOutputProcess01 \
            .decode \
            (
                'ascii' \
            )
        ) \
        [
            'ID' \
        ] \
        + \
        '_' \
        + \
        str \
        (
            TimeStamper \
            (
            )
        ) \
        + \
        '.sigk'
    global \
        MeLog
    MeLog \
    .append \
    (
        ':sign: ' \
    )
    print \
    (
        ':sign: ' \
            ,
    )
    MeLog \
    .append \
    (
        ':' \
    )
    print \
    (
        ':' \
            ,
    )
    print \
    (
        '' \
            ,
        end \
            = \
            '' \
            ,
    )
    #pyperclip0
    print \
    (
        colorama \
        .Fore \
        .RESET \
            ,
        end \
            = \
            ''
    )
    print \
    (
        '?'
            ,
        colorama \
        .Fore \
        .YELLOW \
            ,
        pyperclip \
        .paste \
        (
        ) \
            ,
        colorama \
        .Fore \
        .RESET \
            ,
        '\n'
            ,
        sep \
            = \
            '' \
            ,
        end \
            = \
            '' \
            ,
    )
    print \
    (
        ':' \
            ,
        end \
            = \
            '' \
            ,
    )
    print \
    (
        colorama \
        .Fore \
        .RESET \
            ,
        end \
            = \
            ''
    )
    Thing \
        = \
        input \
        (
        )
    if \
        Thing \
            == \
            '' \
    :
        Thing \
            = \
            pyperclip \
            .paste \
            (
            )
    MeLog \
    .append \
    (
        ':' \
        + \
        Thing \
    )
    #pyperclip1
    MeLog \
    .append \
    (
        ':' \
        + \
        ' ' \
        + \
        '\n\n' \
    )
    print \
    (
        ':' \
            ,
        '\n\n' \
            ,
    )
    with \
        open \
        (
            os \
            .path \
            .join \
            (
                '.' \
                    ,
                'zoo' \
                    ,
                'things' \
                    ,
                'mores' \
                    ,
                'sigk' \
                    ,
                MeSigk0 \
                    ,
            ) \
                ,
            'wb' \
        ) \
    as \
    (
        FileObject0 \
    ) \
    :
        FileObject0 \
            .write \
            (
                Thing \
                .encode \
                (
                    'ascii' \
                )
            )
    MeCheckOutputProcess00args0 \
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
                    'zoo' \
                        ,
                    'kubo' \
                        ,
                    'kubo.exe' \
                        ,
                ) \
                    ,
                'key' \
                    ,
                'sign' \
                    ,
                '--ipns-base=base32' \
                    ,
                '--' \
                    ,
                '<' \
                    ,
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                    'zoo' \
                        ,
                    'things' \
                        ,
                    'mores' \
                        ,
                    'sigk' \
                        ,
                    MeSigk0 \
                        ,
                ) \
                    ,
            ] \
                ,
        )
    MeCheckOutputProcess00 \
        = \
        subprocess \
        .check_output \
        (
            MeCheckOutputProcess00args0 \
                ,
            cwd \
                = \
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                )
                ,
            env \
                = \
                MePopenProcess00env0 \
                ,
            universal_newlines \
                = \
                False \
                ,
            shell \
                = \
                True \
                ,
        )
    Me0 \
        = \
        json \
        .loads \
        (
            MeCheckOutputProcess00 \
            .decode \
            (
                'ascii' \
            )
        )
    Me0 \
    .update \
    (
        {
            'Data' \
            :
                Thing \
                ,
        }
    )
    with \
        open \
        (
            os \
            .path \
            .join \
            (
                '.' \
                    ,
                'zoo' \
                    ,
                'things' \
                    ,
                'mores' \
                    ,
                'sigk' \
                    ,
                MeSigk0 \
                    ,
            ) \
                ,
            'wb' \
        ) \
    as \
    (
        FileObject0 \
    ) \
    :
        FileObject0 \
            .write \
            (
                json \
                .dumps \
                (
                    Me0 \
                ) \
                .encode \
                (
                    'ascii' \
                )
            )
    MeLog \
    .append \
    (
        ':signed: ' \
        + \
        '\n' \
        + \
        Me0 \
        [
            'Data' \
        ] \
    )
    print \
    (
        ':signed: ' \
            ,
        Me0 \
        [
            'Data' \
        ] \
            ,
        sep \
            = \
            '\n' \
            ,
    )
    MeLog \
    .append \
    (
        ':signed by: ' \
        + \
        '\n' \
        + \
        Me0 \
        [
            'Key' \
        ] \
            [
                'Id' \
            ] \
    )
    print \
    (
        ':signed by: ' \
            ,
        colorama \
        .Fore \
        .MAGENTA \
        + \
        Me0 \
        [
            'Key' \
        ] \
        [
            'Id' \
        ] \
        + \
        colorama \
        .Fore \
        .RESET \
            ,
        sep \
            = \
            '\n' \
            ,
    )
    pyperclip \
    .copy \
    (
        str \
        (
            Me0 \
            [
                'Key' \
            ] \
            [
                'Id' \
            ] \
        )
    )
    MeLog \
    .append \
    (
        ':sigk: ' \
        + \
        '\n' \
        + \
        MeSigk0 \
        + \
        '\n' \
        + \
        '' \
    )
    print \
    (
        ':sigk: ' \
            ,
        MeSigk0 \
            ,
        '' \
            ,
        sep \
            = \
            '\n' \
            ,
    )
def \
    MeInputThingDef3Def1 \
    (
    ) \
:
    try \
    :
        os \
        .chmod \
        (
            os \
            .path \
            .join \
            (
                '.' \
                    ,
                'zoo' \
                    ,
                'things' \
                    ,
                'mores' \
                    ,
                'sigk' \
                    ,
                'z' \
                    ,
            ) \
                ,
            stat \
            .S_IWRITE \
        )
        pathlib \
        .Path \
        (
            os \
            .path \
            .join \
            (
                '.' \
                    ,
                'zoo' \
                    ,
                'things' \
                    ,
                'mores' \
                    ,
                'sigk' \
                    ,
                'z' \
                    ,
            ) \
                ,
        ) \
        .unlink \
        (
            missing_ok \
                = \
                True \
                ,
        )
    except \
    :
        pass
    global \
        MeLog
    MeLog \
    .append \
    (
        ':choose to verify: ' \
    )
    print \
    (
        ':choose to verify: ' \
            ,
    )
    FilesInFilesDir \
        = \
        [
            os \
            .path \
            .join \
            (
                path \
                    ,
                name \
                    ,
            ) \
                for \
                    path \
                        ,
                    subdirs \
                        ,
                    files \
                in \
                    os \
                    .walk \
                    (
                        os \
                        .path \
                        .join \
                        (
                            '.' \
                                ,
                            'zoo' \
                                ,
                            'things' \
                                ,
                            'mores' \
                                ,
                            'sigk' \
                                ,
                        ) \
                    ) \
                        for \
                            name \
                        in \
                            files
        ]
    FilesInFilesDirList \
        = \
        FilesInFilesDir \
        .copy \
        (
        )
    for \
        n \
    in \
        range \
        (
            0 \
                ,
            len \
            (
                FilesInFilesDirList \
            )
        ) \
    :
        FilesInFilesDirList \
        [
            n \
        ] \
            = \
            (
                str \
                (
                    n \
                ) \
                + \
                ' ' \
                + \
                str \
                (
                    FilesInFilesDirList \
                    [
                        n \
                    ]
                ) \
                .rjust \
                (
                    16 \
                        ,
                    ' ' \
                )
            )
    for \
        n \
    in \
        FilesInFilesDirList \
    :
        MeLog \
        .append \
        (
            n \
        )
        print \
        (
            n \
                ,
        )
    MeLog \
    .append \
    (
        '\n' \
    )
    print \
    (
    )
    MeLog \
    .append \
    (
        ':verify num: ' \
    )
    print \
    (
        ':verify num: ' \
            ,
    )
    MeLog \
    .append \
    (
        ':' \
    )
    print \
    (
        ':' \
            ,
    )
    print \
    (
        ':' \
            ,
        end \
            = \
            '' \
            ,
    )
    Thing \
        = \
        FilesInFilesDir \
        [
            int \
            (
                input \
                (
                )
            )
        ]
    MeLog \
    .append \
    (
        ':' \
        + \
        Thing \
    )
    MeLog \
    .append \
    (
        ':' \
        + \
        ' ' \
        + \
        '\n\n' \
    )
    print \
    (
        ':' \
            ,
        '\n\n' \
            ,
    )
    with \
        open \
        (
            os \
            .path \
            .join \
            (
                Thing \
                    ,
            ) \
                ,
            'rb' \
                ,
        ) \
    as \
        FileObject0 \
    :
        try \
        :
            DataBox0 \
                = \
                b''
            while \
                True \
            :
                DataBox0 \
                    += \
                    next \
                    (
                        FileReader \
                        (
                            FileObject0 \
                                ,
                        )
                    )
        except \
        :
            pass
        finally \
        :
            DataBox0 \
                = \
                json \
                .loads \
                (
                    DataBox0 \
                    .decode \
                    (
                        'ascii' \
                    )
                )
            with \
                open \
                (
                    os \
                    .path \
                    .join \
                    (
                        '.' \
                            ,
                        'zoo' \
                            ,
                        'things' \
                            ,
                        'mores' \
                            ,
                        'sigk' \
                            ,
                        'z' \
                            ,
                    ) \
                        ,
                    'wb' \
                        ,
                ) \
            as \
                FileOpened0 \
            :
                FileOpened0 \
                .write \
                (
                    b'' \
                        ,
                )
            with \
                open \
                (
                    os \
                    .path \
                    .join \
                    (
                        '.' \
                            ,
                        'zoo' \
                            ,
                        'things' \
                            ,
                        'mores' \
                            ,
                        'sigk' \
                            ,
                        'z' \
                            ,
                    ) \
                        ,
                    'ab' \
                        ,
                ) \
            as \
                FileOpened0 \
            :
                if \
                    type \
                    (
                        DataBox0 \
                        [
                            'Data' \
                        ] \
                    ) \
                        == \
                        type \
                        (
                            str \
                            (
                            ) \
                        ) \
                :
                    FileOpened0 \
                    .write \
                    (
                        DataBox0 \
                        [
                            'Data' \
                        ] \
                        .encode \
                        (
                            'ascii' \
                        ) \
                            ,
                    )
                elif \
                    type \
                    (
                        DataBox0 \
                        [
                            'Data' \
                        ] \
                    ) \
                        == \
                        type \
                        (
                            dict \
                            (
                            ) \
                        ) \
                :
                    FileOpened0 \
                    .write \
                    (
                        json \
                        .dumps \
                        (
                            DataBox0 \
                            [
                                'Data' \
                            ]
                        ) \
                        .encode \
                        (
                            'ascii' \
                        ) \
                            ,
                    )
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
    MeCheckOutputProcess00args0 \
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
                    'zoo' \
                        ,
                    'kubo' \
                        ,
                    'kubo.exe' \
                        ,
                ) \
                    ,
                'key' \
                    ,
                'verify' \
                    ,
                '-k=' \
                + \
                json \
                .dumps \
                (
                    DataBox0 \
                    [
                        'Key' \
                    ] \
                    [
                        'Id' \
                    ]
                ) \
                    ,
                '-s=' \
                + \
                json \
                .dumps \
                (
                    DataBox0 \
                    [
                        'Signature' \
                    ]
                ) \
                    ,
                '--ipns-base=base32' \
                    ,
                '--' \
                    ,
                '<' \
                    ,
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                    'zoo' \
                        ,
                    'things' \
                        ,
                    'mores' \
                        ,
                    'sigk' \
                        ,
                    'z' \
                        ,
                ) \
                    ,
            ] \
                ,
        )
    MeCheckOutputProcess00 \
        = \
        subprocess \
        .check_output \
        (
            MeCheckOutputProcess00args0 \
                ,
            cwd \
                = \
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                )
                ,
            env \
                = \
                MePopenProcess00env0 \
                ,
            universal_newlines \
                = \
                False \
                ,
            shell \
                = \
                True \
                ,
        )
    try \
    :
        os \
        .chmod \
        (
            os \
            .path \
            .join \
            (
                '.' \
                    ,
                'zoo' \
                    ,
                'things' \
                    ,
                'mores' \
                    ,
                'sigk' \
                    ,
                'z' \
                    ,
            ) \
                ,
            stat \
            .S_IWRITE \
        )
        pathlib \
        .Path \
        (
            os \
            .path \
            .join \
            (
                '.' \
                    ,
                'zoo' \
                    ,
                'things' \
                    ,
                'mores' \
                    ,
                'sigk' \
                    ,
                'z' \
                    ,
            ) \
                ,
        ) \
        .unlink \
        (
            missing_ok \
                = \
                True \
                ,
        )
    except \
    :
        pass
    Me0 \
        = \
        json \
        .loads \
        (
            MeCheckOutputProcess00 \
            .decode \
            (
                'ascii' \
            ) \
        )
    if \
        Me0 \
        [
            'SignatureValid' \
        ] \
            == \
            True \
    :
        print \
        (
            colorama \
            .Fore \
            .GREEN \
                ,
            end \
                = \
                ''
        )
        if \
            type \
            (
                DataBox0 \
                [
                    'Data' \
                ] \
            ) \
                == \
                type \
                (
                    str \
                    (
                    ) \
                ) \
        :
            MeLog \
            .append \
            (
                ':verified: ' \
                + \
                '\n' \
                + \
                DataBox0 \
                [
                    'Data' \
                ] \
            )
            print \
            (
                ':verified: ' \
                    ,
                DataBox0 \
                [
                    'Data' \
                ] \
                    ,
                sep \
                    = \
                    '\n' \
                    ,
            )
        elif \
            type \
            (
                DataBox0 \
                [
                    'Data' \
                ] \
            ) \
                == \
                type \
                (
                    dict \
                    (
                    ) \
                ) \
        :
            MeLog \
            .append \
            (
                ':verified: ' \
            )
            print \
            (
                ':verified: ' \
                    ,
            )
            MeLog \
            .append \
            (
                '{' \
            )
            print \
            (
                '{' \
                    ,
            )
            [
                MeLog \
                .append \
                (
                    '    "' \
                    + \
                    str \
                    (
                        y \
                        [
                            0 \
                        ]
                    ) \
                    + \
                    '" \n    : \n        "' \
                    + \
                    str \
                    (
                        y \
                        [
                            1 \
                        ]
                    ) \
                    + \
                    '" \n        ,' \
                )
                    for \
                        y \
                    in \
                        [
                            x \
                                for \
                                    x \
                                in \
                                    DataBox0 \
                                    [
                                        'Data' \
                                    ] \
                                    .items \
                                    (
                                    )
                        ] \
            ]
            [
                print
                (
                    '    "' \
                    + \
                    str \
                    (
                        y \
                        [
                            0 \
                        ]
                    ) \
                    + \
                    '" \n    : \n        "' \
                    + \
                    str \
                    (
                        y \
                        [
                            1 \
                        ]
                    ) \
                    + \
                    '" \n        ,' \
                )
                    for \
                        y \
                    in \
                        [
                            x \
                                for \
                                    x \
                                in \
                                    DataBox0 \
                                    [
                                        'Data' \
                                    ] \
                                    .items \
                                    (
                                    )
                        ] \
            ]
            print \
            (
                '}' \
                    ,
            )
        MeLog \
        .append \
        (
            ':signed by: ' \
            + \
            '\n' \
            + \
            DataBox0 \
            [
                'Key' \
            ] \
            [
                'Id' \
            ] \
            + \
            '\n' \
            + \
            ':sigk: ' \
            + \
            '\n' \
            + \
            Thing \
            + \
            '\n' \
            + \
            '' \
        )
        print \
        (
            ':signed by: ' \
                ,
            colorama \
            .Fore \
            .MAGENTA \
            + \
            DataBox0 \
            [
                'Key' \
            ] \
            [
                'Id' \
            ] \
            + \
            colorama \
            .Fore \
            .GREEN \
                ,
            ':sigk: ' \
                ,
            Thing \
                ,
            '' \
                ,
            sep \
                = \
                '\n' \
                ,
        )
        pyperclip \
        .copy \
        (
            str \
            (
                DataBox0 \
                [
                    'Key' \
                ] \
                [
                    'Id' \
                ] \
            )
        )
        print \
        (
            colorama \
            .Fore \
            .RESET \
                ,
            end \
                = \
                ''
        )
    elif \
        Me0 \
        [
            'SignatureValid' \
        ] \
            == \
            False \
    :
        print \
        (
            colorama \
            .Fore \
            .RED \
                ,
            end \
                = \
                ''
        )
        if \
            type \
            (
                DataBox0 \
                [
                    'Data' \
                ] \
            ) \
                == \
                type \
                (
                    str \
                    (
                    ) \
                ) \
        :
            MeLog \
            .append \
            (
                ':!WARNING!: ' \
                + \
                '\n' \
                + \
                DataBox0 \
                [
                    'Data' \
                ] \
                + \
                '\n' \
                + \
                ':!WARNING!: ' \
            )
            print \
            (
                ':!WARNING!: ' \
                    ,
                DataBox0 \
                [
                    'Data' \
                ] \
                    ,
                ':!WARNING!: ' \
                    ,
                sep \
                    = \
                    '\n' \
                    ,
            )
        elif \
            type \
            (
                DataBox0 \
                [
                    'Data' \
                ] \
            ) \
                == \
                type \
                (
                    dict \
                    (
                    ) \
                ) \
        :
            MeLog \
            .append \
            (
                ':!WARNING!: ' \
            )
            print \
            (
                ':!WARNING!: ' \
                    ,
            )
            MeLog \
            .append \
            (
                '{' \
            )
            print \
            (
                '{' \
                    ,
            )
            [
                MeLog \
                .append \
                (
                    '    "' \
                    + \
                    str \
                    (
                        y \
                        [
                            0 \
                        ]
                    ) \
                    + \
                    '" \n    : \n        "' \
                    + \
                    str \
                    (
                        y \
                        [
                            1 \
                        ]
                    ) \
                    + \
                    '" \n        ,' \
                )
                    for \
                        y \
                    in \
                        [
                            x \
                                for \
                                    x \
                                in \
                                    DataBox0 \
                                    [
                                        'Data' \
                                    ] \
                                    .items \
                                    (
                                    )
                        ] \
            ]
            [
                print
                (
                    '    "' \
                    + \
                    str \
                    (
                        y \
                        [
                            0 \
                        ]
                    ) \
                    + \
                    '" \n    : \n        "' \
                    + \
                    str \
                    (
                        y \
                        [
                            1 \
                        ]
                    ) \
                    + \
                    '" \n        ,' \
                )
                    for \
                        y \
                    in \
                        [
                            x \
                                for \
                                    x \
                                in \
                                    DataBox0 \
                                    [
                                        'Data' \
                                    ] \
                                    .items \
                                    (
                                    )
                        ] \
            ]
            MeLog \
            .append \
            (
                '}' \
            )
            print \
            (
                '}' \
                    ,
            )
            MeLog \
            .append \
            (
                ':!WARNING!: ' \
            )
            print \
            (
                ':!WARNING!: ' \
                    ,
            )
        MeLog \
        .append \
        (
            Thing \
            + \
            '\n' \
            + \
            '' \
        )
        print \
        (
            Thing \
                ,
            '' \
                ,
            sep \
                = \
                '\n' \
                ,
        )
        print \
        (
            colorama \
            .Fore \
            .RESET \
                ,
            end \
                = \
                ''
        )
def \
    MeInputThingDef3Def2 \
    (
    ) \
:
    global \
        MeLog
    MeLog \
    .append \
    (
        ':qr: ' \
    )
    print \
    (
        ':qr: ' \
            ,
    )
    MeLog \
    .append \
    (
        ':' \
    )
    print \
    (
        ':' \
            ,
    )
    print \
    (
        '' \
            ,
        end \
            = \
            '' \
            ,
    )
    print \
    (
        colorama \
        .Fore \
        .MAGENTA \
            ,
        end \
            = \
            ''
    )
    #pyperclip0
    print \
    (
        colorama \
        .Fore \
        .RESET \
            ,
        end \
            = \
            ''
    )
    print \
    (
        '?'
            ,
        colorama \
        .Fore \
        .YELLOW \
            ,
        pyperclip \
        .paste \
        (
        ) \
            ,
        colorama \
        .Fore \
        .RESET \
            ,
        '\n'
            ,
        sep \
            = \
            '' \
            ,
        end \
            = \
            '' \
            ,
    )
    print \
    (
        ':' \
            ,
        end \
            = \
            '' \
            ,
    )
    print \
    (
        colorama \
        .Fore \
        .MAGENTA \
            ,
        end \
            = \
            ''
    )
    Thing \
        = \
        input \
        (
        )
    if \
        Thing \
            == \
            '' \
    :
        Thing \
            = \
            pyperclip \
            .paste \
            (
            )
    MeLog \
    .append \
    (
        ':' \
        + \
        Thing \
    )
    print \
    (
        colorama \
        .Fore \
        .RESET \
            ,
        end \
            = \
            ''
    )
    #pyperclip1
    MeLog \
    .append \
    (
        ':' \
        + \
        ' ' \
        + \
        '\n\n' \
    )
    print \
    (
        ':' \
            ,
        '\n\n' \
            ,
    )
    MeLog \
    .append \
    (
        '' \
    )
    print \
    (
    )
    MeLog \
    .append \
    (
        ':qr: ' \
    )
    print \
    (
        ':qr: ' \
            ,
    )
    segno \
    .make_qr \
    (
        Thing \
            ,
        error \
            = \
            'h' \
            ,
    ) \
    .terminal \
    (
        compact \
            = \
            True \
            ,
    )
    MeLog \
    .append \
    (
        Thing \
        + \
        ' ' \
        + \
        '\n\n' \
    )
    print \
    (
        colorama \
        .Fore \
        .MAGENTA \
        + \
        Thing \
        + \
        colorama \
        .Fore \
        .RESET \
            ,
        '\n\n' \
            ,
    )
    pyperclip \
    .copy \
    (
        str \
        (
            Thing \
        )
    )
def \
    MeInputThingDef3Def3 \
    (
    ) \
:
    Thing \
        = \
        ''
    while \
        Thing \
            != \
            '9' \
    :
        global \
            MeLog
        MeLog \
        .append \
        (
            '''
_______________________________________________________________________

7:,         8:,         9:return,
4:,         5:,         6:,
1:,         2:modem,    3:,
0:,
                                    :mores:two:''' \
        )
        print \
        (
            '''
_______________________________________________________________________

7:,         8:,         9:return,
4:,         5:,         6:,
1:,         2:modem,    3:,
0:,
                                    :mores:two:''' \
                ,
        )
        print \
        (
            ':' \
                ,
            '\n:' \
                ,
            end \
                = \
                '' \
                ,
        )
        Thing \
            = \
            readchar \
            .readchar \
            (
            )
        MeLog \
        .append \
        (
            ':' \
            + \
            ' ' \
            + \
            '\n:' \
            + \
            Thing \
        )
        print \
        (
            Thing \
                ,
        )
        MeLog \
        .append \
        (
            ':' \
            + \
            ' ' \
            + \
            '\n\n' \
        )
        print \
        (
            ':' \
                ,
            '\n\n' \
                ,
        )
        if \
            (
                Thing \
                    == \
                    '2' \
            ) \
        :
            MeInputThingDef3Def3Def2 \
            (
            )
def \
    MeInputThingDef3Def3Def2 \
    (
    ) \
:
    Thing \
        = \
        ''
    MeStartModemThread \
    (
    )
    while \
        Thing \
            != \
            '9' \
    :
        global \
            MeLog
        MeLog \
        .append \
        (
            '''
_______________________________________________________________________

7:,         8:,         9:return,
4:,         5:,         6:,
1:listen,   2:,         3:,
0:noisy,
                                    :modem:''' \
        )
        print \
        (
            '''
_______________________________________________________________________

7:,         8:,         9:return,
4:,         5:,         6:,
1:listen,   2:,         3:,
0:noisy,
                                    :modem:''' \
                ,
        )
        print \
        (
            ':' \
                ,
            '\n:' \
                ,
            end \
                = \
                '' \
                ,
        )
        Thing \
            = \
            readchar \
            .readchar \
            (
            )
        MeLog \
        .append \
        (
            ':' \
            + \
            ' ' \
            + \
            '\n:' \
            + \
            Thing \
        )
        print \
        (
            Thing \
                ,
        )
        MeLog \
        .append \
        (
            ':' \
            + \
            ' ' \
            + \
            '\n\n' \
        )
        print \
        (
            ':' \
                ,
            '\n\n' \
                ,
        )
        if \
            (
                Thing \
                    == \
                    '0' \
            ) \
        :
            MeInputThingDef3Def3Def2Def0 \
            (
            )
        elif \
            (
                Thing \
                    == \
                    '1' \
            ) \
        :
            MeInputThingDef3Def3Def2Def1 \
            (
            )
    MeStopModemThread \
    (
    )
def \
    MeInputThingDef3Def3Def2Def0 \
    (
    ) \
:
    global \
        MeLog
    MeLog \
    .append \
    (
        ':noisy: ' \
    )
    print \
    (
        ':noisy: ' \
            ,
    )
    MeLog \
    .append \
    (
        ':' \
    )
    print \
    (
        ':' \
            ,
    )
    print \
    (
        '' \
            ,
        end \
            = \
            '' \
            ,
    )
    print \
    (
        colorama \
        .Fore \
        .MAGENTA \
            ,
        end \
            = \
            ''
    )
    #pyperclip0
    print \
    (
        colorama \
        .Fore \
        .RESET \
            ,
        end \
            = \
            ''
    )
    print \
    (
        '?'
            ,
        colorama \
        .Fore \
        .YELLOW \
            ,
        pyperclip \
        .paste \
        (
        ) \
            ,
        colorama \
        .Fore \
        .RESET \
            ,
        '\n'
            ,
        sep \
            = \
            '' \
            ,
        end \
            = \
            '' \
            ,
    )
    print \
    (
        ':' \
            ,
        end \
            = \
            '' \
            ,
    )
    print \
    (
        colorama \
        .Fore \
        .MAGENTA \
            ,
        end \
            = \
            ''
    )
    Thing \
        = \
        input \
        (
        )
    if \
        Thing \
            == \
            '' \
    :
        Thing \
            = \
            pyperclip \
            .paste \
            (
            )
    MeLog \
    .append \
    (
        ':' \
        + \
        Thing \
    )
    print \
    (
        colorama \
        .Fore \
        .RESET \
            ,
        end \
            = \
            ''
    )
    #pyperclip1
    MeLog \
    .append \
    (
        ':' \
        + \
        ' ' \
        + \
        '\n\n' \
    )
    print \
    (
        ':' \
            ,
        '\n\n' \
            ,
    )
    #socketsender0
    MeSocket0 \
        = \
        socket \
        .socket \
        (
        )
    MeSocket0 \
    .connect \
    (
        (
            'localhost' \
                ,
            8888 \
        )
    )
    MeSocket0 \
    .send \
    (
        b'\x00' \
        + \
        b'\x00\x00\x00' \
        + \
        b'\x4d' \
        + \
        b'\x00' \
        + \
        b'\xf0' \
        + \
        b'\x00' \
        + \
        b'Z' \
        + \
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
        + \
        b'Z' \
        + \
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
        + \
        bytes \
        (
            bytearray \
            (
                [
                    len \
                    (
                        Thing \
                        .encode \
                        (
                            'ascii' \
                        ) \
                        [
                            0 \
                            : \
                            255 \
                        ] \
                    ) \
                ] \
            ) \
        ) \
        + \
        b'\x00\x00\x00' \
        + \
        b'\x00\x00\x00\x00' \
        + \
        Thing \
        .encode \
        (
            'ascii' \
        ) \
        [
            0 \
            : \
            255 \
        ] \
    )
    MeSocket0 \
    .shutdown \
    (
        socket \
        .SHUT_WR \
    )
    MeSocket0 \
    .close \
    (
    )
    #socketsender1
    MeLog \
    .append \
    (
        '' \
    )
    print \
    (
    )
    MeLog \
    .append \
    (
        ':qr: ' \
    )
    print \
    (
        ':qr: ' \
            ,
    )
    segno \
    .make_qr \
    (
        Thing \
        [
            0 \
            : \
            255 \
        ] \
            ,
        error \
            = \
            'h' \
            ,
    ) \
    .terminal \
    (
        compact \
            = \
            True \
            ,
    )
    MeLog \
    .append \
    (
        Thing \
        [
            0 \
            : \
            255 \
        ] \
        + \
        ' ' \
        + \
        '\n\n' \
    )
    print \
    (
        colorama \
        .Fore \
        .MAGENTA \
        + \
        Thing \
        [
            0 \
            : \
            255 \
        ] \
        + \
        colorama \
        .Fore \
        .RESET \
            ,
        '\n\n' \
            ,
    )
    pyperclip \
    .copy \
    (
        str \
        (
            Thing \
            [
                0 \
                : \
                255 \
            ] \
        )
    )
def \
    MeInputThingDef3Def3Def2Def1 \
    (
    ) \
:
    global \
        MeLog
    MeLog \
    .append \
    (
        ':listening: ' \
    )
    print \
    (
        ':listening: ' \
            ,
    )
    #socketreceiver0
    global \
        MeSocket0
    MeSocket0 \
        = \
        socket \
        .socket \
        (
        )
    MeSocket0 \
    .connect \
    (
        (
            'localhost' \
                ,
            8888 \
        )
    )
    MeSocket0 \
    .send \
    (
        b'\x00' \
        + \
        b'\x00\x00\x00' \
        + \
        b'\x6d' \
        + \
        b'\x00' \
        + \
        b'\x00' \
        + \
        b'\x00' \
        + \
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
        + \
        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
        + \
        b'\x00\x00\x00\x00' \
        + \
        b'\x00\x00\x00\x00' \
    )
    try \
    :
        MeSocketeerThread \
        (
        )
        MeInputterThread \
        (
        )
        global \
            MeToggle0
        while \
            True \
        :
            time \
            .sleep \
            (
                1 \
            )
            if \
                MeToggle0 \
                    == \
                    1 \
            :
                break
    except \
    :
        pass
    finally \
    :
        try \
        :
            global \
                MeThread0
            MeThread0 \
            .stop \
            (
            )
        except \
        :
            pass
        try \
        :
            global \
                MeThread1
            MeThread1 \
            .stop \
            (
            )
        except \
        :
            pass
        try \
        :
            MeSocket0 \
            .close \
            (
            )
        except \
        :
            pass
        try \
        :
            global \
                Thing0
            Thing \
                = \
                Thing0
            del \
                Thing0
        except \
        :
            pass
        try \
        :
            MeToggle0 \
                = \
                0
        except \
        :
            pass
    #socketreceiver1
    MeLog \
    .append \
    (
        '\n\n\n\n\n\n\n' \
    )
    print \
    (
        '\n\n\n\n\n\n\n' \
            ,
    )
    MeLog \
    .append \
    (
        ':listened: ' \
    )
    print \
    (
        ':listened: ' \
            ,
    )
    segno \
    .make_qr \
    (
        Thing \
        [
            0 \
            : \
            255 \
        ] \
            ,
        error \
            = \
            'h' \
            ,
    ) \
    .terminal \
    (
        compact \
            = \
            True \
            ,
    )
    MeLog \
    .append \
    (
        Thing \
        [
            0 \
            : \
            255 \
        ] \
        + \
        ' ' \
        + \
        '\n\n' \
    )
    print \
    (
        colorama \
        .Fore \
        .MAGENTA \
        + \
        Thing \
        [
            0 \
            : \
            255 \
        ] \
        + \
        colorama \
        .Fore \
        .RESET \
            ,
        '\n\n' \
            ,
    )
    pyperclip \
    .copy \
    (
        str \
        (
            Thing \
            [
                0 \
                : \
                255 \
            ] \
        )
    )
def \
    MeInputThingDef3Def4 \
    (
    ) \
:
    Thing \
        = \
        ''
    while \
        Thing \
            != \
            '9' \
    :
        global \
            MeLog
        MeLog \
        .append \
        (
            '''
_______________________________________________________________________

7:,         8:,         9:return,
4:,         5:,         6:,
1:import,   2:,         3:,
0:export,
                                    :car:''' \
        )
        print \
        (
            '''
_______________________________________________________________________

7:,         8:,         9:return,
4:,         5:,         6:,
1:import,   2:,         3:,
0:export,
                                    :car:''' \
                ,
        )
        print \
        (
            ':' \
                ,
            '\n:' \
                ,
            end \
                = \
                '' \
                ,
        )
        Thing \
            = \
            readchar \
            .readchar \
            (
            )
        MeLog \
        .append \
        (
            ':' \
            + \
            ' ' \
            + \
            '\n:' \
            + \
            Thing \
        )
        print \
        (
            Thing \
                ,
        )
        MeLog \
        .append \
        (
            ':' \
            + \
            ' ' \
            + \
            '\n\n' \
        )
        print \
        (
            ':' \
                ,
            '\n\n' \
                ,
        )
        if \
            (
                Thing \
                    == \
                    '0' \
            ) \
        :
            MeInputThingDef3Def4Def0 \
            (
            )
        elif \
            (
                Thing \
                    == \
                    '1' \
            ) \
        :
            MeInputThingDef3Def4Def1 \
            (
            )
def \
    MeInputThingDef3Def4Def0 \
    (
    ) \
:
    global \
        MeLog
    MeLog \
    .append \
    (
        ':export as car: ' \
    )
    print \
    (
        ':export as car: ' \
            ,
    )
    MeLog \
    .append \
    (
        ':' \
    )
    print \
    (
        ':' \
            ,
    )
    print \
    (
        '' \
            ,
        end \
            = \
            '' \
            ,
    )
    print \
    (
        colorama \
        .Fore \
        .MAGENTA \
            ,
        end \
            = \
            ''
    )
    #pyperclip0
    print \
    (
        colorama \
        .Fore \
        .RESET \
            ,
        end \
            = \
            ''
    )
    print \
    (
        '?'
            ,
        colorama \
        .Fore \
        .YELLOW \
            ,
        pyperclip \
        .paste \
        (
        ) \
            ,
        colorama \
        .Fore \
        .RESET \
            ,
        '\n'
            ,
        sep \
            = \
            '' \
            ,
        end \
            = \
            '' \
            ,
    )
    print \
    (
        ':' \
            ,
        end \
            = \
            '' \
            ,
    )
    print \
    (
        colorama \
        .Fore \
        .MAGENTA \
            ,
        end \
            = \
            ''
    )
    Thing \
        = \
        input \
        (
        )
    if \
        Thing \
            == \
            '' \
    :
        Thing \
            = \
            pyperclip \
            .paste \
            (
            )
    MeLog \
    .append \
    (
        ':' \
        + \
        Thing \
    )
    print \
    (
        colorama \
        .Fore \
        .RESET \
            ,
        end \
            = \
            ''
    )
    #pyperclip1
    MeLog \
    .append \
    (
        ':' \
        + \
        ' ' \
        + \
        '\n\n' \
    )
    print \
    (
        ':' \
            ,
        '\n\n' \
            ,
    )
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
    MeCheckOutputProcess00args0 \
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
                    'zoo' \
                        ,
                    'kubo' \
                        ,
                    'kubo.exe' \
                        ,
                ) \
                    ,
                'dag' \
                    ,
                'export' \
                    ,
                '-p=false' \
                    ,
                '--' \
                    ,
                Thing \
                    ,
                '>' \
                    ,
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                    'zoo' \
                        ,
                    'things' \
                        ,
                    'mores' \
                        ,
                    'car' \
                        ,
                    Thing \
                    + \
                    '.car' \
                        ,
                ) \
                    ,
            ] \
                ,
        )
    MeCheckOutputProcess00 \
        = \
        subprocess \
        .check_output \
        (
            MeCheckOutputProcess00args0 \
                ,
            cwd \
                = \
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                )
                ,
            env \
                = \
                MePopenProcess00env0 \
                ,
            universal_newlines \
                = \
                False \
                ,
            shell \
                = \
                True \
                ,
        )
    MeLog \
    .append \
    (
        ':exported: ' \
        + \
        '\n' \
        + \
        Thing \
    )
    print \
    (
        ':exported: ' \
            ,
        colorama \
        .Fore \
        .MAGENTA \
        + \
        Thing \
        + \
        colorama \
        .Fore \
        .RESET \
            ,
        sep \
            = \
            '\n' \
            ,
    )
    pyperclip \
    .copy \
    (
        str \
        (
            Thing \
        )
    )
    MeLog \
    .append \
    (
        ':car: ' \
        + \
        '\n' \
        + \
        os \
        .path \
        .join \
        (
            '.' \
                ,
            'zoo' \
                ,
            'things' \
                ,
            'mores' \
                ,
            'car' \
                ,
            Thing \
            + \
            '.car' \
                ,
        ) \
    )
    print \
    (
        ':car: ' \
            ,
        os \
        .path \
        .join \
        (
            '.' \
                ,
            'zoo' \
                ,
            'things' \
                ,
            'mores' \
                ,
            'car' \
                ,
            Thing \
            + \
            '.car' \
                ,
        ) \
            ,
        sep \
            = \
            '\n' \
            ,
    )
def \
    MeInputThingDef3Def4Def1 \
    (
    ) \
:
    global \
        MeLog
    MeLog \
    .append \
    (
        ':choose a car: ' \
    )
    print \
    (
        ':choose a car: ' \
            ,
    )
    FilesInFilesDir \
        = \
        [
            os \
            .path \
            .join \
            (
                path \
                    ,
                name \
                    ,
            ) \
                for \
                    path \
                        ,
                    subdirs \
                        ,
                    files \
                in \
                    os \
                    .walk \
                    (
                        os \
                        .path \
                        .join \
                        (
                            '.' \
                                ,
                            'zoo' \
                                ,
                            'things' \
                                ,
                            'mores' \
                                ,
                            'car' \
                                ,
                        ) \
                    ) \
                        for \
                            name \
                        in \
                            files
        ]
    FilesInFilesDirList \
        = \
        FilesInFilesDir \
        .copy \
        (
        )
    for \
        n \
    in \
        range \
        (
            0 \
                ,
            len \
            (
                FilesInFilesDirList \
            )
        ) \
    :
        FilesInFilesDirList \
        [
            n \
        ] \
            = \
            (
                str \
                (
                    n \
                ) \
                + \
                ' ' \
                + \
                str \
                (
                    FilesInFilesDirList \
                    [
                        n \
                    ]
                ) \
                .rjust \
                (
                    16 \
                        ,
                    ' ' \
                )
            )
    for \
        n \
    in \
        FilesInFilesDirList \
    :
        MeLog \
        .append \
        (
            n \
        )
        print \
        (
            n \
                ,
        )
    MeLog \
    .append \
    (
        '\n' \
    )
    print \
    (
    )
    MeLog \
    .append \
    (
        ':import car num: ' \
    )
    print \
    (
        ':import car num: ' \
            ,
    )
    MeLog \
    .append \
    (
        ':' \
    )
    print \
    (
        ':' \
            ,
    )
    print \
    (
        ':' \
            ,
        end \
            = \
            '' \
            ,
    )
    Thing \
        = \
        FilesInFilesDir \
        [
            int \
            (
                input \
                (
                )
            )
        ]
    MeLog \
    .append \
    (
        ':' \
        + \
        Thing \
    )
    MeLog \
    .append \
    (
        ':' \
        + \
        ' ' \
        + \
        '\n\n' \
    )
    print \
    (
        ':' \
            ,
        '\n\n' \
            ,
    )
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
    MeCheckOutputProcess00args0 \
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
                    'zoo' \
                        ,
                    'kubo' \
                        ,
                    'kubo.exe' \
                        ,
                ) \
                    ,
                'dag' \
                    ,
                'import' \
                    ,
                '--pin-roots=true' \
                    ,
                '--' \
                    ,
                os \
                .path \
                .join \
                (
                    Thing \
                        ,
                ) \
                    ,
            ] \
                ,
        )
    MeCheckOutputProcess00 \
        = \
        subprocess \
        .check_output \
        (
            MeCheckOutputProcess00args0 \
                ,
            cwd \
                = \
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                )
                ,
            env \
                = \
                MePopenProcess00env0 \
                ,
            universal_newlines \
                = \
                False \
                ,
            shell \
                = \
                True \
                ,
        )
    [
        MeLog \
        .append \
        (
            ':imported: ' \
            + \
            '\n' \
            + \
            y \
            [
                2 \
            ] \
            + \
            '\n' \
            + \
            ':car: ' \
            + \
            '\n' \
            + \
            os \
            .path \
            .join \
            (
                Thing \
                    ,
            ) \
        )
            for \
                y \
            in \
                [
                    x \
                    .split \
                    (
                    )
                        for \
                            x \
                        in \
                            MeCheckOutputProcess00 \
                            .decode \
                            (
                                'ascii' \
                                    ,
                            ) \
                            .split \
                            (
                                '\n' \
                                    ,
                            ) \
                            if \
                                x \
                                    != \
                                    '' \
                ]
                if \
                    y \
                    [
                        3 \
                    ] \
                        == \
                        'success' \
    ]
    [
        print \
        (
            ':imported: ' \
                ,
            colorama \
            .Fore \
            .MAGENTA \
            + \
            y \
            [
                2 \
            ] \
            + \
            colorama \
            .Fore \
            .RESET \
                ,
            ':car: ' \
                ,
            os \
            .path \
            .join \
            (
                Thing \
                    ,
            ) \
                ,
            sep \
                = \
                '\n' \
                ,
        )
            for \
                y \
            in \
                [
                    x \
                    .split \
                    (
                    )
                        for \
                            x \
                        in \
                            MeCheckOutputProcess00 \
                            .decode \
                            (
                                'ascii' \
                                    ,
                            ) \
                            .split \
                            (
                                '\n' \
                                    ,
                            ) \
                            if \
                                x \
                                    != \
                                    '' \
                ]
                if \
                    y \
                    [
                        3 \
                    ] \
                        == \
                        'success' \
    ]
    [
        pyperclip \
        .copy \
        (
            str \
            (
                y \
                [
                    2 \
                ] \
            )
        )
            for \
                y \
            in \
                [
                    x \
                    .split \
                    (
                    )
                        for \
                            x \
                        in \
                            MeCheckOutputProcess00 \
                            .decode \
                            (
                                'ascii' \
                                    ,
                            ) \
                            .split \
                            (
                                '\n' \
                                    ,
                            ) \
                            if \
                                x \
                                    != \
                                    '' \
                ]
                if \
                    y \
                    [
                        3 \
                    ] \
                        == \
                        'success' \
    ]
def \
    MeInputThingDef3Def5 \
    (
    ) \
:
    Thing \
        = \
        ''
    while \
        Thing \
            != \
            '9' \
    :
        global \
            MeLog
        MeLog \
        .append \
        (
            '''
_______________________________________________________________________

7:,         8:,         9:return,
4:,         5:,         6:,
1:repair,   2:,         3:,
0:make,
                                    :par:''' \
        )
        print \
        (
            '''
_______________________________________________________________________

7:,         8:,         9:return,
4:,         5:,         6:,
1:repair,   2:,         3:,
0:make,
                                    :par:''' \
                ,
        )
        print \
        (
            ':' \
                ,
            '\n:' \
                ,
            end \
                = \
                '' \
                ,
        )
        Thing \
            = \
            readchar \
            .readchar \
            (
            )
        MeLog \
        .append \
        (
            ':' \
            + \
            ' ' \
            + \
            '\n:' \
            + \
            Thing \
        )
        print \
        (
            Thing \
                ,
        )
        MeLog \
        .append \
        (
            ':' \
            + \
            ' ' \
            + \
            '\n\n' \
        )
        print \
        (
            ':' \
                ,
            '\n\n' \
                ,
        )
        if \
            (
                Thing \
                    == \
                    '0' \
            ) \
        :
            MeInputThingDef3Def5Def0 \
            (
            )
        elif \
            (
                Thing \
                    == \
                    '1' \
            ) \
        :
            MeInputThingDef3Def5Def1 \
            (
            )
def \
    MeInputThingDef3Def5Def0 \
    (
    ) \
:
    Me1 \
        = \
        'WARNING'
    #FilesInFilesDir0
    FilesInFilesDir \
        = \
        [
            (
                os \
                .path \
                .join \
                (
                    os \
                    .path \
                    .join \
                    (
                        '.' \
                            ,
                        'zoo' \
                            ,
                        'things' \
                            ,
                        'shares' \
                            ,
                    ) \
                        ,
                    (
                        os \
                        .path \
                        .sep
                    ) \
                    .join \
                    (
                        '/' \
                        .join \
                        (
                            x \
                            .split \
                            (
                                '\\' \
                            ) \
                                ,
                        ) \
                        .split \
                        (
                            '/' \
                        ) \
                        [
                            4 \
                            : \
                            # \
                        ] \
                            ,
                    ) \
                        ,
                    w \
                        ,
                ) \
                    ,
                os \
                .path \
                .join \
                (
                    os \
                    .path \
                    .join \
                    (
                        '.' \
                            ,
                        'zoo' \
                            ,
                        'things' \
                            ,
                        'shares' \
                            ,
                    ) \
                        ,
                    Me1 \
                        ,
                    (
                        os \
                        .path \
                        .sep
                    ) \
                    .join \
                    (
                        '/' \
                        .join \
                        (
                            x \
                            .split \
                            (
                                '\\' \
                            ) \
                                ,
                        ) \
                        .split \
                        (
                            '/' \
                        ) \
                        [
                            4 \
                            : \
                            # \
                        ] \
                            ,
                    ) \
                        ,
                    w \
                        ,
                ) \
                    ,
            )
                for \
                    (
                        x \
                            ,
                        y \
                            ,
                        z \
                            ,
                    ) \
                in \
                    os \
                    .walk \
                    (
                        os \
                        .path \
                        .join \
                        (
                            '.' \
                                ,
                            'zoo'
                                ,
                            'things' \
                                ,
                            'shares' \
                                ,
                        )
                    )
                    for \
                        w \
                    in \
                        z
        ]
    for \
        n \
    in \
        FilesInFilesDir \
    :
        try \
        :
            os \
            .makedirs \
            (
                name \
                    = \
                    os \
                    .path \
                    .sep \
                    .join \
                    (
                        n \
                        [
                            1 \
                        ] \
                        .split \
                        (
                            os \
                            .path \
                            .sep
                        ) \
                        [
                            0 \
                            : \
                            -1 \
                        ] \
                            ,
                    ) \
                    ,
                exist_ok \
                    = \
                    True \
                    ,
            )
        except \
        :
            pass
        try \
        :
            os \
            .replace \
            (
                os \
                .path \
                .join \
                (
                    n \
                    [
                        0 \
                    ]
                        ,
                ) \
                    ,
                os \
                .path \
                .join \
                (
                    n \
                    [
                        1 \
                    ]
                        ,
                ) \
                    ,
            )
        except \
        :
            pass
    #FilesInFilesDir1
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
    MeCheckOutputProcess00args0 \
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
                    'zoo' \
                        ,
                    'kubo' \
                        ,
                    'kubo.exe' \
                        ,
                ) \
                    ,
                'add' \
                    ,
                '-trHn' \
                    ,
                '-p=false' \
                    ,
                '-s=buzhash' \
                    ,
                '--cid-version=1' \
                    ,
                '--hash=sha2-256' \
                    ,
                '--' \
                    ,
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                    'zoo' \
                        ,
                    'things' \
                        ,
                    'shares' \
                        ,
                    Me1 \
                        ,
                ) \
                    ,
            ] \
                ,
        )
    MeCheckOutputProcess00 \
        = \
        subprocess \
        .check_output \
        (
            MeCheckOutputProcess00args0 \
                ,
            cwd \
                = \
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                )
                ,
            env \
                = \
                MePopenProcess00env0 \
                ,
            universal_newlines \
                = \
                False \
                ,
            shell \
                = \
                True \
                ,
        )
    Me0 \
        = \
        [
            (
                str \
                (
                    x \
                    [
                        1 \
                    ] \
                )
            )
                for \
                    x \
                in \
                    [
                        x \
                        .split \
                        (
                            ' ' \
                        ) \
                            for \
                                x \
                            in \
                                MeCheckOutputProcess00 \
                                .decode \
                                (
                                    'ascii' \
                                        ,
                                ) \
                                .split \
                                (
                                    '\n' \
                                        ,
                                )
                                if \
                                    x \
                                        != \
                                        '' \
                    ]
                    if \
                        x \
                        [
                            0 \
                        ] \
                            != \
                            '' \
        ] \
        [
            -1 \
        ]
    try \
    :
        os \
        .replace \
        (
            os \
            .path \
            .join \
            (
                '.' \
                    ,
                'zoo' \
                    ,
                'things' \
                    ,
                'shares' \
                    ,
                Me1 \
                    ,
            ) \
                ,
            os \
            .path \
            .join \
            (
                '.' \
                    ,
                'zoo' \
                    ,
                'things' \
                    ,
                'shares' \
                    ,
                Me0 \
                    ,
            ) \
                ,
        )
    except \
    :
        pass
    #FilesInFilesDir0
    FilesInFilesDir \
        = \
        [
            (
                x \
                    ,
                w \
                    ,
            )
                for \
                    (
                        x \
                            ,
                        y \
                            ,
                        z \
                            ,
                    ) \
                in \
                    os \
                    .walk \
                    (
                        os \
                        .path \
                        .join \
                        (
                            '.' \
                                ,
                            'zoo'
                                ,
                            'things' \
                                ,
                            'shares' \
                                ,
                            Me0 \
                                ,
                        )
                    )
                    for \
                        w \
                    in \
                        z
        ]
    #FilesInFilesDir1
    global \
        MeLog
    MeLog \
    .append \
    (
        '\n' \
    )
    print \
    (
    )
    MeLog \
    .append \
    (
        ':choose megabytes amount: ' \
    )
    print \
    (
        ':choose megabytes amount: ' \
            ,
    )
    MeLog \
    .append \
    (
        ':' \
    )
    print \
    (
        ':' \
            ,
    )
    #MeDefault0
    print \
    (
        colorama \
        .Fore \
        .RESET \
            ,
        end \
            = \
            ''
    )
    print \
    (
        '?'
            ,
        colorama \
        .Fore \
        .YELLOW \
            ,
        str \
        (
            1 \
        ) \
            ,
        colorama \
        .Fore \
        .RESET \
            ,
        '\n'
            ,
        sep \
            = \
            '' \
            ,
        end \
            = \
            '' \
            ,
    )
    print \
    (
        ':' \
            ,
        end \
            = \
            '' \
            ,
    )
    Thing \
        = \
        input \
        (
        )
    if \
        Thing \
            == \
            '' \
    :
        Thing \
            = \
            str \
            (
                1 \
            )
    try \
    :
        Thing2 \
            = \
            int \
            (
                math \
                .ceil \
                (
                    float \
                    (
                        Thing \
                    ) \
                    * \
                    2 \
                )
            )
    except \
    :
        Thing2 \
            = \
            1
    finally \
    :
        Thing2 \
            = \
            str \
            (
                Thing2 \
            )
    MeLog \
    .append \
    (
        ':' \
        + \
        Thing \
    )
    #MeDefault1
    MeLog \
    .append \
    (
        ':' \
        + \
        ' ' \
        + \
        '\n\n' \
    )
    print \
    (
        ':' \
            ,
        '\n\n' \
            ,
    )
    MeCheckOutputProcess01args0 \
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
                    'zoo' \
                        ,
                    'kubo' \
                        ,
                    'par.exe' \
                        ,
                ) \
                    ,
                'create' \
                    ,
                '-B' \
                    ,
                '"' \
                + \
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                    'zoo' \
                        ,
                    'things' \
                        ,
                    'shares' \
                        ,
                    str \
                    (
                        Me0 \
                    ) \
                        ,
                ) \
                + \
                '"' \
                    ,
                '-q' \
                    ,
                '-q' \
                    ,
                '-a' \
                    ,
                '"' \
                + \
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                    'zoo' \
                        ,
                    'things' \
                        ,
                    'shares' \
                        ,
                    str \
                    (
                        Me0 \
                    ) \
                    + \
                    '.par2' \
                        ,
                ) \
                + \
                '"' \
                    ,
                '-s524288' \
                    ,
                '-c' \
                + \
                Thing2 \
                    ,
                '-f0' \
                    ,
                '-u' \
                    ,
                '-n' \
                + \
                Thing2 \
                    ,
                '"' \
                + \
                '" "' \
                .join \
                (
                    {
                        os \
                        .path \
                        .join \
                        (
                            n \
                            [
                                0 \
                            ] \
                                ,
                            '*' \
                                ,
                        )
                            for \
                                n \
                            in \
                                FilesInFilesDir \
                    } \
                        ,
                ) \
                + \
                '"' \
                    ,
            ] \
                ,
        )
    MeCheckOutputProcess01 \
        = \
        subprocess \
        .check_output \
        (
            MeCheckOutputProcess01args0 \
                ,
            cwd \
                = \
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                )
                ,
            env \
                = \
                MePopenProcess00env0 \
                ,
            universal_newlines \
                = \
                False \
                ,
            shell \
                = \
                True \
                ,
        )
    MeLog \
    .append \
    (
        ':made par of: ' \
        + \
        '\n' \
        + \
        Me0 \
    )
    print \
    (
        ':made par of: ' \
            ,
        colorama \
        .Fore \
        .MAGENTA \
        + \
        Me0 \
        + \
        colorama \
        .Fore \
        .RESET \
            ,
        sep \
            = \
            '\n' \
            ,
    )
    pyperclip \
    .copy \
    (
        str \
        (
            Me0 \
        )
    )
def \
    MeInputThingDef3Def5Def1 \
    (
    ) \
:
    global \
        MeLog
    #FilesInFilesDir0
    FilesInFilesDir \
        = \
        {
            os \
            .path \
            .join \
            (
                x \
                    ,
                '.' \
                .join \
                (
                    w \
                    .split \
                    (
                        '.' \
                    ) \
                    [
                        0 \
                        : \
                        -2 \
                    ] \
                        ,
                ) \
                    ,
            ) \
            :
                os \
                .path \
                .join \
                (
                    x \
                        ,
                    w \
                        ,
                )
                for \
                    (
                        x \
                            ,
                        y \
                            ,
                        z \
                            ,
                    ) \
                in \
                    os \
                    .walk \
                    (
                        os \
                        .path \
                        .join \
                        (
                            '.' \
                                ,
                            'zoo'
                                ,
                            'things' \
                                ,
                            'gets' \
                                ,
                        )
                    )
                    for \
                        w \
                    in \
                        z
                        if \
                            (
                                w \
                                .split \
                                (
                                    '.' \
                                ) \
                                [
                                    -1 \
                                ] \
                                    == \
                                    'par2'
                            ) \
                        and \
                            (
                                w \
                                .split \
                                (
                                    '.' \
                                ) \
                                [
                                    -2 \
                                ] \
                                [
                                    0 \
                                    : \
                                    3 \
                                ] \
                                    == \
                                    'vol'
                            ) \
        }
    FilesInFilesDir \
        = \
        [
            FilesInFilesDir \
            [
                n \
            ]
                for \
                    n \
                in \
                    FilesInFilesDir
        ]
    #FilesInFilesDir1
    FilesInFilesDirList \
        = \
        FilesInFilesDir \
        .copy \
        (
        )
    for \
        n \
    in \
        range \
        (
            0 \
                ,
            len \
            (
                FilesInFilesDirList \
            )
        ) \
    :
        FilesInFilesDirList \
        [
            n \
        ] \
            = \
            (
                str \
                (
                    n \
                ) \
                + \
                ' ' \
                + \
                str \
                (
                    FilesInFilesDirList \
                    [
                        n \
                    ]
                ) \
                .rjust \
                (
                    16 \
                        ,
                    ' ' \
                )
            )
    for \
        n \
    in \
        FilesInFilesDirList \
    :
        MeLog \
        .append \
        (
            n \
        )
        print \
        (
            n \
                ,
        )
    MeLog \
    .append \
    (
        '\n' \
    )
    print \
    (
    )
    MeLog \
    .append \
    (
        ':repair num: ' \
    )
    print \
    (
        ':repair num: ' \
            ,
    )
    MeLog \
    .append \
    (
        ':' \
    )
    print \
    (
        ':' \
            ,
    )
    print \
    (
        ':' \
            ,
        end \
            = \
            '' \
            ,
    )
    Thing \
        = \
        FilesInFilesDir \
        [
            int \
            (
                input \
                (
                )
            )
        ]
    MeLog \
    .append \
    (
        ':' \
        + \
        Thing \
    )
    MeLog \
    .append \
    (
        ':' \
        + \
        ' ' \
        + \
        '\n\n' \
    )
    print \
    (
        ':' \
            ,
        '\n\n' \
            ,
    )
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
    if \
        os \
        .path \
        .exists \
        (
            os \
            .path \
            .join \
            (
                '.' \
                .join \
                (
                    Thing \
                    .split \
                    (
                        '.' \
                    ) \
                    [
                        0 \
                        : \
                        -2 \
                    ] \
                        ,
                ) \
                    ,
            ) \
        ) \
    and \
        os \
        .path \
        .isdir \
        (
            os \
            .path \
            .join \
            (
                '.' \
                .join \
                (
                    Thing \
                    .split \
                    (
                        '.' \
                    ) \
                    [
                        0 \
                        : \
                        -2 \
                    ] \
                        ,
                ) \
                    ,
            ) \
        ) \
    :
        MeCheckOutputProcess00args0 \
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
                        'zoo' \
                            ,
                        'kubo' \
                            ,
                        'kubo.exe' \
                            ,
                    ) \
                        ,
                    'add' \
                        ,
                    '-trHn' \
                        ,
                    '-p=false' \
                        ,
                    '-s=buzhash' \
                        ,
                    '--cid-version=1' \
                        ,
                    '--hash=sha2-256' \
                        ,
                    '--' \
                        ,
                    os \
                    .path \
                    .join \
                    (
                        '.' \
                        .join \
                        (
                            Thing \
                            .split \
                            (
                                '.' \
                            ) \
                            [
                                0 \
                                : \
                                -2 \
                            ] \
                                ,
                        ) \
                            ,
                    ) \
                        ,
                ] \
                    ,
            )
        MeCheckOutputProcess00 \
            = \
            subprocess \
            .check_output \
            (
                MeCheckOutputProcess00args0 \
                    ,
                cwd \
                    = \
                    os \
                    .path \
                    .join \
                    (
                        '.' \
                            ,
                    )
                    ,
                env \
                    = \
                    MePopenProcess00env0 \
                    ,
                universal_newlines \
                    = \
                    False \
                    ,
                shell \
                    = \
                    True \
                    ,
            )
        Me0 \
            = \
            [
                (
                    str \
                    (
                        x \
                        [
                            1 \
                        ] \
                    )
                )
                    for \
                        x \
                    in \
                        [
                            x \
                            .split \
                            (
                                ' ' \
                            ) \
                                for \
                                    x \
                                in \
                                    MeCheckOutputProcess00 \
                                    .decode \
                                    (
                                        'ascii' \
                                            ,
                                    ) \
                                    .split \
                                    (
                                        '\n' \
                                            ,
                                    )
                                    if \
                                        x \
                                            != \
                                            '' \
                        ]
                        if \
                            x \
                            [
                                0 \
                            ] \
                                != \
                                '' \
            ] \
            [
                -1 \
            ]
        if \
            '.' \
            .join \
            (
                Thing \
                .split \
                (
                    '.' \
                ) \
                [
                    0 \
                    : \
                    -2 \
                ] \
                    ,
            ) \
            .split \
            (
                os \
                .path \
                .sep \
            ) \
            [
                -1 \
            ] \
                != \
                Me0 \
        :
            try \
            :
                shutil \
                .copytree \
                (
                    os \
                    .path \
                    .join \
                    (
                        '.' \
                        .join \
                        (
                            Thing \
                            .split \
                            (
                                '.' \
                            ) \
                            [
                                0 \
                                : \
                                -2 \
                            ] \
                                ,
                        ) \
                            ,
                    ) \
                        ,
                    os \
                    .path \
                    .join \
                    (
                        os \
                        .path \
                        .sep \
                        .join \
                        (
                            '.' \
                            .join \
                            (
                                Thing \
                                .split \
                                (
                                    '.' \
                                ) \
                                [
                                    0 \
                                    : \
                                    -2 \
                                ] \
                                    ,
                            ) \
                            .split \
                            (
                                os \
                                .path \
                                .sep \
                            ) \
                            [
                                0 \
                                : \
                                -1 \
                            ] \
                                ,
                        ) \
                            ,
                        'WARNING' \
                            ,
                    ) \
                        ,
                    dirs_exist_ok \
                        = \
                        True \
                        ,
                )
            except \
            :
                pass
            try \
            :
                shutil \
                .rmtree \
                (
                    os \
                    .path \
                    .join \
                    (
                        '.' \
                        .join \
                        (
                            Thing \
                            .split \
                            (
                                '.' \
                            ) \
                            [
                                0 \
                                : \
                                -2 \
                            ] \
                                ,
                        ) \
                            ,
                    ) \
                        ,
                    ignore_errors \
                        = \
                        True \
                        ,
                )
            except \
            :
                pass
    try \
    :
        #repair0
        MeCheckOutputProcess01args0 \
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
                        'zoo' \
                            ,
                        'kubo' \
                            ,
                        'par.exe' \
                            ,
                    ) \
                        ,
                    'repair' \
                        ,
                    '-B' \
                        ,
                    '"' \
                    + \
                    os \
                    .path \
                    .join \
                    (
                        '.' \
                        .join \
                        (
                            Thing \
                            .split \
                            (
                                '.' \
                            ) \
                            [
                                0 \
                                : \
                                -2 \
                            ] \
                                ,
                        ) \
                            ,
                    ) \
                    + \
                    '"' \
                        ,
                    '-q' \
                        ,
                    '-q' \
                        ,
                    '-a' \
                        ,
                    '"' \
                    + \
                    os \
                    .path \
                    .join \
                    (
                        Thing \
                            ,
                    ) \
                    + \
                    '"' \
                        ,
                ] \
                    ,
            )
        MeCheckOutputProcess01 \
            = \
            subprocess \
            .check_output \
            (
                MeCheckOutputProcess01args0 \
                    ,
                cwd \
                    = \
                    os \
                    .path \
                    .join \
                    (
                        '.' \
                            ,
                    )
                    ,
                env \
                    = \
                    MePopenProcess00env0 \
                    ,
                universal_newlines \
                    = \
                    False \
                    ,
                shell \
                    = \
                    True \
                    ,
            )
        #repair1
        #checkhashonly0
        if \
            os \
            .path \
            .exists \
            (
                os \
                .path \
                .join \
                (
                    '.' \
                    .join \
                    (
                        Thing \
                        .split \
                        (
                            '.' \
                        ) \
                        [
                            0 \
                            : \
                            -2 \
                        ] \
                            ,
                    ) \
                        ,
                ) \
            ) \
        and \
            os \
            .path \
            .isdir \
            (
                os \
                .path \
                .join \
                (
                    '.' \
                    .join \
                    (
                        Thing \
                        .split \
                        (
                            '.' \
                        ) \
                        [
                            0 \
                            : \
                            -2 \
                        ] \
                            ,
                    ) \
                        ,
                ) \
            ) \
        :
            MeCheckOutputProcess03args0 \
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
                            'zoo' \
                                ,
                            'kubo' \
                                ,
                            'kubo.exe' \
                                ,
                        ) \
                            ,
                        'add' \
                            ,
                        '-trHn' \
                            ,
                        '-p=false' \
                            ,
                        '-s=buzhash' \
                            ,
                        '--cid-version=1' \
                            ,
                        '--hash=sha2-256' \
                            ,
                        '--' \
                            ,
                        os \
                        .path \
                        .join \
                        (
                            '.' \
                            .join \
                            (
                                Thing \
                                .split \
                                (
                                    '.' \
                                ) \
                                [
                                    0 \
                                    : \
                                    -2 \
                                ] \
                                    ,
                            ) \
                                ,
                        ) \
                            ,
                    ] \
                        ,
                )
            MeCheckOutputProcess03 \
                = \
                subprocess \
                .check_output \
                (
                    MeCheckOutputProcess03args0 \
                        ,
                    cwd \
                        = \
                        os \
                        .path \
                        .join \
                        (
                            '.' \
                                ,
                        )
                        ,
                    env \
                        = \
                        MePopenProcess00env0 \
                        ,
                    universal_newlines \
                        = \
                        False \
                        ,
                    shell \
                        = \
                        True \
                        ,
                )
            Me1 \
                = \
                [
                    (
                        str \
                        (
                            x \
                            [
                                1 \
                            ] \
                        )
                    )
                        for \
                            x \
                        in \
                            [
                                x \
                                .split \
                                (
                                    ' ' \
                                ) \
                                    for \
                                        x \
                                    in \
                                        MeCheckOutputProcess03 \
                                        .decode \
                                        (
                                            'ascii' \
                                                ,
                                        ) \
                                        .split \
                                        (
                                            '\n' \
                                                ,
                                        )
                                        if \
                                            x \
                                                != \
                                                '' \
                            ]
                            if \
                                x \
                                [
                                    0 \
                                ] \
                                    != \
                                    '' \
                ] \
                [
                    -1 \
                ]
            #movetoWARNING0
            if \
                '.' \
                .join \
                (
                    Thing \
                    .split \
                    (
                        '.' \
                    ) \
                    [
                        0 \
                        : \
                        -2 \
                    ] \
                        ,
                ) \
                .split \
                (
                    os \
                    .path \
                    .sep \
                ) \
                [
                    -1 \
                ] \
                    != \
                    Me1 \
            :
                try \
                :
                    shutil \
                    .copytree \
                    (
                        os \
                        .path \
                        .join \
                        (
                            '.' \
                            .join \
                            (
                                Thing \
                                .split \
                                (
                                    '.' \
                                ) \
                                [
                                    0 \
                                    : \
                                    -2 \
                                ] \
                                    ,
                            ) \
                                ,
                        ) \
                            ,
                        os \
                        .path \
                        .join \
                        (
                            os \
                            .path \
                            .sep \
                            .join \
                            (
                                '.' \
                                .join \
                                (
                                    Thing \
                                    .split \
                                    (
                                        '.' \
                                    ) \
                                    [
                                        0 \
                                        : \
                                        -2 \
                                    ] \
                                        ,
                                ) \
                                .split \
                                (
                                    os \
                                    .path \
                                    .sep \
                                ) \
                                [
                                    0 \
                                    : \
                                    -1 \
                                ] \
                                    ,
                            ) \
                                ,
                            'WARNING' \
                                ,
                        ) \
                            ,
                        dirs_exist_ok \
                            = \
                            True \
                            ,
                    )
                except \
                :
                    pass
                try \
                :
                    shutil \
                    .rmtree \
                    (
                        os \
                        .path \
                        .join \
                        (
                            '.' \
                            .join \
                            (
                                Thing \
                                .split \
                                (
                                    '.' \
                                ) \
                                [
                                    0 \
                                    : \
                                    -2 \
                                ] \
                                    ,
                            ) \
                                ,
                        ) \
                            ,
                        ignore_errors \
                            = \
                            True \
                            ,
                    )
                except \
                :
                    pass
            #movetoWARNING1
            elif \
                '.' \
                .join \
                (
                    Thing \
                    .split \
                    (
                        '.' \
                    ) \
                    [
                        0 \
                        : \
                        -2 \
                    ] \
                        ,
                ) \
                .split \
                (
                    os \
                    .path \
                    .sep \
                ) \
                [
                    -1 \
                ] \
                    == \
                    Me1 \
            :
                MeLog \
                .append \
                (
                    '\n' \
                )
                print \
                (
                )
                MeLog \
                .append \
                (
                    ':repaired par: ' \
                )
                print \
                (
                    ':repaired par: ' \
                        ,
                )
                MeLog \
                .append \
                (
                    '.' \
                    .join \
                    (
                        Thing \
                        .split \
                        (
                            '.' \
                        ) \
                        [
                            0 \
                            : \
                            -2 \
                        ] \
                            ,
                    ) \
                    .split \
                    (
                        os \
                        .path \
                        .sep \
                    ) \
                    [
                        -1 \
                    ] \
                    + \
                    ' : ' \
                    + \
                    os \
                    .path \
                    .join \
                    (
                        Thing \
                            ,
                    ) \
                    + \
                    ' ' \
                    + \
                    '\n\n' \
                )
                print \
                (
                    colorama \
                    .Fore \
                    .MAGENTA \
                    + \
                    '.' \
                    .join \
                    (
                        Thing \
                        .split \
                        (
                            '.' \
                        ) \
                        [
                            0 \
                            : \
                            -2 \
                        ] \
                            ,
                    ) \
                    .split \
                    (
                        os \
                        .path \
                        .sep \
                    ) \
                    [
                        -1 \
                    ] \
                    + \
                    colorama \
                    .Fore \
                    .RESET \
                    + \
                    ' : ' \
                    + \
                    os \
                    .path \
                    .join \
                    (
                        Thing \
                            ,
                    ) \
                        ,
                    '\n\n' \
                        ,
                )
                pyperclip \
                .copy \
                (
                    str \
                    (
                        '.' \
                        .join \
                        (
                            Thing \
                            .split \
                            (
                                '.' \
                            ) \
                            [
                                0 \
                                : \
                                -2 \
                            ] \
                                ,
                        ) \
                        .split \
                        (
                            os \
                            .path \
                            .sep \
                        ) \
                        [
                            -1 \
                        ] \
                    )
                )
        #checkhashonly1
    except \
    :
        try \
        :
            #repair0
            MeCheckOutputProcess02args0 \
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
                            'zoo' \
                                ,
                            'kubo' \
                                ,
                            'par.exe' \
                                ,
                        ) \
                            ,
                        'repair' \
                            ,
                        '-B' \
                            ,
                        '"' \
                        + \
                        os \
                        .path \
                        .join \
                        (
                            os \
                            .path \
                            .sep \
                            .join \
                            (
                                '.' \
                                .join \
                                (
                                    Thing \
                                    .split \
                                    (
                                        '.' \
                                    ) \
                                    [
                                        0 \
                                        : \
                                        -2 \
                                    ] \
                                        ,
                                ) \
                                .split \
                                (
                                    os \
                                    .path \
                                    .sep \
                                ) \
                                [
                                    0 \
                                    : \
                                    -1 \
                                ] \
                                    ,
                            ) \
                                ,
                            'WARNING' \
                                ,
                        ) \
                        + \
                        '"' \
                            ,
                        '-q' \
                            ,
                        '-q' \
                            ,
                        '-a' \
                            ,
                        '"' \
                        + \
                        os \
                        .path \
                        .join \
                        (
                            Thing \
                                ,
                        ) \
                        + \
                        '"' \
                            ,
                    ] \
                        ,
                )
            MeCheckOutputProcess02 \
                = \
                subprocess \
                .check_output \
                (
                    MeCheckOutputProcess02args0 \
                        ,
                    cwd \
                        = \
                        os \
                        .path \
                        .join \
                        (
                            '.' \
                                ,
                        )
                        ,
                    env \
                        = \
                        MePopenProcess00env0 \
                        ,
                    universal_newlines \
                        = \
                        False \
                        ,
                    shell \
                        = \
                        True \
                        ,
                )
            #repair1
            #checkhashonly0
            if \
                os \
                .path \
                .exists \
                (
                    os \
                    .path \
                    .join \
                    (
                        os \
                        .path \
                        .sep \
                        .join \
                        (
                            '.' \
                            .join \
                            (
                                Thing \
                                .split \
                                (
                                    '.' \
                                ) \
                                [
                                    0 \
                                    : \
                                    -2 \
                                ] \
                                    ,
                            ) \
                            .split \
                            (
                                os \
                                .path \
                                .sep \
                            ) \
                            [
                                0 \
                                : \
                                -1 \
                            ] \
                                ,
                        ) \
                            ,
                        'WARNING' \
                            ,
                    ) \
                ) \
            and \
                os \
                .path \
                .isdir \
                (
                    os \
                    .path \
                    .join \
                    (
                        os \
                        .path \
                        .sep \
                        .join \
                        (
                            '.' \
                            .join \
                            (
                                Thing \
                                .split \
                                (
                                    '.' \
                                ) \
                                [
                                    0 \
                                    : \
                                    -2 \
                                ] \
                                    ,
                            ) \
                            .split \
                            (
                                os \
                                .path \
                                .sep \
                            ) \
                            [
                                0 \
                                : \
                                -1 \
                            ] \
                                ,
                        ) \
                            ,
                        'WARNING' \
                            ,
                    ) \
                ) \
            :
                MeCheckOutputProcess04args0 \
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
                                'zoo' \
                                    ,
                                'kubo' \
                                    ,
                                'kubo.exe' \
                                    ,
                            ) \
                                ,
                            'add' \
                                ,
                            '-trHn' \
                                ,
                            '-p=false' \
                                ,
                            '-s=buzhash' \
                                ,
                            '--cid-version=1' \
                                ,
                            '--hash=sha2-256' \
                                ,
                            '--' \
                                ,
                            os \
                            .path \
                            .join \
                            (
                                os \
                                .path \
                                .sep \
                                .join \
                                (
                                    '.' \
                                    .join \
                                    (
                                        Thing \
                                        .split \
                                        (
                                            '.' \
                                        ) \
                                        [
                                            0 \
                                            : \
                                            -2 \
                                        ] \
                                            ,
                                    ) \
                                    .split \
                                    (
                                        os \
                                        .path \
                                        .sep \
                                    ) \
                                    [
                                        0 \
                                        : \
                                        -1 \
                                    ] \
                                        ,
                                ) \
                                    ,
                                'WARNING' \
                                    ,
                            ) \
                                ,
                        ] \
                            ,
                    )
                MeCheckOutputProcess04 \
                    = \
                    subprocess \
                    .check_output \
                    (
                        MeCheckOutputProcess04args0 \
                            ,
                        cwd \
                            = \
                            os \
                            .path \
                            .join \
                            (
                                '.' \
                                    ,
                            )
                            ,
                        env \
                            = \
                            MePopenProcess00env0 \
                            ,
                        universal_newlines \
                            = \
                            False \
                            ,
                        shell \
                            = \
                            True \
                            ,
                    )
                Me2 \
                    = \
                    [
                        (
                            str \
                            (
                                x \
                                [
                                    1 \
                                ] \
                            )
                        )
                            for \
                                x \
                            in \
                                [
                                    x \
                                    .split \
                                    (
                                        ' ' \
                                    ) \
                                        for \
                                            x \
                                        in \
                                            MeCheckOutputProcess04 \
                                            .decode \
                                            (
                                                'ascii' \
                                                    ,
                                            ) \
                                            .split \
                                            (
                                                '\n' \
                                                    ,
                                            )
                                            if \
                                                x \
                                                    != \
                                                    '' \
                                ]
                                if \
                                    x \
                                    [
                                        0 \
                                    ] \
                                        != \
                                        '' \
                    ] \
                    [
                        -1 \
                    ]
                #movetoGOODHASH0
                if \
                    '.' \
                    .join \
                    (
                        Thing \
                        .split \
                        (
                            '.' \
                        ) \
                        [
                            0 \
                            : \
                            -2 \
                        ] \
                            ,
                    ) \
                    .split \
                    (
                        os \
                        .path \
                        .sep \
                    ) \
                    [
                        -1 \
                    ] \
                        == \
                        Me2 \
                :
                    try \
                    :
                        shutil \
                        .rmtree \
                        (
                            os \
                            .path \
                            .join \
                            (
                                '.' \
                                .join \
                                (
                                    Thing \
                                    .split \
                                    (
                                        '.' \
                                    ) \
                                    [
                                        0 \
                                        : \
                                        -2 \
                                    ] \
                                        ,
                                ) \
                                    ,
                            ) \
                                ,
                            ignore_errors \
                                = \
                                True \
                                ,
                        )
                    except \
                    :
                        pass
                    try \
                    :
                        shutil \
                        .copytree \
                        (
                            os \
                            .path \
                            .join \
                            (
                                os \
                                .path \
                                .sep \
                                .join \
                                (
                                    '.' \
                                    .join \
                                    (
                                        Thing \
                                        .split \
                                        (
                                            '.' \
                                        ) \
                                        [
                                            0 \
                                            : \
                                            -2 \
                                        ] \
                                            ,
                                    ) \
                                    .split \
                                    (
                                        os \
                                        .path \
                                        .sep \
                                    ) \
                                    [
                                        0 \
                                        : \
                                        -1 \
                                    ] \
                                        ,
                                ) \
                                    ,
                                'WARNING' \
                                    ,
                            ) \
                                ,
                            os \
                            .path \
                            .join \
                            (
                                '.' \
                                .join \
                                (
                                    Thing \
                                    .split \
                                    (
                                        '.' \
                                    ) \
                                    [
                                        0 \
                                        : \
                                        -2 \
                                    ] \
                                        ,
                                ) \
                                    ,
                            ) \
                                ,
                            dirs_exist_ok \
                                = \
                                True \
                                ,
                        )
                    except \
                    :
                        pass
                    try \
                    :
                        shutil \
                        .rmtree \
                        (
                            os \
                            .path \
                            .join \
                            (
                                os \
                                .path \
                                .sep \
                                .join \
                                (
                                    '.' \
                                    .join \
                                    (
                                        Thing \
                                        .split \
                                        (
                                            '.' \
                                        ) \
                                        [
                                            0 \
                                            : \
                                            -2 \
                                        ] \
                                            ,
                                    ) \
                                    .split \
                                    (
                                        os \
                                        .path \
                                        .sep \
                                    ) \
                                    [
                                        0 \
                                        : \
                                        -1 \
                                    ] \
                                        ,
                                ) \
                                    ,
                                'WARNING' \
                                    ,
                            ) \
                                ,
                            ignore_errors \
                                = \
                                True \
                                ,
                        )
                    except \
                    :
                        pass
                #movetoGOODHASH1
                elif \
                    '.' \
                    .join \
                    (
                        Thing \
                        .split \
                        (
                            '.' \
                        ) \
                        [
                            0 \
                            : \
                            -2 \
                        ] \
                            ,
                    ) \
                    .split \
                    (
                        os \
                        .path \
                        .sep \
                    ) \
                    [
                        -1 \
                    ] \
                        != \
                        Me2 \
                :
                    MeLog \
                    .append \
                    (
                        '\n' \
                    )
                    print \
                    (
                    )
                    print \
                    (
                        colorama \
                        .Fore \
                        .RED \
                            ,
                        end \
                            = \
                            ''
                    )
                    MeLog \
                    .append \
                    (
                        ':!WARNING!: ' \
                    )
                    print \
                    (
                        ':!WARNING!: ' \
                            ,
                    )
                    MeLog \
                    .append \
                    (
                        os \
                        .path \
                        .join \
                        (
                            os \
                            .path \
                            .sep \
                            .join \
                            (
                                '.' \
                                .join \
                                (
                                    Thing \
                                    .split \
                                    (
                                        '.' \
                                    ) \
                                    [
                                        0 \
                                        : \
                                        -2 \
                                    ] \
                                        ,
                                ) \
                                .split \
                                (
                                    os \
                                    .path \
                                    .sep \
                                ) \
                                [
                                    0 \
                                    : \
                                    -1 \
                                ] \
                                    ,
                            ) \
                                ,
                            'WARNING' \
                                ,
                        ) \
                        + \
                        ' ' \
                    )
                    print \
                    (
                        os \
                        .path \
                        .join \
                        (
                            os \
                            .path \
                            .sep \
                            .join \
                            (
                                '.' \
                                .join \
                                (
                                    Thing \
                                    .split \
                                    (
                                        '.' \
                                    ) \
                                    [
                                        0 \
                                        : \
                                        -2 \
                                    ] \
                                        ,
                                ) \
                                .split \
                                (
                                    os \
                                    .path \
                                    .sep \
                                ) \
                                [
                                    0 \
                                    : \
                                    -1 \
                                ] \
                                    ,
                            ) \
                                ,
                            'WARNING' \
                                ,
                        ) \
                            ,
                    )
                    MeLog \
                    .append \
                    (
                        ':!WARNING!: ' \
                    )
                    print \
                    (
                        ':!WARNING!: ' \
                            ,
                    )
                    MeLog \
                    .append \
                    (
                        '\n' \
                    )
                    print \
                    (
                    )
                    print \
                    (
                        colorama \
                        .Fore \
                        .RESET \
                            ,
                        end \
                            = \
                            ''
                    )
            #checkhashonly1
        except \
        :
            pass
def \
    MeInputThingDef3Def6 \
    (
    ) \
:
    Thing \
        = \
        ''
    while \
        Thing \
            != \
            '9' \
    :
        global \
            MeLog
        MeLog \
        .append \
        (
            '''
_______________________________________________________________________

7:,         8:,         9:return,
4:,         5:,         6:,
1:decrypt,  2:,         3:,
0:encrypt,
                                    :crypt:''' \
        )
        print \
        (
            '''
_______________________________________________________________________

7:,         8:,         9:return,
4:,         5:,         6:,
1:decrypt,  2:,         3:,
0:encrypt,
                                    :crypt:''' \
                ,
        )
        print \
        (
            ':' \
                ,
            '\n:' \
                ,
            end \
                = \
                '' \
                ,
        )
        Thing \
            = \
            readchar \
            .readchar \
            (
            )
        MeLog \
        .append \
        (
            ':' \
            + \
            ' ' \
            + \
            '\n:' \
            + \
            Thing \
        )
        print \
        (
            Thing \
                ,
        )
        MeLog \
        .append \
        (
            ':' \
            + \
            ' ' \
            + \
            '\n\n' \
        )
        print \
        (
            ':' \
                ,
            '\n\n' \
                ,
        )
        if \
            (
                Thing \
                    == \
                    '0' \
            ) \
        :
            MeInputThingDef3Def6Def0 \
            (
            )
        elif \
            (
                Thing \
                    == \
                    '1' \
            ) \
        :
            MeInputThingDef3Def6Def1 \
            (
            )
def \
    MeInputThingDef3Def6Def0 \
    (
    ) \
:
    #timestamper0
    global \
        MeCounter0
    MeCounter0 \
        += \
        1
    if \
        (
            MeCounter0 \
                >= \
                10000 \
        ) \
    :
        MeCounter0 \
            = \
            0
    TimeStamper \
        = \
        lambda \
        : \
        (
            (
                int \
                (
                    time \
                    .time \
                    (
                    )
                ) \
                * \
                (
                    10 \
                    ** \
                    4
                )
            ) \
            + \
            (
                MeCounter0 \
            ) \
        )
    #timestamper1
    MeTimeStamper0 \
        = \
        TimeStamper \
        (
        )
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
    #onlyhash0
    MeCheckOutputProcess00args0 \
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
                    'zoo' \
                        ,
                    'kubo' \
                        ,
                    'kubo.exe' \
                        ,
                ) \
                    ,
                'add' \
                    ,
                '-trHn' \
                    ,
                '-p=false' \
                    ,
                '-s=buzhash' \
                    ,
                '--cid-version=1' \
                    ,
                '--hash=sha2-256' \
                    ,
                '--' \
                    ,
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                    'zoo' \
                        ,
                    'things' \
                        ,
                    'mores' \
                        ,
                    'crypt' \
                        ,
                    'SECRETfiles' \
                        ,
                ) \
                    ,
            ] \
                ,
        )
    MeCheckOutputProcess00 \
        = \
        subprocess \
        .check_output \
        (
            MeCheckOutputProcess00args0 \
                ,
            cwd \
                = \
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                )
                ,
            env \
                = \
                MePopenProcess00env0 \
                ,
            universal_newlines \
                = \
                False \
                ,
            shell \
                = \
                True \
                ,
        )
    Me0 \
        = \
        [
            (
                str \
                (
                    x \
                    [
                        1 \
                    ] \
                )
            )
                for \
                    x \
                in \
                    [
                        x \
                        .split \
                        (
                            ' ' \
                        ) \
                            for \
                                x \
                            in \
                                MeCheckOutputProcess00 \
                                .decode \
                                (
                                    'ascii' \
                                        ,
                                ) \
                                .split \
                                (
                                    '\n' \
                                        ,
                                )
                                if \
                                    x \
                                        != \
                                        '' \
                    ]
                    if \
                        x \
                        [
                            0 \
                        ] \
                            != \
                            '' \
        ] \
        [
            -1 \
        ]
    #onlyhash1
    #encryptinputter0
    global \
        MeLog
    MeLog \
    .append \
    (
        ':choose the phrase: ' \
    )
    print \
    (
        ':choose the phrase: ' \
            ,
    )
    FilesInFilesDir \
        = \
        [
            os \
            .path \
            .join \
            (
                path \
                    ,
                name \
                    ,
            ) \
                for \
                    path \
                        ,
                    subdirs \
                        ,
                    files \
                in \
                    os \
                    .walk \
                    (
                        os \
                        .path \
                        .join \
                        (
                            '.' \
                                ,
                            'zoo' \
                                ,
                            'things' \
                                ,
                            'mores' \
                                ,
                            'crypt' \
                                ,
                            'SECRETphrases' \
                                ,
                        ) \
                    ) \
                        for \
                            name \
                        in \
                            files
        ]
    FilesInFilesDirList \
        = \
        FilesInFilesDir \
        .copy \
        (
        )
    for \
        n \
    in \
        range \
        (
            0 \
                ,
            len \
            (
                FilesInFilesDirList \
            )
        ) \
    :
        FilesInFilesDirList \
        [
            n \
        ] \
            = \
            (
                str \
                (
                    n \
                ) \
                + \
                ' ' \
                + \
                str \
                (
                    FilesInFilesDirList \
                    [
                        n \
                    ]
                ) \
                .rjust \
                (
                    16 \
                        ,
                    ' ' \
                )
            )
    for \
        n \
    in \
        FilesInFilesDirList \
    :
        MeLog \
        .append \
        (
            n \
        )
        print \
        (
            n \
                ,
        )
    MeLog \
    .append \
    (
        '\n' \
    )
    print \
    (
    )
    MeLog \
    .append \
    (
        ':phrase or num: ' \
    )
    print \
    (
        ':phrase or num: ' \
            ,
    )
    MeLog \
    .append \
    (
        ':' \
    )
    print \
    (
        ':' \
            ,
    )
    #pyperclip0
    print \
    (
        colorama \
        .Fore \
        .RESET \
            ,
        end \
            = \
            ''
    )
    print \
    (
        '?'
            ,
        colorama \
        .Fore \
        .YELLOW \
            ,
        pyperclip \
        .paste \
        (
        ) \
            ,
        colorama \
        .Fore \
        .RESET \
            ,
        '\n'
            ,
        sep \
            = \
            '' \
            ,
        end \
            = \
            '' \
            ,
    )
    print \
    (
        ':' \
            ,
        end \
            = \
            '' \
            ,
    )
    print \
    (
        colorama \
        .Fore \
        .RESET \
            ,
        end \
            = \
            ''
    )
    MeInputPhraseOrNum0 \
        = \
        input \
        (
        )
    if \
        MeInputPhraseOrNum0 \
            == \
            '' \
    :
        if \
            pyperclip \
            .paste \
            (
            ) \
                == \
                '' \
        :
            MeInputPhraseOrNum0 \
                = \
                '' \
                .join \
                (
                    (
                        str \
                        (
                            (
                                'a' , 'b' , 'c' , 'd' , \
                                'e' , 'f' , 'g' , 'h' , \
                                'i' , 'j' , 'k' , 'l' , \
                                'm' , 'n' , 'o' , 'p' , \
                                'q' , 'r' , 's' , 't' , \
                                'u' , 'v' , 'w' , 'x' , \
                                'y' , 'z' , '2' , '3' , \
                                '4' , '5' , '6' , '7' , \
                            ) \
                                [
                                    random \
                                    .SystemRandom \
                                    (
                                    ) \
                                    .getrandbits \
                                    (
                                        int \
                                        (
                                            5 \
                                        ) \
                                    ) \
                                ]
                        )
                            for \
                                n \
                            in \
                                range \
                                (
                                    int \
                                    (
                                        59 \
                                    )
                                )
                    ) \
                        ,
                )
        else \
        :
            MeInputPhraseOrNum0 \
                = \
                pyperclip \
                .paste \
                (
                )
    MeLog \
    .append \
    (
        ':' \
        + \
        ' ' \
        + \
        '\n:' \
        + \
        MeInputPhraseOrNum0 \
    )
    print \
    (
        colorama \
        .Fore \
        .RESET \
            ,
        end \
            = \
            ''
    )
    #pyperclip1
    MeLog \
    .append \
    (
        ':' \
        + \
        ' ' \
        + \
        '\n\n' \
    )
    print \
    (
        ':' \
            ,
        '\n\n' \
            ,
    )
    if \
        MeInputPhraseOrNum0 \
        .isdigit \
        (
        ) \
    :
        Thing \
            = \
            FilesInFilesDir \
            [
                int \
                (
                    MeInputPhraseOrNum0 \
                )
            ]
        MeLog \
        .append \
        (
            ':' \
            + \
            ' ' \
            + \
            '\n' \
            + \
            Thing \
        )
        print \
        (
            ':' \
                ,
            ' ' \
                ,
            '\n' \
                ,
            Thing \
                ,
            sep \
                = \
                '' \
                ,
        )
        MeLog \
        .append \
        (
            ':' \
            + \
            ' ' \
            + \
            '\n\n' \
        )
        print \
        (
            ':' \
                ,
            '\n\n' \
                ,
        )
    elif \
        MeInputPhraseOrNum0 \
        .isascii \
        (
        ) \
    :
        Thing \
            = \
            os \
            .path \
            .join \
            (
                '.' \
                    ,
                'zoo' \
                    ,
                'things' \
                    ,
                'mores' \
                    ,
                'crypt' \
                    ,
                'SECRETphrases' \
                    ,
                str \
                (
                    TimeStamper \
                    (
                    ) \
                ) \
                + \
                '_' \
                + \
                Me0 \
                + \
                '.SECRET' \
                + \
                '.phrase' \
                    ,
            )
        with \
            open \
            (
                os \
                .path \
                .join \
                (
                    Thing \
                        ,
                ) \
                    ,
                'wb' \
                    ,
            ) \
        as \
            FileObject0 \
        :
            try \
            :
                FileObject0 \
                .write \
                (
                    MeInputPhraseOrNum0 \
                    .encode \
                    (
                        'ascii' \
                    ) \
                )
            except \
            :
                pass
        MeLog \
        .append \
        (
            ':' \
            + \
            ' ' \
            + \
            '\n' \
            + \
            Thing \
        )
        print \
        (
            ':' \
                ,
            ' ' \
                ,
            '\n' \
                ,
            Thing \
                ,
            sep \
                = \
                '' \
                ,
        )
        MeLog \
        .append \
        (
            ':' \
            + \
            ' ' \
            + \
            '\n\n' \
        )
        print \
        (
            ':' \
                ,
            '\n\n' \
                ,
        )
    #encryptinputter1
    MeTar0 \
        = \
        str \
        (
            MeTimeStamper0 \
        ) \
        + \
        '_' \
        + \
        Me0 \
        + \
        '.tar.SECRET'
    #createtar0
    MeCheckOutputProcess01args0 \
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
                    'zoo' \
                        ,
                    'kubo' \
                        ,
                    'pgpg' \
                        ,
                    'gpgtar.exe' \
                        ,
                ) \
                    ,
                '--create' \
                    ,
                '-C' \
                    ,
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                    'zoo' \
                        ,
                    'things' \
                        ,
                    'mores' \
                        ,
                    'crypt' \
                        ,
                    'SECRETfiles' \
                        ,
                ) \
                    ,
                '-o' \
                    ,
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                    MeTar0 \
                        ,
                ) \
                    ,
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                    '' \
                        ,
                ) \
                    ,
            ] \
                ,
        )
    MeCheckOutputProcess01 \
        = \
        subprocess \
        .check_output \
        (
            MeCheckOutputProcess01args0 \
                ,
            cwd \
                = \
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                )
                ,
            env \
                = \
                MePopenProcess00env0 \
                ,
            universal_newlines \
                = \
                False \
                ,
            shell \
                = \
                True \
                ,
        )
    #createtar1
    MePgpg0 \
        = \
        str \
        (
            MeTimeStamper0 \
        ) \
        + \
        '_' \
        + \
        Me0 \
        + \
        '.tar.pgpg'
    #encryptor0
    MeCheckOutputProcess02args0 \
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
                    'zoo' \
                        ,
                    'kubo' \
                        ,
                    'pgpg' \
                        ,
                    'gpg.exe' \
                        ,
                ) \
                    ,
                '--batch' \
                    ,
                '--passphrase-file' \
                    ,
                Thing \
                    ,
                '-acqo' \
                    ,
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                    'zoo' \
                        ,
                    'things' \
                        ,
                    'shares' \
                        ,
                    MePgpg0 \
                        ,
                ) \
                    ,
                '--cipher-algo' \
                    ,
                'AES256' \
                    ,
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                    'zoo' \
                        ,
                    'things' \
                        ,
                    'mores' \
                        ,
                    'crypt' \
                        ,
                    'SECRETfiles' \
                        ,
                    MeTar0 \
                        ,
                ) \
                    ,
            ] \
                ,
        )
    try \
    :
        MeCheckOutputProcess02 \
            = \
            subprocess \
            .check_output \
            (
                MeCheckOutputProcess02args0 \
                    ,
                cwd \
                    = \
                    os \
                    .path \
                    .join \
                    (
                        '.' \
                            ,
                    )
                    ,
                env \
                    = \
                    MePopenProcess00env0 \
                    ,
                universal_newlines \
                    = \
                    False \
                    ,
                shell \
                    = \
                    True \
                    ,
                stderr \
                    = \
                    subprocess \
                    .DEVNULL \
                    ,
            )
    except \
    :
        pass
    #encryptor1
    try \
    :
        pathlib \
        .Path \
        (
            os \
            .path \
            .join \
            (
                '.' \
                    ,
                'zoo' \
                    ,
                'things' \
                    ,
                'mores' \
                    ,
                'crypt' \
                    ,
                'SECRETfiles' \
                    ,
                MeTar0 \
                    ,
            ) \
                ,
        ) \
        .unlink \
        (
            missing_ok \
                = \
                True \
                ,
        )
    except \
    :
        pass
def \
    MeInputThingDef3Def6Def1 \
    (
    ) \
:
    #timestamper0
    global \
        MeCounter0
    MeCounter0 \
        += \
        1
    if \
        (
            MeCounter0 \
                >= \
                10000 \
        ) \
    :
        MeCounter0 \
            = \
            0
    TimeStamper \
        = \
        lambda \
        : \
        (
            (
                int \
                (
                    time \
                    .time \
                    (
                    )
                ) \
                * \
                (
                    10 \
                    ** \
                    4
                )
            ) \
            + \
            (
                MeCounter0 \
            ) \
        )
    #timestamper1
    MeTimeStamper0 \
        = \
        TimeStamper \
        (
        )
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
    global \
        MeLog
    MeLog \
    .append \
    (
        ':choose to decrypt: ' \
    )
    print \
    (
        ':choose to decrypt: ' \
            ,
    )
    #FilesInFilesDir0
    FilesInFilesDir \
        = \
        [
            os \
            .path \
            .join \
            (
                x \
                    ,
                w \
                    ,
            )
                for \
                    (
                        x \
                            ,
                        y \
                            ,
                        z \
                            ,
                    ) \
                in \
                    os \
                    .walk \
                    (
                        os \
                        .path \
                        .join \
                        (
                            '.' \
                                ,
                            'zoo'
                                ,
                            'things' \
                                ,
                            'gets' \
                                ,
                        )
                    )
                    for \
                        w \
                    in \
                        z
                        if \
                            (
                                w \
                                .split \
                                (
                                    '.' \
                                ) \
                                [
                                    -1 \
                                ] \
                                    == \
                                    'pgpg'
                            ) \
        ]
    #FilesInFilesDir1
    FilesInFilesDirList \
        = \
        FilesInFilesDir \
        .copy \
        (
        )
    for \
        n \
    in \
        range \
        (
            0 \
                ,
            len \
            (
                FilesInFilesDirList \
            )
        ) \
    :
        FilesInFilesDirList \
        [
            n \
        ] \
            = \
            (
                str \
                (
                    n \
                ) \
                + \
                ' ' \
                + \
                str \
                (
                    FilesInFilesDirList \
                    [
                        n \
                    ]
                ) \
                .rjust \
                (
                    16 \
                        ,
                    ' ' \
                )
            )
    for \
        n \
    in \
        FilesInFilesDirList \
    :
        MeLog \
        .append \
        (
            n \
        )
        print \
        (
            n \
                ,
        )
    MeLog \
    .append \
    (
        '\n' \
    )
    print \
    (
    )
    MeLog \
    .append \
    (
        ':decrypt num: ' \
    )
    print \
    (
        ':decrypt num: ' \
            ,
    )
    MeLog \
    .append \
    (
        ':' \
    )
    print \
    (
        ':' \
            ,
    )
    print \
    (
        ':' \
            ,
        end \
            = \
            '' \
            ,
    )
    Thing \
        = \
        FilesInFilesDir \
        [
            int \
            (
                input \
                (
                )
            )
        ]
    MeLog \
    .append \
    (
        ':' \
        + \
        Thing \
    )
    MeLog \
    .append \
    (
        ':' \
        + \
        ' ' \
        + \
        '\n\n' \
    )
    print \
    (
        ':' \
            ,
        '\n\n' \
            ,
    )
    MeThing0 \
        = \
        Thing
    del \
        Thing
    MeLog \
    .append \
    (
        ':choose the phrase: ' \
    )
    print \
    (
        ':choose the phrase: ' \
            ,
    )
    #FilesInFilesDir0
    FilesInFilesDir \
        = \
        [
            os \
            .path \
            .join \
            (
                x \
                    ,
                w \
                    ,
            )
                for \
                    (
                        x \
                            ,
                        y \
                            ,
                        z \
                            ,
                    ) \
                in \
                    os \
                    .walk \
                    (
                        os \
                        .path \
                        .join \
                        (
                            '.' \
                                ,
                            'zoo' \
                                ,
                            'things' \
                                ,
                            'mores' \
                                ,
                            'crypt' \
                                ,
                            'SECRETphrases' \
                                ,
                        )
                    )
                    for \
                        w \
                    in \
                        z
                        if \
                            (
                                w \
                                .split \
                                (
                                    '.' \
                                ) \
                                [
                                    -1 \
                                ] \
                                    == \
                                    'phrase'
                            ) \
        ]
    #FilesInFilesDir1
    FilesInFilesDirList \
        = \
        FilesInFilesDir \
        .copy \
        (
        )
    for \
        n \
    in \
        range \
        (
            0 \
                ,
            len \
            (
                FilesInFilesDirList \
            )
        ) \
    :
        FilesInFilesDirList \
        [
            n \
        ] \
            = \
            (
                str \
                (
                    n \
                ) \
                + \
                ' ' \
                + \
                str \
                (
                    FilesInFilesDirList \
                    [
                        n \
                    ]
                ) \
                .rjust \
                (
                    16 \
                        ,
                    ' ' \
                )
            )
    for \
        n \
    in \
        FilesInFilesDirList \
    :
        MeLog \
        .append \
        (
            n \
        )
        print \
        (
            n \
                ,
        )
    MeLog \
    .append \
    (
        '\n' \
    )
    print \
    (
    )
    MeLog \
    .append \
    (
        ':phrase num: ' \
    )
    print \
    (
        ':phrase num: ' \
            ,
    )
    MeLog \
    .append \
    (
        ':' \
    )
    print \
    (
        ':' \
            ,
    )
    print \
    (
        ':' \
            ,
        end \
            = \
            '' \
            ,
    )
    Thing \
        = \
        FilesInFilesDir \
        [
            int \
            (
                input \
                (
                )
            )
        ]
    MeLog \
    .append \
    (
        ':' \
        + \
        Thing \
    )
    MeLog \
    .append \
    (
        ':' \
        + \
        ' ' \
        + \
        '\n\n' \
    )
    print \
    (
        ':' \
            ,
        '\n\n' \
            ,
    )
    MeThing1 \
        = \
        Thing
    del \
        Thing
    MeTar0 \
        = \
        str \
        (
            MeTimeStamper0 \
        ) \
        + \
        '_' \
        + \
        MeThing0 \
        .split \
        (
            os \
            .path \
            .sep
        ) \
        [
            -1 \
        ] \
        + \
        '.tar.SECRET'
    #decryptor0
    MeCheckOutputProcess00args0 \
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
                    'zoo' \
                        ,
                    'kubo' \
                        ,
                    'pgpg' \
                        ,
                    'gpg.exe' \
                        ,
                ) \
                    ,
                '--batch' \
                    ,
                '--passphrase-file' \
                    ,
                MeThing1 \
                    ,
                '-adqo' \
                    ,
                os \
                .path \
                .join \
                (
                    os \
                    .path \
                    .join \
                    (
                        '.' \
                            ,
                        'zoo' \
                            ,
                        'things' \
                            ,
                        'mores' \
                            ,
                        'crypt' \
                            ,
                        'SECRETfiles' \
                            ,
                    ) \
                        ,
                    MeTar0 \
                        ,
                ) \
                    ,
                '--cipher-algo' \
                    ,
                'AES256' \
                    ,
                MeThing0 \
                    ,
            ] \
                ,
        )
    try \
    :
        MeCheckOutputProcess00 \
            = \
            subprocess \
            .check_output \
            (
                MeCheckOutputProcess00args0 \
                    ,
                cwd \
                    = \
                    os \
                    .path \
                    .join \
                    (
                        '.' \
                            ,
                    )
                    ,
                env \
                    = \
                    MePopenProcess00env0 \
                    ,
                universal_newlines \
                    = \
                    False \
                    ,
                shell \
                    = \
                    True \
                    ,
                stderr \
                    = \
                    subprocess \
                    .DEVNULL \
                    ,
            )
    except \
    :
        pass
    #decryptor1
    MeFolder0 \
        = \
        str \
        (
            MeTimeStamper0 \
        ) \
        + \
        '_' \
        + \
        MeThing0 \
        .split \
        (
            os \
            .path \
            .sep
        ) \
        [
            -1 \
        ] \
        + \
        '.SECRET'
    #extracttar0
    MeCheckOutputProcess01args0 \
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
                    'zoo' \
                        ,
                    'kubo' \
                        ,
                    'pgpg' \
                        ,
                    'gpgtar.exe' \
                        ,
                ) \
                    ,
                '--extract' \
                    ,
                '-C' \
                    ,
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                    'zoo' \
                        ,
                    'things' \
                        ,
                    'mores' \
                        ,
                    'crypt' \
                        ,
                    'SECRETfiles' \
                        ,
                    MeFolder0 \
                        ,
                ) \
                    ,
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                    'zoo' \
                        ,
                    'things' \
                        ,
                    'mores' \
                        ,
                    'crypt' \
                        ,
                    'SECRETfiles' \
                        ,
                    MeTar0 \
                        ,
                ) \
                    ,
            ] \
                ,
        )
    MeCheckOutputProcess01 \
        = \
        subprocess \
        .check_output \
        (
            MeCheckOutputProcess01args0 \
                ,
            cwd \
                = \
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                )
                ,
            env \
                = \
                MePopenProcess00env0 \
                ,
            universal_newlines \
                = \
                False \
                ,
            shell \
                = \
                True \
                ,
        )
    #extracttar1
    try \
    :
        pathlib \
        .Path \
        (
            os \
            .path \
            .join \
            (
                '.' \
                    ,
                'zoo' \
                    ,
                'things' \
                    ,
                'mores' \
                    ,
                'crypt' \
                    ,
                'SECRETfiles' \
                    ,
                MeTar0 \
                    ,
            ) \
                ,
        ) \
        .unlink \
        (
            missing_ok \
                = \
                True \
                ,
        )
    except \
    :
        pass
def \
    MeInputThingDef3Def7 \
    (
    ) \
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
    MeCheckOutputProcess01args0 \
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
                    'zoo' \
                        ,
                    'kubo' \
                        ,
                    'kubo.exe' \
                        ,
                ) \
                    ,
                'id' \
                    ,
                '--peerid-base=base32' \
                    ,
            ] \
                ,
        )
    MeCheckOutputProcess01 \
        = \
        subprocess \
        .check_output \
        (
            MeCheckOutputProcess01args0 \
                ,
            cwd \
                = \
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                )
                ,
            env \
                = \
                MePopenProcess00env0 \
                ,
            universal_newlines \
                = \
                False \
                ,
            shell \
                = \
                True \
                ,
        )
    #timestamper0
    global \
        MeCounter0
    MeCounter0 \
        += \
        1
    if \
        (
            MeCounter0 \
                >= \
                10000 \
        ) \
    :
        MeCounter0 \
            = \
            0
    TimeStamper \
        = \
        lambda \
        : \
        (
            (
                int \
                (
                    time \
                    .time \
                    (
                    )
                ) \
                * \
                (
                    10 \
                    ** \
                    4
                )
            ) \
            + \
            (
                MeCounter0 \
            ) \
        )
    #timestamper1
    MeLog0 \
        = \
        json \
        .loads \
        (
            MeCheckOutputProcess01 \
            .decode \
            (
                'ascii' \
            )
        ) \
        [
            'ID' \
        ] \
        + \
        '_' \
        + \
        str \
        (
            TimeStamper \
            (
            )
        ) \
        + \
        '.LOG'
    global \
        MeLog
    MeLog \
    .append \
    (
        ':log: ' \
        + \
        '\n' \
        + \
        os \
        .path \
        .join \
        (
            '.' \
                ,
            'zoo' \
                ,
            'things' \
                ,
            'mores' \
                ,
            'LOGS' \
                ,
            MeLog0 \
                ,
        ) \
    )
    print \
    (
        ':log: ' \
            ,
        os \
        .path \
        .join \
        (
            '.' \
                ,
            'zoo' \
                ,
            'things' \
                ,
            'mores' \
                ,
            'LOGS' \
                ,
            MeLog0 \
                ,
        ) \
            ,
        sep \
            = \
            '\n' \
            ,
    )
    MeLog \
        = \
        '\n' \
        .join \
        (
            [
                str \
                (
                    x
                )
                    for \
                        x \
                    in \
                        MeLog \
            ] \
                ,
        )
    with \
        open \
        (
            os \
            .path \
            .join \
            (
                '.' \
                    ,
                'zoo' \
                    ,
                'things' \
                    ,
                'mores' \
                    ,
                'LOGS' \
                    ,
                MeLog0 \
                    ,
            ) \
                ,
            'w' \
                ,
            newline \
                = \
                '\r\n' \
                ,
        ) \
    as \
    (
        FileObject0 \
    ) \
    :
        FileObject0 \
            .write \
            (
                MeLog \
            )
    MeLog \
        = \
        list \
        (
        )
    MeLog \
    .append \
    (
        ':saved log: ' \
        + \
        '\n' \
        + \
        os \
        .path \
        .join \
        (
            '.' \
                ,
            'zoo' \
                ,
            'things' \
                ,
            'mores' \
                ,
            'LOGS' \
                ,
            MeLog0 \
                ,
        ) \
    )
    print \
    (
        ':saved log: ' \
            ,
        os \
        .path \
        .join \
        (
            '.' \
                ,
            'zoo' \
                ,
            'things' \
                ,
            'mores' \
                ,
            'LOGS' \
                ,
            MeLog0 \
                ,
        ) \
            ,
        sep \
            = \
            '\n' \
            ,
    )
    pyperclip \
    .copy \
    (
        str \
        (
            MeLog0 \
        )
    )
def \
    MeInputThingDef3Def8 \
    (
    ) \
:
    global \
        MeLog
    MeRndmNum0 \
        = \
        str \
        (
            59 \
        )
    MeLog \
    .append \
    (
        ':rndm num: ' \
    )
    print \
    (
        ':rndm num: ' \
            ,
    )
    MeLog \
    .append \
    (
        ':' \
    )
    print \
    (
        ':' \
            ,
    )
    print \
    (
        '' \
            ,
        end \
            = \
            '' \
            ,
    )
    print \
    (
        colorama \
        .Fore \
        .MAGENTA \
            ,
        end \
            = \
            ''
    )
    #thing0
    print \
    (
        colorama \
        .Fore \
        .RESET \
            ,
        end \
            = \
            ''
    )
    print \
    (
        '?'
            ,
        colorama \
        .Fore \
        .YELLOW \
            ,
        MeRndmNum0 \
            ,
        colorama \
        .Fore \
        .RESET \
            ,
        '\n'
            ,
        sep \
            = \
            '' \
            ,
        end \
            = \
            '' \
            ,
    )
    print \
    (
        ':' \
            ,
        end \
            = \
            '' \
            ,
    )
    print \
    (
        colorama \
        .Fore \
        .RESET \
            ,
        end \
            = \
            ''
    )
    Thing \
        = \
        input \
        (
        )
    if \
        Thing \
            == \
            '' \
    :
        Thing \
            = \
            MeRndmNum0
    MeLog \
    .append \
    (
        ':' \
        + \
        Thing \
    )
    print \
    (
        colorama \
        .Fore \
        .RESET \
            ,
        end \
            = \
            ''
    )
    #thing1
    MeLog \
    .append \
    (
        ':' \
        + \
        ' ' \
        + \
        '\n\n' \
    )
    print \
    (
        ':' \
            ,
        '\n\n' \
            ,
    )
    MeLog \
    .append \
    (
        '' \
    )
    print \
    (
    )
    MeRndm0 \
        = \
        '' \
        .join \
        (
            (
                str \
                (
                    (
                        'a' , 'b' , 'c' , 'd' , \
                        'e' , 'f' , 'g' , 'h' , \
                        'i' , 'j' , 'k' , 'l' , \
                        'm' , 'n' , 'o' , 'p' , \
                        'q' , 'r' , 's' , 't' , \
                        'u' , 'v' , 'w' , 'x' , \
                        'y' , 'z' , '2' , '3' , \
                        '4' , '5' , '6' , '7' , \
                    ) \
                        [
                            random \
                            .SystemRandom \
                            (
                            ) \
                            .getrandbits \
                            (
                                int \
                                (
                                    5 \
                                ) \
                            ) \
                        ]
                )
                    for \
                        n \
                    in \
                        range \
                        (
                            int \
                            (
                                Thing \
                            )
                        )
            ) \
                ,
        )
    MeLog \
    .append \
    (
        ':rndm: ' \
        + \
        '\n' \
        + \
        MeRndm0 \
        + \
        '\n' \
    )
    print \
    (
        ':rndm: ' \
            ,
        colorama \
        .Fore \
        .MAGENTA \
        + \
        MeRndm0 \
        + \
        colorama \
        .Fore \
        .RESET \
            ,
        '' \
            ,
        sep \
            = \
            '\n' \
            ,
    )
    pyperclip \
    .copy \
    (
        str \
        (
            MeRndm0 \
        )
    )
def \
    FileReader \
    (
        FileToReadObject \
            ,
        BytesToReadInFileReaderDotRead \
            = \
            250 \
            ,
    ) \
:
    while \
        True \
    :
        Data \
            = \
            FileToReadObject \
            .read \
            (
                BytesToReadInFileReaderDotRead \
            )
        if \
            not \
                Data \
        :
            break
        yield \
            Data
def \
    MeInputThingDef4 \
    (
    ) \
:
    global \
        MeLog
    MeLog \
    .append \
    (
        ':pin: ' \
    )
    print \
    (
        ':pin: ' \
            ,
    )
    MeLog \
    .append \
    (
        ':' \
    )
    print \
    (
        ':' \
            ,
    )
    print \
    (
        '' \
            ,
        end \
            = \
            '' \
            ,
    )
    print \
    (
        colorama \
        .Fore \
        .MAGENTA \
            ,
        end \
            = \
            ''
    )
    #pyperclip0
    print \
    (
        colorama \
        .Fore \
        .RESET \
            ,
        end \
            = \
            ''
    )
    print \
    (
        '?'
            ,
        colorama \
        .Fore \
        .YELLOW \
            ,
        pyperclip \
        .paste \
        (
        ) \
            ,
        colorama \
        .Fore \
        .RESET \
            ,
        '\n'
            ,
        sep \
            = \
            '' \
            ,
        end \
            = \
            '' \
            ,
    )
    print \
    (
        ':' \
            ,
        end \
            = \
            '' \
            ,
    )
    print \
    (
        colorama \
        .Fore \
        .MAGENTA \
            ,
        end \
            = \
            ''
    )
    Thing \
        = \
        input \
        (
        )
    if \
        Thing \
            == \
            '' \
    :
        Thing \
            = \
            pyperclip \
            .paste \
            (
            )
    MeLog \
    .append \
    (
        ':' \
        + \
        Thing \
    )
    print \
    (
        colorama \
        .Fore \
        .RESET \
            ,
        end \
            = \
            ''
    )
    #pyperclip1
    MeLog \
    .append \
    (
        ':' \
        + \
        ' ' \
        + \
        '\n\n' \
    )
    print \
    (
        ':' \
            ,
        '\n\n' \
            ,
    )
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
    MeCheckOutputProcess00args0 \
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
                    'zoo' \
                        ,
                    'kubo' \
                        ,
                    'kubo.exe' \
                        ,
                ) \
                    ,
                'pin' \
                    ,
                'add' \
                    ,
                '--' \
                    ,
                Thing \
                    ,
            ] \
                ,
        )
    MeCheckOutputProcess00 \
        = \
        subprocess \
        .check_output \
        (
            MeCheckOutputProcess00args0 \
                ,
            cwd \
                = \
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                )
                ,
            env \
                = \
                MePopenProcess00env0 \
                ,
            universal_newlines \
                = \
                False \
                ,
            shell \
                = \
                True \
                ,
        )
    Me0 \
        = \
        [
            x \
            .split \
            (
                ' ' \
            ) \
                for \
                    x \
                in \
                    MeCheckOutputProcess00 \
                    .decode \
                    (
                        'ascii' \
                            ,
                    ) \
                    .split \
                    (
                        '\n' \
                            ,
                    )
                    if \
                        x \
                            != \
                            '' \
        ]
    [
        MeLog \
        .append \
        (
            '' \
            + \
            ' ' \
            + \
            x \
            [
                0 \
            ] \
            + \
            ':' \
            + \
            ' ' \
            + \
            x \
            [
                1 \
            ] \
        ) \
            for \
                x \
            in \
                Me0 \
                if \
                    x \
                    [
                        0 \
                    ] \
                        != \
                        '' \
    ]
    [
        print \
        (
            '' \
                ,
            x \
            [
                0 \
            ] \
            + \
            ':' \
                ,
            colorama \
            .Fore \
            .MAGENTA \
            + \
            x \
            [
                1 \
            ] \
            + \
            colorama \
            .Fore \
            .RESET \
                ,
        ) \
            for \
                x \
            in \
                Me0 \
                if \
                    x \
                    [
                        0 \
                    ] \
                        != \
                        '' \
    ]
    [
        pyperclip \
        .copy \
        (
            str \
            (
                x \
                [
                    1 \
                ] \
            )
        )
            for \
                x \
            in \
                Me0 \
                if \
                    x \
                    [
                        0 \
                    ] \
                        != \
                        '' \
    ]
def \
    MeInputThingDef5 \
    (
    ) \
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
    MeCheckOutputProcess00args0 \
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
                    'zoo' \
                        ,
                    'kubo' \
                        ,
                    'kubo.exe' \
                        ,
                ) \
                    ,
                'pin' \
                    ,
                'ls' \
                    ,
            ] \
                ,
        )
    MeCheckOutputProcess00 \
        = \
        subprocess \
        .check_output \
        (
            MeCheckOutputProcess00args0 \
                ,
            cwd \
                = \
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                )
                ,
            env \
                = \
                MePopenProcess00env0 \
                ,
            universal_newlines \
                = \
                False \
                ,
            shell \
                = \
                True \
                ,
        )
    Me0 \
        = \
        [
            x \
            .split \
            (
                ' ' \
            ) \
                for \
                    x \
                in \
                    MeCheckOutputProcess00 \
                    .decode \
                    (
                        'ascii' \
                            ,
                    ) \
                    .split \
                    (
                        '\n' \
                            ,
                    )
                    if \
                        x \
                            != \
                            '' \
        ]
    global \
        MeLog
    MeLog \
    .append \
    (
        ':pins: ' \
    )
    print \
    (
        ':pins: ' \
            ,
    )
    [
        MeLog \
        .append \
        (
            '    direct: ' \
            + \
            x \
            [
                0 \
            ] \
        ) \
            for \
                x \
            in \
                Me0 \
                if \
                    x \
                    [
                        1 \
                    ] \
                        == \
                        'direct' \
    ]
    [
        print \
        (
            '    direct: ' \
            + \
            colorama \
            .Fore \
            .MAGENTA \
            + \
            x \
            [
                0 \
            ] \
            + \
            colorama \
            .Fore \
            .RESET \
                ,
        ) \
            for \
                x \
            in \
                Me0 \
                if \
                    x \
                    [
                        1 \
                    ] \
                        == \
                        'direct' \
    ]
    [
        MeLog \
        .append \
        (
            ' recursive: ' \
            + \
            x \
            [
                0 \
            ] \
        ) \
            for \
                x \
            in \
                Me0 \
                if \
                    x \
                    [
                        1 \
                    ] \
                        == \
                        'recursive' \
    ]
    [
        print \
        (
            ' recursive: ' \
            + \
            colorama \
            .Fore \
            .MAGENTA \
            + \
            x \
            [
                0 \
            ] \
            + \
            colorama \
            .Fore \
            .RESET \
                ,
        ) \
            for \
                x \
            in \
                Me0 \
                if \
                    x \
                    [
                        1 \
                    ] \
                        == \
                        'recursive' \
    ]
    [
        MeLog \
        .append \
        (
            '  indirect: ' \
            + \
            x \
            [
                0 \
            ] \
        ) \
            for \
                x \
            in \
                Me0 \
                if \
                    x \
                    [
                        1 \
                    ] \
                        == \
                        'indirect' \
    ]
    [
        print \
        (
            '  indirect: ' \
            + \
            colorama \
            .Fore \
            .MAGENTA \
            + \
            x \
            [
                0 \
            ] \
            + \
            colorama \
            .Fore \
            .RESET \
                ,
        ) \
            for \
                x \
            in \
                Me0 \
                if \
                    x \
                    [
                        1 \
                    ] \
                        == \
                        'indirect' \
    ]
def \
    MeInputThingDef6 \
    (
    ) \
:
    global \
        MeLog
    MeLog \
    .append \
    (
        ':unpin: ' \
    )
    print \
    (
        ':unpin: ' \
            ,
    )
    MeLog \
    .append \
    (
        ':' \
    )
    print \
    (
        ':' \
            ,
    )
    print \
    (
        '' \
            ,
        end \
            = \
            '' \
            ,
    )
    print \
    (
        colorama \
        .Fore \
        .MAGENTA \
            ,
        end \
            = \
            ''
    )
    #pyperclip0
    print \
    (
        colorama \
        .Fore \
        .RESET \
            ,
        end \
            = \
            ''
    )
    print \
    (
        '?'
            ,
        colorama \
        .Fore \
        .YELLOW \
            ,
        pyperclip \
        .paste \
        (
        ) \
            ,
        colorama \
        .Fore \
        .RESET \
            ,
        '\n'
            ,
        sep \
            = \
            '' \
            ,
        end \
            = \
            '' \
            ,
    )
    print \
    (
        ':' \
            ,
        end \
            = \
            '' \
            ,
    )
    print \
    (
        colorama \
        .Fore \
        .MAGENTA \
            ,
        end \
            = \
            ''
    )
    Thing \
        = \
        input \
        (
        )
    if \
        Thing \
            == \
            '' \
    :
        Thing \
            = \
            pyperclip \
            .paste \
            (
            )
    MeLog \
    .append \
    (
        ':' \
        + \
        Thing \
    )
    print \
    (
        colorama \
        .Fore \
        .RESET \
            ,
        end \
            = \
            ''
    )
    #pyperclip1
    MeLog \
    .append \
    (
        ':' \
        + \
        ' ' \
        + \
        '\n\n' \
    )
    print \
    (
        ':' \
            ,
        '\n\n' \
            ,
    )
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
    MeCheckOutputProcess00args0 \
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
                    'zoo' \
                        ,
                    'kubo' \
                        ,
                    'kubo.exe' \
                        ,
                ) \
                    ,
                'pin' \
                    ,
                'rm' \
                    ,
                '--' \
                    ,
                Thing \
                    ,
            ] \
                ,
        )
    MeCheckOutputProcess00 \
        = \
        subprocess \
        .check_output \
        (
            MeCheckOutputProcess00args0 \
                ,
            cwd \
                = \
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                )
                ,
            env \
                = \
                MePopenProcess00env0 \
                ,
            universal_newlines \
                = \
                False \
                ,
            shell \
                = \
                True \
                ,
        )
    Me0 \
        = \
        [
            x \
            .split \
            (
                ' ' \
            ) \
                for \
                    x \
                in \
                    MeCheckOutputProcess00 \
                    .decode \
                    (
                        'ascii' \
                            ,
                    ) \
                    .split \
                    (
                        '\n' \
                            ,
                    )
                    if \
                        x \
                            != \
                            '' \
        ]
    [
        MeLog \
        .append \
        (
            '' \
            + \
            ' ' \
            + \
            x \
            [
                0 \
            ] \
            + \
            ':' \
            + \
            ' ' \
            + \
            x \
            [
                1 \
            ] \
        ) \
            for \
                x \
            in \
                Me0 \
                if \
                    x \
                    [
                        0 \
                    ] \
                        != \
                        '' \
    ]
    [
        print \
        (
            '' \
                ,
            x \
            [
                0 \
            ] \
            + \
            ':' \
                ,
            colorama \
            .Fore \
            .MAGENTA \
            + \
            x \
            [
                1 \
            ] \
            + \
            colorama \
            .Fore \
            .RESET \
                ,
        ) \
            for \
                x \
            in \
                Me0 \
                if \
                    x \
                    [
                        0 \
                    ] \
                        != \
                        '' \
    ]
    [
        pyperclip \
        .copy \
        (
            str \
            (
                x \
                [
                    1 \
                ] \
            )
        )
            for \
                x \
            in \
                Me0 \
                if \
                    x \
                    [
                        0 \
                    ] \
                        != \
                        '' \
    ]
def \
    MeInputThingDef7 \
    (
    ) \
:
    MeStopDaemonThread \
    (
    )
    try \
    :
        os \
        .chmod \
        (
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
                'keystore' \
                    ,
                'key_pi' \
                    ,
            ) \
                ,
            stat \
            .S_IWRITE \
        )
        pathlib \
        .Path \
        (
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
                'keystore' \
                    ,
                'key_pi' \
                    ,
            ) \
                ,
        ) \
        .unlink \
        (
            missing_ok \
                = \
                True \
                ,
        )
    except \
    :
        pass
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
    MeCheckOutputProcess01args0 \
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
                    'zoo' \
                        ,
                    'kubo' \
                        ,
                    'kubo.exe' \
                        ,
                ) \
                    ,
                'id' \
                    ,
                '--peerid-base=base32' \
                    ,
            ] \
                ,
        )
    MeCheckOutputProcess01 \
        = \
        subprocess \
        .check_output \
        (
            MeCheckOutputProcess01args0 \
                ,
            cwd \
                = \
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                )
                ,
            env \
                = \
                MePopenProcess00env0 \
                ,
            universal_newlines \
                = \
                False \
                ,
            shell \
                = \
                True \
                ,
        )
    MeCheckOutputProcess00args0 \
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
                    'zoo' \
                        ,
                    'kubo' \
                        ,
                    'kubo.exe' \
                        ,
                ) \
                    ,
                'key' \
                    ,
                'rotate' \
                    ,
                '-o=z' \
                    ,
            ] \
                ,
        )
    MeCheckOutputProcess00 \
        = \
        subprocess \
        .check_output \
        (
            MeCheckOutputProcess00args0 \
                ,
            cwd \
                = \
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                )
                ,
            env \
                = \
                MePopenProcess00env0 \
                ,
            universal_newlines \
                = \
                False \
                ,
            shell \
                = \
                True \
                ,
        )
    MeCheckOutputProcess02args0 \
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
                    'zoo' \
                        ,
                    'kubo' \
                        ,
                    'kubo.exe' \
                        ,
                ) \
                    ,
                'id' \
                    ,
                '--peerid-base=base32' \
                    ,
            ] \
                ,
        )
    MeCheckOutputProcess02 \
        = \
        subprocess \
        .check_output \
        (
            MeCheckOutputProcess02args0 \
                ,
            cwd \
                = \
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                )
                ,
            env \
                = \
                MePopenProcess00env0 \
                ,
            universal_newlines \
                = \
                False \
                ,
            shell \
                = \
                True \
                ,
        )
    #timestamper0
    global \
        MeCounter0
    MeCounter0 \
        += \
        1
    if \
        (
            MeCounter0 \
                >= \
                10000 \
        ) \
    :
        MeCounter0 \
            = \
            0
    TimeStamper \
        = \
        lambda \
        : \
        (
            (
                int \
                (
                    time \
                    .time \
                    (
                    )
                ) \
                * \
                (
                    10 \
                    ** \
                    4
                )
            ) \
            + \
            (
                MeCounter0 \
            ) \
        )
    #timestamper1
    MeSigk0 \
        = \
        json \
        .loads \
        (
            MeCheckOutputProcess01 \
            .decode \
            (
                'ascii' \
            )
        ) \
        [
            'ID' \
        ] \
        + \
        '_' \
        + \
        json \
        .loads \
        (
            MeCheckOutputProcess02 \
            .decode \
            (
                'ascii' \
            )
        ) \
        [
            'ID' \
        ] \
        + \
        '.sigk'
    Thing \
        = \
        json \
        .dumps \
        (
            {
                json \
                .loads \
                (
                    MeCheckOutputProcess01 \
                    .decode \
                    (
                        'ascii' \
                    )
                ) \
                [
                    'ID' \
                ] \
                :
                    json \
                    .loads \
                    (
                        MeCheckOutputProcess02 \
                        .decode \
                        (
                            'ascii' \
                        )
                    ) \
                    [
                        'ID' \
                    ]
                    ,
            }
        )
    with \
        open \
        (
            os \
            .path \
            .join \
            (
                '.' \
                    ,
                'zoo' \
                    ,
                'things' \
                    ,
                'mores' \
                    ,
                'sigk' \
                    ,
                MeSigk0 \
                    ,
            ) \
                ,
            'wb' \
        ) \
    as \
    (
        FileObject0 \
    ) \
    :
        FileObject0 \
            .write \
            (
                Thing \
                .encode \
                (
                    'ascii' \
                )
            )
    MeCheckOutputProcess03args0 \
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
                    'zoo' \
                        ,
                    'kubo' \
                        ,
                    'kubo.exe' \
                        ,
                ) \
                    ,
                'key' \
                    ,
                'sign' \
                    ,
                '-k=z' \
                    ,
                '--ipns-base=base32' \
                    ,
                '--' \
                    ,
                '<' \
                    ,
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                    'zoo' \
                        ,
                    'things' \
                        ,
                    'mores' \
                        ,
                    'sigk' \
                        ,
                    MeSigk0 \
                        ,
                ) \
                    ,
            ] \
                ,
        )
    MeCheckOutputProcess03 \
        = \
        subprocess \
        .check_output \
        (
            MeCheckOutputProcess03args0 \
                ,
            cwd \
                = \
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                )
                ,
            env \
                = \
                MePopenProcess00env0 \
                ,
            universal_newlines \
                = \
                False \
                ,
            shell \
                = \
                True \
                ,
        )
    Me0 \
        = \
        json \
        .loads \
        (
            MeCheckOutputProcess03 \
            .decode \
            (
                'ascii' \
            )
        )
    Me0 \
    .update \
    (
        {
            'Data' \
            :
                json \
                .loads \
                (
                    Thing \
                ) \
                ,
        }
    )
    with \
        open \
        (
            os \
            .path \
            .join \
            (
                '.' \
                    ,
                'zoo' \
                    ,
                'things' \
                    ,
                'mores' \
                    ,
                'sigk' \
                    ,
                MeSigk0 \
                    ,
            ) \
                ,
            'wb' \
        ) \
    as \
    (
        FileObject0 \
    ) \
    :
        FileObject0 \
            .write \
            (
                json \
                .dumps \
                (
                    Me0 \
                ) \
                .encode \
                (
                    'ascii' \
                )
            )
    global \
        MeLog
    MeLog \
    .append \
    (
        ':rotated key: ' \
        + \
        '\n\n' \
    )
    print \
    (
        ':rotated key: ' \
            ,
        end \
            = \
            '\n\n' \
            ,
    )
    MeLog \
    .append \
    (
        ':signed: ' \
    )
    print \
    (
        ':signed: ' \
            ,
    )
    MeLog \
    .append \
    (
        '{' \
    )
    print \
    (
        '{' \
            ,
    )
    [
        MeLog \
        .append \
        (
            '    "' \
            + \
            str \
            (
                y \
                [
                    0 \
                ]
            ) \
            + \
            '" \n    : \n        "' \
            + \
            str \
            (
                y \
                [
                    1 \
                ]
            ) \
            + \
            '" \n        ,' \
        )
            for \
                y \
            in \
                [
                    x \
                        for \
                            x \
                        in \
                            Me0 \
                            [
                                'Data' \
                            ] \
                            .items \
                            (
                            )
                ] \
    ]
    [
        print \
        (
            '    "' \
            + \
            str \
            (
                y \
                [
                    0 \
                ]
            ) \
            + \
            '" \n    : \n        "' \
            + \
            str \
            (
                y \
                [
                    1 \
                ]
            ) \
            + \
            '" \n        ,' \
        )
            for \
                y \
            in \
                [
                    x \
                        for \
                            x \
                        in \
                            Me0 \
                            [
                                'Data' \
                            ] \
                            .items \
                            (
                            )
                ] \
    ]
    MeLog \
    .append \
    (
        '}' \
    )
    print \
    (
        '}' \
            ,
    )
    MeLog \
    .append \
    (
        ':signed by: ' \
        + \
        '\n' \
        + \
        Me0 \
        [
            'Key' \
        ] \
            [
                'Id' \
            ] \
    )
    print \
    (
        ':signed by: ' \
            ,
        colorama \
        .Fore \
        .MAGENTA \
        + \
        Me0 \
        [
            'Key' \
        ] \
            [
                'Id' \
            ] \
        + \
        colorama \
        .Fore \
        .RESET \
            ,
        sep \
            = \
            '\n' \
            ,
    )
    MeLog \
    .append \
    (
        ':sigk: ' \
        + \
        '\n' \
        + \
        MeSigk0 \
        + \
        '\n' \
        + \
        '' \
    )
    print \
    (
        ':sigk: ' \
            ,
        MeSigk0 \
            ,
        '' \
            ,
        sep \
            = \
            '\n' \
            ,
    )
    try \
    :
        shutil \
        .move \
        (
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
                'keystore' \
                    ,
                'key_pi' \
                    ,
            ) \
                ,
            os \
            .path \
            .join \
            (
                '.' \
                    ,
                'zoo' \
                    ,
                'things' \
                    ,
                'secrets' \
                    ,
                json \
                .loads \
                (
                    MeCheckOutputProcess01 \
                    .decode \
                    (
                        'ascii' \
                    )
                ) \
                [
                    'ID' \
                ] \
                + \
                '.SECRET' \
                + \
                '.web3key' \
                    ,
            ) \
                ,
        )
    except \
    :
        pass
    try \
    :
        os \
        .chmod \
        (
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
                'keystore' \
                    ,
                'key_pi' \
                    ,
            ) \
                ,
            stat \
            .S_IWRITE \
                ,
        )
        pathlib \
        .Path \
        (
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
                'keystore' \
                    ,
                'key_pi' \
                    ,
            ) \
                ,
        ) \
        .unlink \
        (
            missing_ok \
                = \
                True \
                ,
        )
    except \
    :
        pass
    MeLog \
    .append \
    (
        ':secrets: ' \
    )
    print \
    (
        ':secrets: ' \
            ,
    )
    MeLog \
    .append \
    (
        ' old secret: ' \
        + \
        json \
        .loads \
        (
            MeCheckOutputProcess01 \
            .decode \
            (
                'ascii' \
            )
        ) \
        [
            'ID' \
        ] \
        + \
        '\n' \
        + \
        ' new web3id: ' \
        + \
        json \
        .loads \
        (
            MeCheckOutputProcess02 \
            .decode \
            (
                'ascii' \
            )
        ) \
        [
            'ID' \
        ] \
    )
    print \
    (
        ' old secret: ' \
        + \
        colorama \
        .Fore \
        .MAGENTA \
        + \
        json \
        .loads \
        (
            MeCheckOutputProcess01 \
            .decode \
            (
                'ascii' \
            )
        ) \
        [
            'ID' \
        ] \
        + \
        colorama \
        .Fore \
        .RESET \
            ,
        ' new web3id: ' \
        + \
        colorama \
        .Fore \
        .MAGENTA \
        + \
        json \
        .loads \
        (
            MeCheckOutputProcess02 \
            .decode \
            (
                'ascii' \
            )
        ) \
        [
            'ID' \
        ] \
        + \
        colorama \
        .Fore \
        .RESET \
            ,
        sep \
            = \
            '\n' \
            ,
    )
    MeStartDaemonThread \
    (
    )
    pyperclip \
    .copy \
    (
        str \
        (
            json \
            .loads \
            (
                MeCheckOutputProcess02 \
                .decode \
                (
                    'ascii' \
                )
            ) \
            [
                'ID' \
            ] \
        )
    )
def \
    MeInputThingDef8 \
    (
    ) \
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
    MeCheckOutputProcess00args0 \
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
                    'zoo' \
                        ,
                    'kubo' \
                        ,
                    'kubo.exe' \
                        ,
                ) \
                    ,
                'repo' \
                    ,
                'gc' \
                    ,
            ] \
                ,
        )
    MeCheckOutputProcess00 \
        = \
        subprocess \
        .check_output \
        (
            MeCheckOutputProcess00args0 \
                ,
            cwd \
                = \
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                )
                ,
            env \
                = \
                MePopenProcess00env0 \
                ,
            universal_newlines \
                = \
                False \
                ,
            shell \
                = \
                True \
                ,
        )
    Me0 \
        = \
        [
            x \
            .split \
            (
                ' ' \
            ) \
                for \
                    x \
                in \
                    MeCheckOutputProcess00 \
                    .decode \
                    (
                        'ascii' \
                            ,
                    ) \
                    .split \
                    (
                        '\n' \
                            ,
                    )
                    if \
                        x \
                            != \
                            '' \
        ]
    global \
        MeLog
    MeLog \
    .append \
    (
        ':garbage cleanings: ' \
        + \
        '\n\n' \
    )
    print \
    (
        ':garbage cleanings: ' \
            ,
        end \
            = \
            '\n\n' \
            ,
    )
    [
        MeLog \
        .append \
        (
            '' \
            + \
            ' ' \
            + \
            x \
            [
                0 \
            ] \
            + \
            ':' \
            + \
            ' ' \
            + \
            x \
            [
                1 \
            ] \
        ) \
            for \
                x \
            in \
                Me0 \
                if \
                    x \
                    [
                        0 \
                    ] \
                        != \
                        '' \
    ]
    [
        print \
        (
            '' \
                ,
            x \
            [
                0 \
            ] \
            + \
            ':' \
                ,
            colorama \
            .Fore \
            .MAGENTA \
            + \
            x \
            [
                1 \
            ] \
            + \
            colorama \
            .Fore \
            .RESET \
                ,
        ) \
            for \
                x \
            in \
                Me0 \
                if \
                    x \
                    [
                        0 \
                    ] \
                        != \
                        '' \
    ]
def \
    MeInputThingDef9 \
    (
    ) \
:
    global \
        MeLog
    MeLog \
    .append \
    (
        ':quit: ' \
        + \
        '\n\n' \
    )
    print \
    (
        ':quit: ' \
            ,
        end \
            = \
            '\n\n' \
            ,
    )
    global \
        MeStuffNeedToBreak
    MeStuffNeedToBreak \
        = \
        True
#_____________________________________________________________________
#_____________________________________________________________
try \
:
    for \
        x \
    in \
        [
            os \
            .path \
            .sep \
            .join \
            (
                y \
                    ,
            )
                for \
                    y \
                in \
                    [
                        (
                            '.' \
                                ,
                            'zoo' \
                                ,
                            'kubo' \
                                ,
                            '.unixfs' \
                                ,
                        ) \
                            ,
                        (
                            '.' \
                                ,
                            'zoo' \
                                ,
                            'kubo' \
                                ,
                            'pgpg' \
                                ,
                        ) \
                            ,
                        (
                            '.' \
                                ,
                            'zoo' \
                                ,
                            'kubo' \
                                ,
                            'modem' \
                                ,
                        ) \
                            ,
                    ] \
                    + \
                    [
                        (
                            '.' \
                                ,
                            'zoo' \
                                ,
                            'things' \
                                ,
                            z \
                                ,
                        )
                            for \
                                z \
                            in \
                                [
                                    os \
                                    .path \
                                    .sep \
                                    .join \
                                    (
                                        [
                                            'mores' \
                                                ,
                                            'car' \
                                                ,
                                        ] \
                                            ,
                                    )
                                        ,
                                    os \
                                    .path \
                                    .sep \
                                    .join \
                                    (
                                        [
                                            'mores' \
                                                ,
                                            'crypt' \
                                                ,
                                            'SECRETfiles' \
                                                ,
                                        ] \
                                            ,
                                    )
                                        ,
                                    os \
                                    .path \
                                    .sep \
                                    .join \
                                    (
                                        [
                                            'mores' \
                                                ,
                                            'crypt' \
                                                ,
                                            'SECRETphrases' \
                                                ,
                                        ] \
                                            ,
                                    )
                                        ,
                                    'gets' \
                                        ,
                                    os \
                                    .path \
                                    .sep \
                                    .join \
                                    (
                                        [
                                            'mores' \
                                                ,
                                            'LOGS' \
                                                ,
                                        ] \
                                            ,
                                    )
                                        ,
                                    'secrets' \
                                        ,
                                    'shares' \
                                        ,
                                    os \
                                    .path \
                                    .sep \
                                    .join \
                                    (
                                        [
                                            'mores' \
                                                ,
                                            'sigk' \
                                                ,
                                        ] \
                                            ,
                                    )
                                        ,
                                ]
                    ]
        ] \
    :
        try \
        :
            os \
            .makedirs \
            (
                name \
                    = \
                    x \
                    ,
                exist_ok \
                    = \
                    True \
                    ,
            )
        except \
        :
            pass
except \
:
    pass
#_____________________________________________________________________
#_____________________________________________________________
try \
:
    atexit \
    .register \
    (
        MeStopThreads \
            ,
    )
except \
:
    pass
try \
:
    signal \
    .signal \
    (
        signal \
        .SIGINT \
            ,
        MeStopThreads \
            ,
    )
except \
:
    pass
try \
:
    signal \
    .signal \
    (
        signal \
        .SIGTERM \
            ,
        MeStopThreads \
            ,
    )
except \
:
    pass
try \
:
    signal \
    .signal \
    (
        signal \
        .SIGBREAK \
            ,
        MeStopThreads \
            ,
    )
except \
:
    pass
#_____________________________________________________________
#_____________________________________________________________
try \
:
    MeStartDaemonThread \
    (
    )
except \
:
    pass
#_____________________________________________________________________
#_____________________________________________________________________
while \
    True \
:
    try \
    :
        print \
        (
            colorama \
            .Fore \
            .RESET \
                ,
            end \
                = \
                ''
        )
        MeDisplayMenu \
        (
        )
        MeAskForInput \
        (
        )
        MeSaveInput \
        (
        )
        MeCheckInputForStuff \
        (
        )
        MeDoInputThing \
        (
        )
        if \
            MeStuffNeedToBreak \
                == \
                True \
        :
            MeStopThreads \
            (
            )
            break
    except \
    :
        MeStopModemThread \
        (
        )
        if \
            str \
            (
                sys \
                .exception \
                (
                ) \
            ) \
            .find \
            (
                '233' \
            ) \
                != \
                -1 \
        :
            sys \
            .exit \
            (
            )
#_____________________________________________________________________
#________________________________________________________________
def \
    main \
    (
    ) \
:
    pass

if \
    __name__ \
        == \
        '__main__' \
:
    main \
    (
    )
