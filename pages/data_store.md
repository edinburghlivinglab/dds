---
layout: page
title: "Using DataStore for Data Management"
permalink: "/data_store/"
---
# Overview

The University's [DataStore](http://www.ed.ac.uk/information-services/research-support/data-management/data-storage) is a central file store intended for researchers. In DDS, we will be using it as a shared place where data that is gathered by teams can be securely shared. 

This is particularly crucial since some of the research data collected by DDS teams is likely to count as personal data. On the other hand, team members will need to share the data they have collected. Rather than using a 3rd party cloud service for sharing, students should upload the relevant files to DataStore. Within the filespace identified below, each team will have their own subfolder, named `team_1`,..., `team_7` as appropriate, where files can be shared amongst the team members.

# Accessing DataStore

In order to access DataStore, you must be on a machine connected to the University network, or connected to the University VPN. The University's Information Services gives [detailed instructions](http://www.ed.ac.uk/information-services/computing/desktop-personal/network-shares) on how to get network access to DataStore, but we'll give you the short version here. In each case, you will have to authenticate by entering your UUN (University login name) and your corresponding password.

Once you have established a connection to the DataStore DDS folder, you should be able to upload and download files to a local computer. Please make sure that any computing device that you use for storing files is adequately protected, following the guidelines [Your responsibilities at work](http://www.ed.ac.uk/information-services/computing/desktop-personal/information-security/your-responsibilities).

## Windows

1. Select **Start** > **Computer** > **Map network drive**.
2. In the **Drive** list, click a drive letter. You can choose any available letter.
3. In the **Folder** box, type the following address for the DDS folder:

```
csce.datastore.ed.ac.uk\csce\inf\groups\ell\dds
```

## Mac OS

2. In the Finder, select **Go** from the menu bar at the top of the desktop, then select **Connect to Server**...
3. In the **Connect to Server** window, type the following address for the DDS folder:

```
smb://csce.datastore.ed.ac.uk/csce/inf/groups/ell/dds
```

## Linux (including DICE)

1. Open Graphical File manager window
2. Select **Connect to Server**
3. In the **Server Address** window, type the following address of the DDS folder:

```
smb://csce.datastore.ed.ac.uk/csce/inf/groups/ell/dds
```

If you are feeling masochistic, you should also be able to connect on the command line with the following commands:

<code>
smbclient \\\\csce.datastore.ed.ac.uk\\csce -W ED -U UUN<br/>
cd \inf\groups\ell
</code>

<!--

https://www.wiki.ed.ac.uk/display/ecdfwiki/DataStore+service
https://www.wiki.ed.ac.uk/display/ecdfwiki/DataStore+-+General+Instructions#DataStore-GeneralInstructions-ManagingAccessPermissions



http://www.ed.ac.uk/records-management/records-management/staff-guidance/technical-guidance/storage-standards
-->
