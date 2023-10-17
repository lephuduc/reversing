from distutils.core import setup

setup(
  name = 'rev',         # How you named your package folder (MyLib)
  packages = ['rev'],   # Chose the same as "name"
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Reverse module for easier scripting',   # Give a short description about your library
  author = 'lephuduc',                   # Type in your name
  author_email = 'lephuduc111@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/lephuduc/rev',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/lephuduc/rev/archive/rev_01.tar.gz',    # I explain this later on
  keywords = ['REV', 'REVERSE', 'SCRIPTING'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pycryptodome',
          'arc4',
          'threading',
          'queue',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.7',     
    'Programming Language :: Python :: 3.10',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.11',     
  ],
)