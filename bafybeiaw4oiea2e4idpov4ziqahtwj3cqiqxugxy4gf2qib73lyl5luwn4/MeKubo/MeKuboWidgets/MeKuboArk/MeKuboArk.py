#-----------------------------------------------------------------------
# Name:    MeKuboArk
# Purpose:    MeKuboArk
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
import json
import math
import os
import pathlib
import random
import shutil
import signal
import socket
import stat
import subprocess
import sys
import threading
import time
import tkinter
import tkinter \
    .filedialog
import traceback
#
#
import colorama
import pyperclip
import segno
#
#_____________________________________________________________________
#_____________________________________________________________________
try \
:
    colorama \
    .just_fix_windows_console \
    (
    )
except \
:
    pass
#_____________________________________________________________________
#_____________________________________________________________________
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
#_____________________________________________________________________
#_____________________________________________________________________
MeCounter0 \
    = \
    0
###timestamper0
##global \
##    MeCounter0
##MeCounter0 \
##    += \
##    1
##if \
##    (
##        MeCounter0 \
##            >= \
##            10000 \
##    ) \
##:
##    MeCounter0 \
##        = \
##        0
##TimeStamper \
##    = \
##    lambda \
##    : \
##    (
##        (
##            int \
##            (
##                time \
##                .time \
##                (
##                )
##            ) \
##            * \
##            (
##                10 \
##                ** \
##                4
##            )
##        ) \
##        + \
##        (
##            MeCounter0 \
##        ) \
##    )
###timestamper1
MeToggle0 \
    = \
    0
MeTimeStamper \
    = \
    None
MeSep0 \
    = \
    '    '
MeSep1 \
    = \
    '_'
MeCounter1 \
    = \
    0
#_____________________________________________________________________
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
#_____________________________________________________________________
try \
:
    atexit \
    .register \
    (
        MeExceptor \
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
        MeExceptor \
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
        MeExceptor \
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
        MeExceptor \
            ,
    )
except \
:
    pass
#_____________________________________________________________________
#_____________________________________________________________________
def \
    MeToggly0 \
    (
        Thing \
            = \
            None \
            ,
    ) \
:
    global \
        MeToggle0
    MeToggle0 \
        = \
        Thing
#_____________________________________________________________________
#_____________________________________________________________________
def \
    MeFileWriter \
    (
        Thing \
            = \
            None \
            ,
    ) \
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
                .join \
                (
                    '.' \
                        ,
                    'LOGS' \
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
    with \
        open \
        (
            os \
            .path \
            .join \
            (
                '.' \
                    ,
                'LOGS' \
                    ,
                MeTimeStamper \
                    ,
            ) \
                ,
            'a' \
                ,
            newline \
                = \
                '\r\n' \
                ,
        ) \
    as \
        FileOpened0 \
    :
        FileOpened0 \
        .write \
        (
            Thing \
                ,
        )
#_____________________________________________________________________
#_____________________________________________________________________
def \
    MeKuboDagGet \
    (
        Thing \
            = \
            None \
            ,
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
                    MeTwoPaths1 \
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
                    MeTwoPaths0 \
                        ,
                ) \
                    ,
                'dag' \
                    ,
                'get' \
                    ,
                '--' \
                    ,
                Thing \
                    ,
            ] \
                ,
        )
    MePopenProcess00 \
        = \
        subprocess \
        .check_output \
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
        )
    return \
        MePopenProcess00
#_____________________________________________________________________
#_____________________________________________________________________
def \
    MeKuboDagGetJsonLoads \
    (
        Thing \
            = \
            None \
            ,
    ) \
:
    return \
        json \
        .loads \
        (
            MeKuboDagGet \
            (
                Thing \
                    = \
                    Thing \
                    ,
            )
        )
#_____________________________________________________________________
#_____________________________________________________________________
def \
    MeKuboDagGetTreeMaker \
    (
        Thing \
            = \
            None \
            ,
    ) \
:
    global \
        MeCounter1
    MeTree0 \
        = \
        MeKuboDagGetJsonLoads \
        (
            Thing \
                = \
                Thing \
                ,
        )
    MeFileWriter \
    (
        Thing \
            = \
            str \
            (
                MeSep0 \
                * \
                MeCounter1 \
            ) \
            + \
            Thing \
            + \
            '\n' \
            ,
    )
    if \
        'Links' \
    in \
        MeTree0 \
    :
        for \
            x \
        in \
            MeTree0 \
            [
                'Links' \
            ] \
        :
            MeCounter1 \
                += \
                1
            if \
                x \
                [
                    'Name' \
                ] \
                    != \
                    '' \
            :
                MeFileWriter \
                (
                    Thing \
                        = \
                        str \
                        (
                            MeSep1 \
                            * \
                            (
                                128 \
                            ) \
                        ) \
                        + \
                        '\n' \
                        ,
                )
                MeFileWriter \
                (
                    Thing \
                        = \
                        str \
                        (
                            ' ' \
                            * \
                            (
                                127 \
                                - \
                                len \
                                (
                                    x \
                                    [
                                        'Name' \
                                    ] \
                                ) \
                            ) \
                        ) \
                        + \
                        x \
                        [
                            'Name' \
                        ] \
                        + \
                        '\n' \
                        ,
                )
            MeCheckHashTypeOf \
            (
                Thing \
                    = \
                    x \
                    [
                        'Hash' \
                    ] \
                    [
                        '/' \
                    ] \
                    ,
            )
            MeCounter1 \
                -= \
                1
    else \
    :
        return \
            None
#_____________________________________________________________________
#_____________________________________________________________________
def \
    MeCheckHashTypeOf \
    (
        Thing \
            = \
            None \
            ,
    ) \
:
    if \
        Thing \
            == \
            '' \
    :
        return \
            'none'
    elif \
        Thing \
        [
            0 \
            : \
            7 \
        ] \
            == \
            'bafkrei' \
    :
##        MeFileWriter \
##        (
##            Thing \
##                = \
##                str \
##                (
##                    MeSep0 \
##                    * \
##                    MeCounter1 \
##                ) \
##                + \
##                Thing \
##                + \
##                '\n' \
##                ,
##        )
##        return \
##            'krei'
        return \
            'none'
    else \
    :
        MeKuboDagGetTreeMaker \
        (
            Thing \
                = \
                Thing \
                ,
        )
#_____________________________________________________________________
#_____________________________________________________________________
def \
    MeHaveTxtFile \
    (
    ) \
:
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
                '2paths.ini' \
                    ,
            ) \
                ,
            mode \
                = \
                'rb' \
                ,
        ) \
    as \
        FileObject1 \
    :
        global \
            MeTwoPaths0
        MeTwoPaths0 \
            = \
            FileObject1 \
            .readline \
            (
            ) \
            .decode \
            (
                'ascii' \
                    ,
            ) \
            .strip \
            (
            )
        global \
            MeTwoPaths1
        MeTwoPaths1 \
            = \
            FileObject1 \
            .readline \
            (
            ) \
            .decode \
            (
                'ascii' \
                    ,
            ) \
            .strip \
            (
            )
#have a txt file with
#2paths to
#kubo exe &
#.unixfs repo path;
#_____________________________________________________________________
#_____________________________________________________________________
def \
    MeShowTkGuiFolderChooser \
    (
    ) \
:
    global \
        MeSelectedFolder0
    MeSelectedFolder0 \
        = \
        ''
    try \
    :
        root \
            = \
            tkinter \
            .Tk \
            (
            )
        root \
        .update_idletasks \
        (
        )
        root \
        .attributes \
        (
            '-alpha' \
                ,
            0.0 \
                ,
        )
        root \
        .attributes \
        (
            '-topmost' \
                ,
            True \
                ,
        )
    except \
    :
        pass
    try \
    :
        MeSelectedFolder0 \
            = \
            tkinter \
            .filedialog \
            .askdirectory \
            (
                parent \
                    = \
                    root \
                    ,
                title \
                    = \
'CHOOSE DIRECTORY TO PUBLISH & SHARE THE WHOLE THING WITH EVERYBODY!' \
                    ,
            )
    except \
    :
        pass
    try \
    :
        root \
        .destroy \
        (
        )
    except \
    :
        pass
    if \
        MeSelectedFolder0 \
            != \
            '' \
    :
        MeKuboAddGuiChosenFolder \
        (
        )
    elif \
        MeSelectedFolder0 \
            == \
            '' \
    :
        MePromptForCidHashManual \
        (
        )
#show tkGUI to
#select folder to
#share PUBLICLY EVERYTHING IN THAT FOLDER!;
#_____________________________________________________________________
#_____________________________________________________________________
def \
    MeKuboAddGuiChosenFolder \
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
                    MeTwoPaths1 \
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
                    MeTwoPaths0 \
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
                        MeSelectedFolder0 \
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
    print \
    (
        ':' \
            ,
    )
    print \
    (
        ':shares: ' \
            ,
    )
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
            '' \
            .join \
            (
                [
                    '/' \
                    + \
                    y
                        for \
                            y \
                        in \
                            [
                                '/' \
                                .join \
                                (
                                    x \
                                    [
                                        2 \
                                    ] \
                                    .split \
                                    (
                                        '/' \
                                            ,
                                    ) \
                                    [
                                        1 \
                                        : \
                                        # \
                                    ] \
                                ) \
                            ] \
                            if \
                                y \
                                    != \
                                    ''
                ]
            ) \
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
    print \
    (
        ':' \
            ,
    )
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
    global \
        MeRootCidHash0
    MeRootCidHash0 \
        = \
        pyperclip \
        .paste \
        (
        )
    if \
        MeRootCidHash0 \
            == \
            '' \
    :
        MeToggly0 \
        (
            1 \
                ,
        )
    else \
    :
        MeShowThatRootCidHash \
        (
        )
#kubo add using MeStdCmdKuboAddOptions for me
#add that GUI chosen folder to web3
#now has CID hash;
#_____________________________________________________________________
#_____________________________________________________________________
def \
    MePromptForCidHashManual \
    (
    ) \
:
    print \
    (
        ':' \
            ,
    )
    print \
    (
        ':' \
            ,
    )
    print \
    (
        '/ipfs/' \
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
            '' \
            ,
    )
    MePromptedCid0 \
        = \
        input \
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
            '' \
            ,
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
    )
    if \
        MePromptedCid0 \
            == \
            '' \
    :
        MeShowTkGuiFolderChooser \
        (
        )
        return \
            None
    elif \
        MePromptedCid0 \
            != \
            '' \
    :
        MeToggly0 \
        (
            0 \
                ,
        )
    pyperclip \
    .copy \
    (
        MePromptedCid0 \
            ,
    )
    global \
        MeRootCidHash0
    MeRootCidHash0 \
        = \
        pyperclip \
        .paste \
        (
        )
    if \
        MeRootCidHash0 \
            == \
            '' \
    :
        MeToggly0 \
        (
            1 \
                ,
        )
    else \
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
                        MeTwoPaths1 \
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
                        MeTwoPaths0 \
                            ,
                    ) \
                        ,
                    'dag' \
                        ,
                    'stat' \
                        ,
                    '-p=false' \
                        ,
                    '--' \
                        ,
                    MeRootCidHash0 \
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
        MeShowThatRootCidHash \
        (
        )
#if cancelled tkGUI folder chooser,
#then instead
#prompt for
#CidHash manual entry to be
#the custom nominated root CID hash
#instead;
#_____________________________________________________________________
#_____________________________________________________________________
def \
    MeShowThatRootCidHash \
    (
    ) \
:
    if \
        MeRootCidHash0 \
            == \
            '' \
    :
        MeToggly0 \
        (
            1 \
                ,
        )
    else \
    :
        MeMakeWidgetHashTreeLog \
        (
        )
#show that root CID hash;
#_____________________________________________________________________
#_____________________________________________________________________
def \
    MeMakeWidgetHashTreeLog \
    (
    ) \
:
    if \
        MeRootCidHash0 \
            == \
            '' \
    :
        MeToggly0 \
        (
            1 \
                ,
        )
    else \
    :
        MeInput0 \
            = \
            MeRootCidHash0
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
        global \
            MeTimeStamper
        MeTimeStamper \
            = \
            MeInput0 \
            + \
            '.LOG'
        with \
            open \
            (
                os \
                .path \
                .join \
                (
                    '.' \
                        ,
                    'LOGS' \
                        ,
                    MeTimeStamper \
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
            FileOpened0 \
        :
            FileOpened0 \
            .write \
            (
                '' \
                    ,
            )
        if \
            MeInput0 \
                != \
                '' \
        :
            MeFileWriter \
            (
                Thing \
                    = \
                    str \
                    (
                        MeSep1 \
                        * \
                        (
                            128 \
                        ) \
                    ) \
                    + \
                    '\n' \
                    ,
            )
        MeInputChecked \
            = \
            MeCheckHashTypeOf \
            (
                Thing \
                    = \
                    MeInput0 \
                    ,
            )
        if \
            MeInput0 \
                != \
                '' \
        :
            MeFileWriter \
            (
                Thing \
                    = \
                    str \
                    (
                        MeSep1 \
                        * \
                        (
                            128 \
                        ) \
                    ) \
                    + \
                    '\n' \
                    ,
            )
        global \
            MeLogFile0
        MeLogFile0 \
            = \
            MeTimeStamper
        MeKuboAddLogFile \
        (
        )
#use
#root CID hash from share add hash &
#make MeWidgetHashTree .LOG
#(put .LOG file into widget subfolder) &
#_____________________________________________________________________
#_____________________________________________________________________
def \
    MeKuboAddLogFile \
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
                    MeTwoPaths1 \
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
                    MeTwoPaths0 \
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
                        'LOGS' \
                            ,
                        MeLogFile0 \
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
    print \
    (
        ':' \
            ,
    )
    print \
    (
        ':LOGS: ' \
            ,
    )
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
            '' \
            .join \
            (
                [
                    '/' \
                    + \
                    y
                        for \
                            y \
                        in \
                            [
                                '/' \
                                .join \
                                (
                                    x \
                                    [
                                        2 \
                                    ] \
                                    .split \
                                    (
                                        '/' \
                                            ,
                                    ) \
                                    [
                                        0 \
                                        : \
                                        # \
                                    ] \
                                ) \
                            ] \
                            if \
                                y \
                                    != \
                                    ''
                ]
            ) \
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
    print \
    (
        ':' \
            ,
    )
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
    global \
        MeHashTreeLogHash0
    MeHashTreeLogHash0 \
        = \
        pyperclip \
        .paste \
        (
        )
    if \
        MeHashTreeLogHash0 \
            == \
            '' \
    :
        MeToggly0 \
        (
            1 \
                ,
        )
    else \
    :
        MeKuboFilesCpRootCidHash \
        (
        )
#kubo add this .LOG file to make a web3 hash;
#_____________________________________________________________________
#_____________________________________________________________________
def \
    MeKuboFilesCpRootCidHash \
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
                    MeTwoPaths1 \
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
                    MeTwoPaths0 \
                        ,
                ) \
                    ,
                'files' \
                    ,
                'rm' \
                    ,
                '--force' \
                    ,
                '--' \
                    ,
                '/' \
                + \
                MeRootCidHash0 \
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
                    MeTwoPaths0 \
                        ,
                ) \
                    ,
                'files' \
                    ,
                'cp' \
                    ,
                '-p' \
                    ,
                '--' \
                    ,
                '/ipfs/' \
                + \
                MeRootCidHash0 \
                    ,
                '/' \
                + \
                MeRootCidHash0 \
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
    MeKuboFilesCpHashTreeLog \
    (
    )
#make
#a new MFS directory with
#kubo files cp /ipfs/ThatRootCidHash
#(not need directory maker QmUNLL)
#/ThatRootCidHash
#to put that root CID hash lazy copy into MFS;
#_____________________________________________________________________
#_____________________________________________________________________
def \
    MeKuboFilesCpHashTreeLog \
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
                    MeTwoPaths1 \
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
                    MeTwoPaths0 \
                        ,
                ) \
                    ,
                'files' \
                    ,
                'rm' \
                    ,
                '--force' \
                    ,
                '--' \
                    ,
                '/LOGS/' \
                + \
                MeLogFile0 \
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
                    MeTwoPaths0 \
                        ,
                ) \
                    ,
                'files' \
                    ,
                'cp' \
                    ,
                '-p' \
                    ,
                '--' \
                    ,
                '/ipfs/' \
                + \
                MeHashTreeLogHash0 \
                    ,
                '/LOGS/' \
                + \
                MeLogFile0 \
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
    MeKuboFilesStatHashCidBase32 \
    (
    )
#now
#kubo files cp HashTree .LOG CID hash
#to MFS with
#kubo files cp /ipfs/ThatHashTreeLogCid
#(not need directory maker QmUNLL)
#/LOGS
#(if need /LOGS/ThatHashTreeLogCid,
#then do that instead);
#_____________________________________________________________________
#_____________________________________________________________________
def \
    MeKuboFilesStatHashCidBase32 \
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
                    MeTwoPaths1 \
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
                    MeTwoPaths0 \
                        ,
                ) \
                    ,
                'files' \
                    ,
                'stat' \
                    ,
                '--hash' \
                    ,
                '--' \
                    ,
                '/' \
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
    pyperclip \
    .copy \
    (
        MeCheckOutputProcess00 \
        .decode \
        (
            'ascii' \
                ,
        ) \
        .strip \
        (
        )
    )
    print \
    (
        ':' \
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
            '' \
            ,
    )
    print \
    (
        pyperclip \
        .paste \
        (
        ) \
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
            '' \
            ,
    )
    print \
    (
        ':' \
            ,
    )
    global \
        MeFilesStatHashCid0
    MeFilesStatHashCid0 \
        = \
        pyperclip \
        .paste \
        (
        )
    MeKuboNamePublishThatRootMfsHash \
    (
    )
#do
#kubo files stat --hash -- /
#|
#kubo cid base32 --
#(just store as variable instead of piping
#so can use checkoutput subprocesses only);
#_____________________________________________________________________
#_____________________________________________________________________
def \
    MeKuboNamePublishThatRootMfsHash \
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
                    MeTwoPaths1 \
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
                    MeTwoPaths0 \
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
                '--ipns-base=base32' \
                    ,
                '--' \
                    ,
                MeFilesStatHashCid0 \
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
    pyperclip \
    .copy \
    (
        MeCheckOutputProcess00 \
        .decode \
        (
            'ascii' \
                ,
        ) \
        .strip \
        (
        ) \
        .split \
        (
            ' ' \
                ,
        ) \
        [
            2 \
        ] \
        .split \
        (
            ':' \
                ,
        ) \
        [
            0 \
        ]
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
                    MeTwoPaths1 \
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
                    MeTwoPaths0 \
                        ,
                ) \
                    ,
                'cid' \
                    ,
                'base32' \
                    ,
                '--' \
                    ,
                pyperclip \
                .paste \
                (
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
    pyperclip \
    .copy \
    (
        MeCheckOutputProcess00 \
        .decode \
        (
            'ascii' \
                ,
        ) \
        .strip \
        (
        )
    )
    print \
    (
        ':' \
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
            '' \
            ,
    )
    print \
    (
        pyperclip \
        .paste \
        (
        ) \
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
            '' \
            ,
    )
    print \
    (
        ':' \
            ,
    )
    global \
        MePublishedRootMfsHash0
    MePublishedRootMfsHash0 \
        = \
        pyperclip \
        .paste \
        (
        )
    pyperclip \
    .copy \
    (
        MeFilesStatHashCid0
    )
    segno \
    .make_qr \
    (
        MeFilesStatHashCid0 \
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
    print \
    (
        colorama \
        .Fore \
        .MAGENTA \
            ,
        end \
            = \
            '' \
            ,
    )
    print \
    (
        pyperclip \
        .paste \
        (
        ) \
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
            '' \
            ,
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
    )
    input \
    (
        ':' \
            ,
    )
#kubo name publish that root MFS hash
#with self key;
#_____________________________________________________________________
#_____________________________________________________________________
#finally,
#the LOGS part of the published ipns record
#should be accessible by MeCgArkWebsitey as
#/ipns/SelfKey/LOGS;
#_____________________________________________________________________
#_____________________________________________________________________
def \
    MeKuboFilesChcidVer \
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
                    MeTwoPaths1 \
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
                    MeTwoPaths0 \
                        ,
                ) \
                    ,
                'files' \
                    ,
                'chcid' \
                    ,
                '--cid-version=1' \
                    ,
                '--' \
                    ,
                '/' \
                    ,
            ] \
                ,
        )
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
#_____________________________________________________________________
#_____________________________________________________________________
try \
:
    MeHaveTxtFile \
    (
    )
except \
:
    pass
try \
:
    MeKuboFilesChcidVer \
    (
    )
except \
:
    pass
try \
:
    while \
        True \
    :
        try \
        :
            MeShowTkGuiFolderChooser \
            (
            )
            if \
                MeToggle0 \
                    == \
                    1 \
            :
                break
        except \
        :
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
except \
:
    pass
#_____________________________________________________________________
#_____________________________________________________________________
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
#_____________________________________________________________________
