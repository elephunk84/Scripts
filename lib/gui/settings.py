import socket
from lib.gui.hosts import *

hostname=socket.gethostname()
if hostname in IainsLaptop:
    workingdir="/home/iainstott/GitRepo/Scripts"
if hostname in AlienServer:
    workingdir="/mnt/LOCAL/Backup/GitRepo/Scripts"
if hostname in TheBeastServer:
    workingdir="/mnt/NFS/Backup/GitRepo/Scripts"

lib_path = os.path.abspath(os.path.join(workingdir, 'lib'))
sys.path.append(lib_path)

dbdir='/mnt/NFS/Backup/GitRepo/Scripts/lib/gui/data/logger'

DOCUMENTS={
        'fstab':['/etc/fstab',['local', 'remote']],
        'exports':['/etc/exports',['local', 'remote']],
        'interfaces':['/etc/networking/interfaces',['local', 'remote']],
        'resolv.conf':['/etc/resolv.conf',['local', 'remote']],
        'sources.list':['/etc/apt/sources.list',['local', 'remote']],
        'apache default site available':['/etc/apache2/sites-available/default',['remote']],
        'nginx default site available':['/etc/apache2/sites-available/default',['remote']],
        'nginx proxy site available':['/etc/apache2/sites-available/default',['remote']],
        'pxe boot menu':['/etc/ballsack',['remote']],
        'rc.local':['/etc/rc.local',['local', 'remote']],
        '.bashrc':['/home/iainstott/.bashrc',['local', 'remote']],
        'hosts':['/etc/hosts',['local', 'remote']]
}
DOCUMENTSLIST=list(DOCUMENTS.keys())

PROGRAMS={
        'Geany':['/usr/bin/geany'],
        'Geany New':['/usr/bin/geany -i'],
        'Nano':['/usr/bin/nano'],
        'Rsync':['/usr/bin/rsync -avzP --exclude-from=/home/iainstott/GitRepo/Scripts/lib/rsync_exclude.txt '],
        'Kate':['/usr/bin/kate'],
        'Yaourt GUI':['yaourt-gui'],
        'Manjaro Settings':['manjaro-settings-manager']
}
PROGRAMSLIST=list(PROGRAMS.keys())

COMMANDS={
        'Reboot':['sudo shutdown -r -t 00', 'system'],
        'Shutdown':['sudo shutdown -t 00', 'system'],
        'Update Pacman':['sudo pacman -Syy', 'arch'],
        'Lock Arch':['qdbus org.freedesktop.ScreenSaver /ScreenSaver Lock', 'arch'],
        'Install Pacman':['sudo pacman -Sy ', 'arch'],
        'Install AUR':['pacaur -Sy ', 'arch'],
        'Update Apt':['sudo apt update', 'debian'],
        'Install Apt':['sudo apt-get install -y ', 'debian'],
        'Add Repository':['sudo apt-add-repository -y ', 'debian'],
        'SSH Keygen':['ssh-keygen ', 'system'],
        'SSH Copy ID':['ssh-copy-id ', 'system']
}
COMMANDSLIST=list(COMMANDS.keys())

FILESYSTEMS={
        'Local Root':'/',
        'Primary Backup':'/mnt/NFS/Backup',
        'Primary Storage':'/mnt/NFS/Data',
        'Secodary Storage':'/mnt/NFS/Storage'
}

KODISETTINGS={
        'path_KodiConfig':['/home/iainstott/.kodi'],
        'path_KodiLocal':['/home/iainstott/Kodi'],
        'path_KodiRemote':['/mnt/NFS/Backup/Iains/KodiRepo'],
        'path_GitRepoRemote':['/mnt/NFS/Backup/GitRepo'],
        'path_ScriptsLocalData':['/lib/gui/data'],
        'path_ScriptsRemoteData':['/Scripts/lib/gui/data'],
        'file_rsyncExclude':['/home/iainstott/GitRepo/Scripts/lib/rsync_exclude.txt'],
        'file_IPTVChannelList':['/mnt/NFS/Backup/Iains/KodiRepo/IPTVLists/Channel_LIST.txt'],
        'file_IPTVChannelsAvailable':['/mnt/NFS/Backup/Iains/KodiRepo/IPTVLists/Channels.txt'],
        'file_IPTVChannelsNOTFOUND':['/mnt/NFS/Backup/Iains/KodiRepo/IPTVLists/NotFound.txt']
}

servicesLIST=['networking', 'sshd', 'dhpcd', 'bind9', 'autofs', 'nfs-kernel-server', 'apache2', 'nginx', 'tvheadend']
servicesCommandLIST=['start', 'stop', 'restart', 'enable', 'disable', 'info']
GenKeysLIST=['rsa', 'gpg']

cmd_reboot="shutdown -r -t 00"
cmd_lock="qdbus org.freedesktop.ScreenSaver /ScreenSaver Lock"
cmd_archUpdate='sudo pacman -Syy'
prog_Rsync="/usr/bin/rsync -avzP --exclude-from=/home/iainstott/GitRepo/Scripts/lib/rsync_exclude.txt "
prog_Nano='/usr/bin/nano'
prog_Geany='/usr/bin/geany -i '
prog_Kate='/usr/bin/kate '
prog_yaourtgui='yaourt-gui'
prog_manjsettings='manjaro-settings-manager'

GLOBALBGCOLOR='grey86'
GLOBALBGCOLOR2='grey92'
title_h=('helvetica', 24)
h1=('helvetica', 16)
h2=('helvetica', 14)
h3=('helvetica', 12)
h4=('helvetica', 10)
text_fg='black'
text_fgGREEN='green'

CH_STATUS=''
CURRENTTEMP=''
SETTEMP=''
STATUStext=''
CTEMPtext=''
STEMPtext=''
HOSTNAME=''
OS=''
OS_VER=''
OS_Details=''
INTIP=''
EXTIP=''
HOSTNAME=''

timer=0

path_GitRepoRemote='/mnt/NFS/Backup/GitRepo'
path_ScriptsLocalData=workingdir+'/lib/gui/data'
path_ScriptsRemoteData=path_GitRepoRemote+'/Scripts/lib/gui/data'
file_rsyncExclude='/home/iainstott/GitRepo/Scripts/lib/rsync_exclude.txt'

icon=workingdir+'/lib/gui/data/images/mainicon.png'

