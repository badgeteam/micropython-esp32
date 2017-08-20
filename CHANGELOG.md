# Change Log

## [Unreleased](https://github.com/SHA2017-badge/micropython-esp32/tree/HEAD)

[Full Changelog](https://github.com/SHA2017-badge/micropython-esp32/compare/sha2...HEAD)

**Implemented enhancements:**

- add badge.mpr121\_get\_touch\_info\(\) [\#175](https://github.com/SHA2017-badge/micropython-esp32/pull/175) ([basvs](https://github.com/basvs))
- Fix msg function as per roosteds request [\#144](https://github.com/SHA2017-badge/micropython-esp32/pull/144) ([rnplus](https://github.com/rnplus))

**Fixed bugs:**

- Launcher reset index switching category [\#140](https://github.com/SHA2017-badge/micropython-esp32/issues/140)
- Compensation for bad battery voltage measurements [\#94](https://github.com/SHA2017-badge/micropython-esp32/issues/94)

**Closed issues:**

- Some NVS settings are unreachable [\#209](https://github.com/SHA2017-badge/micropython-esp32/issues/209)
- Flipping the screen doesn't work as expected [\#206](https://github.com/SHA2017-badge/micropython-esp32/issues/206)
- When waking up from touch interrupt, the information about the touch event is lost [\#154](https://github.com/SHA2017-badge/micropython-esp32/issues/154)
- Splash does too many refreshes [\#149](https://github.com/SHA2017-badge/micropython-esp32/issues/149)
- Leaving badge in launcher or installer accidentally drains battery fast [\#148](https://github.com/SHA2017-badge/micropython-esp32/issues/148)
- open\(\) does not allow binary IO [\#146](https://github.com/SHA2017-badge/micropython-esp32/issues/146)
- Lots of ghosting after initial boot & sponsor app [\#137](https://github.com/SHA2017-badge/micropython-esp32/issues/137)
- boot.py not update-able via OTA [\#115](https://github.com/SHA2017-badge/micropython-esp32/issues/115)
- Put peripherals to sleep on deepsleep [\#114](https://github.com/SHA2017-badge/micropython-esp32/issues/114)
- Choose your own \(fancy nick etc\) screensaver [\#110](https://github.com/SHA2017-badge/micropython-esp32/issues/110)
- missing uos.urandom\(n\) in emulator [\#108](https://github.com/SHA2017-badge/micropython-esp32/issues/108)
- If battery is almost empty, nick is not visible anymore [\#96](https://github.com/SHA2017-badge/micropython-esp32/issues/96)
- Battery does not last half a day [\#95](https://github.com/SHA2017-badge/micropython-esp32/issues/95)
- No folders / categories in the launcher and installer [\#91](https://github.com/SHA2017-badge/micropython-esp32/issues/91)
- 'enter' on the OSK should submit the prompt [\#48](https://github.com/SHA2017-badge/micropython-esp32/issues/48)

**Merged pull requests:**

- Run applications from bpp and sdcard as well. [\#228](https://github.com/SHA2017-badge/micropython-esp32/pull/228) ([basvs](https://github.com/basvs))
- add badge.i2c\_read\_reg\(\) and badge.i2c\_write\_reg\(\) [\#226](https://github.com/SHA2017-badge/micropython-esp32/pull/226) ([basvs](https://github.com/basvs))
- add badge.eink\_png\_info\(filename or bytestring\) [\#225](https://github.com/SHA2017-badge/micropython-esp32/pull/225) ([basvs](https://github.com/basvs))
- when the splash screen doesn't start, revert to default splash screen. [\#223](https://github.com/SHA2017-badge/micropython-esp32/pull/223) ([basvs](https://github.com/basvs))
- add justifyTop when drawing text in an ugfx list item. [\#222](https://github.com/SHA2017-badge/micropython-esp32/pull/222) ([basvs](https://github.com/basvs))
- move tm12x6\_font terminus font to read-only memory. [\#220](https://github.com/SHA2017-badge/micropython-esp32/pull/220) ([basvs](https://github.com/basvs))
- Remove badge-event-reminder [\#219](https://github.com/SHA2017-badge/micropython-esp32/pull/219) ([basvs](https://github.com/basvs))
- Add/fixup timezone support [\#218](https://github.com/SHA2017-badge/micropython-esp32/pull/218) ([basvs](https://github.com/basvs))
- Merge upstream [\#217](https://github.com/SHA2017-badge/micropython-esp32/pull/217) ([basvs](https://github.com/basvs))
- work around time.time\(\) brokenness [\#215](https://github.com/SHA2017-badge/micropython-esp32/pull/215) ([basvs](https://github.com/basvs))
- Stop the badge waking up every few tens of seconds [\#213](https://github.com/SHA2017-badge/micropython-esp32/pull/213) ([gavanfantom](https://github.com/gavanfantom))
- allow chdir to mountpoints \('/', '/sdcard' and '/bpp'\) [\#212](https://github.com/SHA2017-badge/micropython-esp32/pull/212) ([basvs](https://github.com/basvs))
- Introduce ugfx\_screen\_flipped in the emulator, too [\#211](https://github.com/SHA2017-badge/micropython-esp32/pull/211) ([raboof](https://github.com/raboof))
- rewrite set\_orientation to use the ugfx\_screen\_flip for rotations \>= … [\#210](https://github.com/SHA2017-badge/micropython-esp32/pull/210) ([basvs](https://github.com/basvs))
- Added small, simple alternative GUI library \(freedomgfx\), which respects all four freedoms [\#208](https://github.com/SHA2017-badge/micropython-esp32/pull/208) ([chca42](https://github.com/chca42))
- update event time and room [\#207](https://github.com/SHA2017-badge/micropython-esp32/pull/207) ([basvs](https://github.com/basvs))
- Safe mode to allow recovery from malware [\#205](https://github.com/SHA2017-badge/micropython-esp32/pull/205) ([gavanfantom](https://github.com/gavanfantom))
- push sponsors app [\#204](https://github.com/SHA2017-badge/micropython-esp32/pull/204) ([basvs](https://github.com/basvs))
- soft reboot in raw REPL mode skips boot.py \(for ampy, pyboard\) [\#203](https://github.com/SHA2017-badge/micropython-esp32/pull/203) ([projectgus](https://github.com/projectgus))
- Read PNG files directly from byte-string. [\#202](https://github.com/SHA2017-badge/micropython-esp32/pull/202) ([basvs](https://github.com/basvs))
- update esp-idf git hash [\#201](https://github.com/SHA2017-badge/micropython-esp32/pull/201) ([basvs](https://github.com/basvs))
- fix update all; update next egg if update failed. [\#200](https://github.com/SHA2017-badge/micropython-esp32/pull/200) ([basvs](https://github.com/basvs))
- add option to stay awake on usb; suppress debug logging [\#199](https://github.com/SHA2017-badge/micropython-esp32/pull/199) ([basvs](https://github.com/basvs))
- Suppress vfs\_native\_file open file error [\#198](https://github.com/SHA2017-badge/micropython-esp32/pull/198) ([basvs](https://github.com/basvs))
- fix max open file descriptors in woezel [\#197](https://github.com/SHA2017-badge/micropython-esp32/pull/197) ([basvs](https://github.com/basvs))
- If a package fails to install, report this to the user. If the reason [\#196](https://github.com/SHA2017-badge/micropython-esp32/pull/196) ([gavanfantom](https://github.com/gavanfantom))
- Erase the otadata partition when flashing firmware, so that we can be… [\#195](https://github.com/SHA2017-badge/micropython-esp32/pull/195) ([gavanfantom](https://github.com/gavanfantom))
- Use a timeout on fetching data, and handle failures gracefully. [\#194](https://github.com/SHA2017-badge/micropython-esp32/pull/194) ([gavanfantom](https://github.com/gavanfantom))
- Use 'with open\(\) as f:' instead of 'f = open\(\)' [\#193](https://github.com/SHA2017-badge/micropython-esp32/pull/193) ([basvs](https://github.com/basvs))
- Revert "Upy use powerdown mgr" [\#191](https://github.com/SHA2017-badge/micropython-esp32/pull/191) ([basvs](https://github.com/basvs))
- fix big-endian packing to 8 bytes [\#190](https://github.com/SHA2017-badge/micropython-esp32/pull/190) ([basvs](https://github.com/basvs))
- Make Jan Henk again. [\#189](https://github.com/SHA2017-badge/micropython-esp32/pull/189) ([ranzbak](https://github.com/ranzbak))
- Change lipo bat indicator voltages [\#188](https://github.com/SHA2017-badge/micropython-esp32/pull/188) ([Roosted7](https://github.com/Roosted7))
- Add make flash to makefile [\#187](https://github.com/SHA2017-badge/micropython-esp32/pull/187) ([Roosted7](https://github.com/Roosted7))
- add experimental temperature sensor and hall sensor. [\#186](https://github.com/SHA2017-badge/micropython-esp32/pull/186) ([basvs](https://github.com/basvs))
- Add a new optional argument to the draw\(\) function in a service, whic… [\#185](https://github.com/SHA2017-badge/micropython-esp32/pull/185) ([gavanfantom](https://github.com/gavanfantom))
- Fix redraw loop when idle [\#184](https://github.com/SHA2017-badge/micropython-esp32/pull/184) ([gavanfantom](https://github.com/gavanfantom))
- Add time to OTA check [\#182](https://github.com/SHA2017-badge/micropython-esp32/pull/182) ([rnplus](https://github.com/rnplus))
- Allow services to execute a special draw function just before sleeping [\#181](https://github.com/SHA2017-badge/micropython-esp32/pull/181) ([rnplus](https://github.com/rnplus))
- Exception reporting and post OTA update script [\#180](https://github.com/SHA2017-badge/micropython-esp32/pull/180) ([rnplus](https://github.com/rnplus))
- add wrapper around badge\_eink\_display\(\) method [\#179](https://github.com/SHA2017-badge/micropython-esp32/pull/179) ([basvs](https://github.com/basvs))
- New launcher [\#178](https://github.com/SHA2017-badge/micropython-esp32/pull/178) ([rnplus](https://github.com/rnplus))
- add simple wrapper for low-level bpp flash data [\#177](https://github.com/SHA2017-badge/micropython-esp32/pull/177) ([basvs](https://github.com/basvs))
- do not re-install the gpio-isr-service. it's already installed. [\#176](https://github.com/SHA2017-badge/micropython-esp32/pull/176) ([basvs](https://github.com/basvs))
- Add set\_timeout to power management [\#174](https://github.com/SHA2017-badge/micropython-esp32/pull/174) ([rnplus](https://github.com/rnplus))
- Add update all app to firmware [\#173](https://github.com/SHA2017-badge/micropython-esp32/pull/173) ([rnplus](https://github.com/rnplus))
- Add power management to launcher [\#172](https://github.com/SHA2017-badge/micropython-esp32/pull/172) ([rnplus](https://github.com/rnplus))
- Move mount-code to modbadge; add sdcard support [\#171](https://github.com/SHA2017-badge/micropython-esp32/pull/171) ([basvs](https://github.com/basvs))
- Change led brightness for event reminder and make rtc mandatory again [\#170](https://github.com/SHA2017-badge/micropython-esp32/pull/170) ([rnplus](https://github.com/rnplus))
- Fixed a couple of small bugs [\#169](https://github.com/SHA2017-badge/micropython-esp32/pull/169) ([rnplus](https://github.com/rnplus))
- Add some sugar and spice to make things nice [\#168](https://github.com/SHA2017-badge/micropython-esp32/pull/168) ([rnplus](https://github.com/rnplus))
- Renze cleanup [\#167](https://github.com/SHA2017-badge/micropython-esp32/pull/167) ([rnplus](https://github.com/rnplus))
- set type after determining type.. [\#166](https://github.com/SHA2017-badge/micropython-esp32/pull/166) ([basvs](https://github.com/basvs))
- Add nice change by raboof [\#165](https://github.com/SHA2017-badge/micropython-esp32/pull/165) ([rnplus](https://github.com/rnplus))
- Working services [\#164](https://github.com/SHA2017-badge/micropython-esp32/pull/164) ([rnplus](https://github.com/rnplus))
- Add some warning notes when using badge.leds\_send\_data\(\) incorrectly [\#163](https://github.com/SHA2017-badge/micropython-esp32/pull/163) ([basvs](https://github.com/basvs))
- Add optional timestamp argument to easyrtc.string\(\) [\#160](https://github.com/SHA2017-badge/micropython-esp32/pull/160) ([rnplus](https://github.com/rnplus))
- Upy use powerdown mgr [\#159](https://github.com/SHA2017-badge/micropython-esp32/pull/159) ([Spritetm](https://github.com/Spritetm))
- Service api v2 [\#158](https://github.com/SHA2017-badge/micropython-esp32/pull/158) ([rnplus](https://github.com/rnplus))
- Lower loglevel of wifi at runtime [\#157](https://github.com/SHA2017-badge/micropython-esp32/pull/157) ([Roosted7](https://github.com/Roosted7))
- Fix errors introduced by changing easydraw.msg\(\) function [\#155](https://github.com/SHA2017-badge/micropython-esp32/pull/155) ([rnplus](https://github.com/rnplus))
- add badge.eink\_deep\_sleep\(\) and badge.eink\_wakeup\(\) [\#153](https://github.com/SHA2017-badge/micropython-esp32/pull/153) ([basvs](https://github.com/basvs))
- Add more badge\_power hooks. [\#151](https://github.com/SHA2017-badge/micropython-esp32/pull/151) ([basvs](https://github.com/basvs))
- add badge.GREYSCALE const. [\#150](https://github.com/SHA2017-badge/micropython-esp32/pull/150) ([basvs](https://github.com/basvs))
- initialize with default eink type. \(as configured in make menuconfig\) [\#145](https://github.com/SHA2017-badge/micropython-esp32/pull/145) ([basvs](https://github.com/basvs))
- Fix a big bug and a little bit of cleaning [\#143](https://github.com/SHA2017-badge/micropython-esp32/pull/143) ([rnplus](https://github.com/rnplus))
- Split splash into smaller parts, thereby creating helper files for some functions [\#142](https://github.com/SHA2017-badge/micropython-esp32/pull/142) ([rnplus](https://github.com/rnplus))
- Makefile improvements [\#141](https://github.com/SHA2017-badge/micropython-esp32/pull/141) ([basvs](https://github.com/basvs))
- Bugfixes for splash [\#139](https://github.com/SHA2017-badge/micropython-esp32/pull/139) ([rnplus](https://github.com/rnplus))
- Updated splash code and try to mount bpp [\#138](https://github.com/SHA2017-badge/micropython-esp32/pull/138) ([rnplus](https://github.com/rnplus))
- Up installer WiFi timeout from 4s to 15s [\#136](https://github.com/SHA2017-badge/micropython-esp32/pull/136) ([niekproductions](https://github.com/niekproductions))
- Update demo.py [\#135](https://github.com/SHA2017-badge/micropython-esp32/pull/135) ([powermik](https://github.com/powermik))
- renamed badge\_portexp to badge\_fxl6408 [\#134](https://github.com/SHA2017-badge/micropython-esp32/pull/134) ([basvs](https://github.com/basvs))
- Pull changes from upstream [\#133](https://github.com/SHA2017-badge/micropython-esp32/pull/133) ([Roosted7](https://github.com/Roosted7))
- badge\_touch -\> badge\_cpt112s [\#132](https://github.com/SHA2017-badge/micropython-esp32/pull/132) ([basvs](https://github.com/basvs))
- uos.urandom\(\) bugfix. [\#131](https://github.com/SHA2017-badge/micropython-esp32/pull/131) ([basvs](https://github.com/basvs))
- Added gfx\_userfs glue to micropython build [\#130](https://github.com/SHA2017-badge/micropython-esp32/pull/130) ([aczid](https://github.com/aczid))
- Add support for removal of NVS page [\#129](https://github.com/SHA2017-badge/micropython-esp32/pull/129) ([Roosted7](https://github.com/Roosted7))
- Added a urandom port for Unix build [\#127](https://github.com/SHA2017-badge/micropython-esp32/pull/127) ([aczid](https://github.com/aczid))

## [sha2](https://github.com/SHA2017-badge/micropython-esp32/tree/sha2) (2017-07-26)
[Full Changelog](https://github.com/SHA2017-badge/micropython-esp32/compare/sha1...sha2)

**Implemented enhancements:**

- Installer rewrite w/ category support [\#120](https://github.com/SHA2017-badge/micropython-esp32/pull/120) ([niekproductions](https://github.com/niekproductions))
- Launcher UX fixes [\#107](https://github.com/SHA2017-badge/micropython-esp32/pull/107) ([niekproductions](https://github.com/niekproductions))

**Closed issues:**

- Led driver not working properly above Hex 0x7F [\#119](https://github.com/SHA2017-badge/micropython-esp32/issues/119)
- ugfx.init\(\) flashes screen [\#112](https://github.com/SHA2017-badge/micropython-esp32/issues/112)
- rtcmem: check if offset is valid [\#111](https://github.com/SHA2017-badge/micropython-esp32/issues/111)
- 'Flash' button not used [\#99](https://github.com/SHA2017-badge/micropython-esp32/issues/99)
- nvs\_\[get/set\]\_u\[8/16\] not working [\#93](https://github.com/SHA2017-badge/micropython-esp32/issues/93)
- woezel unzip dict size [\#82](https://github.com/SHA2017-badge/micropython-esp32/issues/82)
- Sponsor app not working [\#78](https://github.com/SHA2017-badge/micropython-esp32/issues/78)

**Merged pull requests:**

- Consistent UI and updated installer [\#126](https://github.com/SHA2017-badge/micropython-esp32/pull/126) ([Roosted7](https://github.com/Roosted7))
- use input framework to check for waiting input. [\#125](https://github.com/SHA2017-badge/micropython-esp32/pull/125) ([basvs](https://github.com/basvs))
- New setup and default name [\#124](https://github.com/SHA2017-badge/micropython-esp32/pull/124) ([Roosted7](https://github.com/Roosted7))
- support negative offsets in png image loading [\#122](https://github.com/SHA2017-badge/micropython-esp32/pull/122) ([annejan](https://github.com/annejan))
- cleanup esp-rtcmem code. throw out-of-range exceptions. [\#121](https://github.com/SHA2017-badge/micropython-esp32/pull/121) ([basvs](https://github.com/basvs))
- Update makefile: faster boot and flash [\#118](https://github.com/SHA2017-badge/micropython-esp32/pull/118) ([Roosted7](https://github.com/Roosted7))
- Major python code change [\#116](https://github.com/SHA2017-badge/micropython-esp32/pull/116) ([Roosted7](https://github.com/Roosted7))
- Added extra urandom functions [\#109](https://github.com/SHA2017-badge/micropython-esp32/pull/109) ([aczid](https://github.com/aczid))
- lower max\_files from 8 to 3. [\#106](https://github.com/SHA2017-badge/micropython-esp32/pull/106) ([basvs](https://github.com/basvs))
- Remove deprecated led function [\#105](https://github.com/SHA2017-badge/micropython-esp32/pull/105) ([Roosted7](https://github.com/Roosted7))
- expose badge.nvs\_erase\_key\(\) [\#103](https://github.com/SHA2017-badge/micropython-esp32/pull/103) ([basvs](https://github.com/basvs))
- Code cleanup of the badge.nvs\_\* code. [\#102](https://github.com/SHA2017-badge/micropython-esp32/pull/102) ([basvs](https://github.com/basvs))
- Setup.state as u8 and shorter keys [\#101](https://github.com/SHA2017-badge/micropython-esp32/pull/101) ([rnplus](https://github.com/rnplus))
- report tls error messages instead of crashing. [\#100](https://github.com/SHA2017-badge/micropython-esp32/pull/100) ([basvs](https://github.com/basvs))

## [sha1](https://github.com/SHA2017-badge/micropython-esp32/tree/sha1) (2017-07-21)
[Full Changelog](https://github.com/SHA2017-badge/micropython-esp32/compare/v1.9.1...sha1)

**Implemented enhancements:**

- Nicer launcher \(Sebastius' work\) [\#67](https://github.com/SHA2017-badge/micropython-esp32/pull/67) ([niekproductions](https://github.com/niekproductions))

**Closed issues:**

- initial fatfs for micropython [\#80](https://github.com/SHA2017-badge/micropython-esp32/issues/80)
- '123' on the OSK crashes the badge [\#49](https://github.com/SHA2017-badge/micropython-esp32/issues/49)
- 'shift' on the OSK restarts the app [\#47](https://github.com/SHA2017-badge/micropython-esp32/issues/47)

**Merged pull requests:**

- Zo is ie mooier. [\#88](https://github.com/SHA2017-badge/micropython-esp32/pull/88) ([rnplus](https://github.com/rnplus))
- About [\#87](https://github.com/SHA2017-badge/micropython-esp32/pull/87) ([rnplus](https://github.com/rnplus))
- OTA check + Other fixes [\#86](https://github.com/SHA2017-badge/micropython-esp32/pull/86) ([rnplus](https://github.com/rnplus))
- dump esp heap info. [\#85](https://github.com/SHA2017-badge/micropython-esp32/pull/85) ([basvs](https://github.com/basvs))
- Basvs ugfx greyscale [\#84](https://github.com/SHA2017-badge/micropython-esp32/pull/84) ([annejan](https://github.com/annejan))
- Basvs preseed unzip [\#83](https://github.com/SHA2017-badge/micropython-esp32/pull/83) ([annejan](https://github.com/annejan))
- update wifiSetup [\#81](https://github.com/SHA2017-badge/micropython-esp32/pull/81) ([Roosted7](https://github.com/Roosted7))
- Add static wifiSetup module [\#79](https://github.com/SHA2017-badge/micropython-esp32/pull/79) ([Roosted7](https://github.com/Roosted7))
- Remove flashing script from upy dir [\#77](https://github.com/SHA2017-badge/micropython-esp32/pull/77) ([Roosted7](https://github.com/Roosted7))
- add badge\_eink\_fb.o [\#76](https://github.com/SHA2017-badge/micropython-esp32/pull/76) ([annejan](https://github.com/annejan))
- Use esp-idf vfs [\#75](https://github.com/SHA2017-badge/micropython-esp32/pull/75) ([annejan](https://github.com/annejan))
- Use the async dialogs.prompt\_text api [\#74](https://github.com/SHA2017-badge/micropython-esp32/pull/74) ([raboof](https://github.com/raboof))
- First-run crashes . . [\#73](https://github.com/SHA2017-badge/micropython-esp32/pull/73) ([annejan](https://github.com/annejan))
- Add BPP and extra NVS options to splash [\#72](https://github.com/SHA2017-badge/micropython-esp32/pull/72) ([rnplus](https://github.com/rnplus))
- NTP timeout from NVS [\#71](https://github.com/SHA2017-badge/micropython-esp32/pull/71) ([rnplus](https://github.com/rnplus))
- Lots of stuff: a bugfix in the service routine, moar settings and a c… [\#70](https://github.com/SHA2017-badge/micropython-esp32/pull/70) ([rnplus](https://github.com/rnplus))
- Dialogs: async API for text prompt [\#68](https://github.com/SHA2017-badge/micropython-esp32/pull/68) ([raboof](https://github.com/raboof))
- Allow services to draw on homescreen [\#66](https://github.com/SHA2017-badge/micropython-esp32/pull/66) ([rnplus](https://github.com/rnplus))
- tell nvs\_get\_str\(\) the buffer-length; lower buffer size to 256 bytes [\#65](https://github.com/SHA2017-badge/micropython-esp32/pull/65) ([basvs](https://github.com/basvs))
- Updated launcher, added nickname setup and non-functional sponsors app [\#64](https://github.com/SHA2017-badge/micropython-esp32/pull/64) ([rnplus](https://github.com/rnplus))
- Remove esp.start\_sleeping \(use machine.deepsleep instead\). Add services to splash.py. [\#63](https://github.com/SHA2017-badge/micropython-esp32/pull/63) ([rnplus](https://github.com/rnplus))
- Put installer and OTA at the top of the menu [\#62](https://github.com/SHA2017-badge/micropython-esp32/pull/62) ([Roosted7](https://github.com/Roosted7))
- Flash firmware faster [\#61](https://github.com/SHA2017-badge/micropython-esp32/pull/61) ([Roosted7](https://github.com/Roosted7))
- Ported from @loboris [\#60](https://github.com/SHA2017-badge/micropython-esp32/pull/60) ([annejan](https://github.com/annejan))
- Fix timer in dialogs.py [\#58](https://github.com/SHA2017-badge/micropython-esp32/pull/58) ([Roosted7](https://github.com/Roosted7))
- use esp partition data to determine fat location and size. [\#57](https://github.com/SHA2017-badge/micropython-esp32/pull/57) ([basvs](https://github.com/basvs))
- Be able to pass do\_select variable to  [\#56](https://github.com/SHA2017-badge/micropython-esp32/pull/56) ([dennisdegreef](https://github.com/dennisdegreef))
- Add splash / home screen application [\#55](https://github.com/SHA2017-badge/micropython-esp32/pull/55) ([rnplus](https://github.com/rnplus))
- NVS as config store [\#53](https://github.com/SHA2017-badge/micropython-esp32/pull/53) ([annejan](https://github.com/annejan))
- small bug fix in flashfbdev.py/modesp.c [\#52](https://github.com/SHA2017-badge/micropython-esp32/pull/52) ([annejan](https://github.com/annejan))
- Preliminary support for callbacks for buttons [\#51](https://github.com/SHA2017-badge/micropython-esp32/pull/51) ([raboof](https://github.com/raboof))
- Support capitals in prompt\_text \(fixes \#47\) [\#50](https://github.com/SHA2017-badge/micropython-esp32/pull/50) ([raboof](https://github.com/raboof))
- Correctly detect presence of keyword parameters [\#46](https://github.com/SHA2017-badge/micropython-esp32/pull/46) ([raboof](https://github.com/raboof))
- Support dialog.prompt\_text with on-screen keyboard [\#45](https://github.com/SHA2017-badge/micropython-esp32/pull/45) ([raboof](https://github.com/raboof))
- Wear levelling proposed upstream [\#44](https://github.com/SHA2017-badge/micropython-esp32/pull/44) ([annejan](https://github.com/annejan))
- Fix dialog.notice and .prompt\_boolean [\#43](https://github.com/SHA2017-badge/micropython-esp32/pull/43) ([raboof](https://github.com/raboof))
- Fix launching the installer [\#42](https://github.com/SHA2017-badge/micropython-esp32/pull/42) ([raboof](https://github.com/raboof))
- OTA attempt and ussl entropy fix [\#41](https://github.com/SHA2017-badge/micropython-esp32/pull/41) ([annejan](https://github.com/annejan))
- Reduce flushes [\#40](https://github.com/SHA2017-badge/micropython-esp32/pull/40) ([raboof](https://github.com/raboof))
- SSL validation for sha2017.org subdomains [\#38](https://github.com/SHA2017-badge/micropython-esp32/pull/38) ([annejan](https://github.com/annejan))
- Cleanup of build process [\#37](https://github.com/SHA2017-badge/micropython-esp32/pull/37) ([annejan](https://github.com/annejan))
- badge.eink\_busy\(\) and badge.eink\_busy\_wait\(\) [\#36](https://github.com/SHA2017-badge/micropython-esp32/pull/36) ([annejan](https://github.com/annejan))
- Only flush once per keypress [\#35](https://github.com/SHA2017-badge/micropython-esp32/pull/35) ([raboof](https://github.com/raboof))
- Destroy list before launching app [\#34](https://github.com/SHA2017-badge/micropython-esp32/pull/34) ([raboof](https://github.com/raboof))
- Sebastius [\#33](https://github.com/SHA2017-badge/micropython-esp32/pull/33) ([sebastius](https://github.com/sebastius))
- Lets boot straight to launcher instead of a demo app. [\#32](https://github.com/SHA2017-badge/micropython-esp32/pull/32) ([sebastius](https://github.com/sebastius))
- Fix for len= global overwrite [\#31](https://github.com/SHA2017-badge/micropython-esp32/pull/31) ([aczid](https://github.com/aczid))
- Added required tjpegd source file for JPG decoder [\#30](https://github.com/SHA2017-badge/micropython-esp32/pull/30) ([aczid](https://github.com/aczid))
- Enabled support for JPEG images [\#29](https://github.com/SHA2017-badge/micropython-esp32/pull/29) ([aczid](https://github.com/aczid))
- Testable BMP/PNG support [\#28](https://github.com/SHA2017-badge/micropython-esp32/pull/28) ([aczid](https://github.com/aczid))
- Updated UGFX widget bindings [\#27](https://github.com/SHA2017-badge/micropython-esp32/pull/27) ([aczid](https://github.com/aczid))
- .search\(query\), an empty query lists all eggs [\#26](https://github.com/SHA2017-badge/micropython-esp32/pull/26) ([f0x52](https://github.com/f0x52))
- .search .list [\#25](https://github.com/SHA2017-badge/micropython-esp32/pull/25) ([f0x52](https://github.com/f0x52))
- Added listing, dumping and loading of fonts [\#24](https://github.com/SHA2017-badge/micropython-esp32/pull/24) ([aczid](https://github.com/aczid))
- Master [\#23](https://github.com/SHA2017-badge/micropython-esp32/pull/23) ([annejan](https://github.com/annejan))
- Only link led driver when the driver is enabled through the device config [\#22](https://github.com/SHA2017-badge/micropython-esp32/pull/22) ([aczid](https://github.com/aczid))
- Unix version works on macOS now [\#21](https://github.com/SHA2017-badge/micropython-esp32/pull/21) ([annejan](https://github.com/annejan))
- Dev ussl nonblocking [\#20](https://github.com/SHA2017-badge/micropython-esp32/pull/20) ([annejan](https://github.com/annejan))
- Upstream updates [\#18](https://github.com/SHA2017-badge/micropython-esp32/pull/18) ([annejan](https://github.com/annejan))
- esp32/main.c: Added machine.reset\_cause\(\) [\#17](https://github.com/SHA2017-badge/micropython-esp32/pull/17) ([annejan](https://github.com/annejan))
- Fixed button callbacks to start from 1-index not 0 [\#16](https://github.com/SHA2017-badge/micropython-esp32/pull/16) ([aczid](https://github.com/aczid))
- help\(\) function intro text [\#15](https://github.com/SHA2017-badge/micropython-esp32/pull/15) ([aczid](https://github.com/aczid))
- Merge new serial features from micropython upstream [\#14](https://github.com/SHA2017-badge/micropython-esp32/pull/14) ([Roosted7](https://github.com/Roosted7))
- Using mutex-locked version of ginputToggleWakeup [\#13](https://github.com/SHA2017-badge/micropython-esp32/pull/13) ([aczid](https://github.com/aczid))
- Added symlinks for sdcard / vibrator drivers [\#12](https://github.com/SHA2017-badge/micropython-esp32/pull/12) ([aczid](https://github.com/aczid))
- UGFX input driver for micropython + SDL keyboard driver [\#11](https://github.com/SHA2017-badge/micropython-esp32/pull/11) ([aczid](https://github.com/aczid))
- Added modules woezel and urequests to unix build [\#10](https://github.com/SHA2017-badge/micropython-esp32/pull/10) ([aczid](https://github.com/aczid))

## [v1.9.1](https://github.com/SHA2017-badge/micropython-esp32/tree/v1.9.1) (2017-06-11)
[Full Changelog](https://github.com/SHA2017-badge/micropython-esp32/compare/v1.9...v1.9.1)

**Merged pull requests:**

- More fixes for Unix build [\#9](https://github.com/SHA2017-badge/micropython-esp32/pull/9) ([aczid](https://github.com/aczid))
- Added mocks for modbadge / modnetwork [\#8](https://github.com/SHA2017-badge/micropython-esp32/pull/8) ([aczid](https://github.com/aczid))
- Made the demo thingy properly center text.  [\#7](https://github.com/SHA2017-badge/micropython-esp32/pull/7) ([Peetz0r](https://github.com/Peetz0r))
- Added support for compiling micropython on Linux with SDL-backed ugfx [\#6](https://github.com/SHA2017-badge/micropython-esp32/pull/6) ([aczid](https://github.com/aczid))
- Roosted7's update to latest ESP-IDF [\#5](https://github.com/SHA2017-badge/micropython-esp32/pull/5) ([annejan](https://github.com/annejan))
- Proper deepsleep as proposed upstream  [\#4](https://github.com/SHA2017-badge/micropython-esp32/pull/4) ([annejan](https://github.com/annejan))
- esp32/modsocket: Make read/write return None when in non-blocking mode. [\#3](https://github.com/SHA2017-badge/micropython-esp32/pull/3) ([annejan](https://github.com/annejan))
- Add a mp api that allows for using the RTC non-volatile memory. [\#2](https://github.com/SHA2017-badge/micropython-esp32/pull/2) ([rnplus](https://github.com/rnplus))
- Updated from micropython-esp32 [\#1](https://github.com/SHA2017-badge/micropython-esp32/pull/1) ([annejan](https://github.com/annejan))

## [v1.9](https://github.com/SHA2017-badge/micropython-esp32/tree/v1.9) (2017-05-26)
[Full Changelog](https://github.com/SHA2017-badge/micropython-esp32/compare/v1.8.7...v1.9)

**Merged pull requests:**

- Dev machine unique [\#19](https://github.com/SHA2017-badge/micropython-esp32/pull/19) ([annejan](https://github.com/annejan))

## [v1.8.7](https://github.com/SHA2017-badge/micropython-esp32/tree/v1.8.7) (2017-01-08)
[Full Changelog](https://github.com/SHA2017-badge/micropython-esp32/compare/v1.8.6...v1.8.7)

## [v1.8.6](https://github.com/SHA2017-badge/micropython-esp32/tree/v1.8.6) (2016-11-10)
[Full Changelog](https://github.com/SHA2017-badge/micropython-esp32/compare/v1.8.5...v1.8.6)

## [v1.8.5](https://github.com/SHA2017-badge/micropython-esp32/tree/v1.8.5) (2016-10-17)
[Full Changelog](https://github.com/SHA2017-badge/micropython-esp32/compare/v1.8.4...v1.8.5)

## [v1.8.4](https://github.com/SHA2017-badge/micropython-esp32/tree/v1.8.4) (2016-09-09)
[Full Changelog](https://github.com/SHA2017-badge/micropython-esp32/compare/v1.8.3...v1.8.4)

## [v1.8.3](https://github.com/SHA2017-badge/micropython-esp32/tree/v1.8.3) (2016-08-09)
[Full Changelog](https://github.com/SHA2017-badge/micropython-esp32/compare/v1.8.2...v1.8.3)

## [v1.8.2](https://github.com/SHA2017-badge/micropython-esp32/tree/v1.8.2) (2016-07-10)
[Full Changelog](https://github.com/SHA2017-badge/micropython-esp32/compare/v1.8.1...v1.8.2)

## [v1.8.1](https://github.com/SHA2017-badge/micropython-esp32/tree/v1.8.1) (2016-06-03)
[Full Changelog](https://github.com/SHA2017-badge/micropython-esp32/compare/v1.8...v1.8.1)

## [v1.8](https://github.com/SHA2017-badge/micropython-esp32/tree/v1.8) (2016-05-03)
[Full Changelog](https://github.com/SHA2017-badge/micropython-esp32/compare/v1.7...v1.8)

## [v1.7](https://github.com/SHA2017-badge/micropython-esp32/tree/v1.7) (2016-04-11)
[Full Changelog](https://github.com/SHA2017-badge/micropython-esp32/compare/v1.6...v1.7)

## [v1.6](https://github.com/SHA2017-badge/micropython-esp32/tree/v1.6) (2016-01-31)
[Full Changelog](https://github.com/SHA2017-badge/micropython-esp32/compare/v1.5.2...v1.6)

## [v1.5.2](https://github.com/SHA2017-badge/micropython-esp32/tree/v1.5.2) (2015-12-31)
[Full Changelog](https://github.com/SHA2017-badge/micropython-esp32/compare/v1.5.1...v1.5.2)

## [v1.5.1](https://github.com/SHA2017-badge/micropython-esp32/tree/v1.5.1) (2015-11-23)
[Full Changelog](https://github.com/SHA2017-badge/micropython-esp32/compare/v1.5...v1.5.1)

## [v1.5](https://github.com/SHA2017-badge/micropython-esp32/tree/v1.5) (2015-10-21)
[Full Changelog](https://github.com/SHA2017-badge/micropython-esp32/compare/v1.4.6...v1.5)

## [v1.4.6](https://github.com/SHA2017-badge/micropython-esp32/tree/v1.4.6) (2015-09-23)
[Full Changelog](https://github.com/SHA2017-badge/micropython-esp32/compare/v1.4.5...v1.4.6)

## [v1.4.5](https://github.com/SHA2017-badge/micropython-esp32/tree/v1.4.5) (2015-08-11)
[Full Changelog](https://github.com/SHA2017-badge/micropython-esp32/compare/v1.4.4...v1.4.5)

## [v1.4.4](https://github.com/SHA2017-badge/micropython-esp32/tree/v1.4.4) (2015-06-15)
[Full Changelog](https://github.com/SHA2017-badge/micropython-esp32/compare/v1.4.3...v1.4.4)

## [v1.4.3](https://github.com/SHA2017-badge/micropython-esp32/tree/v1.4.3) (2015-05-16)
[Full Changelog](https://github.com/SHA2017-badge/micropython-esp32/compare/v1.4.2...v1.4.3)

## [v1.4.2](https://github.com/SHA2017-badge/micropython-esp32/tree/v1.4.2) (2015-04-21)
[Full Changelog](https://github.com/SHA2017-badge/micropython-esp32/compare/v1.4.1...v1.4.2)

## [v1.4.1](https://github.com/SHA2017-badge/micropython-esp32/tree/v1.4.1) (2015-04-04)
[Full Changelog](https://github.com/SHA2017-badge/micropython-esp32/compare/v1.4...v1.4.1)

## [v1.4](https://github.com/SHA2017-badge/micropython-esp32/tree/v1.4) (2015-03-29)
[Full Changelog](https://github.com/SHA2017-badge/micropython-esp32/compare/v1.3.10...v1.4)

## [v1.3.10](https://github.com/SHA2017-badge/micropython-esp32/tree/v1.3.10) (2015-02-13)
[Full Changelog](https://github.com/SHA2017-badge/micropython-esp32/compare/v1.3.9...v1.3.10)

## [v1.3.9](https://github.com/SHA2017-badge/micropython-esp32/tree/v1.3.9) (2015-01-25)
[Full Changelog](https://github.com/SHA2017-badge/micropython-esp32/compare/v1.3.8...v1.3.9)

## [v1.3.8](https://github.com/SHA2017-badge/micropython-esp32/tree/v1.3.8) (2014-12-28)
[Full Changelog](https://github.com/SHA2017-badge/micropython-esp32/compare/v1.3.7...v1.3.8)

## [v1.3.7](https://github.com/SHA2017-badge/micropython-esp32/tree/v1.3.7) (2014-11-28)
[Full Changelog](https://github.com/SHA2017-badge/micropython-esp32/compare/v1.3.6...v1.3.7)

## [v1.3.6](https://github.com/SHA2017-badge/micropython-esp32/tree/v1.3.6) (2014-11-04)
[Full Changelog](https://github.com/SHA2017-badge/micropython-esp32/compare/v1.3.5...v1.3.6)

## [v1.3.5](https://github.com/SHA2017-badge/micropython-esp32/tree/v1.3.5) (2014-10-26)
[Full Changelog](https://github.com/SHA2017-badge/micropython-esp32/compare/v1.3.4...v1.3.5)

## [v1.3.4](https://github.com/SHA2017-badge/micropython-esp32/tree/v1.3.4) (2014-10-21)
[Full Changelog](https://github.com/SHA2017-badge/micropython-esp32/compare/v1.3.3...v1.3.4)

## [v1.3.3](https://github.com/SHA2017-badge/micropython-esp32/tree/v1.3.3) (2014-10-02)
[Full Changelog](https://github.com/SHA2017-badge/micropython-esp32/compare/v1.3.2...v1.3.3)

## [v1.3.2](https://github.com/SHA2017-badge/micropython-esp32/tree/v1.3.2) (2014-09-25)
[Full Changelog](https://github.com/SHA2017-badge/micropython-esp32/compare/v1.3.1...v1.3.2)

## [v1.3.1](https://github.com/SHA2017-badge/micropython-esp32/tree/v1.3.1) (2014-08-28)
[Full Changelog](https://github.com/SHA2017-badge/micropython-esp32/compare/v1.3...v1.3.1)

## [v1.3](https://github.com/SHA2017-badge/micropython-esp32/tree/v1.3) (2014-08-12)
[Full Changelog](https://github.com/SHA2017-badge/micropython-esp32/compare/v1.2...v1.3)

## [v1.2](https://github.com/SHA2017-badge/micropython-esp32/tree/v1.2) (2014-07-13)
[Full Changelog](https://github.com/SHA2017-badge/micropython-esp32/compare/v1.1.1...v1.2)

## [v1.1.1](https://github.com/SHA2017-badge/micropython-esp32/tree/v1.1.1) (2014-06-15)
[Full Changelog](https://github.com/SHA2017-badge/micropython-esp32/compare/v1.1...v1.1.1)

## [v1.1](https://github.com/SHA2017-badge/micropython-esp32/tree/v1.1) (2014-06-12)
[Full Changelog](https://github.com/SHA2017-badge/micropython-esp32/compare/v1.0.1...v1.1)

## [v1.0.1](https://github.com/SHA2017-badge/micropython-esp32/tree/v1.0.1) (2014-05-11)
[Full Changelog](https://github.com/SHA2017-badge/micropython-esp32/compare/v1.0...v1.0.1)

## [v1.0](https://github.com/SHA2017-badge/micropython-esp32/tree/v1.0) (2014-05-03)
[Full Changelog](https://github.com/SHA2017-badge/micropython-esp32/compare/v1.0-rc1...v1.0)

## [v1.0-rc1](https://github.com/SHA2017-badge/micropython-esp32/tree/v1.0-rc1) (2014-05-03)


\* *This Change Log was automatically generated by [github_changelog_generator](https://github.com/skywinder/Github-Changelog-Generator)*