#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.
#
# Download and build the data if it does not exist.

from parlai.core.build_data import DownloadableFile
import parlai.core.build_data as build_data
import os

RESOURCES = [
    DownloadableFile(
        '1k4b5WJS8aH48Scn3RZlHqQg600QDh7jP',
        'example.zip',
        
        'ef86c1b24517544c0f0a9f4962a94d65a1dffe7556f5c74118e107ea001e0e58',
        from_google=True,
    ),
        DownloadableFile(
        '1mR5HD1IRidAIRhEgQrwq8o6q6R1x3vT5',
        'example2.zip',
        '398d0c4dc31af0122ba0218510d924adfc08e3883bed5d800f250da34514a86e',
        from_google=True,
    )
]

def build(opt):
    # get path to data directory
    dpath = os.path.join(opt['datapath'], 'example')
    # define version if any
    version = None

    # check if data had been previously built
    if not build_data.built(dpath, version_string=version):
        print('[building data: ' + dpath + ']')

        # make a clean directory if needed
        if build_data.built(dpath):
            # an older version exists, so remove these outdated files.
            build_data.remove_dir(dpath)
        build_data.make_dir(dpath)

        # download the data.
        for downloadable_file in RESOURCES:
            downloadable_file.download_file(dpath)

        # mark the data as built
        build_data.mark_done(dpath, version_string=version)
