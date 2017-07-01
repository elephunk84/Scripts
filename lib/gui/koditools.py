#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os, sys, subprocess, sqlite3, datetime, time, glob, fileinput, re, string, filecmp
import tkinter as Tk
from tkinter import ttk

dateTimeLIST=[]

kodiDB="/home/iainstott/GitRepo/Scripts/lib/gui/data/kodi.db"
kodiTABLES=['buildDATA']

kodiIgnore=['temp', 'packages']

kodiBuildDate=''
kodiBuildVer=''
kodiLocalBuildVer=''
kodiBuildNotes=''
kodiBuildDescription=''
dateTimeLIST=[]
dbData=[]
dbData2=[]
Channels=[]
NotFOUND=[]

file_IPTVChannelList='/mnt/NFS/Backup/Iains/KodiRepo/IPTVLists/Channel_LIST.txt'
file_IPTVChannelsAvailable='/mnt/NFS/Backup/Iains/KodiRepo/IPTVLists/Channels.txt'
file_IPTVChannelsNOTFOUND='/mnt/NFS/Backup/Iains/KodiRepo/IPTVLists/NotFound.txt'

kodiBUILDDIR='/home/iainstott/.kodi/'
kodiADDONSDIR=kodiBUILDDIR+'addons/'
kodiInstalledPACKAGES=kodiADDONSDIR+'packages/'
kodiREPODIR='/home/iainstott/Kodi/'
kodiGitREPO=kodiREPODIR+'Addons/'
kodiARCHIVEDIR=kodiREPODIR+'Archive/'
kodiADDONSARCHIVEDIR=kodiREPODIR+'Addons/'
kodiBUILDARCHIVEDIR=kodiARCHIVEDIR+'BuildArchive/'
kodiCURRENTBUILDDIR=kodiARCHIVEDIR+'currentBuild/'
kodiCURRENTBUILDADDONS=kodiCURRENTBUILDDIR+'addons/'

kodiCurrentZIP=kodiREPODIR+'current.zip'
kodiResetZIP=kodiREPODIR+'reset.zip'

kodiREPOREMOTEDIR='/mnt/NFS/Backup/Iains/KodiRepo/'

kodiADDONSLIST=['repository.elephunk84', 'plugin.program.iainstool', 'plugin.program.super.favourites', 'script.tvguide.fullscreen', 'plugin.video.megaiptv']

kodi_GiRepo_SuperFavourites='https://github.com/spoyser/spoyser-repo.git'

kodiRsync_Get_IPTVLists="rsync -avzP --delete-during "+kodiREPOREMOTEDIR+"IPTVLists/ "+kodiREPODIR+"IPTVLists/"
kodiRsync_Build_Current="rsync -avzP --delete-during --exclude=Thumbnails/  --exclude=Temp/ --exclude='*.zip' --exclude=Media/ --exclude=userdata/addon_data/ "+kodiBUILDDIR+" "+kodiCURRENTBUILDDIR
kodiRsync_LocalToRemote="rsync -aP --delete-during --exclude=IPTVLists/ --exclude=.git/ "+kodiREPODIR+" iainstott@192.168.0.2:/mnt/LOCAL/Backup/BackupFolder/Backup/Iains/KodiRepo/"
kodiRsync_RemoteToLocal="rsync -avzP --delete-during --exclude=Archive/BuildArchive "+kodiREPODIR+" "+kodiREPOREMOTEDIR
kodiRsync_Backup_Addons="rsync -avzP "+kodiInstalledPACKAGES+" "+kodiADDONSARCHIVEDIR

textStringList=[
        'Removing Addon Links...',
        'Making Addon Links...',
        'Creating Reset Archive...',
        'Restoring Reset Archive...',
        'Creating Build ...',
        'Backing Up to Current Folder...',
        'Creating Archive...',
        'Creating Current Build...',
        'Syncing To Remote Server...',
        'Updating Git Repository...'
]

kodiversion = subprocess.check_output(["/usr/bin/kodi", "--version"])
kodiversion=str(kodiversion)
kodiversion=kodiversion.split('Git', 1)[0]
kodiversion=kodiversion.split("'", 1)[1]
kodiPackagesDIR=os.listdir(kodiADDONSDIR)
kodiPackagesDIR2=[]
kodiPackages=os.listdir(kodiInstalledPACKAGES)

if sys.version < '3':
    import codecs
    def u(x):
        return codecs.unicode_escape_decode(x)[0]
else:
    def u(x):
        return x

def same_folders(dcmp):
    if dcmp.diff_files:
        return False
    for sub_dcmp in dcmp.subdirs.values():
        return same_folders(sub_dcmp)
    return True

def kodiDBinit():
    global kodiBuildVer, kodiBuildDate, kodiBuildNotes, kodiLocalBuildVer, kodiOldBuildADDONS, kodiBuildDescription
    KodiNow=datetime.datetime.now()
    kodiBuildDate=KodiNow.strftime("%d/%B/%Y")
    kodiBuildVer='0.0.1'
    kodiLocalBuildVer='0.0.2'
    kodiBuildDescription='Database Initialization....'
    kodiBuildNotes='First Run For System. Automatic Database Initialization'
    subprocess.call(['touch', kodiDB])
    with sqlite3.connect(kodiDB) as kodiconn:
        curs=kodiconn.cursor()
        kodiTableCheck='create table if not exists ' + kodiTABLES[0] + '(BuildDate text, BuildVer text, LocalBuildVer text, InstalledADDONS text, BuildDesctiption text, BuildNotes text);'
        curs.execute(kodiTableCheck)
    kodiDBLogBuild()

def kodiDBGetData():
    global kodiBuildVer, kodiBuildDate, kodiBuildNotes, kodiLocalBuildVer, kodiOldBuildADDONS, kodiBuildDescription
    with sqlite3.connect(kodiDB) as kodiconn:
        curs=kodiconn.cursor()
        curs.execute('SELECT * FROM '+kodiTABLES[0]+' ORDER BY ROWID DESC LIMIT 1')
        kodiDBData=curs.fetchone()
        kodiBuildDate=kodiDBData[0]
        kodiBuildVer=kodiDBData[1]
        kodiLocalBuildVer=kodiDBData[2]
        kodiOldBuildADDONS=kodiDBData[3]
        kodiBuildDescription=kodiDBData[4]
        kodiBuildNotes=kodiDBData[5]

def kodiDBLogBuild():
    global kodiBuildVer, kodiBuildDate, kodiBuildNotes, kodiLocalBuildVer, kodiPackagesDIR2, kodiBuildDescription
    with sqlite3.connect(kodiDB) as kodiconn:
        curs=kodiconn.cursor()
        curs.execute("INSERT INTO " + kodiTABLES[0] + " values (?, ?, ?, ?, ?, ?);",  (kodiBuildDate, kodiBuildVer, kodiLocalBuildVer, str(kodiPackagesDIR2), kodiBuildDescription, kodiBuildNotes))


for item in kodiPackagesDIR:
    if item in kodiIgnore:
        pass
    else:
        kodiPackagesDIR2.append(item)
        kodiPackagesDIR2=sorted(kodiPackagesDIR2, reverse=True)
if os.path.isfile(kodiDB) and os.access(kodiDB, os.R_OK):
    try:
        kodiDBGetData()
    except:
        kodiDBinit()
        kodiDBGetData()
else:
    kodiDBinit()
    kodiDBGetData()
with open(file_IPTVChannelsAvailable, 'r') as f:
    for line in f:
        line=line.split('\n', 1)[0]
        if line.endswith(' | GOT'):
            pass
        else:
            Channels.append(line)
channelsAvail=sorted(Channels, reverse=True)
with open(file_IPTVChannelsNOTFOUND, 'r') as f:
    for line in f:
        line=line.split('\n', 1)[0]
        NotFOUND.append(line)
notFound=sorted(NotFOUND, reverse=True)

def kodi_GetAddonVER():
    matches=[]
    for addon in kodiADDONSLIST:
        filename=open(addon+'/addon.xml').read()
        if addon == kodiADDONSLIST[0]:
            match=re.findall(r'name="Elephunk84 Repository" version=\"(.+?)\"', filename)
        if addon == kodiADDONSLIST[1]:
            match=re.findall(r'name="Iain\'s Update Tool" version=\"(.+?)\"', filename)
        if addon == kodiADDONSLIST[2]:
            match=re.findall(r'name="Super Favourites" version=\"(.+?)\"', filename)
        if addon == kodiADDONSLIST[3]:
            match=re.findall(r'name="TV Guide Fullscreen" version=\"(.+?)\"', filename)
        if addon == kodiADDONSLIST[4]:
            match=re.findall(r'name="Mega IPTV" version=\"(.+?)\"', filename)
        if match:
            matches.append(match)
    return matches

def dateTime():
    global dateTimeLIST
    dateTimeLIST.append(now.strftime("%A"))
    dateTimeLIST.append(now.strftime("%d/%B/%Y"))
    dateTimeLIST.append(str(now.strftime("%H:%M:%S")))
    dateTimeLIST.append(str(now.strftime("%H:%M")))
    dateTimeLIST.append(yesterday)
    dateTimeLIST.append(now.strftime("%d"))
    dateTimeLIST.append(now.strftime("%B"))
    dateTimeLIST.append(now.strftime("%Y"))

class Generator:
    """
        Generates a new addons.xml file from each addons addon.xml file
        and a new addons.xml.md5 hash file. Must be run from the root of
        the checked-out repo. Only handles single depth folder structure.
    """
    def __init__( self ):
        # generate files
        self._generate_addons_file()
        self._generate_md5_file()
        # notify user
        print("Finished updating addons xml and md5 files")

    def _generate_addons_file( self ):
        # addon list
        addons = os.listdir( "." )
        # final addons text
        addons_xml = u("<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"yes\"?>\n<addons>\n")
        # loop thru and add each addons addon.xml file
        for addon in addons:
            try:
                # skip any file or .svn folder or .git folder
                if ( not os.path.isdir( addon ) or addon == ".svn" or addon == ".git" ): continue
                # create path
                _path = os.path.join( addon, "addon.xml" )
                # split lines for stripping
                xml_lines = open( _path, "r" , encoding="UTF-8").read().splitlines()
                # new addon
                addon_xml = ""
                # loop thru cleaning each line
                for line in xml_lines:
                    # skip encoding format line
                    if ( line.find( "<?xml" ) >= 0 ): continue
                    # add line
                    if sys.version < '3':
                        addon_xml += unicode( line.rstrip() + "\n", "UTF-8" )
                    else:
                        addon_xml += line.rstrip() + "\n"
                # we succeeded so add to our final addons.xml text
                addons_xml += addon_xml.rstrip() + "\n\n"
            except Exception as e:
                # missing or poorly formatted addon.xml
                print("Excluding %s for %s" % ( _path, e ))
        # clean and add closing tag
        addons_xml = addons_xml.strip() + u("\n</addons>\n")
        # save file
        self._save_file( addons_xml.encode( "UTF-8" ), file="addons.xml" )

    def _generate_md5_file( self ):
        # create a new md5 hash
        try:
            import md5
            m = md5.new( open( "addons.xml", "r" ).read() ).hexdigest()
        except ImportError:
            import hashlib
            m = hashlib.md5( open( "addons.xml", "r", encoding="UTF-8" ).read().encode( "UTF-8" ) ).hexdigest()

        # save file
        try:
            self._save_file( m.encode( "UTF-8" ), file="addons.xml.md5" )
        except Exception as e:
            # oops
            print("An error occurred creating addons.xml.md5 file!\n%s" % e)

    def _save_file( self, data, file ):
        try:
            # write data to the file (use b for Python 3)
            open( file, "wb" ).write( data )
        except Exception as e:
            # oops
            print("An error occurred saving %s file!\n%s" % ( file, e ))

def kodi_RemoveAddonLINKS():
    pass

def kodi_CreateAddonLINKS():
    pass

def kodi_GUI_GenAddons():
    os.chdir(kodiGitREPO)
    top=Tk.Tk()
    app=Kodi_GEN_ADDONS(top)
    top.geometry('400x200+200+200')
    top.mainloop()

class Kodi_GEN_ADDONS(Tk.Toplevel):
    def __init__(self, parent):
        self.root=parent
        self.RepoVERS, self.ToolVERS, self.SuperVERS, self.TVGuideVERS, self.IPTVVERS=kodi_GetAddonVER()
        self.dirLIST=glob.glob(kodiGitREPO+'*/')
        self.zipLIST=glob.glob(kodiGitREPO+'*.zip')
        self.RepoVerLabel=Tk.Label(self.root, text="Repo Version = ", width=20)
        self.RepoVerLabel.pack()
        self.RepoVerLabel.place(x=5, y=5)
        self.RepoVerStringVar=Tk.StringVar()
        self.RepoVerStringVar.set(self.RepoVERS[0])
        self.RepoVerENTRY=Tk.Entry(self.root, textvariable=self.RepoVerStringVar, width=10)
        self.RepoVerENTRY.pack()
        self.RepoVerENTRY.place(x=170, y=5)
        self.ToolVerLabel=Tk.Label(self.root, text="Tool Version = ", width=20)
        self.ToolVerLabel.pack()
        self.ToolVerLabel.place(x=5, y=35)
        self.ToolVerStringVar=Tk.StringVar()
        self.ToolVerStringVar.set(self.ToolVERS[0])
        self.ToolVerENTRY=Tk.Entry(self.root, textvariable=self.ToolVerStringVar, width=10)
        self.ToolVerENTRY.pack()
        self.ToolVerENTRY.place(x=170, y=35)
        self.SuperFavVerLabel=Tk.Label(self.root, text="SuperFav Version = ", width=20)
        self.SuperFavVerLabel.pack()
        self.SuperFavVerLabel.place(x=5, y=65)
        self.SuperFavVerStringVar=Tk.StringVar()
        self.SuperFavVerStringVar.set(self.SuperVERS[0])
        self.SuperFavVerENTRY=Tk.Entry(self.root, textvariable=self.SuperFavVerStringVar, width=10)
        self.SuperFavVerENTRY.pack()
        self.SuperFavVerENTRY.place(x=170, y=65)
        self.TVGuideVerLabel=Tk.Label(self.root, text="TV Guide Version = ", width=20)
        self.TVGuideVerLabel.pack()
        self.TVGuideVerLabel.place(x=5, y=95)
        self.TVGuideVerStringVar=Tk.StringVar()
        self.TVGuideVerStringVar.set(self.TVGuideVERS[0])
        self.TVGuideVerENTRY=Tk.Entry(self.root, textvariable=self.TVGuideVerStringVar, width=10)
        self.TVGuideVerENTRY.pack()
        self.TVGuideVerENTRY.place(x=170, y=95)
        self.IPTVVerLabel=Tk.Label(self.root, text="Mega IPTV Version = ", width=20)
        self.IPTVVerLabel.pack()
        self.IPTVVerLabel.place(x=5, y=125)
        self.IPTVVerStringVar=Tk.StringVar()
        self.IPTVVerStringVar.set(self.IPTVVERS[0])
        self.IPTVVerENTRY=Tk.Entry(self.root, textvariable=self.IPTVVerStringVar, width=10)
        self.IPTVVerENTRY.pack()
        self.IPTVVerENTRY.place(x=170, y=125)
        self.button=Tk.Button(self.root, text="Create", command=lambda:self.OnClick())
        self.button.pack()
        self.button.place(x=320, y=160)

    def OnClick(self):
        for zipFILE in self.zipLIST:
            os.remove(zipFILE)
        iainsrepo_VER=self.RepoVerStringVar.get()
        iainstool_VER=self.ToolVerStringVar.get()
        superfav_VER=self.SuperFavVerStringVar.get()
        tvguide_VER=self.TVGuideVerStringVar.get()
        megaiptv_VER=self.IPTVVerStringVar.get()
        if iainsrepo_VER.startswith("("):
            iainsrepo_VER=re.findall(r"'(.*?)'", iainsrepo_VER, re.DOTALL)
        if type(iainsrepo_VER) is list:
            iainsrepo_VER=iainsrepo_VER[0]
        if iainstool_VER.startswith("("):
            iainstool_VER=re.findall(r"'(.*?)'", iainstool_VER, re.DOTALL)
        if type(iainstool_VER) is list:
            iainstool_VER=iainstool_VER[0]
        if superfav_VER.startswith("("):
            superfav_VER=re.findall(r"'(.*?)'", superfav_VER, re.DOTALL)
        if type(superfav_VER) is list:
            superfav_VER=superfav_VER[0]
        if tvguide_VER.startswith("("):
            tvguide_VER=re.findall(r"'(.*?)'", tvguide_VER, re.DOTALL)
        if type(tvguide_VER) is list:
            tvguide_VER=tvguide_VER[0]
        if megaiptv_VER.startswith("("):
            megaiptv_VER=re.findall(r"'(.*?)'", megaiptv_VER, re.DOTALL)
        if type(megaiptv_VER) is list:
            megaiptv_VER=megaiptv_VER[0]
        self.RepoVerStringVar.set(iainsrepo_VER)
        self.ToolVerStringVar.set(iainstool_VER)
        self.SuperFavVerStringVar.set(superfav_VER)
        self.TVGuideVerStringVar.set(tvguide_VER)
        self.IPTVVerStringVar.set(megaiptv_VER)
        self.repover=self.RepoVerStringVar.get()
        self.toolver=self.ToolVerStringVar.get()
        self.superfavver=self.SuperFavVerStringVar.get()
        self.tvguidever=self.TVGuideVerStringVar.get()
        self.megaiptvver=self.IPTVVerStringVar.get()
        if self.repover.startswith("("):
            self.repover=re.findall(r"'(.*?)'", self.repover, re.DOTALL)
        if self.toolver.startswith("("):
            self.toolver=re.findall(r"'(.*?)'", self.toolver, re.DOTALL)
        if self.superfavver.startswith("("):
            self.superfavver=re.findall(r"'(.*?)'", self.superfavver, re.DOTALL)
        if self.tvguidever.startswith("("):
            self.tvguidever=re.findall(r"'(.*?)'", self.tvguidever, re.DOTALL)
        if self.megaiptvver.startswith("("):
            self.megaiptvver=re.findall(r"'(.*?)'", self.megaiptvver, re.DOTALL)
        for item in self.dirLIST:
            name=item.rsplit('/',2)[1]
            if name == kodiADDONSLIST[0]:
                if type(self.repover) is list:
                    self.repover=self.repover[0]
                if self.repover not in self.AddonVERS[0]:
                    xml=open(name+'/addon.xml').read()
                    texttofind=(r'name="Elephunk84 Repository" version=\"(.+?)\"')
                    texttoreplace=self.repover
                    matches=re.findall(texttofind, xml)
                    for m in matches:
                        xml=xml.replace( m , texttoreplace)
                    with open(name+'/addon.xml', 'w') as f:
                        f.write(xml)
                zipver=name+'-'+self.repover
                os.system('zip -r -0 '+zipver+'.zip '+name+' -x "*.zip"')
                os.system('cp '+zipver+'.zip '+item+'/'+zipver+'.zip')
            if name == kodiADDONSLIST[1]:
                if type(self.toolver) is list:
                    self.toolver=self.toolver[0]
                if self.toolver not in self.AddonVERS[1]:
                    xml=open(name+'/addon.xml').read()
                    texttofind=(r'name="Iain\'s Update Tool" version=\"(.+?)\"')
                    texttoreplace=self.toolver
                    matches=re.findall(texttofind, xml)
                    for m in matches:
                        xml=xml.replace( m , texttoreplace)
                    with open(name+'/addon.xml', 'w') as f:
                        f.write(xml)
                zipver=name+'-'+self.toolver
                os.system('zip -r -0 '+zipver+'.zip '+name+' -x "*.zip"')
                os.system('cp '+zipver+'.zip '+item+'/'+zipver+'.zip')
            if name == kodiADDONSLIST[2]:
                if type(self.superfavver) is list:
                    self.superfavver=self.superfavver[0]
                if self.superfavver not in self.AddonVERS[2]:
                    xml=open(name+'/addon.xml').read()
                    texttofind=(r'name="Super Favourites" version=\"(.+?)\"')
                    texttoreplace=self.superfavver
                    matches=re.findall(texttofind, xml)
                    for m in matches:
                        xml=xml.replace( m , texttoreplace)
                    with open(name+'/addon.xml', 'w') as f:
                        f.write(xml)
                zipver=name+'-'+self.superfavver
                os.system('zip -r -0 '+zipver+'.zip '+name+' -x "*.zip"')
                os.system('cp '+zipver+'.zip '+item+'/'+zipver+'.zip')
            if name == kodiADDONSLIST[3]:
                if type(self.tvguidever) is list:
                    self.tvguidever=self.tvguidever[0]
                if self.tvguidever not in self.AddonVERS[3]:
                    xml=open(name+'/addon.xml').read()
                    texttofind=(r'name="TV Guide Fullscreen" version=\"(.+?)\"')
                    texttoreplace=self.tvguidever
                    matches=re.findall(texttofind, xml)
                    for m in matches:
                        xml=xml.replace( m , texttoreplace)
                    with open(name+'/addon.xml', 'w') as f:
                        f.write(xml)
                zipver=name+'-'+self.tvguidever
                os.system('zip -r -0 '+zipver+'.zip '+name+' -x "*.zip"')
                os.system('cp '+zipver+'.zip '+item+'/'+zipver+'.zip')
            if name == kodiADDONSLIST[4]:
                if type(self.megaiptvver) is list:
                    self.megaiptvver=self.megaiptvver[0]
                if self.megaiptvver not in self.AddonVERS[4]:
                    xml=open(name+'/addon.xml').read()
                    texttofind=(r'name="Mega IPTV" version=\"(.+?)\"')
                    texttoreplace=self.megaiptvver
                    matches=re.findall(texttofind, xml)
                    for m in matches:
                        xml=xml.replace( m , texttoreplace)
                    with open(name+'/addon.xml', 'w') as f:
                        f.write(xml)
                zipver=name+'-'+self.megaiptvver
                os.system('zip -r -0 '+zipver+'.zip '+name+' -x "*.zip"')
                os.system('cp '+zipver+'.zip '+item+'/'+zipver+'.zip')
        Generator()
        os.system('git add --all')
        os.system('git commit -m "automatic update"')
        os.system('git push -u origin master')
        os.system(kodiRsync_LocalToRemote)
        self.root.quit()

def kodi_GUI_GenBuild():
    os.chdir(kodiGitREPO)
    top=Tk.Tk()
    app=Kodi_GEN_BUILD(top)
    top.geometry('800x400+200+200')
    top.mainloop()

class Kodi_GEN_BUILD(Tk.Toplevel):
    def __init__(self, parent):
        self.previousADDONS=[]
        self.recentlyINSTALLED=[]
        self.recentlyREMOVED=[]
        self.kodiOldBuildADDONS=kodiOldBuildADDONS.split(', ')
        for addon in self.kodiOldBuildADDONS:
            addon=str(addon).replace('[', '').replace(']', '').replace("'", '')
            self.previousADDONS.append(addon)
        for addon in kodiPackagesDIR2:
            if addon not in self.previousADDONS:
                self.recentlyINSTALLED.append(addon)
            dir1=kodiADDONSDIR+addon
            dir2=kodiCURRENTBUILDADDONS+addon+'/'
            print(dir1)
            print(dir2)
            try:
                result=same_folders(filecmp.dircmp(dir1, dir2))
            except:
                pass
            if result == False:
                self.recentlyINSTALLED.append(addon)
        for addon in self.previousADDONS:
            if addon not in kodiPackagesDIR2:
                self.recentlyREMOVED.append(addon)
        self.root=parent
        self.root.title("Kodi Build Details...")
        self.PanedWindow=ttk.Panedwindow(self.root, orient=Tk.VERTICAL)
        self.BuildINFOLabelFrame=Tk.LabelFrame(self.PanedWindow, text="Build Info...", width=780, height=200)
        self.BuildVerLabel=Tk.Label(self.BuildINFOLabelFrame, text="Current Build Version = ", width=20)
        self.BuildVerLabel.pack()
        self.BuildVerLabel.place(x=5, y=5)
        self.BuildVerStringVar=Tk.StringVar()
        self.BuildVerStringVar.set(kodiBuildVer)
        self.BuildVerENTRY=Tk.Entry(self.BuildINFOLabelFrame, textvariable=self.BuildVerStringVar, width=10)
        self.BuildVerENTRY.pack()
        self.BuildVerENTRY.place(x=170, y=5)

        self.NextBuildVerLabel=Tk.Label(self.BuildINFOLabelFrame, text="Next Build Version = ", width=20)
        self.NextBuildVerLabel.pack()
        self.NextBuildVerLabel.place(x=5, y=35)
        self.NextBuildVerStringVar=Tk.StringVar()
        self.NextBuildVerStringVar.set(kodiLocalBuildVer)
        self.NextBuildVerENTRY=Tk.Entry(self.BuildINFOLabelFrame, textvariable=self.NextBuildVerStringVar, width=10)
        self.NextBuildVerENTRY.pack()
        self.NextBuildVerENTRY.place(x=170, y=35)

        self.NextBuildDescLabel=Tk.Label(self.BuildINFOLabelFrame, text="Build Description", width=20)
        self.NextBuildDescLabel.pack()
        self.NextBuildDescLabel.place(x=0, y=75)
        self.NextBuildDescStringVar=Tk.StringVar()
        self.NextBuildDescStringVar.set(kodiBuildDescription)
        self.NextBuildDescENTRY=Tk.Entry(self.BuildINFOLabelFrame, textvariable=self.NextBuildDescStringVar, width=36, justify=Tk.LEFT)
        self.NextBuildDescENTRY.pack()
        self.NextBuildDescENTRY.place(x=5, y=95)

        self.NextBuildNotesLabel=Tk.Label(self.BuildINFOLabelFrame, text="Build Notes", width=20, justify=Tk.LEFT)
        self.NextBuildNotesLabel.pack()
        self.NextBuildNotesLabel.place(x=0, y=125)
        self.NextBuildNotesStringVar=Tk.StringVar()
        self.NextBuildNotesStringVar.set(kodiBuildNotes)
        self.NextBuildNotesENTRY=Tk.Entry(self.BuildINFOLabelFrame, textvariable=self.NextBuildNotesStringVar, width=36)
        self.NextBuildNotesENTRY.pack(ipady=3)
        self.NextBuildNotesENTRY.place(x=5, y=145)

        self.RecentlyInstalled=Tk.Label(self.BuildINFOLabelFrame, text='Recently Installed or Updated')
        self.RecentlyInstalled.pack()
        self.RecentlyInstalled.place(x=320, y=5)
        self.RecentlyInstalledADDONS=Tk.Listbox(self.BuildINFOLabelFrame, height=8, width=27)
        for package in self.recentlyINSTALLED:
            self.RecentlyInstalledADDONS.insert(0, package)
        self.RecentlyInstalledADDONS.pack()
        self.RecentlyInstalledADDONS.place(x=320, y=25)
        self.RecentlyRemoved=Tk.Label(self.BuildINFOLabelFrame, text='Recently Removed')
        self.RecentlyRemoved.pack()
        self.RecentlyRemoved.place(x=545, y=5)
        self.RecentlyRemovedADDONS=Tk.Listbox(self.BuildINFOLabelFrame, height=8, width=27)
        for package in self.recentlyREMOVED:
            self.RecentlyRemovedADDONS.insert(0, package)
        self.RecentlyRemovedADDONS.pack()
        self.RecentlyRemovedADDONS.place(x=545, y=25)
        self.PanedWindow.add(self.BuildINFOLabelFrame)
        self.PanedWindow.place(x=5, y=5)
        self.button=Tk.Button(self.root, text="Create", command=lambda:self.OnClick())
        self.button.pack()
        self.button.place(x=720, y=360)

    def OnClick(self):
        os.system(kodiRsync_LocalToRemote)
        self.root.quit()

def kodi_CreateResetBUILD():
    pass

def kodi_RevertToResetBUILD():
    pass

def kodi_CreateBACKUP():
    os.system(kodiRsync_Get_IPTVLists)
    os.system(kodiRsync_Build_Current)


