# -*- coding: utf-8 -*-

#
# Copyright (c) 2012 Virtual Cable S.L.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
#    * Redistributions of source code must retain the above copyright notice,
#      this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright notice,
#      this list of conditions and the following disclaimer in the documentation
#      and/or other materials provided with the distribution.
#    * Neither the name of Virtual Cable S.L. nor the names of its contributors
#      may be used to endorse or promote products derived from this software
#      without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

'''
.. moduleauthor:: Adolfo Gómez, dkmaster at dkmon dot com
'''
from __future__ import unicode_literals

import base64
DEFAULT_IMAGE = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00y\x00\x00\x00\x80\x08\x03\x00\x00\x00\x18\xb96\xaa\x00\x00\x03\x00PLTE\x00\x00\x00\xff\xff\xff\x18\x7f\xf2BX\x08]{\x05\xb8\xca\x16\xd5\xe1K\x18\x7f\xf24k\x91BX\x08]{\x05\xb8\xca\x16\xd5\xe1K\x18\x7f\xf2BX\x08]{\x05\xb8\xca\x16\xd5\xe1K\x18\x7f\xf2BX\x08]{\x05\xb8\xca\x16\xd5\xe1K\x18\x7f\xf2BX\x08]{\x05w\x91\x17\xb8\xca\x16\xd5\xe1K\x18\x7f\xf2BX\x08]{\x05\xb8\xca\x16\xd5\xe1K\x18\x7f\xf2BX\x08]{\x05\xb8\xca\x16\xd5\xe1K\x18\x7f\xf2BX\x08]{\x05f\x9a\xb1\xb8\xca\x16\xd5\xe1K\x18\x7f\xf2BX\x08]{\x05\xb8\xca\x16\xd5\xe1K\x18\x7f\xf2BX\x08]{\x05\xb8\xca\x16\xd5\xe1K\x18\x7f\xf2BX\x08]{\x05\xb8\xca\x16\xcb\xd8F\xd5\xe1K\x18\x7f\xf2BX\x08]{\x05\xb8\xca\x16\xd5\xe1K\x18\x7f\xf2BX\x08]{\x05\xb8\xca\x16\xd5\xe1K\x18\x7f\xf2BX\x08Vj\n]{\x05\xad\xbf\x12\xb8\xca\x16\xd5\xe1K\x18\x7f\xf2BX\x08]{\x05\xb3\xc5\x15\xb8\xca\x16\xd5\xe1K\x10c\xc9\x11f\xce\x11k\xd3\x12e\xcc\x12n\xd8\x13i\xd1\x14l\xd6\x14o\xdb\x15s\xe1\x15v\xe6\x16b\xbf\x16q\xde\x16y\xeb\x17t\xe3\x17x\xe8\x17}\xf0\x18{\xed\x18\x7f\xf2\x1cb\xb6\x1ep\xcc\x1e|\xe7\x1f`\xac"y\xdb$_\xa2%i\xc1&w\xd0\'_\x98*u\xc4+^\x8e+r\xb7+~\xe0+\x83\xe8-^\x83.o\xaa1]x1m\x9d3\\m4k\x914p\xb85[b6i\x838[V8fu:ZI;df=Z;=_F=aW>Y.?]6?w\xb0AY\x1dA["BX\x08B~\xbaF\x8c\xd3Ja\x08K~\xa6Q\x91\xc7S\x94\xffTh\nT\x92\xf3U\x8f\xdaU\x91\xe7V\x84\x9eV\x8d\xceW\x89\xb4W\x8b\xc1X\x88\xa7Z\x85\x8aZ\x86\x99[p\n[\x82m[\x83|\\}9\\\x7fL\\\x81]]{\x05]|$]\x99\xf6a\x8b\x94b\x8d\x9cc\x81\x05dx\ne\x82\nf\x9a\xb1g\x9d\xecj\x86\x06k\x7f\rk\x91\x8bn\x89\x12o\x9f\xa5p\x8b\x06p\xa2\xe3r\x87\rt\x98\x82u\x8eCv\x90\nv\x90\x17w\xa4\x99y\xa7\xd9{\x8d\x0e{\x95\x0b}\x9ew~\x96\x1c\x81\x9a\x0c\x82\x95\x10\x86\x9d \x86\xa4m\x87\x9f\x0c\x88\x9c\x10\x89\xad\x80\x8a\xb1\xc5\x8d\xa4\r\x8e\xa4&\x8f\xaba\x90\xa2\x10\x92\xb6\xba\x93\xa9\x0e\x95\xaa*\x97\xa9\x10\x98\xae\x0e\x98\xb1V\x99\xb7d\x9a\xba\xb0\x9d\xb0-\x9e\xb0\x13\x9e\xb3\x0f\xa0\xb8I\xa1\xbcU\xa2\xbf\xa5\xa3\xb61\xa3\xb7\x13\xa3\xbbi\xa5\xb6\x13\xa8\xbc\x13\xa8\xbd<\xaa\xc0D\xaa\xc4\x99\xab\xbd\x13\xab\xbd6\xad\xc1\x14\xb0\xc4+\xb1\xc52\xb2\xc3\x16\xb2\xc3:\xb3\xc6\x15\xb8\xca\x16\xb8\xce\x83\xb9\xc9=\xc0\xcf@\xc0\xd3u\xc7\xd6E\xc7\xd8i\xce\xdbH\xce\xdcZ\xd5\xe1K\xf1\xf1\xf1\xf2\xf2\xf2\xf3\xf3\xf3\xf4\xf4\xf4\xf5\xf5\xf5\xf6\xf6\xf6\xf7\xf7\xf7\xf8\xf8\xf8\xf9\xf9\xf9\xfa\xfa\xfa\xfb\xfb\xfb\xfc\xfc\xfc\xfd\xfd\xfd\xfe\xfe\xfe\xff\xff\xff>\xe5\x11\x9c\x00\x00\x00TtRNS\x00\x00\x10\x10\x10\x10\x10      00000@@@@@PPPPPP`````ppppp\x80\x80\x80\x80\x80\x80\x8f\x8f\x8f\x8f\x8f\x9f\x9f\x9f\x9f\x9f\xaf\xaf\xaf\xaf\xaf\xaf\xbf\xbf\xbf\xbf\xbf\xcf\xcf\xcf\xcf\xcf\xdf\xdf\xdf\xdf\xdf\xdf\xdf\xef\xef\xef\xef\xef\xef(<\x17\xc4\x00\x00\x04{IDATx\x9c\xed\xdb1k\x14A\x14\x00\xe0\x15<B\x0c\x9a\x03\xb9\xca\xe6@\x02\x91\x03Ia\n\xaf\x08\x07*X\x08j\x88Z\x89\xd5\x81\x8d\xa4\x16\x04k\x0b9\x89 \x18#fS\x08\xa2\x85\x8d\x08\x82\x16\x8a\x8d`\xa7\x8d\xdah\xe14\x16\xf9\t\xde\xce\xeclff\xdf\xcc\xbc73{\x81\x90W\x85\xbd\xd9\xf7\xed\x9b\xdd\x9d\x9d\xd9\xbbd\x07v+\xb2}y\xd7\xe5\x0c\x13\x9dNo0\xb8\xc0\x8a\xf8\xf1\xf1\xc3\xd28\xe6\xa7]\xed#\xe4\xd6\x80\xe9\xf1\xe4\x9e5\x96\x12\xc9]V\x0f\xbbZE\xa4l\x16\x8avM\x9c$\xf7A\xd5t\xef\x16a\xb5\x8f\x06\xc8\x16\x96\xb1We\xd2\x15=\x86<Vmu\xa3e\xab[\x96l\xb0+\xd7\x86j\xdcQ\xe9\x8b$\xd9\x013\x08\xbe>4\xe3\xe6\x0e}\x86 \xbb`\x06\xc05\x97\x87F\xe3d\'\xcc\x1e a\xc5\xc6\xca\xd0\xfd\xab\x15\x8d\x85U\x1a%\x7f\xf6\xc8\x0c\r\x0f\x87\xb7$\x8d\x92s\x9f\xcc\xd0pUu*\xf9\xd7\x0e|\xc5#\x97\xf4I\x9c\xec\xa7\xbfaK\xae\x8aF\xca\xcf\xd1\xfd\xed\x85%\x8d\x92g\x11E\xb3F\xe4,\xc7\xd3\xe9e$}5\xb1\x8c\xa3\xff\x8c\xe5\x1b\xa9\xe5\x82~\xef\xa5\xef\xa7\xefmQ\xf4\x17L\x7f\'\x97\xd1\xa7:\xbd\x8c\xa5\x1b\x92\xd3\xd0T\x99\xd3_\xfdt\x032\xa7\x7f\xc6\xd3\xb7\xe92\xf2T\xbf@\x95\x8c{V\xa92\x82\xfe\x8e\x91\x89k\x0c$\xfd)\xbd\xcci\xff\x13\xd3}\xaa\xc3\xe4S\x05\xfd\xdaO\xbfM.c\xfb\xdbq\xae\xc5rg\x9a\xbe\x96\xc4\xd2\xd6\x1e\'\xcdz\xb3 Z4?\x9cX\xf6?1+z\x1cS\t\xe4\xedq\xe4\xc8a\x94\xb1\x96r\xc0S\x9a|\x9c(o\x8b@\xf77\xcb\xb4P\xe4\x8c"o\xefD(\x9d\x85\xc8\xff\x14x\xb4\x15A\xafR\xe5<\xaf\xdcq\xe4\xc8\x01\x05\xa0i\xab\xd8\xf2\x8a\x96\xae\xa4Q\xb2y\xae9|\x84(\xe7\xf9H\xc6Z0-KF\xcb\xb3\xba<\xda\x08\xa5\xc9rf\xc8\xa2\xbfqt/\xad,\xe8\xbf\xd4\xa2\xe7%\x1c!\x87]e\xe7\xe9\xf2\xa5\x9aL\xb8\xab\xcd{\x8b$g5\x99r\xaa\x01\xda*\xd7Z\x16\xcac\x80~\x13Z\xb4~\x0c\x1e\xd9(:\xfc\xae&\xc9\x07\xeb\xf2h\x13O\xcf\x84\xcb\xc0\x89&\x9d\xea\x08\xf9t\x1c\xdd\t\x97\xc1\xa2\x05\xfd;\xaah\x9c\xbc\x19^t\x84\xec(\x1aC\xc7\xca\x16\x1a1M\x98\x8b\x90\xe1\xa2\xd1\x03x\x8c\\\x1f\xbc)\xfd\x1d#\xf3\xa2\xd7C\xe9(\xf9\x84\xa3\xbf}\x03\xf8b\x94l\xb9\xc8P\xa7\xda\x06#eNo\x04\xf5w\xac\x0c=8$\xfd\xb2Q9\xb8\xbf\xad\t\xd1\xb2\x85^\xf7\xd0\x83\x04\xb2k({\x17P2Av\xd1\x010E>[\x18[\x14\xda\x95\x8d"\x8b\x97S\xb5\xaa\xf9\xdc\x08\xfc&\xd1\x99\x8c$\x8b\xfe~\x86-\xda\x9d\x8b&\x9bkK\'\xedIE\x94a\x1a\x94}\x99\xa82HC\x13po"\xb2,\xaeph\xc1\xa3\xba]\x7f\x1e\xba\\V\xfd\xa8&\xe748@.o.\xb5lc\xd1\x81I\x12$\xcb\xb2\x1fV\xf2SM\xc6\xe5\x08\x93K:\x07{\x1b\x99"P.\xaf\xb3\xd2^S\xe466C\xa8\\\x95=^\\\xcb\xbf(\x05\xc7\xc8\x15\x9d+2a\xf7\x08\xd9\xb4\xf5\xd7\xcb\xcd\xca\xd9!M\xa6\xed\x1b\'gJ\xdd\xb4\x82\x13\xc8\xe5\xd2\xfe2}\xbfx94\xf6\xe5}y\x0f\xc8\xc7\xe4\x03T};f\xc8\x8eQ_\xfd\x04\xfa\xb1\xad\xedE\xe3\xb2ej\x98N\x86w\x95\x9f\x0cz\xbde\xbdU\xb8\xac}x\xceb\x9b\xdb\xda|C/\xa1\x0c2b\x8b\xadUJYT\xd4\xd2v\xb1\x1c\xe0Lb\xd9\xb4,\xd9\xc4\xe6\xc4\xb2\x8e1\xf8-s3\xf21C\x06\xef\xb5Fd\xadhG\xb6=%w\x94.nW7\xef$d\xad\xd0\xc5r|\x81&i\xcd\xca\xda\xcf\xde\xdb\x93\x95u\\\xfdh\x02\xb2\xdc\xa1\x8a\xd6$e\x1e\x8bZ\xe1\x93\x94y\xf4\xa5\xdd\x88l\xfd\xbe\x86\x87\xf8\xcf\x83fG\x12\xc7\xc1\x11\xe4.YvW\xc1\xd02\xc3\xcb\xfd\x10\xb9\xd8\x06\x7f\xdb\x82\x94\x95f\xc5\xbc\xabK\x92\xc1\x9c\x03\xed\x90\x9c3\x83\x05\xf0`\xd5h\x15\x1dc\xca\xeey\x84Of\xda\xf11\x1b\r]a\xb6\xe6\xc6F\xc7\x0cp\xce\xdc\x00\xb7k\x03k\x0c&>\xa8\xa5T\x9f7\x80\xac\x8d\x8c\xda\xc6\x05\xa8!\xb8\xbai\x95I\xfa\xc5\x1c\xaa\xa7\x0ex\x9a\x0cE\xediX\xcd\xee\xf5dE;@\x86\xfe?\xd1H\x08\xca\xf6{\x02l\x08\xcazr\xfb\x8f\x14\xb0\xd1c@2\xab\xdcxp\xef?R\xd0\xe5\xcf\xb7\xd5\x91\x97\x00\x00\x00\x00IEND\xaeB`\x82'
DEFAULT_IMAGE_BASE64 = base64.encodestring(DEFAULT_IMAGE).replace('\n', '')

DEFAULT_THUMB = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00.\x00\x00\x000\x08\x03\x00\x00\x00Y\xbb\xb8\xee\x00\x00\x03\x00PLTE\x00\x00\x00\xff\xff\xff\x18\x7f\xf2BX\x08]{\x05\xb8\xca\x16\xd5\xe1K\x18\x7f\xf24k\x91BX\x08]{\x05\xb8\xca\x16\xd5\xe1K\x18\x7f\xf2BX\x08]{\x05\xb8\xca\x16\xd5\xe1K\x18\x7f\xf2BX\x08]{\x05\xb8\xca\x16\xd5\xe1K\x18\x7f\xf2BX\x08]{\x05w\x91\x17\xb8\xca\x16\xd5\xe1K\x18\x7f\xf2BX\x08]{\x05\xb8\xca\x16\xd5\xe1K\x18\x7f\xf2BX\x08]{\x05\xb8\xca\x16\xd5\xe1K\x18\x7f\xf2BX\x08]{\x05f\x9a\xb1\xb8\xca\x16\xd5\xe1K\x18\x7f\xf2BX\x08]{\x05\xb8\xca\x16\xd5\xe1K\x18\x7f\xf2BX\x08]{\x05\xb8\xca\x16\xd5\xe1K\x18\x7f\xf2BX\x08]{\x05\xb8\xca\x16\xcb\xd8F\xd5\xe1K\x18\x7f\xf2BX\x08]{\x05\xb8\xca\x16\xd5\xe1K\x18\x7f\xf2BX\x08]{\x05\xb8\xca\x16\xd5\xe1K\x18\x7f\xf2BX\x08Vj\n]{\x05\xad\xbf\x12\xb8\xca\x16\xd5\xe1K\x18\x7f\xf2BX\x08]{\x05\xb3\xc5\x15\xb8\xca\x16\xd5\xe1K\x10c\xc9\x11f\xce\x11k\xd3\x12e\xcc\x12n\xd8\x13i\xd1\x14l\xd6\x14o\xdb\x15s\xe1\x15v\xe6\x16b\xbf\x16q\xde\x16y\xeb\x17t\xe3\x17x\xe8\x17}\xf0\x18{\xed\x18\x7f\xf2\x1cb\xb6\x1ep\xcc\x1e|\xe7\x1f`\xac"y\xdb$_\xa2%i\xc1&w\xd0\'_\x98*u\xc4+^\x8e+r\xb7+~\xe0+\x83\xe8-^\x83.o\xaa1]x1m\x9d3\\m4k\x914p\xb85[b6i\x838[V8fu:ZI;df=Z;=_F=aW>Y.?]6?w\xb0AY\x1dA["BX\x08B~\xbaF\x8c\xd3Ja\x08K~\xa6Q\x91\xc7S\x94\xffTh\nT\x92\xf3U\x8f\xdaU\x91\xe7V\x84\x9eV\x8d\xceW\x89\xb4W\x8b\xc1X\x88\xa7Z\x85\x8aZ\x86\x99[p\n[\x82m[\x83|\\}9\\\x7fL\\\x81]]{\x05]|$]\x99\xf6a\x8b\x94b\x8d\x9cc\x81\x05dx\ne\x82\nf\x9a\xb1g\x9d\xecj\x86\x06k\x7f\rk\x91\x8bn\x89\x12o\x9f\xa5p\x8b\x06p\xa2\xe3r\x87\rt\x98\x82u\x8eCv\x90\nv\x90\x17w\xa4\x99y\xa7\xd9{\x8d\x0e{\x95\x0b}\x9ew~\x96\x1c\x81\x9a\x0c\x82\x95\x10\x86\x9d \x86\xa4m\x87\x9f\x0c\x88\x9c\x10\x89\xad\x80\x8a\xb1\xc5\x8d\xa4\r\x8e\xa4&\x8f\xaba\x90\xa2\x10\x92\xb6\xba\x93\xa9\x0e\x95\xaa*\x97\xa9\x10\x98\xae\x0e\x98\xb1V\x99\xb7d\x9a\xba\xb0\x9d\xb0-\x9e\xb0\x13\x9e\xb3\x0f\xa0\xb8I\xa1\xbcU\xa2\xbf\xa5\xa3\xb61\xa3\xb7\x13\xa3\xbbi\xa5\xb6\x13\xa8\xbc\x13\xa8\xbd<\xaa\xc0D\xaa\xc4\x99\xab\xbd\x13\xab\xbd6\xad\xc1\x14\xb0\xc4+\xb1\xc52\xb2\xc3\x16\xb2\xc3:\xb3\xc6\x15\xb8\xca\x16\xb8\xce\x83\xb9\xc9=\xc0\xcf@\xc0\xd3u\xc7\xd6E\xc7\xd8i\xce\xdbH\xce\xdcZ\xd5\xe1K\xf1\xf1\xf1\xf2\xf2\xf2\xf3\xf3\xf3\xf4\xf4\xf4\xf5\xf5\xf5\xf6\xf6\xf6\xf7\xf7\xf7\xf8\xf8\xf8\xf9\xf9\xf9\xfa\xfa\xfa\xfb\xfb\xfb\xfc\xfc\xfc\xfd\xfd\xfd\xfe\xfe\xfe\xff\xff\xff>\xe5\x11\x9c\x00\x00\x00TtRNS\x00\x00\x10\x10\x10\x10\x10      00000@@@@@PPPPPP`````ppppp\x80\x80\x80\x80\x80\x80\x8f\x8f\x8f\x8f\x8f\x9f\x9f\x9f\x9f\x9f\xaf\xaf\xaf\xaf\xaf\xaf\xbf\xbf\xbf\xbf\xbf\xcf\xcf\xcf\xcf\xcf\xdf\xdf\xdf\xdf\xdf\xdf\xdf\xef\xef\xef\xef\xef\xef(<\x17\xc4\x00\x00\x01LIDATx\x9c\x9d\xd5=NC1\x0c\x00`#\xc1\x02\x12\x0b\x17\xe0\x12\x0ct\xea\x15@H\x9c #g\xe8\xfc\xa6\xb0#$|\r$\xc6\x8e\x8c\x9c\xc1\xeb;\x02M\x9e\x93\x17;I\x9d\xd6Sm}\xc9s\xfeT\xb88)\xe0L\x0e)\xb6\x14\xe2c\xca\xc1\xf5\x9aS\x8a\xc8v\xbb<\xe2\xae\xc1\xa9\xd0/1^]\x08\xfe\x84\xe2\xab\xa6\xf7E\xbb\x1c\xc1K\xbe/8)\xed\xde*\x8e\xa4}\xc1\xc3\xf4\xaa\x19\xed\x9d\x93^/Uy\x93\xe3I\x1c\xf0W\xccoq\xd5\xce\x9f\xd0\x8dS\x95\xed\x90\xc5\xb5\'\x93\xff\x08\x1ej=>\x87P\xd3\xc7\x01\xd0\xe48\xcf\xde\xebv\x16?M\xb75G\xefk\xcf\xbc\xbe\xc0\x0boz\xc9\x81\xd7\xe9\xbb>\xbd\xa8\x82_v\xf8M\x9b\x0fL/80\xd7\xbe\xcb\xf3\xf48\xc2;\xed\x98\\\xfa./\xfc\xb7\xb5\x91\xc2\x7f\xe1\xbe\xd65\xaf\xda\x87\xe3\xfc\xe0\xb1\xd8\x1d\xb08\xfb\xcf\xc8\xc1\xe6\xcb\x800\xbb\xaew8\\cS\xf78\xc0#>5\xaa]\xde\x8e\xb3\xf8\xdae\xfc\xa5\xef\xf9s>\x816O\t\x81H\r^\x8f\xb68\x89t\x8c\xaf\x87;\xc2\x81\xffk\xaf\x86y\x88\xcdX\xefe\xc6<\x95\xb6\x92s\xeb9\xdd\xf0\xa9\xa6\x12\x1d\xddw\xca\x97\xe0\xbe|:\xfa\x91r\xfapX\xea?\xa2-jG\x94i0\xb7\x00\x00\x00\x00IEND\xaeB`\x82'
DEFAULT_THUMB_BASE64 = base64.encodestring(DEFAULT_THUMB).replace('\n', '')
