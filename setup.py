from setuptools import setup, find_packages
setup(
    name="Web Pirate",
    version="0.1",
    packages=find_packages(),
    scripts=["detective_pirate.py"],

    install_requires=["beautifulsoup4==4.8.2",
                    "brotli==1.0.7",
                    "colorit==0.1.0",
                    "cryptography==2.8",
                    "Cython==0.29.15",
                    "importlib_metadata==1.5.0",
                    "ipaddr==2.2.0",
                    "keyring==21.2.0",
                    "lockfile==0.12.2",
                    "lxml==4.5.0",
                    "mock==4.0.2",
                    "mypy_extensions==0.4.3",
                    "numpy==1.18.2",
                    "ordereddict==1.1",
                    "protobuf==3.11.3",
                    "proxyscrape==0.3.0",
                    "pyOpenSSL==19.1.0",
                    "simplejson==3.17.0",
                    "toml==0.10.0",
                    "wincertstore==0.2",
                    "zipp==3.1.0"
                    ],

    package_data={
        
        "": ["README.txt","seed.txt", "dark_db.json"],
        
        "hello": ["A Command line tool written in python for detecting Cryptojacking Malware in website.msg"],
    },

    author="Bigpenguin",
    author_email="waqarsher66@gmail.com",
    description='''A Command line tool written for detecting Cryptojacking malware in website. All you need to do is to give url of a website 
    and it crawl down everything from the website and tell you whether this website has cryptojacking malware (it will provide infecting links)
    or not (will provide nodthing) soon we will be providing python module for such tasks''',
    keywords="Cryptojacking Malware , Python , web Crawlers ",
    url={
	"Source Code": "https://github.com/Cybernorse/Crytojacking-Malware-detection-with-web-pirate",
	},
    classifiers=[
        "License :: Apache License 2.0"
    ]

    
)
