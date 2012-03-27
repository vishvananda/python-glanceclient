# Copyright 2012 OpenStack LLC.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import copy

from glanceclient.common import utils


def do_image_list(gc, args):
    """List images."""
    images = gc.images.list()
    columns = ['ID', 'Name', 'Disk Format', 'Container Format', 'Size']
    utils.print_list(images, columns)


@utils.arg('id', metavar='<IMAGE_ID>', help='ID of image to describe.')
def do_image_show(gc, args):
    """Describe a specific image."""
    image = gc.images.get(args.id)

    # Flatten image properties dict
    info = copy.deepcopy(image._info)
    for (k, v) in info.pop('properties').iteritems():
        info['Property \'%s\'' % k] = v

    utils.print_dict(info)