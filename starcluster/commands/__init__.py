#!/usr/bin/env python
from start import CmdStart
from addnode import CmdAddNode
from removenode import CmdRemoveNode
from stop import CmdStop
from terminate import CmdTerminate
from restart import CmdRestart
from sshmaster import CmdSshMaster
from sshnode import CmdSshNode
from sshinstance import CmdSshInstance
from listclusters import CmdListClusters
from createimage import CmdCreateImage
from downloadimage import CmdDownloadImage
from createvolume import CmdCreateVolume
from resizevolume import CmdResizeVolume
from listkeypairs import CmdListKeyPairs
from listzones import CmdListZones
from listregions import CmdListRegions
from listimages import CmdListImages
from listbuckets import CmdListBuckets
from showimage import CmdShowImage
from showbucket import CmdShowBucket
from removevolume import CmdRemoveVolume
from removeimage import CmdRemoveImage
from listinstances import CmdListInstances
from listspots import CmdListSpots
from showconsole import CmdShowConsole
from listvolumes import CmdListVolumes
from listpublic import CmdListPublic
from runplugin import CmdRunPlugin
from spothistory import CmdSpotHistory
from loadbalance import CmdLoadBalance
from shell import CmdShell
from createkey import CmdCreateKey
from removekey import CmdRemoveKey
from help import CmdHelp

all_cmds = [
    CmdStart(),
    CmdStop(),
    CmdTerminate(),
    CmdRestart(),
    CmdListClusters(),
    CmdSshMaster(),
    CmdSshNode(),
    CmdAddNode(),
    CmdRemoveNode(),
    CmdLoadBalance(),
    CmdSshInstance(),
    CmdListInstances(),
    CmdListImages(),
    CmdListPublic(),
    CmdListKeyPairs(),
    CmdCreateKey(),
    CmdRemoveKey(),
    CmdCreateImage(),
    CmdRemoveImage(),
    CmdDownloadImage(),
    CmdListVolumes(),
    CmdCreateVolume(),
    CmdResizeVolume(),
    CmdRemoveVolume(),
    CmdListSpots(),
    CmdSpotHistory(),
    CmdShowConsole(),
    CmdListRegions(),
    CmdListZones(),
    CmdListBuckets(),
    CmdShowBucket(),
    CmdShowImage(),
    CmdRunPlugin(),
    CmdShell(),
    CmdHelp(),
]