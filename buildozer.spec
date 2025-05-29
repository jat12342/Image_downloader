[app]
title = Image Downloader
package.name = imagedownloader
package.domain = org.example

source.dir = .
source.main = main.py
source.include_exts = py,png,jpg,kv,atlas

version = 0.1
orientation = portrait
fullscreen = 1

# Permissions your app needs
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Requirements — include all needed python modules and kivy, kivymd
requirements = python3,kivy,kivymd,requests

# Architecture (most phones support armeabi-v7a)
android.arch = armeabi-v7a

[buildozer]
warn_on_root = 1
log_level = 2