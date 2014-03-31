![Concentric Sky](https://concentricsky.com/media/uploads/images/csky_logo.jpg)

Django Sky Settings
===================

Sky Settings provides a model to allow configuration of site-wide settings using the contrib.admin interface.


### Table of Contents
- [Version History](#version-history)
- [Installation](#installation)
- [Getting Started](#getting-started)
- [License](#license)
- [About Concentric Sky](#about-concentric-sky)


## Version History
- v0.9.4 Added a description field and a unicode function
- v0.9.0 Project was created



## Installation

To install Sky Settings, create a virtualenv and run the following command:

    pip install git+https://github.com/concentricsky/django-sky-settings.git

Include Sky Settings in your settings.py. 

    INSTALLED_APPS = [
        ...

        'sky_settings',

        ...

    ]


## Getting Started 

To create Sky Settings, add settings and values to the Setting model in Django's admin interface. Or, use the set_value() function on the Setting class.

    from sky_settings.models import Setting

    string_setting = Setting.set_value('STRING_NAME', 'a value')
    int_setting = Setting.set_value('INT_NAME', 100)

To get a setting, use the get_value() function on the Setting class. It accepts a default value to fall back to if the setting is not found.

    from sky_settings.models import Setting

    string_setting = Setting.get_value('STRING_NAME', 'a default value')
    int_setting = Setting.get_value('INT_NAME', 200)


## License

This project is licensed under the Apache License, Version 2.0. Details can be found in the LICENSE.md file.


## About Concentric Sky

_For nearly a decade, Concentric Sky has been building technology solutions that impact people everywhere. We work in the mobile, enterprise and web application spaces. Our team, based in Eugene Oregon, loves to solve complex problems. Concentric Sky believes in contributing back to our community and one of the ways we do that is by open sourcing our code on GitHub. Contact Concentric Sky at hello@concentricsky.com._
