[app]
title = FitApp
package.name = fitapp
package.domain = org.nrvnitish
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy,kivymd
orientation = portrait
osx.kivy_version = 2.1.0

[buildozer]
log_level = 2
warn_on_root = 1

[app:android]
android.api = 31
android.sdk = 31
android.ndk = 23b
android.arch = armeabi-v7a
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.build_tools_version = 30.0.3
