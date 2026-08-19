[app]

# (str) Title of your application
title = My Application

# (str) Package name
package.name = myapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (leave empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to exclude (let empty to not exclude anything)
source.exclude_exts = spec

# (list) List of directory to exclude (from source.dir)
source.exclude_dirs = tests, bin, venv

# (list) List of inclusions/exclusions pattern
source.include_patterns = assets/*, images/*

# (str) Application versioning
version = 0.1

# (list) Application requirements
# Add other dependencies here if needed (e.g., pypdf)
requirements = python3,kivy

# (list) Custom source folders for requirements
#requirements.source_dirname =

# (list) Supported orientations
orientation = portrait

# (list) List of services to declare
#services =

#
# OSX Specific
#

#
# Author
#
author = Developer

# (str) Icon of the application
#icon.filename = %(source.dir)s/data/icon.png

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (list) Permissions
#android.permissions = INTERNET

# (list) Features
#android.features = android.hardware.usb.host

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK / AAB will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (int) Android SDK version to use
#android.sdk = 33

# (str) ANT version to use
#android.ant = 1.10.8

# (bool) Use AndroidX
android.androidx = True

# (str) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
