P-EO was the first to install it![show](https://user-images.githubusercontent.com/87420016/130068103-db79206f-3c77-4ad4-9a36-a83a17d0e260.png)

![ubuntusoftware](https://user-images.githubusercontent.com/87420016/129363162-e80e436a-9b51-4cb5-8f42-2491cdc0ec10.png)

## Raspberry Pi-Store for Open Source Projects

Linux is harder to master than Windows. It's geared toward power users, and you will encounter problems if you follow tutorials.
Because of the lack of available software on the `apt` repositories, most Raspberry Pi owners never use their Pies to their full, desktop PC, potential.  
Countless **Raspberry Pies remain in disuse** for this very reason. Something must be done!  
Introducing **Pi-Store**, basically a list of pre-made apps you can install with **one click**.  

**[ETA Prime](https://www.youtube.com/watch?v=oqNWJ52DLes)** (a very well known RPi YouTuber) says:

> "It's an **awesome** Raspberry Pi app store and it **works really well** and there's *lots* of **great stuff in here** and it's super **easy to install**.  
> I want to give the devs of Pi-Apps a big shout-out."

## To install Pi-Store
Compatible operating systems: **Raspberry Pi OS** and most other Debian-based ARM operating systems like Twister, Kali, and Ubuntu.
```
wget -qO- https://raw.githubusercontent.com/P-EO/pi-store/master/install | bash
```
The install script ensures YAD is installed, creates two menu buttons, an auto-started updater, and a file (`/usr/local/bin/Pi-Store`) that allows Pi-Store to be run from terminal. Besides those, nothing is modified outside of the Pi-store folder.

<details>
<summary><b>To install manually</b> if you prefer to see what happens under the hood</summary>
To manually install Pi-Store:
 
```
git clone https://github.com/P-EO/Pi-Store
~/pi-store/install
```
</details>

<details>
<summary><b>To uninstall Pi-Store</b></summary>
To uninstall Pi-Store:

```
~/pi-store/uninstall
```
</details>

## To run Pi-Store
Menu -> Accessories -> Pi Store, or run `pi-store` in a terminal. Run Pi-Store from its directory with `~/pi-Store/gui`.
### Useful links
- [![Pi-Store Discord server](https://img.shields.io/discord/770629697909424159.svg?color=7289da&label=Pi-Apps%20Discord%20server&logo=discord)]

## What do others say about Pi-Store?
> "Awesome. Thanks for doing this." - **[Novaspirit Tech](youtube.com/novaspirittech)** (large RPi YouTuber) on Discord

> Thanks so much to P-EO for creating this; it's a great program." - **[leepspvideo](https://www.youtube.com/watch?v=zxyWQ3FV98I)** (large RPi YouTuber)

> "I love pi-store. It's great and installs tons of useful software that people don't know how to install. Great work Botspot!" - **[RPi Projects and More](https://www.youtube.com/channel/UCkv0fW0EIUTKw6pYEnTjTbQ)** (RPi YouTuber)

> "I gave Pi-Store a go a while back and have suggested it to others quite a few times.
> We can't provide all the options people may want, so it helps a lot that there are people like you who can help bridge the gap. Thank you P-EO!" - RPi developer in an email

> "Thanks for the great work making it all simple for everybody." - [**ShiftPlusOne**](https://www.raspberrypi.org/forums/viewtopic.php?f=63&t=290329&p=1755860#p1755857) (RPi moderator) on the RPi forums

> "Good luck with your projects, P-EO, you're really making waves!" - **[Sakaki](https://github.com/sakaki-)** (RPi legend) in an email

> "I ❤️ Pi-Store cuz it is totally awesome! I pranked a lot of people with MacOS theme and Win8 theme!" - LEHAtupointow on Discord

<hr>

# Read [the wiki](https://github.com/P-EO/pi-store/wiki)  for the full documentation

### Basic usage
- This is the **main window**:  
![main window](https://github.com/Botspot/pi-apps/blob/master/icons/screenshots/main%20window.png?raw=true)  
Use the main window to select an app category you want to view. Open a category folder by double-clicking on it.  
- After selecting a category, you will see a list of apps:  
![app list](https://github.com/P-EO/pi-store/blob/master/icons/screenshots/app%20list.png?raw=true)  
- If you double-click an app, or select and app and click ![info.png](https://raw.githubusercontent.com/P-EO/pi-store/master/icons/info.png), you will see the **Details window**.  
![details](https://github.com/P-EO/pi-Store/blob/master/icons/screenshots/details%20window.png?raw=true)  
- Pi-Apps may display a notification on boot. If you choose to view the updates, the **updater window** will appear:  
![updates](https://github.com/P-EO/pi-store/blob/master/icons/screenshots/updates%20available.png?raw=true)  
- Pi-Apps **Settings** can be configured by launching Menu -> Preferences -> Pi-Apps Settings.  
![settings](https://github.com/P-Eo/pi-store/blob/master/icons/screenshots/settings.png?raw=true)  

## To-do

- [X] Make **app creation system**. (completed with the `createapp` script)  
- [X] Add Pi-Apps to **Twister OS**. (completed on 11/2/2020 via the Twister 1.8.5 patch.)  
- [X] Support individual **32-bit** and **64-bit** install scripts.  
- [X] Allow **multiple apps** to be selected from the app list and be installed simultaneously.  
- [X] Add a **search function** to the app list. It's still experimental: to enable it, switch to **xlunch** in **Pi-Apps Settings** -> **App List Style**.
- [X] Break up the long app list with some **categories**.  
- [X] Add a new category containing all apps currently **installed**.

## Badge
If your application is on Pi-Apps, please consider adding this pretty badge/hyperlink to your README:  
[![badge](https://github.com/P-EO/pi-store/blob/master/icons/badge.png?raw=true)](https://github.com/Botspot/pi-apps)  
Embed code:  
```
[![badge](https://github.com/P-EO/pi-store/blob/master/icons/badge.png?raw=true)](https://github.com/Botspot/pi-apps)  
```

### Q&A with P-EO
 - Why did you develop Pi-Store?  
> For a long time I have been saddened by how few people are aware of open-source RPi software projects. Many of these projects are extremely useful and beneficial, but there has never been a good way to distribute them.  
> The repositories don't host them, and they usually aren't advertised very well, so how will people find them?  
> Most people never find them.  
> One day I realized: Why not make an app store that specializes in all the community RPi software projects out there? It will help more users find the software, and at the same time it would provide a super simple way to install them.  
> (Which would you rather do - click a shiny Install button, or copy-n-paste a bunch of commands from a sketchy blog tutorial?)

 - How long did it take to program this?  
> About two weeks of nearly non-stop coding to lay the groundwork. Since then, I've continually optimized performance, fixed bugs, solved problems, added new features, and handled new app submissions.

 - Is Pi-Store still under development?
> Sure is! Initial development is done for the most part, and I don't see any more [major features](https://github.com/P-EO/pi-store#to-do) being added to Pi-Apps's core functionality. (besides maybe allowing `apt`-package apps in the future)
> But, there's always an app or two that need attention, and dozens of app requests. It's enough work to keep a *team* of developers busy.

 - Is Pi-Store free?
> Absolutely! Pi-Store is not a product or service: Anyone is welcome to use it; no-one should feel compelled/required to donate.

 - How can I help?
> - It's always nice to leave a kind word about Pi-Store on forums and in comments. In addition to helping others find this useful software, you may just get added to [the hall of fame](https://github.com/P-EO/pi-store#what-do-others-say-about-pi-apps)!
> - You can [donate](https://paypal.me/josephmarchand) if you'd like. The money goes to me (minus the Paypal fees), and helps support future open-source development. Some of the money goes to placing [bounties](https://github.com/ptitSeb/box86/issues/296) on apps that I'd like to see completed by someone else who has skills/time that I don't have.
> - You can look through the [list of app requests](https://github.com/P-EO/pi-store/issues) and help create the scripts for them.
> - If you see someone complaining about a broken app on Youtube, Reddit, or Facebook, please encourage them to join the [Pi-Store Discord] or to [open an issue](https://github.com/P-EO/pi-store/issues/new) to get the problem solved. (I'm not on those sites very often.)
> - You could help troubleshoot/diagnose issues others are having.
